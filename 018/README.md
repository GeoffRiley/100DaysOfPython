# Day 18: 18<sup>th</sup> January 2020
Try out awesome library [_pyshorteners_](https://github.com/ellisonleao/pyshorteners) 
—A pure Python URL shortening lib.

## Requirements
`pip install pyshorteners`

## Notes
The homepage for this library on GitHub has been under review for the 
last ten months or so and holds a warning to not work from the on page
docs. There is a brief message with details of the 'latest' version on 
PyPi, but the description is somewhat unclear.

The available 'shorteners' in the working source are :

- `Shorteners.ADFLY` 
- `Shorteners.AWSM` 
- `Shorteners.BITLY`
- `Shorteners.CHILPIT` 
- `Shorteners.CLCKRU` 
- `Shorteners.DAGD`
- `Shorteners.GOOGLE` 
- `Shorteners.ISGD` 
- `Shorteners.OSDB`
- `Shorteners.OWLY` 
- `Shorteners.QPSRU` 
- `Shorteners.QRCX`
- `Shorteners.READABILITY` 
- `Shorteners.SENTALA` 
- `Shorteners.SIMPLE`
- `Shorteners.TINYURL` 
- `Shorteners.WPACO`

These are used in the following manner:
```python
import pyshorteners
from pyshorteners import Shorteners

s = pyshorteners.Shortener(Shorteners.TINYURL)
shorturl = s.short('https://codechalleng.es/')
print(shorturl)
```
The output from this (http://tinyurl.com/qol4yhh) is a short url created
using the `tinyurl` system.

_tinyurl_ uses a global database for storing its shortened urls and so
requires no setup parameters, other services may require user or 
application keys in order to generate urls specific to an identity. This
is done so that tracking may be performed on the number of click-throughs
and so on. 

## Outcome
Checking the above tinyurl on https://tinyurl.com shows:
```text
Preview of TinyURL.com/qol4yhh

This TinyURL redirects to:
https://codechalleng.es/
```

Requesting a shortcut for the same url will always return the same
resulting tinyurl, with other services the shortcut is normally the 
same when requested with the same identity, but different when requested
with a different identity.

## Comments
Another useful url shortener, let down mostly by the out of sync 
documentation. The new version is still being worked upon but, at time
of writing, was not building so could not be tested in order to compare
the _simplified_ API.
