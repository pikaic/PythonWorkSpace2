# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:32:48 2017

@author: GFS49
"""

class Tree:
    __code=0
    __name=""
    __width=0
    __height=0
    __amount_spent=0
    
    def __init__(self,code,name,width,height,amount):
        self.__code=code
        self.__name=name
        self.__width=width
        self.__height=height
        self.__amount_spent=amount
        
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    
    def set_width(self,width):
        self.__width=width
    def get_width(self):
        return self.__width
    
    def set_height(self,height):
        self.__height=height
    def get_height(self):
        return self.__height
    
    def set_amount_spent(self,amount_spent):
        self.__amount_spent=amount_spent
    def get_amount_spent(self):
        return self.__amount_spent
    
class Mango(Tree):
    __yield=0
    
    def __init__(self,code,name,width,height,amount,yield1):
        self.__yield=yield1
        super(Mango,self).__init__(code,name,width,height,amount)
        
    def set_yield(self,yield1):
        self.__yield=yield1
    def get_yield(self):
        return self.__yield

class Garden:
    
    def __init__(self,t1,t2,m1,m2,m3):
        self.__t1=t1
        self.__t2=t2
        self.__m1=m1
        self.__m2=m2
        self.__m3=m3
        
    def total_amount_spent(self):
        return (self.__t1.get_amount_spent()+self.__t2.get_amount_spent()+self.__m1.get_amount_spent()+self.__m2.get_amount_spent()+self.__m3.get_amount_spent())
    
    def total_yield(self):
        return(self.__m1.get_yield()+self.__m2.get_yield()+self.__m3.get_yield())
        
t1=Tree(1,"Orange",10,40,1000)
t2=Tree(1,"Orange",10,40,1000)
m1=Mango(1,"mango",10,40,3000,50)
m2=Mango(1,"mango",10,40,4000,60)
m3=Mango(1,"mango",10,40,5000,70)
g=Garden(t1,t2,m1,m2,m3)
print("The toal amount spent is",g.total_amount_spent())
print("The toal yield from the mango trees is",g.total_yield())
