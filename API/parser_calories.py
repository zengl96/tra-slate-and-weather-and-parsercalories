import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from time import sleep
import json
import csv
import random

url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.0.1044 Yowser/2.5 Safari/537.36"
}

src = urlopen('https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie')
soup = BeautifulSoup(src , "lxml")
all_product = soup.find_all(class_="mzr-tc-group-item-href")
all_category = {}
for item in all_product:
    item_text=item.text
    item_href='https://health-diet.ru'+item.get("href")
    all_category [item_text]=item_href
with open("all_categories_dict.json", "w") as file:
    json.dump(all_category, file, indent=4, ensure_ascii=False)
with open("all_categories_dict.json") as file:
    all = json.load(file)
iteration_count = int(len(all)) - 1
count = 0
print(f"Всего итераций: {iteration_count}")
for category_name, category_href in all.items():
        req = requests.get(url=category_href, headers=headers)
        src = req.text
        with open(f"{category_name}.html", "w" , encoding="utf-8") as file:
                file.write(src)
        with open(f"{category_name}.html" , encoding='utf-8') as file:
                src = file.read()
        soup = BeautifulSoup (src , 'lxml')
        alert_block = soup.find(class_="uk-alert-danger")
        if alert_block  is not None:
            continue
        table= soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
        Product = table[0].text
        Calorie = table[1].text
        Proteins = table[2].text
        Fats = table[3].text
        Carbohydrates = table[4].text
        with open(f"{category_name}.csv", "w" ) as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    Product,
                    Calorie,
                    Proteins,
                    Fats,
                    Carbohydrates
                    )
                )
        datu = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")
        for items in datu :
            rty = items.find_all('td')
            title = rty[0].find('a').text
            Calorie = rty[1].text
            Proteins = rty[2].text
            Fats = rty[3].text
            Carbohydrates = rty[4].text
            with open(f"{category_name}.csv", "a" , encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(
                       (
                        title,
                        Calorie,
                        Proteins,
                        Fats,
                        Carbohydrates
                       )
                    )
        count = count+1
        print(f"# Итерация {count}. {category_name} записан...")
        iteration_count = iteration_count - 1

        if iteration_count == 0:
            print("Работа завершена")
            break

        print(f"Осталось итераций: {iteration_count}")
        sleep(random.randrange(0 , 1))