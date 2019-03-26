#!/usr/bin/python
# -*- coding: UTF-8 -*-
# URL：：http://www.runoob.com/python/func-number-random.html 
import random
'''
print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数  
print( random.random() )             # 产生 0 到 1 之间的随机浮点数
print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
#print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数
'''
a=[1,3,5,6,7, 200,999]                # 将序列a中的元素顺序打乱
print("org= ", a) 
random.shuffle(a)
print(a)

afloat =[10.01, 20.2002, 30.30003, -120.0001]
print("ORG Floating num. List ", afloat)
print(afloat) 
random.shuffle(afloat)
print("Now, Shuffled as ", end=" -- " )
print(afloat)

'''
# https://pynative.com/online-python-code-editor-to-execute-python-code/ 
'''
# import random
weight_set = {40, 50, 55, 65, 75,80}
print ("使用Sample()方法從集合中選擇 4 個隨機項:: ",random.sample(weight_set, k=4))
# 
marks_dict = {
  "Kelly": 55,
  "jhon": 70,
  "Donald": 60,
  "Lennin" :50,
  "Yao1" : "初九:潛龍，勿用",
  "Yao6" : "上九:亢龍有悔", 
  "用九": "見群龍無首，吉"
}
print ("Test1:: 選擇1個隨機項目：：",random.sample(marks_dict.items(), k=1))
print ("Test2:: 選擇2個隨機項目：：",random.sample(marks_dict.items(), k=2))
print ("Test3:: 選擇3個隨機項目：：",random.sample(marks_dict.items(), k=3))

#
import numpy
print("4 x 4 array of ints between 10 and 20 inclusive：：")
newArray = numpy.random.randint(10, 50, size=(4, 4))
print(newArray)