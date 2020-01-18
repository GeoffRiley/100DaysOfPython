import pyshorteners

print('\n'.join([f'Shorteners.{s}' for s in dir(pyshorteners.Shorteners) if not s.startswith('__')]))
# Shorteners.ADFLY
# Shorteners.AWSM
# Shorteners.BITLY
# Shorteners.CHILPIT
# Shorteners.CLCKRU
# Shorteners.DAGD
# Shorteners.GOOGLE
# Shorteners.ISGD
# Shorteners.OSDB
# Shorteners.OWLY
# Shorteners.QPSRU
# Shorteners.QRCX
# Shorteners.READABILITY
# Shorteners.SENTALA
# Shorteners.SIMPLE
# Shorteners.TINYURL
# Shorteners.WPACO

from pyshorteners import Shorteners

s = pyshorteners.Shortener(Shorteners.TINYURL)
shorturl = s.short('https://codechalleng.es/')
print(shorturl)
