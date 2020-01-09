from dotted.collection import DottedCollection, DottedDict, DottedList

dlist = DottedList([0, 1, 2, 3, [4, 5, 6], 7, 8, [9, 10]])

assert dlist[0] == 0
assert dlist['1'] == 1
assert dlist['4.0'] == 4
assert dlist['4.1'] == 5
assert dlist['5'] == 7
assert dlist[5] == 7
assert dlist[7][1] == 10
assert dlist['7.1'] == 10

ddict = DottedDict({'hello': {'world': {'wide': 'web'}}})

assert ddict['hello'] == {'world': {'wide': 'web'}}
assert ddict['hello.world'] == {'wide': 'web'}
assert ddict['hello.world.wide'] == 'web'

assert ddict.hello == {'world': {'wide': 'web'}}
assert ddict.hello.world == {'wide': 'web'}
assert ddict.hello.world.wide == 'web'

dfact = DottedCollection.factory({
    'hello': [{'world': {'wide': ['web', 'web1', 'web2']}}]
})

assert dfact.hello.to_json() == '[{"world": {"wide": ["web", "web1", "web2"]}}]'
assert dfact['hello.0.world'].to_json() == '{"wide": ["web", "web1", "web2"]}'
assert dfact.hello[0].world['wide.0'] == 'web'
assert dfact.hello['0.world'].wide[1] == 'web1'
