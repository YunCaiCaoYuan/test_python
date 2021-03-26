#!/usr/bin/python
import demjson

if __name__ == '__main__':
    # data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    # data = {'result': 'this is a test'}
    # data = {'result': '这是一个测试'}
    # data = {'result': "这是一个测试"}
    data = {'result': str("这是一个测试")}

    json = demjson.encode(data)
    print(json)
