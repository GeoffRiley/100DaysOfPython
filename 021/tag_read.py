import os
from math import floor

from tinytag import TinyTag

directory = os.path.expanduser('~/Music')

for file in os.listdir(directory):
    if file.lower()[-4:] in ['.mp3', '.ogg']:
        tag = TinyTag.get(os.path.join(directory, file))
        print(f'File: {file}')
        print(f'\tTitle: {tag.title}')
        print(f'\tArtist: {tag.artist}')
        t = divmod(tag.duration, 60)
        ms = round((t[1] - floor(t[1])) * 1000)
        t = [floor(x) for x in t]
        print(f'\tDuration: {t[0]}m {t[1]}s {ms}ms')
        print()
