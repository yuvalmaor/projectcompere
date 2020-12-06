import sys
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import re

def getprice(a):
    link=a
    try:
        r = requests.get(link)
    except:
        return -1
    #printlist(fixed)
    a=r.text

    a=a.splitlines()
    
    x=""
    for i in a:
	    x=x+i+"_"
    x = re.sub(r"<section .{0,}?\/section>", "", x)
    x = re.sub(r"<a .{0,}?\/a>", "", x)
    x = re.sub(r"<link [^\>]*\/>", "", x)
    x = re.sub(r"\(.{0,}?\)", "", x)
    x = re.sub("prices","",x)
    
    ret = re.findall(r"price[^0-9\(\)\<]*[0-9]+[^\<\>]*\<", x)
    #for i in ret:
        #print(i)

    r=[]
    if(len(ret)==0):
        return -1
    for i in ret:
       r.append(getiprice(i))

    return minprice(r)

       
def minprice(r):
    a=r[0]
    for i in r:
        if(i==-1):
            continue
        if(i<a):
            a=i
    return a 

def getiprice(a):
    b=re.findall(r"[0-9][0-9\.\,]*[0-9]", a)
    if(len(b)==0):
        return -1
    if(b[0].find('.')!=-1):
        b[0]=b[0][:b[0].find('.')]
    b[0]=b[0].replace(",", "")
    
    return int(b[0])
def gettextfromhtmlbylink(a):#not finish func
    link=a
    r = requests.get(link)
    #printlist(fixed)
    a=r.text
    b=r
    a=a.splitlines()

    x=""
    for i in a:
	    x=x+i+"_"
    
   
    for i in range(5):
        x = re.sub(r"\{[^\}\{]*\}", "", x)
        x = re.sub(r"\<[^\>\<]*\>", "", x)
        x = re.sub(r"\[[^\[\]]*\]", "", x)
        x = re.sub(r'\"[^\"]*\"', '', x)
        x = re.sub(r'\([^\(\)]*\)', '', x)
        x = re.sub("  ", " ", x)
    
    x = re.sub(r"\}", "", x)
    x = re.sub(r"\;", "", x)
    x = re.sub(r"\|", "", x)
    x = re.sub(r"if", "", x)
    x = re.sub(r"else","", x)
    x = re.sub(r"false","", x)
    x = re.sub(r"null","", x)
    x = re.sub(r"\:","", x)
    #x = re.sub(r"else","", x)
    x = re.sub(r"\(", "", x)
    #print(x)

    #print(a)
    #findcarddata(r.text,fixed[0])
    #return fixed 
    return x
    print("function in build")

def getlinksfromhtmlbylink(a):



    link=a
    r = requests.get(link)
    #printlist(fixed)
    a=r.text
    b=r
    a=a.splitlines()
    c=1
    ct=8
    x=""
    for i in a:
        x=x+i

        
        

        

    ret = re.findall(r"href=\"[^\"\>]*\"", x)
    print("got ret")
    return ret
    
    