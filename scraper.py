from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def extract_data(soup):
    teacher_names = []
    teacher_titles = []
    teacher_locations = []
    teacher_emails = []

    content = soup.select(".fsConstituentItem")
    for i in content:
        teacher_name = i.select("h3.fsFullName")
        if teacher_name is None:
            teacher_names.append(None)
        else:
            teacher_names.append(teacher_name[0].get_text().strip())
   
        teacher_title = i.select("div.fsTitles")
        if len(teacher_title) == 0:
            teacher_titles.append(None)
        else:
            teacher_titles.append(teacher_title[0].get_text().strip())

        teacher_location = i.select("div.fsLocations")
        if len(teacher_location) == 0:
            teacher_locations.append(None)
        else:
            teacher_locations.append(teacher_location[0].get_text().strip())

        teacher_email = i.select("div.fsEmail a")
        if len(teacher_email) == 0:
            teacher_emails.append(None)
        else:
            teacher_emails.append(teacher_email[0].get_text().strip())


    data = []
    for teacher_name, teacher_title, teacher_location, teacher_email in zip(teacher_names, teacher_titles, teacher_locations, teacher_emails):
        data.append({
            "Name": teacher_name,
            "Title": teacher_title,
            "Location": teacher_location,
            "Email": teacher_email
        })

    return data

url = "https://www.sanjuan.edu/connect/staff-directory"
driver.get(url)

all_data = []
count = 1
while True:
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    page_data = extract_data(soup)
    all_data.extend(page_data)
    count += 1
    
    if count == 55:
        break
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fsNextPageLink')))
    element.click()


driver.quit()
print(count)


df = pd.DataFrame(all_data, columns=["Name", "Title", "Location", "Email"])
df.to_csv("teachers.csv", index=False)
