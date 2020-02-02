# Day 26: 2<sup>nd</sup> February 2020
Try out awesome library [_scikit-video_](https://github.com/aizvorski/scikit-video) 
—Video processing routines for SciPy.

## Requirements
- System installation of `ffmpeg` or `aconv`
- scipy
- pillow
- numpy

`pip install scikit-video`

## Notes
Whilst this library is updated for Python 3, it is marked as as _Alpha_ status
and has had no commits since May 2016. The README claims _Beta_ status. There 
is no documentation beyond the root README suggesting what the library may 
eventually build into. 

The library as it stands is minial in extent and barely foes further than 
providing wrappers around `ffmpeg` or `aconv`. It has a definite abandoned
feel about it.

The developer does not seem to have made any contributions to any projects 
since 2018.

## Outcome
Well, yes, it loads videos.  I haven't got a camera to test how it copes with
creating videos, but I have no reason to suppose that will not work as it 
utilises the system functions. There are a few open issues for 2017 concerning
video capture.

## Comments
I have one concern with the stated aim—the author wants to stick to pure Python 
coding, opposed to the work of OpenCV which pushes all the complex maths into 
C++ taking advantage of the speed of compiled code.  I cannot see how this 
project would ever hope to compete under such circumstances, especially with 
the numbers of developers involved in the OpenCV project.

However, as it appears to have been abandoned as a project, these details are 
undoubtedly moot.
