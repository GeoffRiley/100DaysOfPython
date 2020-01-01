from pypattyrn.behavioral.chain import Chain, ChainLink


class LinkThree(ChainLink):
    def handle(self, request):
        if request == 'three':
            return 'Handled three'
        else:
            return self.successor_handle(request)


class LinkTwo(ChainLink):
    def __init__(self):
        super().__init__()
        self.set_successor(LinkThree())

    def handle(self, request):
        if request == 'two':
            return 'Handled two'
        else:
            return self.successor_handle(request)


class LinkOne(ChainLink):
    def __init__(self):
        super().__init__()
        self.set_successor(LinkTwo())

    def handle(self, request):
        if request == 'one':
            return 'Handled one'
        else:
            return self.successor_handle(request)


class ChainHead(Chain):
    def __init__(self):
        super().__init__(LinkOne())

    def fail(self):
        return 'Not recognised'


chain = ChainHead()

assert chain.handle('one') == 'Handled one'
assert chain.handle('two') == 'Handled two'
assert chain.handle('three') == 'Handled three'
assert chain.handle('four') == 'Not recognised'
