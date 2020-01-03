import re

import valideer

"""
From Advent of Code 2015 Day 11
url: https://adventofcode.com/2015/day/11

Password verification

Corporate policy dictates that passwords must be exactly eight lowercase 
letters (for security reasons)…

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password 
requirements:

-   Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. 
    They cannot skip letters; abd doesn't count.
-   Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are 
    therefore confusing.
-   Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

"""


class Password(valideer.String):
    name = 'password'

    def __init__(self):
        super().__init__(min_length=8, max_length=8)
        self.required_length = 8

    def validate(self, value, adapt=True):
        super().validate(value)

        if len(list(filter(str.islower, value))) != self.required_length:
            raise valideer.ValidationError(f'All passwords must be {self.required_length} lower case characters long')
        if len(set(value).intersection('ilo')) > 0:
            raise valideer.ValidationError('Password must not contain the letters "i", "l" or "o"')
        if len(re.findall(r'(.)\1', value)) < 2:
            raise valideer.ValidationError('Password must contain at least two different, '
                                           'non-overlaping pairs of letters')
        v = bytearray(value, encoding='ascii')
        for n in range(len(v) - 2):
            if v[n] == v[n + 1] - 1 == v[n + 2] - 2:
                break
        else:
            raise valideer.ValidationError('Password must include one increasing straight of at least three letters')

        return value


valideer.register('password', Password())
validator = valideer.parse('password').is_valid

trial_pwds = [
    'hijklmmn',
    'abbceffg',
    'abbcegjk',
    'abcdffaa',
    'ghjaabcc'
]

for pwd in trial_pwds:
    print(f'Password {pwd} → {validator(pwd)}')
