# © Individual creative task by Vitalii (ncx), ver. 2.0
# Індивідуальне творче завдання
# Варіант завдання: Логіст

import os
from Scraper import Scrap


def continue_point():  # Clear console
    input("Press enter to continue...\n")
    os.system('clear')


def check_userchoice(text): # Check input number of user
	try:
		number = int(input(text))
	except ValueError:
		os.system('clear')
		print("{ERROR} Ви ввели невірне значення.\n")
		return None
	else:
		return number

def show_content(title, data, number=100, id=1):
	count = 0
	print(f"\n________<{title}>________")
	if id == 1:
		for key, value in data.items():
			print(f"{count+1}) <{key}>:\n\n{value}")
			count += 1
			if count == number:
				break
	elif id == 2:
		for key, value in data.items():
			print(f"{count+1}) {key}:\n{value}\n")
			count += 1
			if count == number:
				break
	elif id == 3:
		for key, value in data.items():
			print(f"{key+1}) {value}\n")
			if count == number:
				break
	elif id == 4:
		for key, value in data.items():
			print(f"{count+1}) {key}:  {value} грн.")
			count += 1
			if count == number:
				break
	continue_point() 


def last_logistic_news(view=True):  # Value 1
	title, data = Scrap("https://logist.fm/news").get_last_news()
	if view:
		number = check_userchoice("Введіть кількість новин (1-15) ---> ")
		if number == None or number not in range(1,16):
			print("Виникла помилка, невірне значення")
			continue_point()
		else:
			show_content(title, data, number)
	else:
		return title, data


def flat_price(view=True): # Value 2
	title, data = Scrap("https://dom.ria.com/uk/arenda-kom-nedvizhimosti/vinnitsa-pomeshcheniye/").get_flat_price()
	if view:
		number = check_userchoice("Введіть кількість оголошень (1-16) ---> ")
		if number == None or number not in range(1,17):
			print("{ERROR} Виникла помилка, невірне значення")
			continue_point()
		else:
			show_content(title, data, number, id=2)
	else:
		return title, data
	

def exchange_rate(view=True): # Value 3
	title, data = Scrap("https://my.ukrsibbank.com/ua/personal/operations/currency_exchange/").get_exchange_rate()
	if view:
		show_content(title, data, id=3)
	else:
		return title, data

def get_fuel_price(view=True):  # Value 4
	title, data = Scrap("https://index.minfin.com.ua/ua/markets/fuel/").get_fuelprice_data()
	if view:
		show_content(title, data, id=4)
	else:
		return title, data


def average_logistics_salary(view=True):  # Value 5
	title, data = Scrap("https://www.work.ua/salary-%D0%BB%D0%BE%D0%B3%D0%B8%D1%81%D1%82/").get_logist_salary()
	if view:
		show_content(title, data, id=4)
	else:
		return title, data


def shipping_cost_services(view=True): # Value 6
	title = "Сервіси для вирахування вартості доставки"
	services = {
		"Нова Пошта": "https://novaposhta.ua/delivery",
		"Укрпошта": "https://calc.ukrposhta.ua/domestic-calculator",
		"Justin": "https://justin.ua/calculate",
		"Delivery": "https://www.delivery-auto.com/uk-UA/CalculateCost",
		"Meest": "https://ua.meest.com/calculator",
		"Sat": "https://www.sat.ua/order/calculation/",
		"Автолюкс": "https://autolux-post.com.ua/calc/"
	}
	if view:
		show_content(title, services, id=4)
	else:
		return title, services


def save_to_file():  # Value 7
	number = check_userchoice("Виберіть пункт меню, який потрібно зберегти (1-6) ---> ")
	if number == None or number not in range(1,7):
		print("{ERROR} Виникла помилка, дані не збережено")
		continue_point()
	else:
		if number == 1:
			title, data = last_logistic_news(False)
		elif number == 2:
			title, data = flat_price(False)
		elif number == 3:
			title, data = exchange_rate(False)
		elif number == 4:
			title, data = get_fuel_price(False)
		elif number == 5:
			title, data = average_logistics_salary(False)
		else:
			title, data = shipping_cost_services(False)
		try:
			with open("result_data.txt", "a") as f:
				f.write(("/\\"*15)+"\n")
				f.write(f"___<{title}>___\n")
				for key, value in data.items():
					f.write(f"{key}:  {value}\n")
				f.write(("/\\"*15)+"\n\n")
			print("Дані успішно збережено")
		except:
			print("Виникла помилка, дані не збережено")
		continue_point()


def program_info():  # Value 8
    info_about_script = [["_" * 12 + "<Про програму>" + "_" * 12],
                         ["Розробив: Насіковський Віталій Валерійович"],
                         ["Група: КН-20-В"]]
    for n in info_about_script:
        print(n[0])
    continue_point()


def program_exit():  # Value 0
    input("Press enter to exit....")
    exit()


def start_menu(logo):  # start menu, list of all function of this program
    tasks_list = {
        -5: '•| ━━━━━━━━━━━━━━━━━━━━❪✇❫━━━━━━━━━━━━━━━━━━━━━ |•',
        -4: '    	Програма "Помічник Логіста"   (ver. 2.0)',
        -3: "•| ━━━━━━━━━━━━━━━━━━━━❪✇❫━━━━━━━━━━━━━━━━━━━━━ |•",
        -2: '╭──────────────────────╯⌬╰──────────────────────╮',
        1: "Останні новини у Логістиці                |",
        2: "Оренда приміщень                          |",
        3: "Курс валют                                |",
        4: "Середні ціни на пальне                    |",
        5: "Середня зарплата Логіста                  |",
        6: "Сервіси для вирахування вартості доставки |",
        7: "Збереження даних у файл                   |",
        8: "Про програму                              |",
        0: "Вихід                                     |",
        -1: '╰──────────────────────╮⌬╭──────────────────────╯'
    }
    for key, value in tasks_list.items():
        if key >= 0:
            print("|", key, "|", value)
        elif logo:
            print(value)


def main():
	program_name = True  # show program logo
	while True:
		start_menu(program_name)
		number = check_userchoice("Виберіть пункт меню із списку --> ")
		if (number not in [1,2,3,4,5,6,7,8,0]) or number == None:
			program_name = False
			os.system("clear")
			print("{ERROR} Виникла помилка, невірне значення\n")
			continue
		else:
			if number == 1:
				last_logistic_news()
			elif number == 2:
				flat_price()
			elif number == 3:
				exchange_rate()
			elif number == 4:
				get_fuel_price()
			elif number == 5:
				average_logistics_salary()
			elif number == 6:
				shipping_cost_services()
			elif number == 7:
				save_to_file()
			elif number == 8:
				program_info()
			elif number == 0:
				program_exit()
			program_name = False


if __name__ == "__main__":
    main()