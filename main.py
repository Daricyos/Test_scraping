import requests
from bs4 import BeautifulSoup

def get_articles_urls(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text,"lxml")

    item_name = soup.find(class_ ='additional-details').find_all("div")

    product_info = {
        'Article': item_name[0].find("span", class_= 'value').get_text(strip=True),
        'Availability for delivery': item_name[1].find("span", class_= 'value').get_text(strip=True),
        "Availability forecast in Poland": item_name[2].find("span", class_= 'value').get_text(strip=True),
        "Availability in Lviv": item_name[4].find("span", class_= 'value').get_text(strip=True),
    }

    with open('product.txt', 'w') as file:
        for key, value in product_info.items():
            file.write(f"{key}: {value}\n")
        print("Registration was successful!")


def main():
    get_articles_urls(url="https://home-club.com.ua/ua/sku-90507603?gclid=CjwKCAjwzY2bBhB6EiwAPpUpZhSieA2DRWXhLcbNCpIvJcC9dLHc534Djx5FKNpL9iXaLZlSQaNyLBoCEwYQAvD_BwE")

if __name__ == '__main__':
    main()