import numpy as np
import random
from splay import SplayTree

arr = np.array([random.randint(1, 10**6) for x in range(10_000)])

pick_100 = np.random.choice(arr, 100, replace=False)
pick_1000 = np.random.choice(arr, 1000, replace=False)


splay_tree = SplayTree()
for i in arr:
    splay_tree.insert(i)