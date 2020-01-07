# Day 7: 7<sup>th</sup> January 2020
Try out awesome library [_sanitize_](https://github.com/Alir3z4/python-sanitize) 
—Bringing sanity to world of messed-up data. 

## Requirements
- This library requires the `sgmllib` module which has been deprecated since Python 2.6
and removed in Python 3.

- for Python 2: `pip install sanitize`

## Notes
By its own description, "_sanitize_ is a Python module for making sure 
various things (e.g. HTML) are safe to use." This is slightly misleading
since the example of _HTML_ is the only thing that is sanitised through
the use of the library.

### However…
This library has not been attended to since September 2014 when an 
annotation was added to suggest that Python 3 support needed adding as 
an _enhancement_. The repository from which it was originally branched 
has had no development since December 2011.

Additionally there are no branches of the repository that have been 
developed any further.

## Outcome
I attempted to upgrade the library to operate with Python 3.

It was necessary to replace `sgmllib` before any progress could be made 
and I selected the Python 3 `html.parser` module to do this given its 
similar API to that of the old `sgmllib` module. Re-writing the interface
to use the new library required the change of methodology associated with
Python 3 with regards to class hierarchy.

I have not been able to get this running.  Only 2 of 18 test cases are
currently passing.

## Comments
This would be an interesting library if only it worked on Python 3.

It is probably unlikely to be worth upgrading in the long run as packages
such as `html-sanitizer` and `bleach` are already fully Python 3 
compatible.
