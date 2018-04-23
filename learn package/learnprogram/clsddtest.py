# -*- coding: utf-8 -*-
'class test'

class Student(object):
    def __init__(self,name):
        self.name=name
    def __li__(self):
        return 'Student object (name:%S)'%self.name
print Student('Michael')
