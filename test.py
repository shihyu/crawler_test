import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

def getContent(url,pid):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept':'text/html;q=0.9,*/*;q=0.8','Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding':'gzip','Connection':'close'}
    res = requests.get(url, verify=False, headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    #print soup.text
    t = soup.find('td', id=re.compile("postmessage_\d+")).text
    date = soup.find('em', id=re.compile("authorposton\d+")).text
    author = soup.find('a', class_="author-id").text
   
    print pid, author, date, t

def getPage():
    
    url = 'http://www.citytalk.tw/bbs/forum.php?mod=forumdisplay&fid=107'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept':'text/html;q=0.9,*/*;q=0.8','Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding':'gzip','Connection':'close'}
    res = requests.get(url, verify=False, headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    a = soup.findAll("a", class_="s")
    #print res.request.headers
    
    c = 5
    for link in a:
        surl = link.get('href')
        c = c - 1
        if c < 0:
            break
        if not re.search(r'thread-51', surl) and not re.search(r'thread-160193', surl) and not re.search(r'thread-50261', surl):
            print surl
            pid = re.match(r'thread-(\d+)',surl).group(1)
            getContent('http://www.citytalk.tw/bbs/'+surl,pid)
            
getPage()
