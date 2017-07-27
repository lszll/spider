# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:19:25 2017

@author: Shinelon
"""

import requests
import bs4
import re
import traceback

def getHTMLText(url, code="utf-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""
    

def getStockList(lst, stockURL):
    html = getHTMLText(stockURL, "GB2312")
    soup = BeautifulSoup(html, "html.parser")
    a = soup.find_all('a')
    for i in a:
        try:
            herf = i.attrs('href')
            lst.append(re.findall(r"[s][hz]\d{6}", herf)[0])
        except:
            continue

def getStockInfo(lst, stockURL, fpath):
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHMTLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(url, "html.parser")
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})
            
            name = stockInfo.fiind_all(attrs={'class':'bet-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})
            
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
                
            with open(fpath, 'a', encoding='utf-8' as f):
                f.write(str(infoDict)+ '\n')
                count = count + 1
                print('\r当前进度 : {:.2f}%', format(count*100/len(lst)),end='')
        except:
            traceback.print_exc()
            continue
    
def main():
    stock_list_url = 'http://quote.eastmoney.com/sta'
    
    
if __name__ == "__main__":
    main()