# Day 12: 12<sup>th</sup> January 2020
Try out awesome library [_python-currencies_](https://github.com/Alir3z4/python-currencies)
—Display money format and its filthy currencies.

## Requirements
- Python 2

`pip install currencies`

## Notes
Although this is a Python 2 library, the 'fix' to allow it to run all
its tests correctly on Python 3 involved adding a `list()` to the
return value of `get_currency_formats()`. This switches the Python 3 
`dict_key` into a `list` as specified by the docstring. 

```python
    @classmethod
    def get_currency_formats(cls):
        """
        :rtype: list
        """
        return list(cls.money_formats.keys())
```

The purpose of the library _python-currencies_ is to format currencies
appropriate to the country specified.  It does not make any attempt to
perform currency conversions.

## Outcome
I forked the master repository of the library and applied the above 
mentioned modification, I also modified the `setup.py` file to flag
compatibility with Python 3.

## Comments
I have submitted a [pull request for Python 3 
updates](https://github.com/Alir3z4/python-currencies/pull/4)
