import sys
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import re

class Site:
    def __init__(self, name, link):
        self.name = name
        self.link = link

    def sitename(self):
        print("site:"+self.name+ " link is :" + self.link)

    def getlink(self):
        return self.link

    def getname(self):
        return self.name

    def print(self):
        self.sitename()

