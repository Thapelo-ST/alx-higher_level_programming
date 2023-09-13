#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, attr, value):
        if not hasattr(self, attr) and attr != 'first_name':
            raise AttributeError(f"'LockedClass' object has no attribute '{attr}'")
        object.__setattr__(self, attr, value)

