from cipherLib import open, Log
import sys

try:
	open.OPEN(str(sys.argv[1]))
except:
	Log.badLog("No params provided. ")
	Log.goodLog("Usage: python3 cipherGate.py <url> ")

