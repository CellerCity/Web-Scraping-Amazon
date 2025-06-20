from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os


def collect_data(PRODUCT_NAME, PAGE_LIMIT = 20):
    try:
        driver = webdriver.Chrome()
        fileNo = 0

        if not os.path.exists(f"data/{PRODUCT_NAME}"):
            os.makedirs(f"data/{PRODUCT_NAME}")
        else:
            print("Directory already exists, file(s) if present are being overwritten.")

        for pg_no in range(1, PAGE_LIMIT+1):
            try:
                driver.get(f"https://www.amazon.in/s?k={PRODUCT_NAME}&page={pg_no}&xpid=p6R2p8eyjv8jS&crid=336WPVN714Y10&qid=1748109290&sprefix=laptop%2Caps%2C477&ref=sr_pg_2")

                elems = driver.find_elements(By.CLASS_NAME, 'puis-card-container')
                for elem in elems:
                    d = elem.get_attribute("outerHTML")
                    with open(f"data/{PRODUCT_NAME}/{fileNo}.html", "w", encoding="utf-8") as f:
                        f.write(d)
                        fileNo += 1
                
                time.sleep(2)
            except Exception as e:
                print(e) # some exception while reading a page

        driver.close()
        print("Data collected successfully")
        return True
    
    except Exception as e:
        print(e) # can't access the website
        return False
