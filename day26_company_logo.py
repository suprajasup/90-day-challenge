#!/bin/python3
from collections import Counter, OrderedDict
import math
import os
import random
import re
import sys


class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]




if __name__ == '__main__':
    s = input()
