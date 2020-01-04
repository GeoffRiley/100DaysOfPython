# Day 4: 4<sup>th</sup> January 2020
Try out awesome library [_Plan_](https://github.com/fengsp/plan) 
—Writing crontab file in Python like a charm.

## Requirements
`pip install plan`

## Notes
When looking at the [documentation](http://plan.readthedocs.org/) I checked
the compatibility for Python 3, particularly as Python 2 is now retired and
was a little surprised to find the following:
>Though, Python 3 currently has very few users

This leads me to realise that this particular library has had no work done
upon it for the past five or six years. That being said there are only four 
pull requests and two issues currently logged so it has clearly passed the
test of time. 

The purpose of _Plan_ is to enable simple creation (and manipulation) of 
[crontab (5)](https://linux.die.net/man/5/crontab) files. These are one of 
the mainstays of the Linux operating system control structures, taking care
of repetitive tasks with the flexibility to launch those tasks at anything
from minutes to multiple years. Many maintenance systems use crontabs to 
ensure that processes continue to run, that log files are properly rotated,
that other processes do not stay running indefinitely, and so on.

A utility `plan-quickstart` is supplied that creates an example `schedule.py`
file in the current direction.  This file contains an error in its examples
though:
```python
# cron.module('calendar', every='feburary', at='day.3')
``` 
February is spelt incorrectly. However, as only the first three letters are
examined for determination of the month, this error does not stop the example
working.

_Plan_ automagically converted the supplied date and time specifiers into the 
appropriate _crontab (5)_ time strings ready for writing to the actual `crontab`
file.

## Outcome
This is a library with a very particular purpose… it is most certainly a Linux 
or Mac only library as Windows™ does not have a compatible cronjob system.
Reading through the source, there are very sensible limits placed upon what can
be specified in the date and time descriptions; however, this does mean that
some of the more complex timings cannot be issued.  In order to overcome this
limitation it is possible to give a full _crontab (5)_ time string instead.

Running the `plan-quickstart` examples:
```python
from plan import Plan

cron = Plan()

# register one command, script or module
cron.command('command', every='1.day')
cron.script('script.py', path='/web/yourproject/scripts', every='1.month')
# Yes, this example has a spelling mistake!
cron.module('calendar', every='feburary', at='day.3')

cron.run()
```
results in
```text
# Begin Plan generated jobs for: main
0 0 * * * command
0 0 1 * * cd /web/yourproject/scripts && /…/python script.py
0 0 3 2 * /…/python -m calendar
# End Plan generated jobs for: main
```
(paths trimmed out appropriately.)

## Comments
I can see that _Plan_ will have its uses, perhaps in packages installation 
scripts, but I would not use it purely to add a new _crontab (5)_ entry though
since using `crontab -e` works perfectly well for me at the shell prompt loading
the existing crontab into [`vim`](https://linux.die.net/man/1/vi) and updating
automatically upon save.
