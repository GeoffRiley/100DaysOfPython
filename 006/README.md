# Day 6: 6<sup>th</sup> January 2020
Try out awesome library [_short_url_](https://github.com/Alir3z4/python-short_url)
—Python implementation for generating Tiny URL and bit.ly-like URLs.

## Requirements
`pip install short_url`

## Notes
The idea behind generating short urls was originally due to the character
limit imposed upon 'tweets' on [Twitter](https://twitter.com/). However,
one of the problems associated with generating short urls is to make them
difficult to just guess thereby hijacking someone elses link.  Typically 
various hashing algorithms have been used to convert either the actual 
url or an index into a _psuedo-random_ string that can be stored alongside
the url.

_short_url_ takes a different approach by using a reversible bit-shuffling 
algorithm on the integer id value. This has the advantage that the short
url does not need to be stored once generated.

## Outcome

The following code briefly demonstrates the action of _short_url_. It adds 
six urls to a database, using the id of each to generate a short url, 
decodes that short url and then retrieves the full url from the database. 

```python
import short_url
import sqlite3

urls = [
    'https://codechalleng.es/100days/',
    'https://pybit.es',
    'https://pybit.es/pages/articles.html',
    'http://pbreadinglist.herokuapp.com',
    'https://pybit.es/pages/challenges.html',
    'https://stackoverflow.com'
]

con = sqlite3.connect('/tmp/url_store.sqlite')
cur = con.cursor()

drop_table = 'drop table if exists urls'
table_create = 'CREATE TABLE urls (id integer PRIMARY KEY, url text NOT NULL)'
add_url = 'INSERT INTO urls (url) VALUES (?)'
read_url = 'SELECT url FROM urls WHERE id=(?)'

cur.execute(drop_table)
cur.execute(table_create)

for url in urls:
    print(f'** Working on {url}')
    cur.execute(add_url, [url])
    id = cur.lastrowid
    print(f'   added to database with id:{id}')
    encoded_url = short_url.encode_url(id)
    print(f'   short url:{encoded_url}')
    decoded_url = short_url.decode_url(encoded_url)
    print(f'   decoded url id:{decoded_url}')
    cur.execute(read_url, [decoded_url])
    read_back = cur.fetchone()[0]
    print(f'   url retrieved from database: {read_back}\n')
```
The resulting output is as follows:
```text
** Working on https://codechalleng.es/100days/
   added to database with id:1
   short url:867nv
   decoded url id:1
   url retrieved from database: https://codechalleng.es/100days/

** Working on https://pybit.es
   added to database with id:2
   short url:25t52
   decoded url id:2
   url retrieved from database: https://pybit.es

** Working on https://pybit.es/pages/articles.html
   added to database with id:3
   short url:ghpzy
   decoded url id:3
   url retrieved from database: https://pybit.es/pages/articles.html

** Working on http://pbreadinglist.herokuapp.com
   added to database with id:4
   short url:6vyv6
   decoded url id:4
   url retrieved from database: http://pbreadinglist.herokuapp.com

** Working on https://pybit.es/pages/challenges.html
   added to database with id:5
   short url:pbq8b
   decoded url id:5
   url retrieved from database: https://pybit.es/pages/challenges.html

** Working on https://stackoverflow.com
   added to database with id:6
   short url:4xct4
   decoded url id:6
   url retrieved from database: https://stackoverflow.com
```
From this it can be seen that the generated short urls are clearly none 
sequential, even with regularly sequential ids.

## Comments
Super little library with a well designed and polished interface. The
default encoder as used above will, of course, be less secure as anyone
with access to the source can work out appropriate values to use.

Creating a custom encoder is very simple. It merely requires an instance
of `UrlEncoder()` being created with a different _alphabet_, that is a
personalised ordering of characters to use in the short urls. The default 
alphabet is `mn6j2c4rv8bpygw95z7hsdaetxuk3fq`, but by shuffling this
around a new—and unpredictable—short url scheme will be created.

Example:
```python
new_alphabet = 'qmn6j2c4rv8bpygw95z7hsdaetxuk3f'
new_encoder = short_url.UrlEncoder(alphabet=new_alphabet)

read_row = 'SELECT id, url FROM urls'
cur.execute(read_row)
print(f'{"url":^40}|{"default":^10}|{"new":^10}')
print(f'{"-"*40}+{"-"*10}+{"-"*10}')
for row in cur.fetchall():
    id, url = row
    ori_short = short_url.encode_url(id)
    new_short = new_encoder.encode_url(id)
    print(f'{url:<40}|{ori_short:^10}|{new_short:^10}')
```
Result:
```text
                  url                   | default  |   new    
----------------------------------------+----------+----------
https://codechalleng.es/100days/        |  867nv   |  vnzmr   
https://pybit.es                        |  25t52   |  j9e9j   
https://pybit.es/pages/articles.html    |  ghpzy   |  y7b5p   
http://pbreadinglist.herokuapp.com      |  6vyv6   |  nrprn   
https://pybit.es/pages/challenges.html  |  pbq8b   |  b8fv8   
https://stackoverflow.com               |  4xct4   |  ct2ec   
```
In this example I have purely moved the 'q' from the end of the default
alphabet to the beginning of a _new alphabet_.  Examining the results it
is clear that the short codes generated are the same, but the characters
have been shuffled—for example, what was '8' in the default code changes
to 'v' in the new code (first and fifth entries), and so on.

Modifying the block_size or specifying a different key length would 
introduce further variance.
