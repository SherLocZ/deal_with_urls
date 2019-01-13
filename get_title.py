# -*- conding:utf-8 -*- 
#获取网站title

import requests
from bs4 import BeautifulSoup
from requests.exceptions import ReadTimeout

with open("end.txt","r+") as f:
	for url in f.readlines():
		url = url.replace("\n","")
		# print(url)
		try:
			r = requests.get(url,timeout=3)
			soup = BeautifulSoup(r.content,"lxml")
			# print(soup)
			print("[+]" + url + "| title: " + soup.title.text.strip())
		except:
			print("[-]" + url + "| connect failed " )