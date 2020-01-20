# Day 19: 19<sup>th</sup> January 2020
Try out awesome library [_Demiurge_](https://github.com/matiasb/demiurge) 
—PyQuery-based scraping micro-framework.

## Requirements
- Relies upon `pyquery`, `cssselect` and `lxml`

`pip install demiurge`

## Notes
Although the library is fully compatible with Python 2 and 3, the documentation
is minimal and the example code no longer works as the website that it was set
to scrape have been closed down for years.

## Outcome
I attempted to scrape the [IMDB](https://www.imdb.com/) front page to extract
people with birthdays 'today'.  However, I think that the page must be built by
scripts once it has been loaded as nothing was being picked up.

No explanation of the required syntax is given to explain how the various 
`selector` items should be put together: even a link to the 
[_PyQuery_ git archive](https://github.com/gawel/pyquery/) or to its
[documentation](https://pyquery.readthedocs.io/en/latest/) would have
been useful for this. 

## Comments
I had good hopes for this library, in spite of its odd name… sadly I was unable
to get any kind of useful operation out of it.

…and I'm a day behind.
