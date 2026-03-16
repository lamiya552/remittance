import requests
import re

# 1. Get the data
url = "https://nblmt.com.my/display/ajax_rate.php"
response = requests.get(url)
html_content = response.text

# 2. Find the 31.16 value using Regex
# We look for the text after 'Bangladesh (account)'
match = re.search(r'Bangladesh \(account\).*?(\d+\.\d+)', html_content, re.DOTALL)

if match:
    remote_value = float(match.group(1)) # This captures 31.16
    print(f"Captured Rate: {remote_value}")

    # 3. Your formula: (1000 * rate% * 102.5 - 10 * 31.7) / 1000
    # Note: 31.16 is already the rate, so we use it as 0.3116
    result = (1000 * (remote_value / 100) * 102.5 - 10 * 31.7) / 1000
    
    # 4. Save to a file for your website
    with open("index.html", "w") as f:
        f.write(f"<html><body><h1>Current Result: {round(result, 4)}</h1><p>Based on rate: {remote_value}</p></body></html>")
