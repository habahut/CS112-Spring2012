#! usr/bin/env python

class Borg(object):
    _shared_dict = {}

    def __init__(self):
        self.__dict__ = Borg._shared_dict


## lots of instances, but they all have the same values

A = Borg()
A.x = 3
A.y = 4

B = Borg()
print B.x, B.y

B.x = 7

print A.x
