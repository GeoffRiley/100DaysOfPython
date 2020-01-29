# Day 24: 29<sup>th</sup> January 2020
Try out awesome library [_simpleq_](https://github.com/rdegges/simpleq) 
—A simple, infinitely scalable, Amazon SQS based queue.

## Requirements
- Amazon Web Services with Simple Queue Service
- Python 2
- Installation from GitHub repository

## Notes
This library appears to be abandoned, the documentation is absent and (judging by
[issue number 1](https://github.com/rdegges/simpleq/issues/1) raised on 
3<sup>rd</sup> September 2014) has never actually been created—in spite of 
the link presented. 

No activity since 2015 when the developer 
[stated](https://github.com/rdegges/simpleq/issues/2#issuecomment-103143566):
> The project in it's current state is mainly a 'playground' for my 
> experimentation with how I'd like this to work. I'm 100% open to 
> suggestions / etc. The main goal is to keep it simple / easy to maintain =)

## Outcome
As this library requires services that I do not have access to, as well as not
being up to date with Python 3, it is impossible to do more that examine the
code. The code itself is generally just wrappers around API calls to the 
[_boto_](https://github.com/boto/boto) AWS interface library.

## Comments
Another disappointing library, it possibly has a use to someone using the 
Amazon SQS—however, as the _boto_ (or rather _boto3_ now) library has support
for communicating with the SQS anyway for both Python 2 and 3, it seems somewhat
redundant.
