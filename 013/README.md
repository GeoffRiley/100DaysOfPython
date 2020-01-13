# Day 13: 13<sup>th</sup> January 2020
Try out awesome library [_forex-python_](https://github.com/MicroPyramid/forex-python) 
—Foreign exchange rates, Bitcoin price index and currency conversion.

## Requirements
`pip install forex-python`

## Notes
Compared to [yesterdays](../012) library, this is much more current. It
is also designed to compute conversions between currencies rather than
purely documenting currency formats.

_Forex-python_ uses [Rates API](https://ratesapi.io/) to obtain its 
conversion rate details, this is a fully open source service providing
data from the [Central European Bank](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html). 
Source for _ratesapi_ is available on [GitHub](https://github.com/apilayer/ratesapi).

This library will also allow the retrieval of currency names and symbols.
It has a larger complement of national currencies available in its library
than _python-currencies_ but makes no attempt to provide formatting hints
for any of them.

## Outcome
Depending upon your use case both _forex-python_ **and** _python-currencies_
are likely to be of use to someone wanting to provide financial references
within a package.

## Comments
It was good to have a library that is already fully Python 3 compatible…
it works straight from install in spite of a warning on the main 
[README.rst](https://github.com/MicroPyramid/forex-python/blob/master/README.rst)
that versions later than 1.1 may give `RatesNotAvailableError` exceptions.
