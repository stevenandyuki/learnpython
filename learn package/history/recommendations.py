
critics={'Lisa Rose':{'Lady in the Water':2.5,'Snakes on a Plane':3.5,
                      'Just My Luck':3.0,'Superman Returns':3.5,  
                      'You,Me and Dupree':2.5,'The Night Listener':3.0},                      
         'Gene Seymour':{'Lady in the Water':3.0,'Snakes on a Plane':3.5,   
                         'Just My Luck':1.5,'Superman Returns':5.0,  
                         'The Nighr Listener':3.0,'You,Me and Dupree':3.5},  
         'Michael Phillips':{'Lady in the Water':2.5,  
                              'The Nighr Listener':4.0},  
         'Claudia Puig':{'Snakes on a Plane':3.5,'Just My Luck':3.0,  
                         'The Night Listener':4.5,'Superman Returns':4.0,  
                         'You,Me and Dupree':2.5},  
         'Mick LaSalle':{'Lady in the Water':3.0,'Snakes on a Plane':4.0,  
                         'Just My Luck':2.0,'Superman Returns':3.0,  
                         'The Night Listener':3.0,'You,Me and Dupree':2.0},  
         'Jack Matthews':{'Lady in the Water':3.0,'Snakes on a Plane':4.0,  
                          'The Night Listener':3.0,'Superman Returns':5.0,  
                          'You,Me and Dupree':3.5},  
         'Toby':{'Snakes on a Plane':4.5,'You,Me and Dupree':1.0,  
                 'Superman Returns':4.0}}
from math import sqrt

def sim_person(perfs,p1,p2) :
 si={}
 for item in perfs[p1] :
  if item in perfs[p2]:
   si[item]=1
 n=len(si)  
  if len(si)==0 ：
   return 1
 sum1=sum((prefs[p1][item] for item in si))  
 sum2=sum((perfs[p2][item] for item in si))
 sum1sq=sum((pow(perfs[p1][item],2)for item in si))
 sum2sq=sum((pow(perfs[p2][item],2)for item in si))
 
 pSum=sum(pow(perfs[p1][item])*pow(perfs[p2][item]) for item in si )
 
 num=pSum-(sum1*sum2/n)
 den=sqrt((sum1sq-pow(sum1,2)/n)*(sum2sq-pow(sum2,2)/n))
 if den=0:
  return 0
  
 x=num/den
 return x
 
print sim_person(critics,"Jack Matthews",'Toby')