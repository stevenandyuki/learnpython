class Person:
 '''Represents is a person'''
 population=0
 
 def __init__(self,name):
  '''In itializes ther person's data'''
  self.name=name
  print'(In itializes%s)'%self.name
  
  Person.poplulation+=1
  
 def __del__(self):
  '''I am dying'''
  print '%ssaysbye'%self.name
 
  Person.poplulation-=1
 
  if Person.population==0:
   print 'I am the last one'
  else :
   print 'There are still%d people left'%Person.population
 
 def sayHI(self):
  '''Greeting by the person'''
  print 'HI,myname is%s'%self.name
  
 def howMany(self):
  '''print the current population'''
  if Person.population==1:
   print 'I am the only person here'
  else :
   print "We have %d persons here"%Person.population

swaroop=Person('Swaroop')
swaroop.sayHI()
swaroop.howMany()

kalam = Person('Ab dul Kalam')
Kalam.sayHI()
Kalam.howMany()

swarrop.sayHI()
swaroop.howMany()
