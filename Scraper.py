import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class Scrap():
	
	def __init__(self, link):
		self.object = self.get_html(self.get_response(link))
	
	def get_response(self, link):
		return requests.get(link, headers={'User-Agent': UserAgent().chrome})
	
	def get_html(self, response):
		html = response.content
		return BeautifulSoup(html, 'html.parser')
		
	def get_fuelprice_data(self):
		data = [[], []]
		all_work_data = self.object.find('table', attrs={'class': 'line'})
		title = all_work_data.find('caption').text
	
		for i in all_work_data.find_all('a'):
			data[0].append(i.text)

		for k in all_work_data.find_all('big'):
			data[1].append(k.text)

		return title, dict(zip(data[0], data[1]))
