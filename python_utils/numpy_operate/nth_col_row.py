# _*_ coding:utf-8 _*_

"""
This file is about ways to get nth column from array
"""
import numpy as np


def get_nth_column():
    """
    this is about how to get nth column from array
    :return:none
    """
    arr = np.arange(9).reshape((3, 3))
    print arr
    # [[0 1 2]
    #  [3 4 5]
    #  [6 7 8]]
    arr_c2 = arr[:, [0, 2]]  # arr_c2 deep copy from arr
    print arr_c2
    # [[0 2]
    #  [3 5]
    #  [6 8]]
    arr_c2[:, [0]] = 9
    print arr  # no change, as we see this is deep copy
    print arr_c2
    # [[9 2]
    #  [9 5]
    #  [9 8]]
    arr_c1 = arr[:, 0]
    print arr_c1
    # [0 3 6]
    arr_c11 = arr[:, [0]]
    print arr_c11
    # [[0]
    #  [3]
    #  [6]]


def get_nth_row():
    """
    get nth row
    :return: none
    """
    arr = np.arange(12).reshape(3, 4)
    print arr
    # [[ 0  1  2  3]
    #  [ 4  5  6  7]
    #  [ 8  9 10 11]]
    print arr[1, :]   # or just arr[1]
    # [4 5 6 7]


def change_nth_col_value():
    """
    change nth column value by condition
    :return:
    """
    arr = np.arange(12).reshape(4, 3)
    print arr
    a_col = arr[:, 0]
    print a_col
    # [0 3 6 9]
    print [a if a % 2 else 111 for a in arr[:, 0]]
    # [111, 3, 111, 9]
    print arr  # no change
    # [[ 0  1  2]
    #  [ 3  4  5]
    # [ 6  7  8]
    # [ 9 10 11]]

    for i in xrange(arr.shape[0]):
        if arr[i][0] % 2 == 0:
            arr[i][0] = 111

    print arr
    # [[111   1   2]
    #  [  3   4   5]
    # [111   7   8]
    # [  9  10  11]]

    arr = np.arange(12).reshape(4, 3)
    print [arr[i][0] if arr[i][0] % 2 else 111 for i in xrange(arr.shape[0])]
    # [111, 3, 111, 9]
    print arr
    # [[ 0  1  2]
    #  [ 3  4  5]
    # [ 6  7  8]
    # [ 9 10 11]]


def add_row_2arr():
    a1 = np.array([[0, 1, 2], [0, 2, 0]])
    a2 = np.array([[1, 1, 1], [2, 2, 2], [3, 2, 0]])
    print a2[:, 0]
    # [1 2 3]
    print [a2[:, 0] < 3]
    # [array([ True,  True, False], dtype=bool)]
    print a2[a2[:, 0] < 3]
    # [[1 1 1]
    #  [2 2 2]]

    a1 = np.vstack((a1, a2[a2[:, 0] < 3]))
    print a1
    # [[0 1 2]
    #  [0 2 0]
    #  [1 1 1]
    #  [2 2 2]]


def add_row_2arr_v2():
    a1 = np.array([[1, 2], [3, 4]])
    a2 = np.array([[5, 6]])
    print np.concatenate((a1, a2), axis=0)
    # [[1 2]
    #  [3 4]
    # [5 6]]
    print np.concatenate((a1, a2.T), axis=1)
    # [[1 2 5]
    #  [3 4 6]]


def add_row_2arr_v3():
    print np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]])
    # [1 2 3 4 5 6 7 8 9]
    print np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], axis=0)
    # [[1 2 3]
    #  [4 5 6]
    #  [7 8 9]]
    print np.append([[1, 2, 3], [4, 5, 6]], [[7], [8]], axis=1)
    # [[1 2 3 7]
    #  [4 5 6 8]]


def v_h_column_stack():
    print np.vstack(([1, 2, 3], [4, 5, 6]))
    # [[1 2 3]
    #  [4 5 6]]
    print np.column_stack(([1, 2, 3], [4, 5, 6]))
    # [[1 4]
    #  [2 5]
    # [3 6]]
    print np.hstack(([1, 2, 3], [4, 5, 6]))
    # [1 2 3 4 5 6]

    print np.hstack(([[1], [2], [3]], [[4], [5], [6]]))
    # equivalent to np.column_stack(([1, 2, 3], [4, 5, 6]))


def iter_row_column():
    arr = np.arange(6).reshape(2, 3)
    print arr
    # [[0 1 2]
    #  [3 4 5]]

    for r in arr:
        print r
    # [0 1 2]
    # [3 4 5]

    for c in arr.T:
        print c
    # [0 3]
    # [1 4]
    # [2 5]

    for c_idx in range(arr.shape[1]):
        print arr[:, c_idx]

    # [0 3]
    # [1 4]
    # [2 5]


def iter_sp_row():
    arr = np.arange(8).reshape(4, 2)
    print arr
    # [[0 1]
    #  [2 3]
    #  [4 5]
    #  [6 7]]
    lst_idx = [1, 3]
    for idx in lst_idx:
        print arr[idx]
    # [2 3]
    # [6 7]

    import operator
    print operator.itemgetter(lst_idx)(arr)
    # [[2 3]
    #  [6 7]]


def dic_arr_append():
    a1 = np.array([1, 2])
    d = {1: a1}
    # d[1].append([2, 3, 4])
    # AttributeError: 'numpy.ndarray' object has no attribute 'append'

    lst = [1, 2]
    a1 = np.array([lst])
    print a1
    # [[1 2]]
    d = {1: a1}
    np.append(d[1], [2, 3])
    print d
    # {1: array([[1, 2]])}

    print np.append(a1, [2, 3])
    # [1 2 2 3]
    print a1
    # [[1 2]]

    print np.append(a1, [[2, 3]])
    # [1 2 2 3]
    print np.append(a1, [[2, 3]], axis=0)
    # [[1 2]
    #  [2 3]]
    print a1
    # [[1 2]]

    # print np.append(a1, [2, 3], axis=0)
    # ValueError: all the input arrays must have same number of dimensions


def dic_arr_concat():
    lst = [1, 2]
    a1 = np.array([lst])
    print a1
    # [[1 2]
    #  [2 3]]
    d = {1: a1}

    # np.concatenate((d[1], [2, 3]))
    # ValueError: all the input arrays must have same number of dimensions

    print np.concatenate((d[1], [[2, 3]]))
    # [[1 2]
    #  [2 3]]
    print d
    # {1: array([[1, 2]])}

    print np.concatenate((a1, [[2, 3]]))
    # [[1 2]
    #  [2 3]]
    print a1
    # [[1 2]]

if __name__ == '__main__':
    # dic_arr_append()
    dic_arr_concat()
    # iter_sp_row()
    # iter_row_column()
    # v_h_column_stack()
    # add_row_2arr_v3()
    # add_row_2arr_v2()
    # add_row_2arr()
    # get_nth_column()
    # get_nth_row()
    # change_nth_col_value()
    pass
