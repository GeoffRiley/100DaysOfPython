# Day 2: [2<sup>nd</sup> January 2020](./002)

Try out awesome library [_bidict_](https://github.com/jab/bidict)—Efficient, Pythonic bidirectional map data structures and related functionality.

## Requirements
pip install bidict

## Notes
_bidict_ is a bi-directional dictionary. The purpose is to be able to access both `keys` and `value` by their 
appropriate representation and in each case returning the opposite. If the same interface was to be used to retrieve
either, however, it would be impossible to discern which was being returned. Therefore the normal dictionary method is 
used to return the value for a key, and a new method, `inverse[]`, is implemented to retrieve a key appropriate to a 
value.

In the background the _bidict_ class maintains two synchronised dictionaries intelligently, updating as and when 
necessary.

### Limitations
As _bidict_ maintains two internal dictionaries to provide the functionality it is imperative that both the key and the
value are _hashable_ **and** _unique_. Obviously the key has these requirements, but in order for the secondary mapping
to be provided internally, then it is necessary to place the same requirements on the values—since they become the keys 
in the other mapping! 

Given these limitations attempting to perform the following:
```python
from bidict import bidict

b = bidict({'fred': 1})
b.update({'wilmer': 1})
```
would result in a `ValueDuplicationError` exception being raised due to the duplication of the value '1'.  If such an 
assignment is genuinely required (replacing 'fred' with 'wilmer'), then the functions `forceput()` and `forceupdate()`
will make the replacement without raising an exception.

## Outcome
A fascinating read through of the library code, including its variants, has brought an extremely useful tool to my
attention.  I can think of a number of occasions that this would have been useful when completing the 
[Advent of Code](https://adventofcode.com/) during last December, particularly with regard to some of the `Intcode`
exercises. 

## Comments
Although I generated no actual code for this day, I have learnt from the examination of the code and reading the 
author's accompanying notes a number of interesting aspects of different Python interpreters: in particular the handling
of 'nan' by CPython and Pypy where the former is over-eager in converting the string value into the numeric _not a 
number_.

Only two days in and I'm already eagerly looking forward to what tomorrow has in store.
