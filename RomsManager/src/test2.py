# -*- coding : utf-8 -*-
'''
Created on 2021. 4. 5.

@author: evegood

@description :
'''

import csv

fp = csv.reader(open('systemId.csv'))

fpow = open('system_id.csv','w')
fpw = csv.writer(fpow, lineterminator='\n', quotechar='"', quoting=csv.QUOTE_ALL)

for line in fp:
    uid = line[0]
    s_list = line[1:]
    tmpList = []
#     print(s_list)
    for s_ in s_list:
        sy = s_.strip()
        tmpList.append(sy)
    print(tmpList)
    fpw.writerow([uid]+tmpList)
