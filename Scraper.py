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
	

	def get_last_news(self):
		data_news_title = self.object.find_all("div", attrs={'class': 'article_title'})
		data_news_text = self.object.find_all("div", attrs={'class': 'article_text'})

		return "Новини у логістиці", dict(zip([a.text for a in data_news_title], [a.text for a in data_news_text]))
	

	def get_flat_price(self):
		title = self.object.find("h1").text
		street = self.object.find_all("a", attrs={'class': 'blue'})
		price = self.object.find_all("b", attrs={'class': 'green size22'})
		
		return title, dict(zip([("Адреса: " + a.text) for a in street], [("Ціна: " + a.text) for a in price]))
	

	def get_exchange_rate(self):
		data = self.object.find("table", attrs={'class': 'currency__table'})
		title = self.object.find("h1").text
		values = data.find_all("tr")
		
		return title, dict(zip([a for a in range(len(values))], [i.get_text(" ").strip() for i in values]))
