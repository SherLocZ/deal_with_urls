#-*-coding:utf-8-*-
#去重脚本
def write_in_file(file_name,url_list):		#去重并写入到文件中
	new_url_list = []
	for url in url_list:
		if url not in new_url_list:
			new_url_list.append(url)
	print(len(new_url_list))
	with open(file_name,"w+") as f:
		for url in new_url_list:
			f.write(url.strip() + "\n")
	f.close()

def get_urls(file_name,url_list):		#从文件中读取url
	with open(file_name,"r+") as f:
		for url in f.readlines():
			url_list.append(url.strip())
	return url_list


if __name__ == '__main__':
	url_list = []
	get_urls("layer.txt",url_list)
	# print(len(url_list))
	get_urls("brute.txt",url_list)
	# print(len(url_list))
	write_in_file("urls.txt",url_list)