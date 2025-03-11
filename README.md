# Cisco Packet Tracer Bot
This was a simple bot I made to configure routers and computers as i was tired of doing it in class all the time

## Use case
Run the `main.py` file

To setup a router type r
To setup a computer type c

Enter the number of devices you want

## Setting up a computer

The base ip is the 1 digit of the routers ip which would be 192.168.0.1 (would be 0)

**To know the default gateway without checking, you first must know how the order that router was made**

e.g.

If its the first router made:

- The ip for the 1st ethernet port is 192.168.0.1 with the 0 increacing each time for each other router

So on the First router:

- Ethernet port 0: 192.168.0.1
- Ethernet port 1: 192.168.1.1

So on the Seccond router:

- Ethernet port 0: 192.168.2.1
- Ethernet port 1: 192.168.3.1

etc..

If you enter the number of routers you already have, it will do the same but +3 to the number of routers

e.g.

If you say you have 3 routers

- Ethernet port 0: 192.168.6.1
- Ethernet port 1: 192.168.7.1

**Make sure, when creating a new device that you clear the space it optimises**
