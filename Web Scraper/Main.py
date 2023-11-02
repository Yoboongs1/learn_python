from Websites.WeWorkRemotely import wwr_jobs
from Websites.Indeed import extract_jobs_indeed

search_term = input("What do you want to search for?")

wwr = wwr_jobs(search_term)
indeed = extract_jobs_indeed(search_term)
jobs = indeed + wwr

file = open(f"{search_term}.csv",'w', encoding ="utf-8")
file.write("Position,Company,Location,Link\n")

for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()