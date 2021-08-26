# def: 定义函数 define function
from typing import Mapping


def print_hello():
    print("Hello World")


# print_hello()


# 定义有参数的函数string, 输出hello
def print_hello_string(str_word):
    print(str_word)


# print_hello_string("hello")

# return


def print_hello_return():
    return "Hello World"


_ = print_hello_return()
# print(_)


def add(a=0, b=0, c=0):
    return a + b + c

# # 只有在当前文件执行时, 才会执行
# if __name__ == "__main__":
#     # print(add(1, 2, 3))
#     pass


# 列表[] 元组() 字典{}
list1 = [1, 3, 5, 7, 100]
tuple1 = (1, 3, 5, 7, 100)
dict1 = {
    "name": "张三",
    "age": 18
}

# print(list1[-1])  # -1从后往前取

# # 添加元素
# list1.append(200)  # 往后追加
# list1.insert(1, 400)
# print(list1)

# # 删除元素
# list1.remove(3)  # 删除指定元素
# print(list1)

# # 按照索引删除
# del list1[0]
# print(list1)


# # 排序
# list2 = [10, 9, 8, 7, 100]
# print(sorted(list2, reverse=True))

# # 改变原始列表
# list2.sort()
# print(list2)

# list3 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# print(sorted(list3, key=len))  # key 接收函数


# # 元组 元组中的元素是无法修改  添加、删除、修改
# t = ('张三', 38, True, '四川成都')
# print(t)

# # 修改元素
# list_t = list(t)
# list_t[0] = '王大锤'
# print(tuple(list_t))


# 集合 set
# set1 = {1, 2, 3, 3, 3, 2}
# print(set1)

# list4 = [1, 2, 3, 3, 3, 2]
# tuple4 = (1, 2, 3, 3, 3, 2)
# print(set(list4))
# print(set(tuple4))

# # 添加元素
# set1.add(4)
# print(set1)


# set2 = set(range(1, 10))  # 左闭右开
# print(set2)

# # 一次性添加多个元素
# set2.update([10, 11, 12])
# print(set2)

# # 丢弃元素
# set2.discard(5)
# print(set2)

# # 从左边丢掉一个元素
# set2.pop()
# set2.pop()
# print(set2)


# 字典

scores = {'张三': 95, '李四': 78, '王五': 82}
# 通过键可以获取字典中对应的值
# print(scores['张三'])


# for key in scores:
#     print(key, scores[key])

# 一次性取出键和值
for key, value in scores.items():
    print(key, value)

# # 修改值
# scores['张三'] = 100

# # 一次性取出键和值
# for key, value in scores.items():
#     print(key, value)

# # 判断键是否存在
# if '张三1' in scores:
#     print(scores['张三'])
# else:
#     print("不存在")
    
# # get方法
# print(scores.get('张三'))
# print(scores.get('张三', 200))  # 如果键存在, 不管是否有默认值, 都返回原值
# print(scores.get('张三1', 100))  # 如果键不存在, 则返回默认值

# # 删除字典中的元素
# print(scores.popitem())  # 返回的是删除的键值对
# print(scores.popitem())
# print(scores.pop('张三', 95))  # 返回删除的值
# print(scores)

