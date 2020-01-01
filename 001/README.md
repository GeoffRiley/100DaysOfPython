# Day 1: 1<sup>st</sup> January 2020
Try out awesome library [_PyPattyrn_](https://github.com/tylerlaberge/PyPattyrn)—a simple yet effective library for implementing common design patterns.

## Requirements
pip install pypattyrn

## Notes
Design patterns are a language agnostic subject set of principles that may be applied to similar problems in any system.
In this case the  _PyPattyn_ library is a set of skeletal templates to enable the simple implementation of a large 
number of patterns in the _Python_ language.

The library is divided into the three main pattern types:
 - Behavioural,
 - Creational, and
 - Structural 

I am already familiar with most of these patterns from use in other languages, so I shall concentrate upon the ones that
I have less familiarity:
 - Chain of Responsibility,
 - Command, and
 - Flyweight
 
 ## Outcome
 Programming-wise I coded an example to perform a fairly simple task in a rather complex manner: I used the _Chain of 
 Responsibility_ pattern to identify the operators within a maths expression. This can obviously be performed in far 
 simpler ways, but it was something that could easily give immediate feedback and is not so abstract as to be beyond
 understanding.
 
 The _Command_ pattern is a different beast completely—whilst _Chain of Responsibilty_ undertakes to identify the 
 appropriate command as the chain is traversed _Command_ holds a curated set of regulated functions that are marshalled
 by the pattern, allowing histories of commands to be maintained such that they may be reversed to _undo_ to any level.
 This is **not**, however, reflected by a _redo_ function.
 
 The _Flyweight_ pattern is interesting, I have met it before, but I do not recall it being so named.  It effectively 
 maintains a whole set of related singletons—the example provided as a deck of cards is very clear in that a deck can 
 only ever have a single card of each suit and value.
 
 ## Comment
 On this, my first day, I actually spent almost two hours on the project as I was setting up the [Conda](https://docs.conda.io/en/latest/) environment 
 within [PyCharm](https://www.jetbrains.com/pycharm/) and the repository on GitHub.
 