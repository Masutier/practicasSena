import numpy as np



sample_list = [1, 2, 3]
my_matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]


sl = np.array(sample_list)
mm = np.array(my_matrix)

arr1 = np.arange(0,5)
arr2 = np.arange(1,11,2)

new0arr = np.zeros(4)
new1arr = np.ones(5)

linarr = np.linspace(0, 1, 10)

eye1Arr = np.eye(1)
eye5Arr = np.eye(5)
eye50Arr = np.eye(50)

rand1arr = np.random.rand(1)
rand5arr = np.random.randn(5)
randintarr = np.random.randint(1, 10)


arr = np.array([0,1,2,3,4,5])

resh = arr.reshape(2,3)

sum1 = 2 + arr
sum2 = arr + arr

res1 = 2 - arr
res2 = arr - arr

print(sl)
print(mm)

print(arr1)
print(arr2)

print(new0arr)
print(new1arr)

print(linarr)

print(eye1Arr)
print(eye5Arr)
print(eye50Arr)

print(rand1arr)
print(rand5arr)
print(randintarr)

print(resh)

print(sum1)
print(sum2)

print(res1)
print(res2)