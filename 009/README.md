# Day 9: 9<sup>th</sup> January 2020
Try out awesome library [_dotted_](https://github.com/carlosescri/DottedDict)
—A library that provides a method of accessing lists and dicts with a dotted path notation.

## Requirements
`pip install dotted`

## Notes
A very interesting little library here: sometimes nested levels of list 
and/or dictionaries can lead to a profusion of square brackets directing
down to the appropriate level and make the code far less readable than
it could be.  This _dotted_ library takes the general principle of 
reaching the target element and allows it to be squashed down into a 
more concise format.

This is particularly useful when it comes to JSON files which can tend 
toward being deeply nested.

## Outcome
I fished out a JSON file from an on-line game and used 
`dotted.utils.dot_json()` to load in the file. It worked perfectly and
made it very simple to pick out details in order to tabulate some 
elements from the file.  Additionally, it is easy to use the extracted
information to select records and massage them into different sequences.

As an example the JSON file that I picked out holds the details of a set
of `heros` from the game. Each hero has a set of `tags` that specify
what abilities or attributes the hero is empowered with. I took these 
tags and built up a secondary list composed of heros with matching tags.

## Comments
Of course the same could be performed using the standard _json_ library, 
but it would have been more verbose and therefore less readable.
