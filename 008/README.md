# Day 8: 8<sup>th</sup> January 2020
Try out awesome library [_django-elastic-transcoder_](https://github.com/StreetVoice/django-elastic-transcoder) 
—Django + [Amazon Elastic Transcoder](https://aws.amazon.com/elastictranscoder/).

## Requirements
- Django framework running on [Amazon Web Services](https://aws.amazon.com/)
including the [Amazon ElastiCache service](https://aws.amazon.com/elasticache/)
- Note: not working on Django >= 1.10, although an alternative 
[branch](https://github.com/rk2810/django-elastic-transcoder) has been 
updated to operate with Django < 2.3

`pip install django-elastic-transcoder`

## Notes
This is a Django app providing a connector to the AWS Elastic database 
systems. The package contains a `Transcoder` class, an endpoint for 
receiving notifications from the SNS service, signals for _PROGRESS_, 
_ERROR_ and _COMPLETE_ and an `EncodeJob` model.

## Outcome
Yet another module that I was unable to actually test out, however, at
least I was able to confirm that a version of the module exists and is
(apparently) working.

## Comments
It seems that this #100DaysOfCode list is a little too reliant upon 
services that are installed beyond my current means (or needs) and so will
be skipping any that fall into that category.  

I will substitute a different coding item in their stead.
