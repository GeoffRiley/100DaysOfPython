import operator

from pypattyrn.behavioral.chain import Chain, ChainLink


class CalcSub(ChainLink):
    def handle(self, request):
        if request == '-':
            return operator.sub
        else:
            return self.successor_handle(request)


class CalcAdd(ChainLink):
    def __init__(self):
        super().__init__()
        self.set_successor(CalcSub())

    def handle(self, request):
        if request == '+':
            return operator.add
        else:
            return self.successor_handle(request)


class CalcDivide(ChainLink):
    def __init__(self):
        super().__init__()
        self.set_successor(CalcAdd())

    def handle(self, request):
        if request == '/':
            return operator.floordiv
        else:
            return self.successor_handle(request)


class CalcMultiply(ChainLink):
    def __init__(self):
        super().__init__()
        self.set_successor(CalcDivide())

    def handle(self, request):
        if request == '*':
            return operator.mul
        else:
            return self.successor_handle(request)


class Calc(Chain):
    def __init__(self):
        super().__init__(CalcMultiply())

    def fail(self):
        raise TypeError('Unrecognised function')


calc = Calc()

the_sum = '5 * 4 + 1 / 7'

acc = 0
op = None
for s in the_sum.split():
    if s.isdigit():
        if op:
            acc = op(acc, int(s))
        else:
            acc = int(s)
    else:
        op = calc.handle(s)
print(f'{the_sum} → {acc}')

assert acc == 3
