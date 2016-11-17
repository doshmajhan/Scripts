# Script to scrape

import gspread
import json
from oauth2client.client import SignedJwtAssertionCredentials

url = "https://spreadsheets.google.com/feeds"
key_file = "Google-Key.json"
sheet = "Shareeek Creds (Responses)"

json_key = json.load(open(key_file))
credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                            json_key['private_key'],
                                            url)

g = gspread.authorize(credentials)

cred_sheet = g.open(sheet)
cred_sheet = cred_sheet.sheet1
records = cred_sheet.get_all_records()
for r in records:
    print(r['Email'], r['Password'])
