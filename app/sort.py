import random
R = random.Random(42)

def qsort(L):
    quicksort(L,0,len(L))

def quicksort(L,start,stop):
    if stop - start < 2: return
    key = L[R.randrange(start,stop)]
    e = u = start
    g = stop
    while u < g:
        if L[u] < key:
            swap(L,u,e)
          e = e + 1
          u = u + 1
        elif L[u] == key:
            u = u + 1
        else:
            g = g - 1
            swap(L,u,g)
    quicksort(L,start,e)
    quicksort(L,g,stop)

def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

L = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9]
qsort(L)
print L
