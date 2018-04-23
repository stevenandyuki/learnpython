# -*- coding: utf-8 -*-
# 切片
'a cut test file'
def cut(s):
    n=len(s)
    print n
    for i in range(n):
     if s[0:1]==' ':
        s=s[1:]
        b=len(s)
     elif s[-1:]==' ':
         n=n-1
         s=s[0:n]
         print n
     else :
         return s


def p(s):
    if s[:1]==' ':
        return p(s[1:])
    if s[-1:]==' ':
        return p(s[:-1])
    return s




