# Day 16: 16<sup>th</sup> January 2020
Try out awesome library [_MarkupSafe_](https://github.com/pallets/markupsafe) 
—Implements a XML/HTML/XHTML Markup safe string for Python.

## Requirements
`pip install MarkupSafe`

## Notes
This is a very neat and small library that assists in keeping 'dangerous' 
character constructions out of data flows: this allows user input to be
sanitised in order to prevent script injection attacks.

_MarkupSafe_ is Python 2 and 3 compatible using `unicode` class for 
Python 2 and `str` for Python 3.

The library uses two main interfaces, a function `escape()` and a class
`Markup()`. The former will seek out all occurrences of `&`, `<`, `>`, 
`'` and `"` and replaces them with html safe sequences, it returns an 
instance of the `Markup()` class.  Instantiating the class directly will
allow any string to be set as a safe string. The following script
demonstrate this:
```python
from markupsafe import Markup, escape

# Here is a lovely bit of json injection
# Unprotected it would pop up an alert box if pushed into
# a web page
json_injection = '<script>alert(document.cookie);</script>'

# If we escape the string then any 'harmful' characters
# are automatically converted into harmless control sequences
escaped = escape(json_injection)

# If, on the other hand, the string is really wanted like that
# then using Markup indicates that the string is 'safe'
markup = Markup(json_injection)

print(f'Escaped: {escaped}')
print(f'Markup:  {markup}')

# Escaped: &lt;script&gt;alert(document.cookie);&lt;/script&gt;
# Markup:  <script>alert(document.cookie);</script>
```

The `Markup()` class has a further function: if it is created with
parameter placeholders, then when the substitution happens the 
parameters are escaped.  Here is a demonstration:
```python
# A marked up string with parameter replacements will have those
# parameters escaped:
str1 = '<em>Squirrels</em>'
str2 = 'Wilderness'
str3 = '"Ice bun terror"'

param_string = Markup('"This is a test." …or <b>How to get %s in a string</b>.')

print(param_string)
print(param_string % str1)
print(param_string % str2)
print(param_string % str3)

# "This is a test." …or <b>How to get %s in a string</b>.
# "This is a test." …or <b>How to get &lt;em&gt;Squirrels&lt;/em&gt; in a string</b>.
# "This is a test." …or <b>How to get Wilderness in a string</b>.
# "This is a test." …or <b>How to get &#34;Ice bun terror&#34; in a string</b>.
```  

## Outcome
A useful library for anyone that might need to display or record 
information entered by users in a html or xml based system. It appears
to be well maintained with a large cohort of contributors.

## Comments
A fine example of a simple and efficient interface with a clearly
defined purpose.  Excellent.
