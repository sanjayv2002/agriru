import weather
import pandas as pd 


def loc_att(city, dis):
    temp , hum = weather.weather(city)
    rf=pd.read_csv(r'./resources/raw/rainfall.csv')
    rnf = rf[rf['district']==dis.upper()]['rainfall']
    return [temp,hum,rnf]  

    