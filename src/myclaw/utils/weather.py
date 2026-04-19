# 天气信息查询工具类

import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry
from typing import Dict,Any


class weather_util:
    
    @staticmethod
    def getTemp(latitude:float , longitude:float) :
        # Setup the Open-Meteo API client with cache and retry on error
        cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        openmeteo = openmeteo_requests.Client()

        # Make sure all required weather variables are listed here
        # The order of variables in hourly or daily is important to assign them correctly below
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m",
        }
        responses = openmeteo.weather_api(url, params = params)

        # Process first location. Add a for-loop for multiple locations or weather models
        response = responses[0]
        
        # Process hourly data. The order of variables needs to be the same as requested.
        return response.Hourly()



if __name__ == "__main__":
   temp = weather_util.getTemp(latitude=52.52,longitude=13.419)
   print(temp)