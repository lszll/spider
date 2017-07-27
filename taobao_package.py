# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 10:59:57 2017

@author: Shinelon
"""

import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""        

    
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_prince\"\:\"[\d\.]*\"', html)  #正则搜索的结果为 “view_price” : "{d.}"
        tlt = re.findall(r'\"raw_title\"\:\:.*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")
        

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = "书包"
    depth = 3
    start_url = 'http://s.taobao.com/serach?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)  #每页44个数据
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList) 
  


if __name__ == "__main__":
    main()
    
