from selenium import webdriver
from colorama import Fore
from cipherLib import scan

def OPEN(kuri):
	x = scan.SCAN(kuri)
	if (x == True):
		driver = webdriver.Firefox()
		driver.get(kuri)
	else:
		print(Fore.RED + "URL is not safe to open, exiting..." + Fore.RESET)