# Day 21: 21<sup>st</sup> January 2020
Try out awesome library [_tinytag_](https://github.com/devsnd/tinytag) 
—A library for reading music meta data of MP3, OGG, FLAC and Wave files.

## Requirements
`pip install tinytag`

## Notes
Here's an interesting library. Purely a tag reader it operates on the major music
formats without the complication of attempting to do any writing, this keeps the
library small and relatively simple. The developer is active and responding to 
issues in a very timely manner, not that there have been any real issues for
around nine months.

## Outcome
After some pretty heavy libraries in recent days this is a wonderful easy to use
and practical library. _Tinytag_ is very simple to use library with nothing but
the minimum requirements to perform its task.  I pointed it at a directory full
of audio files of mixed type and it correctly identified and extracted information
from each very quickly.

## Comments
I wanted a library like this some time back and couldn't find one that worked… 
at that time I ended up running an external command to extract the tags and 
interpreted the output to get what I wanted.  This would have made life so much
simpler—and a whole load faster!
