import sys
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import re

import sqlite3

class mydb:
    def __init__(self):
        self.db="myTables.db"
        
    
    def initlinkstable(self):
        try:
            connection = sqlite3.connect(self.db) 
            crsr = connection.cursor() 
            sql_command = """CREATE TABLE links (  site VARCHAR(100), link VARCHAR(1000) UNIQUE);"""
            crsr.execute(sql_command)
            connection.commit() 
            connection.close()
        except:
            print("table exist")
        

    def inititemstable(self):
        try:
            connection = sqlite3.connect(self.db) 
            crsr = connection.cursor() 
            sql_command = """CREATE TABLE items (site VARCHAR(100),link VARCHAR(1000) UNIQUE,price int);"""
            crsr.execute(sql_command)
            connection.commit() 
            connection.close()
        except:
            print("table exist")
    
    def additem(self,site,link,sum):
        print(link[8:17])
        link=str(link)
        link=link[:len(link)-1]
        print(type(link))
        try:
            s='INSERT INTO items (site,link,price) VALUES ("'+site+'", "'+link+'",'+str(sum)+');'
            print(s)
            connection = sqlite3.connect(self.db) 
            crsr = connection.cursor() 
            print(s)
            sql_command = 'INSERT INTO items (site,link,price) VALUES ("'+site+'", "'+link+'",'+str(sum)+');'
            print(sql_command)
            crsr.execute(sql_command) 
            connection.commit() 
            connection.close()
        except:
          x=0


    def addlink(self,site,link):
      try:
        connection = sqlite3.connect(self.db) 
        crsr = connection.cursor() 
        link=link[8:len(link)-1]
        sql_command = r'INSERT INTO links (site,link) VALUES ("'+site+'", "'+link+'");'
        crsr.execute(sql_command) 
        connection.commit() 
        connection.close()
      except:
        x=0


    def addlinks(self,site,links):
        connection = sqlite3.connect(self.db) 
        crsr = connection.cursor() 
        for i in links:
            i=i[8:len(i)-1]
            sql_command = r'INSERT INTO links (site,link) VALUES ("'+site+'", "'+i+'");'
             
            try:
                crsr.execute(sql_command) 
                connection.commit() 
            except:
                x=0
        connection.close()

    def getlinks(self):
        connection = sqlite3.connect(self.db) 
        crsr = connection.cursor() 
        crsr.execute("SELECT * FROM links") 
        ans = crsr.fetchall() 
        print(ans)
        connection.commit() 
        connection.close()
        return ans 

    def getitems(self):
        connection = sqlite3.connect(self.db) 
        crsr = connection.cursor() 
        crsr.execute("SELECT * FROM items") 
        ans = crsr.fetchall() 
        connection.commit() 
        connection.close()
        return ans 
        



        






