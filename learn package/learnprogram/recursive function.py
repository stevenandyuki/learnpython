# -*- coding: utf-8 -*-

def move(n,A,B,C):
    if n==1:
        print A,"->",C
    else :
        move(n-1,A,C,B)
        move(1,A,B,C)
        move(n-1,B,A,C)

move(4,'A','B','C')

