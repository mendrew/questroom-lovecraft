import numpy as np

array_one = np.ones([5,7], dtype=np.float32)*2
array_some = np.ones([5,7], dtype=np.float32)* 5

print("array one: {}".format(array_one))
print("array some: {}".format(array_some))

mean = np.mean(np.array([array_one, array_some]), axis=0)
print("mean: {}".format(mean))
