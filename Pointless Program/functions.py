#!/usr/bin/env python

class A:
    pass

class B:
    pass

class Dangerous:
    pass

#redefine what import * actually imports
__all__ = ["A", "Dangerous"]
