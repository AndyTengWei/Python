import numpy as np

w = np.zeros(6)
x = np.zeros(6)

y = np.zeros(6)
f = open("C:\\Users\\Administrator\\Desktop\\training_set.txt", 'r')
lines = f.readlines()
for line in lines:
    np.array(line.split(" "))
    print(x[0])

f.close()