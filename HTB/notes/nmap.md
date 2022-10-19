# Nmap
(Last edited 19/10/22)

A tool for scanning a network. WHen possible it wil grab info about processes running on open ports, such as version numbers, firewalls, etc.

It can be broken down into the following:
 - Host discovery
 - Port scanning
 - Service enumeration and detection
 - OS detection
 - Scriptable interaction with the target service (Nmap Scripting Engine)

## Syntax

Typical nmap syntax will look something like:

`nmap <scan types> <options> <target>`

## How it Works

In order to scan thousands of ports at a time, I imagine nmap is multithreaded; Each thread sends a TCP handshake and whichever ports respond are logged.
 
 - If a port replies with a SYS-ACK, the port is open
 - If a port replies with RST, it is closed
 - If a port doesn't reply, it's tagged as filtered. Depending on firewall configurations, a port could still be open but return nothing.

## Example Scan

Scanning myself would look similar to this:

```bash
sam@sam  ~/Cyber/HTB/notes   main ± sudo nmap -sS localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2022-10-19 03:02 BST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0000020s latency).
Not shown: 999 closed ports
PORT    STATE SERVICE
631/tcp open  ipp

Nmap done: 1 IP address (1 host up) scanned in 0.10 seconds
```

## Recon with nmap

It's important to log every scan done on a network when trying to figure out exactly what you're up against. This will be looked into more depth below.

An example of finding all ip's on a network would be as follows:

```bash
sudo nmap 10.129.2.0/24 -sn -oA tnet | grep for | cut -d" " -f5

10.129.2.4
10.129.2.10
10.129.2.11
10.129.2.18
10.129.2.19
10.129.2.20
10.129.2.28
```

### Ping Scan

Here we used `-sn` (a ping scan) to discover ports. The default no arguments scan is called a list scan. We can use a ping scan to quickly decide if an ip is alive or not, depending on the output. THis can be pared with `--reason` to give a reason as to why it thinks the host is alive (usually a response). For example:

```bash
sudo nmap localhost -PE --reason -sn
Starting Nmap 7.80 ( https://nmap.org ) at 2022-10-19 03:26 BST
Nmap scan report for localhost (127.0.0.1)
Host is up, received localhost-response.
Nmap done: 1 IP address (1 host up) scanned in 0.00 seconds
```

### File Output and Input

We also use `-oA tnet`. This is the output file to put results. By default, it will output `xml`, `nmap` and `gnmap` files. 

The `grep` and `cut` commands here only parse the output to stdout, not the file. And they cut down the output into ip's so it's easier to read for the example.

If we are given multiple hosts to lookat, we can use the `-iL` argument to read from a file:

```bash
sudo nmap -sn -oA tnet -iL hosts.lst | grep for | cut -d" " -f5
```

### Range of IP's

We can also define a range of ip's, if they're next to each other:

```bash
sudo nmap -sn -oA tnet 10.129.2.18-20| grep for | cut -d" " -f5
```

This will scan .18 to .20, including 20.

### Quick Excersise

Based on the following output, determin the OS of the host:

```bash
sudo nmap 10.129.2.18 -sn -oA host -PE --packet-trace --disable-arp-ping 

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 00:12 CEST
SENT (0.0107s) ICMP [10.10.14.2 > 10.129.2.18 Echo request (type=8/code=0) id=13607 seq=0] IP [ttl=255 id=23541 iplen=28 ]
RCVD (0.0152s) ICMP [10.129.2.18 > 10.10.14.2 Echo reply (type=0/code=0) id=13607 seq=0] IP [ttl=128 id=40622 iplen=28 ]
Nmap scan report for 10.129.2.18
Host is up (0.086s latency).
MAC Address: DE:AD:00:00:BE:EF
Nmap done: 1 IP address (1 host up) scanned in 0.11 seconds
```

### Answer

`Windows`!

Different OS's have different default ttl (Time-To-Live) defaults. Linux is 64 and windows is 128. This defines how long a packet should exist before being discarded.

### Port Descriptions

 - open; port has been scanned and has replied
 - closed; port replied with a packet but that packet contains an RST flag (TCP)
 - filtered; nmap can't determin it's state. Either it got no reply or an error message
 - unfiltered; (TCP-ACK only) Port is accessed, but not clear if its open or closed
 - nmap will default to open|filtered if it thinks a firewall blocked the packet.

### Defining Ports

We can define ports using the `-p` argument. e.g. `-p 255,256` or `-p 1-255`. We can also use the `--top-ports=10` argument to scan the most frequently accessed ports.

### Flags

 - SYN -> SYN-ACK <- ACK ->
 - SYN; 'Pinged' to the host. Host replies when it sees the packet. Packet contains senders IP
 - SYN-ACK; Sent from the host back to the sender, acknowledges the first ping
 - ACK; Sent back from the host, acknowledges the SYN-ACK
 - FIN ( / RST); Send at the end of data transmission. Used to close the connection

### UDP

If we specify `-sU` (UDP Scan), we will scan all UDP ports. Sometimes these are forgotten about and not filtered as heavily as TCP ones are. However UDP isn't a handshake protocol and therefore takes a lot longer to preform. If UDP ports are `open`, we won't get a response unless the port is specifically configured to do so.

### ICMP

ICMP `error code 3` indicates the port is unreachable. The ICMP type and error code are highlighted below:

`RCVD (0.1498s) ICMP [10.129.2.28 > 10.10.14.2 Port unreachable **(type=3/code=3)** ] IP [ttl=64 id=11903 iplen=56 ]`

### -A

THe `-A` argument is very useful to discover hostname as well as OS version. Very fruity

An example of -A output would look like:

```bash
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-19 04:50 BST
Stats: 0:02:53 elapsed; 0 hosts completed (1 up), 1 undergoing Traceroute
Traceroute Timing: About 32.26% done; ETC: 04:53 (0:00:00 remaining)
Stats: 0:03:03 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 99.79% done; ETC: 04:53 (0:00:00 remaining)
Stats: 0:03:04 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 99.79% done; ETC: 04:53 (0:00:00 remaining)
Nmap scan report for 10.129.78.135
Host is up (0.072s latency).
Not shown: 993 closed tcp ports (reset)
PORT      STATE SERVICE     VERSION
22/tcp    open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 71:c1:89:90:7f:fd:4f:60:e0:54:f3:85:e6:35:6c:2b (RSA)
|   256 e1:8e:53:18:42:af:2a:de:c0:12:1e:2e:54:06:4f:70 (ECDSA)
|_  256 1a:cc:ac:d4:94:5c:d6:1d:71:e7:39:de:14:27:3c:3c (ED25519)
80/tcp    open  http        Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
110/tcp   open  pop3        Dovecot pop3d
|_pop3-capabilities: AUTH-RESP-CODE RESP-CODES UIDL TOP PIPELINING SASL CAPA
139/tcp   open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
143/tcp   open  imap        Dovecot imapd
|_imap-capabilities: IMAP4rev1 SASL-IR LOGINDISABLEDA0001 have post-login ENABLE listed more Pre-login capabilities LOGIN-REFERRALS OK ID IDLE LITERAL+
445/tcp   open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
31337/tcp open  Elite?
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=10/19%OT=22%CT=1%CU=38138%PV=Y%DS=2%DC=T%G=Y%TM=634F74
OS:B5%P=x86_64-pc-linux-gnu)SEQ(SP=108%GCD=1%ISR=10B%TI=Z%CI=I%II=I%TS=8)OP
OS:S(O1=M539ST11NW7%O2=M539ST11NW7%O3=M539NNT11NW7%O4=M539ST11NW7%O5=M539ST
OS:11NW7%O6=M539ST11)WIN(W1=7120%W2=7120%W3=7120%W4=7120%W5=7120%W6=7120)EC
OS:N(R=Y%DF=Y%T=40%W=7210%O=M539NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=
OS:AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(
OS:R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%
OS:F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N
OS:%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%C
OS:D=S)

Network Distance: 2 hops
Service Info: Host: NIX-NMAP-DEFAULT; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -38m00s, deviation: 1h09m16s, median: 1m58s
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: NIX-NMAP-DEFAUL, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-time: 
|   date: 2022-10-19T03:55:09
|_  start_date: N/A
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: nix-nmap-default
|   NetBIOS computer name: NIX-NMAP-DEFAULT\x00
|   Domain name: \x00
|   FQDN: nix-nmap-default
|_  System time: 2022-10-19T05:55:09+02:00

TRACEROUTE (using port 995/tcp)
HOP RTT      ADDRESS
1   73.19 ms 10.10.14.1
2   73.22 ms 10.129.78.135

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 189.39 seconds
```

