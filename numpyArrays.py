#! python3
# numpyArrays.py - read large csv into 3D array using numpy
# OSU CS 519
# by Paul ReFalo 30 Nov 2017

from numpy import genfromtxt

npArray = genfromtxt('array-final.txt', dtype=int, delimiter=',')       # read in .txt to np array

arr3D = npArray.reshape((50, 50, 50)) # shape 125000 elements into 50 x 50 x 50 cube

def findCube(arr3D):    # function takes a 3D numpy array and finds largest value of 3 x 3 x 3 cube and index
    highestCube = 0          # local var to hold result
    highestCubeIndex = [0, 0, 0]    # local var for index result

    for i in range(0, 48):      # nested i, j, k loop for each dimension of 3D array
        for j in range(0, 48):
            for k in range(0, 48):
                cube = arr3D[i:i+3, j:j+3, k:k+3]       # slice 3 x 3 x 3 cube from larger array at index [i, j, k]
                sumCube = cube.sum(-1).sum(-1).sum(-1)  # sum the 27 elements
                if sumCube > highestCube:           # if sum is highest yet, update value and index of highest
                    highestCube = sumCube
                    highestCubeIndex = [i, j, k]

    # print results and return them
    print('The highest 3 x 3 x 3 cube value is: ', highestCube)
    print('The index of the highest value cube nearest the origin is: ', highestCubeIndex)
    return(highestCube, highestCubeIndex)

def get2Darray(arr3D):  # function takes a 3D numpy array and sums first dimension into a 50 x 50 2D array
    arr2D = arr3D[0:50].sum(-1)         # create new 2D numpy array by summing the row
    print('The 50 x 50 2D array of sums is:')
    print(arr2D)    # print and return arr2D
    return(arr2D)

# Call functions and get results
maxCube, maxCubeIndex = findCube(arr3D)  # 198541 and [35, 3, 36]
print('=========================================')
arr2D = get2Darray(arr3D)


'''
Example Output:
The highest 3 x 3 x 3 cube value is:  198541
The index of the highest value cube nearest the origin is:  [35, 3, 36]
=========================================
The 50 x 50 2D array of sums is:
[[264072 277397 229712 ..., 262733 254362 262602]
 [253473 291426 210584 ..., 228267 271821 257256]
 [309368 260653 264055 ..., 264513 264948 250184]
 ..., 
 [226719 260804 251889 ..., 280459 242387 272088]
 [266683 254895 250290 ..., 238804 251329 274558]
 [244105 284355 237605 ..., 253670 238710 273112]]
 
 '''