<!-- <iframe src="https://infosec.exchange/@mac_attack_hacker/109968497908574904/embed" class="mastodon-embed" style="max-width: 100%; border: 0" width="400" allowfullscreen="allowfullscreen"></iframe><script src="https://assets.infosec.exchange/embed.js" async="async"></script> -->

# CipherGate
Privacy-oriented browser tool with integrated developer tools
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![MIT License](https://img.shields.io/badge/version-beta-red
)](https://img.shields.io/badge/version-beta-red
)

## Running the Beta Release
### Downloads
#### Clone the GitHub repo

```git clone https://github.com/mac-lawson/CipherGate.git```

#### Install Python deps
```
python3 -m pip install colorama 
python3 -m pip install selenium
```
#### Modify the Key.txt file
```
Key.txt must contain the user's VirusTotal API key, which is required to run the script
```

#### Running the demo script 
```
python3 cipherGate.py https://google.com
```

### Scanning Process
| Virustotal Scan | Return     | Returns                |
| :-------- | :------- | :------------------------- |
| modify `key.txt` file with API Key  | `False` | `URL is not safe to open, exiting...`|

| Virustotal Scan | Return     | Returns                |
| :-------- | :------- | :------------------------- |
| modify `key.txt` file with API Key | `True` | Opens URI in Browser|

## Authors

- [@mac-lawson](https://www.github.com/mac-lawson) Lead Developer

