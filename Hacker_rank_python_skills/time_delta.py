# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000


import math
import os
import random
import re
import sys

# Complete the time_delta function below.
# def time_delta(t1, t2):
#    times1 = (t1[-4:])
#    time2 = t2[-4 : ]
#    hours1,minutes1 =int(times1[:2]),int(times1[2:])*60
#    hours1 = hours1 * 60 * 60 + minutes1
#    hours2 , minutes2 = int(time2[:2])*60*60 ,int(time2[2:])*60
#    print(hours1 - hours2)

# if __name__ == '__main__':
#
#     t = int(input())
#
#     for t_itr in range(t):
#         t1 = input()
#
#         t2 = input()
#
#         delta = time_delta(t1, t2)

from datetime import datetime as dt


fmt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int(abs((dt.strptime(input(), fmt) -
                   dt.strptime(input(), fmt)).total_seconds())))