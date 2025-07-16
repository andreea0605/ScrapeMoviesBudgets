from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time

# webdrive settings
options = Options()
options.add_argument("--headless")  # rulează fără UI
driver = webdriver.Chrome(options=options)

base_url = "https://www.the-numbers.com/movie/budgets/all/"
offsets = range(1, 2001, 100)  # pages: 1, 101, 201, ..., 1901

all_data = []
header = ["Rank", "Release Date", "Movie", "Production Budget", "Domestic Gross", "Worldwide Gross"]

for offset in offsets:
    url = base_url + str(offset)
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Find table
        tables = soup.find_all("table")
        target_table = None
        for t in tables:
            rows = t.find_all("tr")
            if len(rows) > 1 and len(rows[1].find_all("td")) == 6:
                target_table = t
                break

        if not target_table:
            print(f"Table not found {url}")
            continue

        for row in target_table.find_all("tr")[1:]:
            cols = row.find_all("td")
            if len(cols) == 6:
                rank = cols[0].text.strip()
                release_date = cols[1].text.strip()
                movie = cols[2].text.strip()
                budget = cols[3].text.strip().replace("\xa0", "").replace("$", "").replace(",", "")
                domestic = cols[4].text.strip().replace("\xa0", "").replace("$", "").replace(",", "")
                worldwide = cols[5].text.strip().replace("\xa0", "").replace("$", "").replace(",", "")
                all_data.append([
                    rank, release_date, movie,
                    int(budget) if budget else 0,
                    int(domestic) if domestic else 0,
                    int(worldwide) if worldwide else 0
                ])

        time.sleep(1)

    except Exception as e:
        print(f"Error at page {url}: {e}")
        continue

driver.quit()

# Salvare în CSV
with open("all_movie_budgets.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(all_data)

print(f"{len(all_data)} rows în all_movie_budgets.csv")