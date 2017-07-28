# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 13:43:54 2017

@author: Shinelon
"""

import requests
import bs4
import re
import thread

class BookSpider():
    
    def __init__(self):
        self.pages = []
        self.page = 1
        self.flag = True
        self.url = url
        
    def getHTMLText(url, code='utf-8'):
        try:
            r = requests.get(url)
            r.raise_for_status()
            r.encoding = code
            return r.text
        except:
            return "搜索失败"
        
    def getBookContent():
        html = getHtMLText(url, "gbk")
        soup = BeautifulSoup4(html, "html.parser")
        a = soup.find_all('a')
        for i in a:
            try:
                title = i.attr["title"]
        
    def getBookAuthor(lst, stockURL):
        pass
    
    def getBookName(lst, stockURL):
        pass
    
    def getBookHref():
        pass


def main():
    pass


if __name__ == "__main__":
    main()