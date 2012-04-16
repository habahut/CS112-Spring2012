#! us/r/bin/env ptython

def not_none(call):
    for v in call:
        if v is not None:
            yield v

N = 0
E = 1
S = 2
W = 3


class Cell:
    def __init__(self):
        self._neighbors = [None, None, None, None]

    # whenever you assign a value to north it calls this method
    @property
    def north(self): return self._neighbors[N]
    @north.setter
    def north(self,value):
        if isinstance(value, Cell):
            self._neighbors[N] = value
            value._neighbor[S] = self

    @north.deleter
    def north(self):
        if self._neighbors[N]:
            # delete my north neighbors south neighbor
            # aka delete self
            del self._neighbors[N]._neighbors[S]
            #or, because "_neighbors" is a list
            #self._neighbors[N].remove(self)
            
    @property
    def south(self): return self._neighbors[S]
    @south.setter
    def south(self,value):
        if isinstance(value, Cell):
            self._neighbors[S] = value
            
            
    @property
    def east(self):  return self._neighbors[E]
    @property
    def west(self):  return self._neighbors[W]


cellA = Cell()
cellB = Cell()

# since it is a property we can call it without ()
print cellA.north
cellA.north = cellB

