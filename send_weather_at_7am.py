import sys
sys.path.insert(1, '/apps')

import datetime
from apps import weather
from apps import command
import re
import re
import time

import config
import vk_api 

vk_session = vk_api.VkApi(token=config.token) # получение vk_session


def weather_at_7am_for_user(vk_session,vk_api):
    
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    
    if hour == 7 and minute == 30:

        f = open('base_user_txt/user_weather.txt', 'r')
        
        try:
            ids_weather = f.readlines()
            red = re.compile('[id\n]')
            
            temp, wind_speed, cloudiness = weather.get_weather()
            for x in ids_weather:

                user_id = red.sub('', x)
                command.send_weather_at_7am_for_user(vk_session,user_id,vk_api,temp, wind_speed, cloudiness)
            
            time.sleep(61)
        finally:
            f.close()


while True:
    weather_at_7am_for_user(vk_session,vk_api)
    time.sleep(55)
    