import vk_api
from bs4 import BeautifulSoup
import requests
from vk_api.longpoll import VkLongPoll, VkEventType


token = "vk1.a.jJteSNjDo-DWAVJiGb37zSF3DumRdjMGm0SCQ7PZYbAHPTwuIuCRRjSrNsQX2Je-Gd83OTgTfNFEwt5CMee-jmJn2J38OFb0dJVrLPy9RxKUO9RS4J-8nDL6WwQP3BUTpo82AFSPQcyis5ze_MkYbzOasFtMGgeASJexd2cVlUZAt4TWtWSm3cNTMlsdCqSUMaFnRIjipHMIBY14VK0k_g"
URL = "https://www.banki.ru/products/currency/cny/"

vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text, "html.parser")
        item = soup.find("div",class_="currency-table__large-text").text
        item = item.replace(",", ".")
        return item

def get_html(url):
    r = requests.get(url)
    return r

def otpravlaem(id,text):
    vk_session.method("messages.send", {"user_id" : id, "message": text, "random_id" : 0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            if msg == "начать":
                uani = parse()
                otpravlaem(id,"Привет &#128075; \n"
                              "Я бот группы IXE, отправь мне цену в юанях и я рассчитаю стоимость покупки &#128184; \n"
                              "Возникли какие то вопросы &#8265; \n"
                              "Смело задавай,ответим как можно быстрее &#128526;")
            elif msg.isdigit() == True:
                sym = int(msg)
                uani = float(parse()) + 0.6
                otpravlaem(id,"Стоимость покупки составит == "+ str(round(uani * sym)) + " рублей")
