# Day 10: 10<sup>th</sup> January 2020
Try out awesome library [_Python-Modernize_](https://github.com/mitsuhiko/python-modernize)
—Modernizes Python code for eventual Python 3 migration.

## Requirements
`pip install modernize`

## Notes
This is a utility to help with converting old Python 2 projects into
Python 3.  It is a veneer over the top of the standard `lib2to3`, as used
by `2to3` supplied with Python 3.

The main difference between `python_modernize` and `2to3` is that the 
latter only targets producing code compatible with Python 3, whilst the 
former aims to produce code compatible with both Python 3 _and_ Python 2. 

## Outcome
A useful utility for the short term… however, as time moved on and
Python 2 is left further behind it will come to a natural end of its 
useful life. 

## Comments
The last commit was made to the source tree in October 2014 and it 
would seem unlikely that any further development will be performed upon 
the code unless a severe bug was to be found.  Having said that, the 
code base _has_ been advanced in [a different 
branch](https://github.com/tiobe/python-modernize) with numerous updates
up to last December.
