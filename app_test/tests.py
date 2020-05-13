# from django.test import TestCase

# Create your tests here.
# import time
# import eventlet#导入eventlet这个模块
# eventlet.monkey_patch()#必须加这条代码
# with eventlet.Timeout(2,False):#设置超时时间为2秒
#    time.sleep(1)
#    print('没有跳过这条输出')
# print('跳过了输出')

import time
import timeout_decorator
import random

@timeout_decorator.timeout(5)
def mytest():
   a = random.randint(1,5)
   time.sleep(a)
   return a
while 1:
   try:
      print(mytest())
   except:
      print("超时退出")
      break