import requests
import pickle

API_KEY = "53ab15e9fd64393c5d3f6162a57877ce";




def get_weather(city):
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br";
    requisicao = requests.get(link);
    city="";
    requisicao_dic = requisicao.json();
    descricao = requisicao_dic["weather"][0]["description"];
    nostr_disc = pickle.dumps(descricao);
    str_disc = pickle.loads(nostr_disc);
    temperatura = requisicao_dic["main"]["temp"] - 273.15;
    nostr_temp = pickle.dumps(temperatura);
    str_temp = pickle.loads(nostr_temp);



    print(str_disc, f"{str_temp}°C");




