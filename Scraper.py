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
		data = self.object.find('table', attrs={'class': 'line'})
		title = data.find('caption').text

		return title, dict(zip([a.text for a in data.find_all('a')], [a.text for a in data.find_all('big')]))

	def get_logist_salary(self):
		title = self.object.find("h2", attrs={'class': 'cut-bottom'}).text
		data_cityNames = self.object.find_all("div", attrs={'class': 'chart-category'})
		data_salary = self.object.find_all("div", attrs={'class': 'chart-data-digits'})
	
		return title, dict(zip([a.text for a in data_cityNames], [a.text for a in data_salary]))