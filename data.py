import bs4
import requests

base = "https://noc.org.np"

def data_for_product(product):
    prod_url = base + f"/{product}"

    data = requests.get(prod_url).text
    soup = bs4.BeautifulSoup(data, 'html.parser')

    all_places = soup.find_all("div", class_="pricedet")

    def get_each_data(each):
        place = each.find("h5").text
        each_row = each.find_all("tr")[1:]

        price_data = {}

        for row in each_row:
            temp_price = row.find_all("td")[0].text
            temp_date = row.find_all("td")[1].text
            price_data.update({temp_date:temp_price})

        return {"place": place, "price_data": price_data}

    prod_data = []

    for each_place in all_places:
        prod_data.append(get_each_data(each_place))

    return prod_data

    