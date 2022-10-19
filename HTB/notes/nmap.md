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


