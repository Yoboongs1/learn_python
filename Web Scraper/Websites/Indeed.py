from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()

browser = webdriver.Chrome(options=options)

def count_pages(keyword):
    base_url = "https://uk.indeed.com/jobs?q="
    browser.get(f"{base_url}{keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", class_ = "css-jbuxu0 ecydgvn0")
    if pagination == None:
        return 1
    pages = pagination.find_all("div", recursive=False)
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count

count_pages("python")


def extract_jobs_indeed(search_term):
    pages = count_pages(search_term)
    print(f"Found {pages} pages")
    results = []
    for page in range(pages):
        base_url = "https://uk.indeed.com/jobs"
        final_url = f"{base_url}?q={search_term}&start={page*10}"
        browser.get(final_url)
        print(final_url)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_ = "jobsearch-ResultsList")
        jobs = job_list.find_all("li", recursive=False) #recursive = False means we only look at the first descendent layer and not at the deeper layers
        for job in jobs:
            zone = job.find("div", class_ = "mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor.find("span")["title"]
                link = anchor['href']
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
            job_data = {
                "link" : f"https://uk.indeed.com{link}",
                "company" : company.string.replace(","," "),
                "location" : location.string.replace(","," "),
                "position" : title.replace(","," ")
            }
            results.append(job_data)
    return results
