from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
# print(html_text)
soup = BeautifulSoup(html_text,"lxml")



# print(soup)
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')


for job in jobs:

    published_date = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name')
        company_name= company_name.text.replace(' ','')

        skills = job.find('span', class_ = 'srp-skills').text
        skills = skills.replace(' ','')
        # print(skills)

        more_info = job.header.a['href']
        print(f"Comapany Name : {company_name.strip()}")
        print(f"Required Skills: {skills.strip()}")
        print(f"More Info: {more_info}")
        print()