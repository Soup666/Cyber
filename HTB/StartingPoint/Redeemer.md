# Redeemer

Mahcine ip: 10.129.247.91

Useful Links: 
	- https://redis.io/docs/manual/cli/#host-port-password-and-database


## Task 1

Q: Which TCP port is open on the machine? 

Simple nmap scan here. Add options `-p-` and `-T5`
	- `-p-`: Scan all ports
	- `-T5`: Caps the scan delay to 5ms to speed up the scan

A: `nmap 10.129.247.91 -p- -T5`

## Task 2

Q:  Which service is running on the port that is open on the machine? 

A: Redis

## Task 3

Q:  What type of database is Redis? Choose from the following options: (i) In-memory Database, (ii) Traditional Database 

Quick google search

A: In-memory Database

## Task 4

Q:  Which command-line utility is used to interact with the Redis server? Enter the program name you would enter into the terminal without any arguments. 

A: redis-cli

## Task 5

Q:  Which flag is used with the Redis command-line utility to specify the hostname? 

A: `-h`

## Task 6

Q:  Once connected to a Redis server, which command is used to obtain the information and statistics about the Redis server? 

Guess

A: `info`

## Task 7

Q:  What is the version of the Redis server being used on the target machine? 

A: `sudo nmap -p- -T5 10.129.247.91 -sV`

## Task 8

Q:  Which command is used to select the desired database in Redis? 

Guess

A: select

## Task 9

Q:  How many keys are present inside the database with index 0? 

since redis can be ran in interactive mode or command mode, we can send a command and grep the output:
`redis-cli -h 10.129.247.91 info | grep keys`
Redis will automatically use --raw since the output isn't a terminal screen

A: 4

## Task 10

Q: Which command is used to obtain all the keys in a database? 

Note: This didn't seem to work in command mode. Maybe something to do with multiple args? Either way interactive mode works

A: KEYS *

## Final Task

Q: Submit root flag

We know `flag` is a key from the previosu task, so getting it is pretty simple

A: get flag
