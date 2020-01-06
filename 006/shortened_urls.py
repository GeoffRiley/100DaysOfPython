import sqlite3

import short_url

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

new_alphabet = 'qmn6j2c4rv8bpygw95z7hsdaetxuk3f'
new_encoder = short_url.UrlEncoder(alphabet=new_alphabet)

read_row = 'SELECT id, url FROM urls'
cur.execute(read_row)
print(f'{"url":^40}|{"default":^10}|{"new":^10}')
print(f'{"-" * 40}+{"-" * 10}+{"-" * 10}')
for row in cur.fetchall():
    id, url = row
    ori_short = short_url.encode_url(id)
    new_short = new_encoder.encode_url(id)
    print(f'{url:<40}|{ori_short:^10}|{new_short:^10}')
