A simple Python script that converts HTML into PDF using the html2pdf.app API.
Works directly on Android mobile devices (Termux or any environment that supports Python). Only the requests library is required.

# Features

- Convert pasted HTML code to PDF
- Convert uploaded .html files to PDF
- Saves PDF directly to your predefined folder
- No heavy dependencies — only requests
- Simple text-based UI for mobile use

# Requirements

- Python 3

- Requests library

- HTML2PDF.app's API key

# Setup

1. Launch your Pydroid3 or any Python IDE app and load the script

2. Install **requests* from **Pip* section or using `pip install requests`

2. Replace this line with your real API key:

`API_KEY = "YOUR_API_KEY_HERE"`

    - You can get a free API key from https://html2pdf.app

# How It Works

The script gives you two ways to load HTML:

## A) Paste HTML directly

- Paste your HTML

- Type END on a new line to finish


## B) Upload an HTML file

- Enter the relative path

- Script reads from /storage/emulated/0/


After choosing input, enter a PDF filename, and wait for a second, the PDF will be saved automatically in your specified folder. 

# Credits

Made by **Trader Abba**

Follow me: [X @TraderAbba](https://x.com/traderabba)

