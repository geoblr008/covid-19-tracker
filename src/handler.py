from bs4 import BeautifulSoup
import requests

data_check = []
worldmetersLink = "https://www.worldometers.info/coronavirus/"
html_page = requests.get(worldmetersLink)
bs = BeautifulSoup(html_page.content, 'html.parser')
search = bs.select("div tbody tr td")


def data_cleanup(array):
    L = []
    for i in array:
        i = i.replace("+", "")
        i = i.replace("-", "")
        if i == "":
            i = "0"
        L.append(i.strip())
    return L


def get_data(country):
    start = -1
    for i in range(len(search)):
        if search[i].get_text().find(country) != -1:
            start = i
            break
    data = []
    for i in range(1, 8):
        try:
            data = data + [search[start+i].get_text()]
        except:
            data = data + ["0"]

    data = data_cleanup(data)
    keys = ["total_infected", "new_case", "total_deaths",
            "new_deaths", "recovred", "active_case", "serious_critical"]

    data = dict(zip(keys, data))

    return data


def world_data():
    return get_data("World")


def get_top_five():
    index = [177, 199, 221, 243, 265]

    data = []
    for i in range(0, 8):
        try:
            data = data + [search[index[i]].get_text()]
        except:
            data = data + ["0"]
        data = list(filter(("0").__ne__, data))
    country_list = []
    for i in range(len(data)):
        country_list.append(get_data(data[i]))

    return country_list
