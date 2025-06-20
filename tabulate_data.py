import os
from bs4 import BeautifulSoup
import pandas as pd



def tabulate_data(PRODUCT_NAME):
    d = {'title': [], 'price': [], 'rating': [], 'users rated': [], 'link': []}

    for file in os.listdir(f"data/{PRODUCT_NAME}"):    
        try:
            with open(f"data/{PRODUCT_NAME}/{file}") as f:
                html_doc = f.read()
            soup = BeautifulSoup(html_doc, 'html.parser')


            t = soup.find("h2")
            title = t.get_text()

            l = t.parent
            link = "https://amazon.in" + l['href']

            p = soup.find("span", class_ = "a-offscreen")
            price = p.get_text()[3:] # remove the rupee symbol, unreadable character in utf-8
            
            r = soup.find("span", attrs={"class": "a-icon-alt"})
            if r is not None:
                r_temp = r.get_text()
                rating = r_temp.split()[0]
            else:
                rating = "0"


            u = soup.find("span", class_="a-size-base s-underline-text")
            if u is not None:
                users_rated = u.get_text()
            else:
                users_rated = 0

            d['title'].append(title)
            d['link'].append(link)
            d['price'].append(price)
            d['rating'].append(rating)
            d['users rated'].append(users_rated)

        except Exception as e:
            print(e)


    if not os.path.exists(f"results"):
        os.makedirs(f"results")
        
    df = pd.DataFrame(d)
    df.to_csv(f"results/{PRODUCT_NAME}.csv")

    print(f"Records tabulated: {len(d['title'])}")
    return True