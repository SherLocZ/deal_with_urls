# -*- conding:utf-8 -*- 

import queue
import requests
import threading

def write_in_file(file_name,list):		#写入文件
	with open(file_name,"w+") as f:
		for url in list:
			f.write(url.strip() + "\n")

class Mythread(threading.Thread):
	def __init__(self,q):
		threading.Thread.__init__(self)
		self.q = q

	def run(self):		#重写threading的run方法
		while self.q.empty() == False:
			url = self.q.get()
			urls = "http://" + url
			try:
				r = requests.get(urls,timeout=3,allow_redirects=False)
				# print(r.status_code)
				if str(r.status_code) == '200':
					# print(r.status_code)
					list.append(urls)
					# print(list)
					print("Find url:{}".format(urls))
			except:
				pass
		# return list


if __name__ == '__main__':
	q =queue.Queue()
	list = []
	with open("urls.txt","r+") as f:	//从文件中读取url
		for url in f.readlines():
			q.put(url.strip())
	print(q.qsize())
	threads = []
	for i in range(100):
		thread1 = Mythread(q)
		thread1.start()
		threads.append(thread1)

	for t in threads:
	    t.join()
	# print("success")
	print(list)
	write_in_file("end.txt",list)