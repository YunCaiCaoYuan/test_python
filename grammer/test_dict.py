#!/usr/bin/python
#-*- coding:UTF-8 -*-

if __name__ == '__main__':
    dict1 = {}
    list = ["蓝色", "红色"]

    for i in range(0, 10) :
        for k in list:
            list_1 = dict1.get(k, [])
            list_1.append(i)
            dict1[k] = list_1

    print dict1
