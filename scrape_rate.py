import requests
import re

# 1. Fetch the data directly (No proxy needed)
url = "https://nblmt.com.my/display/ajax_rate.php"
headers = {'User-Agent': 'Mozilla/5.0'} # Pretend to be a browser
response = requests.get(url, headers=headers)

if response.status_code == 200:
    html = response.text
    
    # 2. Find the rate for Bangladesh (account)
    # This looks for the text and grabs the first number (31.16)
    match = re.search(r'Bangladesh \(account\).*?>(\d+\.\d+)<', html, re.DOTALL)
    
    if match:
        rate = float(match.group(1))
        print(f"Live Rate Found: {rate}")
        
        # 3. Your Formula: (1,000 * (Rate/100) * 102.5 - 317) / 1,000
        result = (1000 * (rate / 100) * 102.5 - 317) / 1000
        
        print(f"Calculation Result: {round(result, 4)}")
    else:
        print("Could not find the rate in the HTML.")
else:
    print(f"Failed to connect. Status code: {response.status_code}")
