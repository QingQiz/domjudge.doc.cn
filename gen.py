#!/usr/bin/env python3
# -*- coding: utf-8 -*-


num = [4,2,19,7,0,3,5,8,0,3]

template1 = "* [{idx}]({idx}/README.md)"
template2 = "  * [{idx1}]({idx1}/{idx2}.md)"

string = ''
for i in range(len(num)):
    string += template1.format(idx=str(i + 1)) + '\n'
    for j in range(num[i]):
        string += template2.format(idx1=str(i + 1),
                                   idx2=str(i + 1) + '.' + str(j + 1)) + '\n'

print(string)
