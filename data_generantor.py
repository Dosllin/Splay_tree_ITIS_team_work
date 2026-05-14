import numpy as np
import random
from splay import SplayTree
import time
import matplotlib.pyplot as plt

arr = np.array([random.randint(1, 10**6) for x in range(10_000)])

pick_100 = np.random.choice(arr, 100, replace=False)
pick_1000 = np.random.choice(arr, 1000, replace=False)


splay_tree = SplayTree()
for i in arr:
    splay_tree.insert(i)


insert_times = []
insert_iterations = []

search_times = []
search_iterations = []

delete_times = []
delete_iterations = []


# INSERT TEST


test_tree = SplayTree()

for value in arr:
    test_tree.reset_iterations()

    start = time.perf_counter()

    test_tree.insert(value)

    end = time.perf_counter()

    insert_times.append(end - start)
    insert_iterations.append(test_tree.get_iterations())


# SEARCH TEST


for value in pick_100:
    test_tree.reset_iterations()

    start = time.perf_counter()

    test_tree.find(value)

    end = time.perf_counter()

    search_times.append(end - start)
    search_iterations.append(test_tree.get_iterations())


# DELETE TEST


for value in pick_1000:
    test_tree.reset_iterations()

    start = time.perf_counter()

    test_tree.delete(value)

    end = time.perf_counter()

    delete_times.append(end - start)
    delete_iterations.append(test_tree.get_iterations())


# AVERAGES


avg_insert_time = sum(insert_times) / len(insert_times)
avg_insert_iter = sum(insert_iterations) / len(insert_iterations)

avg_search_time = sum(search_times) / len(search_times)
avg_search_iter = sum(search_iterations) / len(search_iterations)

avg_delete_time = sum(delete_times) / len(delete_times)
avg_delete_iter = sum(delete_iterations) / len(delete_iterations)

print("\n========== INSERT ==========")
print("AVG TIME:", avg_insert_time)
print("AVG ITER:", avg_insert_iter)

print("\n========== SEARCH ==========")
print("AVG TIME:", avg_search_time)
print("AVG ITER:", avg_search_iter)

print("\n========== DELETE ==========")
print("AVG TIME:", avg_delete_time)
print("AVG ITER:", avg_delete_iter)


# GRAPHS


plt.figure(figsize=(10, 5))
plt.plot(insert_times)
plt.title("Insert Time")
plt.xlabel("Operation")
plt.ylabel("Time")
plt.grid()

plt.figure(figsize=(10, 5))
plt.plot(search_times)
plt.title("Search Time")
plt.xlabel("Operation")
plt.ylabel("Time")
plt.grid()

plt.figure(figsize=(10, 5))
plt.plot(delete_times)
plt.title("Delete Time")
plt.xlabel("Operation")
plt.ylabel("Time")
plt.grid()

plt.figure(figsize=(10, 5))
plt.plot(insert_iterations)
plt.title("Insert Iterations")
plt.xlabel("Operation")
plt.ylabel("Iterations")
plt.grid()

plt.figure(figsize=(10, 5))
plt.plot(search_iterations)
plt.title("Search Iterations")
plt.xlabel("Operation")
plt.ylabel("Iterations")
plt.grid()

plt.figure(figsize=(10, 5))
plt.plot(delete_iterations)
plt.title("Delete Iterations")
plt.xlabel("Operation")
plt.ylabel("Iterations")
plt.grid()

plt.show()
