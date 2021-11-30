import random
import sys
import threading
import resource
import datetime
from math import floor


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def quickSort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quickSort(a, p, q - 1)
        quickSort(a, q + 1, r)


def maxHepify(i, A, heapSize):
    l = (2 * i) + 1
    r = (2 * i) + 2
    if (l < heapSize) and (A[l] > A[i]):
        largest = l
    else:
        largest = i
    if (r < heapSize) and (A[r] > A[largest]):
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHepify(largest, A, heapSize)


def buildMaxHeap(A):
    for i in range(floor((len(A) - 1) / 2), -1, -1):
        maxHepify(i, A, len(A))


def heapSort(A):
    heapSize = len(A)
    buildMaxHeap(A)
    for i in range(len(A) - 1, -1, -1):
        A[0], A[i] = A[i], A[0]
        heapSize = heapSize - 1
        maxHepify(0, A, heapSize)


def bubbleSort(tab):
    for i in range(len(tab)-1, -1, -1):
        for j in range(0, i):
            if tab[j] < tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]

def insertionSort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key

losowa = []
for i in range(0, 100000):
    losowa.append(random.randint(0, 100000))

resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

sys.setrecursionlimit(1500000)


print("Dane losowe")######################################
tmp = losowa
start = datetime.datetime.now()
insertionSort(tmp)
stop = datetime.datetime.now()
print("Wynik = ", stop-start)

tmp = losowa
start = datetime.datetime.now()
heapSort(tmp)
stop = datetime.datetime.now()
print("Wynik = ", stop-start)


tmp = losowa
start = datetime.datetime.now()
bubbleSort(tmp)
stop = datetime.datetime.now()
print("Wynik = ", stop-start)


tmp = losowa
start = datetime.datetime.now()
quickSort(tmp, 0, len(tmp) - 1)
stop = datetime.datetime.now()
print("Wynik = ", stop-start)
print("done")

print("Dane posortowane")######################################
losowa.sort()
tmp = losowa
start = datetime.datetime.now()
insertionSort(tmp)
stop = datetime.datetime.now()
print("Wynik = ", stop-start)


tmp = losowa
start = datetime.datetime.now()
heapSort(tmp)
stop = datetime.datetime.now()
print("Wynik = ", stop-start)


tmp = losowa
start = datetime.datetime.now()
bubbleSort(tmp)
stop = datetime.datetime.now()
print("Wynik = ", stop-start)


tmp = losowa
start = datetime.datetime.now()
quickSort(tmp, 0, len(tmp) - 1)
stop = datetime.datetime.now()
print("Wynik = ", stop-start)
print("done")

print("Dane posortowane wstecz")######################################
losowa.sort(reverse=True)
tmp = losowa
start = datetime.datetime.now()
insertionSort(tmp)
stop = datetime.datetime.now()
print("Wynik = ", stop-start)


tmp = losowa
start = datetime.datetime.now()
heapSort(tmp)
stop = datetime.datetime.now()
print("Wynik = ", stop-start)


tmp = losowa
start = datetime.datetime.now()
bubbleSort(tmp)
stop = datetime.datetime.now()
print("Wynik = ", stop-start)


tmp = losowa
start = datetime.datetime.now()
quickSort(tmp, 0, len(tmp) - 1)
stop = datetime.datetime.now()
print("Wynik = ", stop-start)
print("done")
