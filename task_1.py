import random as rnd
#arr = rnd.sample(range(10), 9)
arr = [1, 0, 6, 0, 0, 55, 10, 66, 0, 4, 9]
print[arr]
def calc(massiv, nulik):
    j, i = 0, 0
    while i < len(massiv) -j:
        #print ("index ", i, massiv)
        if massiv[i] == nulik:
            j += 1
            massiv.append(massiv.pop(i))
            print ("after ", massiv)
        else:
            i += 1

calc(arr, 0)
print ("result ", arr)