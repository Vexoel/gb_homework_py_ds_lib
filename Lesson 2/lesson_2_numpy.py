# Lesson 2 “Вычисления с помощью Numpy”

import numpy as np


def print_array(arr):
    print(arr)
    print("Размерность: {}".format(arr.ndim))
    print("Форма: {}".format(arr.shape))
    print()


# Task 1
print('Task 1')
a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])
print('a')
print_array(a)

mean_a = np.mean(a, axis=0)
print('mean_a')
print_array(mean_a)

# Task 2
print('Task 2')
a_centered = np.subtract(a, mean_a)
print('a_centered')
print_array(a_centered)

# Task 3
print('Task 3')
a_centered_sp = a_centered[:, 0].dot(a_centered[:, 1])
print(a_centered_sp / (a.shape[0] - 1))

# Task 4
print('Task 4')
print(np.cov(a.T)[0][1])
