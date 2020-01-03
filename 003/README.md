# Day 3: 3<sup>rd</sup> January 2020
Try out awesome library [_valideer_](https://github.com/podio/valideer)
—Lightweight extensible data validation and adaptation library.

## Requirements
`pip install valideer`

## Notes
This is a validation suite with some pretty nifty built in setups. I'm trying it out using the password verification
scheme that was specified in the 2015 [Advent of Code](https://adventofcode.com/) puzzle for 
[Day 11: Corporate Policy](https://adventofcode.com/2015/day/11).

Quote from above site:
> Santa's previous password expired, and he needs help choosing a new one.
>
> To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.
>
> Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.
>
> Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:
>
> - Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
> - Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
> - Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

## Outcome
The password conformity can be encapsulated in a single class:
```python
import valideer
import re

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
```
This is a _User Defined Validator_, it can be registered with _valideer_ to be used as a validator like this:
```python
import valideer as V

V.register('santa_password', Password())
```
and then to use it an instance can be created and used like this:
```python
santa_pass = V.parse('santa_password').is_valid

trial_pwds = [
    'hijklmmn',
    'abbceffg',
    'abbcegjk',
    'abcdffaa',
    'ghjaabcc'
]

for pwd in trial_pwds:
    print(f'Password {pwd} → {santa_pass(pwd)}')
```
resulting in:
```text
Password hijklmmn → False
Password abbceffg → False
Password abbcegjk → False
Password abcdffaa → True
Password ghjaabcc → True
```

## Comments
I've only scratched the surface of this one, it's got a lot of scope for expansion, but even without expansion it has
a wide range of ready built verification filters.
