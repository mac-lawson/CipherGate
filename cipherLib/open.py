from selenium import webdriver
from colorama import Fore
from cipherLib import scan
from cipherLib import Log
import time


def OPEN(kuri):
	print(Fore.BLUE + "CipherGate CE\n")
	# try:
	x = scan.SCAN(kuri)
	if (x == True):
		Log.goodLog("URL is safe to open, opening...")
		driver = webdriver.Firefox()
		driver.get(kuri)
	else:
		Log.badLog("URL is not safe to open, exiting...")
	# except:
	# 	print(Fore.RED + "No VirusTotal API Key Provided in Key.txt" + Fore.RESET)