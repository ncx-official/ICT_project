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
		print(end='\n\n')
		if number < 0 or number > 8:
			os.system('clear')
			print("Ви ввели невірне значення пункту меню.\n")
			return None
	except ValueError:
		os.system('clear')
		print("Ви ввели невірне значення.\n")
		return None
	else:
		return number


def get_fuel_price(view=True):  # Value 1
	title, data = Scrap("https://index.minfin.com.ua/ua/markets/fuel/").get_fuelprice_data()
	
	if view:
		print(f"___<{title}>___")
		cnt = 1
		for key, value in data.items():
			print(f"{cnt}) {key}:  {value} грн.")
			cnt += 1
		continue_point()
	else:
		return title, data

def second():
	pass
def third():
	pass
def fourth():
	pass
def fifth():
	pass
def sixth():
	pass

def save_to_file(number):  # Value 7
	if number == None or number not in range(1,7):
		print("Виникла помилка, дані не збережено")
		continue_point()
	else:
		if number == 1:
			title, data = get_fuel_price(False)
		elif number == 2:
			title, data = second(False)
		elif number == 3:
			title, data = third(False)
		elif number == 4:
			title, data = fourth(False)
		elif number == 5:
			title, data= fifth(False)
		else:
			title, data = sixth(False)
		try:
			with open("result_data.txt", "a") as f:
				f.write(("/\\"*15)+"\n")
				f.write(f"___<{title}>___\n")
				for key, value in data.items():
					f.write(f"{key}:  {value} грн.\n")
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
        -5: '•| ━━━━━━━━━━━━━❪✇❫━━━━━━━━━━━━━ |•',
        -4: '    Програма "Помічник Логіста"   (ver. 2.0)',
        -3: "•| ━━━━━━━━━━━━━❪✇❫━━━━━━━━━━━━━ |•",
        -2: '╭────────────────╯⌬╰────────────────╮',
        1: "Середні ціни на пальне          |",
        2: "###########################    |",
        3: "###########################     |",
        4: "############################## |",
        5: "###########################     |",
        6: "############################## |",
        7: "Збереження даних у файл         |",
        8: "Про програму                   |",
        0: "Вихід                           |",
        -1: '╰────────────────╮⌬╭────────────────╯'
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
        if number == None:
            program_name = False
            continue
        else:
            if number == 1:  # Fuel price in Ukraine
                get_fuel_price()
            elif number == 2:
                pass
            elif number == 3:
                pass
            elif number == 4:
                pass
            elif number == 5:
                pass
            elif number == 6:
                pass
            elif number == 7:
                save_to_file(check_userchoice("Виберіть пункт меню, який потрібно зберегти (1-6) ---> "))
            elif number == 8:
                program_info()
            else:
                program_exit()
            program_name = False


if __name__ == "__main__":
    main()