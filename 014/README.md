# Day 14: 14<sup>th</sup> January 2020
Try out awesome library [_funcy_](https://github.com/Suor/funcy) 
—A fancy and practical functional tools.

## Requirements
`pip install funcy`

## Notes
In the developers own words, _funcy_ is 'a collection of fancy functional
tools focused on practicality.'

This library is fully compatible with Python 2 and 3 but has an 
interesting take on some of the function nomenclature to reflect the
version of Python being used. This is in the cases where a function
could take either a `list` or an `iterator` object… Python 2 defaults to 
the former whereas Python 3 the latter in common with each versions
standard libraries.

### Full table of python dependent function names
From documentation [Python 2/3](https://funcy.readthedocs.io/en/stable/python3.html).

Python 2 list | Python 2 iterator | Python 3 list | Python 3 iterator
---             | ---           | ---           | ---
map             | imap          | lmap          | map
filter          | ifilter       | lfilter       | filter
zip()           | izip          | lzip          | zip()
remove          | iremove       | lremove       | remove
keep            | ikeep         | lkeep         | keep
without         | iwithout      | lwithout      | without
concat          | iconcat       | lconcat       | concat
cat             | icat          | lcat          | cat
flatten         | iflatten      | lflatten      | flatten
mapcat          | imapcat       | lmapcat       | mapcat
distinct        | idistinct     | ldistinct     | distinct
split           | isplit        | lsplit        | split
split_at        | isplit_at     | lsplit_at     | split_at
split_by        | isplit_by     | lsplit_by     | split_by
partition       | ipartition    | lpartition    | partition
chunks          | ichunks       | lchunks       | chunks
partition_by    | ipartition_by | lpartition_by | partition_by
reductions      | ireductions   | lreductions   | reductions
sums            | isums         | lsums         | sums
juxt            | ijuxt         | ljuxt         | juxt
where           | iwhere        | lwhere	    | where
pluck           | ipluck        | lpluck	    | pluck
pluck_attr      | ipluck_attr   | lpluck_attr   | pluck_attr
invoke          | iinvoke       | linvoke       | invoke
-               | izip_values   | -             | zip_values
-               | izip_dicts    | -             | zip_dicts

The above list is _only_ the functions that have variance of implementation
for the different platforms, it only scratches the surface of the full 
set of functions available in the _funcy_ library.

The library functions cover a huge range of different techniques, 
covering sequences, collections, functions, decorators, flaw, string
utils, calculation, type testing, objects, debugging and primitives.

Some functions do nothing in Python 3 as they are designed to bring 
aspects of Python 3 to users of Python 2.  No doubt these will be removed
as Python 2 increasingly disappears. Python 2.6 support has been removed 
already.

## Outcome
Just reading through all the functions of this library is an undertaking,
so I didn't write any code as such but tried out a number of the 
functions at the Python console.

## Comments
This is one very cool—**awesome**—library that contains many very useful
tools that more than just hint at a foundation in functional programming.
