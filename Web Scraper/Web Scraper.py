#URL Formatting

from requests import get

websites = ["google.com", "twitter.com", "https://youtube.com"]
results = {}
for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code == 200: #checking whether website answers succesfully
        results[website] = "OK"
    else:
        results[website] = "FAILED"

print(results)