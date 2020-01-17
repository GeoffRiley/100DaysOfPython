# Day 17: 17<sup>th</sup> January 2020
Try out awesome library [_txZMQ_](https://github.com/smira/txZMQ) 
—Twisted based wrapper for the ZeroMQ message library.

## Requirements
- `zeromq` binary appropriate for OS platform. e.g. `sudo apt-get install libzmq3-dev` 
on Debian based Linux distros
- `libsodium` binary appropriate for OS platform
- `twisted` — along with a whole raft of dependencies
- `pyzmq` for the Python bindings
  - available as conda installation or `pip install pyzmq`

`pip install txZMQ`

## Notes
_txZMQ_, according to the docs, allows to integrate easily ØMQ sockets
into Twisted event loop (reactor).

The first question has to be "What is ØMQ and Twisted?"

Consulting the documentation for each…
- [_ZeroMQ_](https://github.com/zeromq/pyzmq) (also spelled ØMQ, 0MQ or 
ZMQ) is a high-performance asynchronous messaging library, aimed at 
use in distributed or concurrent applications. It provides a message 
queue, but unlike message-oriented middleware, a ZeroMQ system can 
run without a dedicated message broker.
- [_Twisted_](https://github.com/twisted/twisted) is an event-driven
networking engine written in Python—hence the extensive list of required
support packages. It is a complex library providing protocol modules for
a wide variety of standard communication routes.

The purpose of _txZMQ_ is to provide an additional protocol to the 
_twisted_ suite. This extra protocol is based upon multicast UDP packets
which can be used to broadcast to many subscribing targets without the
need to send to each target individually.

## Outcome
The binary for `zeromq` failed to install on my system so I resorted to
installing the conda packages to get the generic pre-compiled wheel.
The number of packages that needed to be installed was as _impressive_
as the variety thereof.

## Comments
I cannot see an immediate use for this library in my coding and _twisted_
seems rather overkill for anything that I would want to use: generally I
will only be grabbing web-pages and the standard _html_ library is more
than sufficient for that purpose. 
