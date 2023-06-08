#!/usr/bin/python3
from hidden_4 import *
if __name__ == "__main__":
    m_names = dir(hidden_4)
    filter_n = [n for n in m_names if not name.startswith('__')]
    sort_n = sorted(filter_n)
    for i in sort_n:
        print(i)
