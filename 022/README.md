# Day 22: 22<sup>nd</sup> January 2020
Try out awesome library [_Tomorrow_](https://github.com/madisonmay/Tomorrow) 
—Magic decorator syntax for asynchronous code.

## Requirements
- Python 2.7 **ONLY**

`pip install tomorrow`

## Notes
This library comes with a warning at the top of it's README:
> Magic decorator syntax for asynchronous code in Python 2.7.
>
> Please don't actually use this in production. It's more of 
> a thought experiment than anything else, and relies heavily 
> on behavior specific to Python's old style classes. Pull 
> requests, issues, comments and suggestions welcome.

I was about to dismiss this library completely out of hand due to the fact that
asynchronous coding styles have changed so completely with the advent of Python 3.
However, there is merit in examining _tomorrow_ for its technique of operation as
a decorator.

## Outcome
The implementation of decorators is well documented elsewhere, but in this 
library there is a working, albeit old, example of how a decorator may be put
together.

The heavy lifting for this decorator is the `threads()` routine.  Like all 
decorators this is introduced with the '@' symbol before the appropriate routine:
```python
@threads()
def decorated_routine(whatever, parameters):
    # Do the work
    pass
```
What this actually does is to pass the routine as a parameter to the decorator:
```python
threads(decorated_routine)
```
In this case `threads()` just passes straight off to the `async()` routine
which performs the actual decoration. Using the standard library `wraps` to 
preserve the original function name etc., a `Tomorrow` class instance is 
returned (in this case) to work the threading magic. 

## Comments
Not such an _awesome_ library, rather a library to avoid. Nevertheless, a 
practical example of how to create and use a decorator is always useful.
