import sys
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import re
import Sites
import handler
import dbhandler





def main():
    print("hello")

    k=Sites.Site("ksp","https://ksp.co.il/")
    k.print()
    db=dbhandler.mydb()
    db.initlinkstable()
    db.inititemstable()
    db.addlinks(k.getlink() ,handler.getlinksfromhtmlbylink(k.getlink()))
    #db.getitems()
    #takeitems(k)
    print(db.getitems())
    #handler.getprice("https://ksp.co.il/?select=.1044..35.&kg=&sis=&list=1&sort=2&glist=1&uin=123585&txt_search=&buy=&minprice=0&maxprice=0&intersect=..&rintersect=&store_real=")

def takeitems(k):
    db=dbhandler.mydb()
    links=db.getlinks()
    print(links)
    for i in links:
        try:
            print(sendlink(i))
            print(k.getlink().find("ksp"))
            print(sendlink(i).find("uin"))
            if(k.getlink().find("ksp")!=-1 and sendlink(i).find("uin")==-1):
                continue
            a=handler.getprice(sendlink(i))
            if(a!=-1):
            
                
                db.additem(k.getlink(),sendlink(i),a)
        except:
            continue
    

def sendlink(a):
    s="https"
    if(a[1].find(s)!=-1):
        return a[1]
    else:
        return s+"://"+a[1]
main()