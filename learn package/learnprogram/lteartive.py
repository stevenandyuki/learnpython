# -*- coding: utf-8 -*-
# 迭代
'lteartive test'
def findMixAndMax(L):
    if len(L)==0:
        return ('none,none')
    min=L[0]
    max=L[0]
    for i in L:
        if max < i:
            max =i
        if max > i:
            min=i
    return (min,max)

print findMixAndMax([1,2,7])


