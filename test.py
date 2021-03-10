import sys
import selenium
import requests

if __name__ == "__main__":
	r = requests.get('https://cpe.cse.nsysu.edu.tw/cpe/')
	print(r.status_code)


	# my_params = {'key1': 'captcha'}
	# r = requests.get('https://cpe.cse.nsysu.edu.tw/cpe/', params = my_params)
	# print(r.url)