import requests
from colorama import Fore
from cipherLib import Log

def check_string_in_file(string_to_check, file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if string_to_check in line:
                return True
    return False

# TODO
# - add the keyword/port check beofre the VT check
def SCAN(url):
    if check_string_in_file(str(url), "./detection/Keywords.txt"):
        Log.badLog("Failed Keyword Inspection")
        return False
    else:
        Log.goodLog("Passed Keyword Inspection")
        x = open('key.txt')
        # print(x.read())
        """Checks if a given URL is safe using VirusTotal"""
        api_key = x.read()
        url_scan_api = 'https://www.virustotal.com/vtapi/v2/url/scan'
        url_report_api = 'https://www.virustotal.com/vtapi/v2/url/report'

        # Send the URL to VirusTotal for scanning
        response = requests.post(url_scan_api, data={'url': url, 'apikey': api_key})

        # Get the scan ID from the response
        scan_id = response.json()['scan_id']

        # Check the scan report to see if the URL is malicious
        params = {'resource': scan_id, 'apikey': api_key}
        response = requests.get(url_report_api, params=params)

        if response.json()['positives'] > 0:
            Log.badLog("Failed VirusTotal Inspection")
            return False
        else:
            Log.goodLog("Passed VirusTotal Inspection")
            return True

