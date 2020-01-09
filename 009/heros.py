from collections import defaultdict

from dotted.utils import dot_json

with open('hero_defines.json') as f:
    heros = dot_json(f.read())

tag_list = defaultdict(list)

for h in heros:
    print(f'{h.id:>3}:{h.seat_id:<3} {h.name:<35}{h.properties.type:^8}{",".join(h.properties.tags)}')
    for t in h.properties.tags:
        tag_list[t].append(h)

for t in tag_list:
    print(f'Type: {t}')
    for h in tag_list[t]:
        print(f'  {h.name}')
