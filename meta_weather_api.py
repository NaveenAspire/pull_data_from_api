
# Not completed

"""This module that pull data from the api and upload to in s3."""
from time import strftime
import requests
import configparser
from datetime import datetime,timedelta
import argparse
import pandas as pd
import json
import os
from s3 import S3Service

config =configparser.ConfigParser()
config.read('develop.ini')
# for value in config['woeid'].values():
#     print(value)
# print(config.items)

# response = requests.get('https://www.metaweather.com/api/location/44418/2013/4/27/')
# print(response.json())

class PullDataFromMetaWeatherApi:
    def __init__(self) -> None:
        """This is the init method of the class of PullDataFromApi"""
        # self.pull_date = pull_date
        self.date = (datetime.now().date()-timedelta(1))
        self.path = os.path.join(os.getcwd(),config['local']['local_file_path'])

    def get_weather_information(self):
        """This method used to get the woeid of city from api"""
        # city_woied = config['woeid']['cities_woeid']
        # print(type(city_woied))
        search_date = self.date.strftime('%Y/%m/%d')
        for key,value in config['woeid'].items():
            # print(value)
            # print(key)
            response = requests.get('https://www.metaweather.com/api/location/'+value+'/'+search_date+'/').json()
            self.get_given_date_response(response,key)
            # if check_date in response[0]['created']:
            #     print()
            # print(response[0]['created'])
            
            return
    
    def get_given_date_response(self, response,city):
        """This method used to get only required date of information alone"""
        check_date = self.date.strftime('%Y-%m-%d')
        for information in response:
            # print(information)
            if check_date in information['created']:
                # print("dsfs")
                with open(self.path+city+'_'+information['created']+'.json','w') as file :
                    json.dump(information,file)
                    print("sucess")
                    return
            
                
    def upload_to_s3(self):
        """This method used to upload the file to s3 which data got from api"""
        s3_service = s3_service()
        for file in os.listdir(self.path):
            pass
    
def main():
    """This is the main method for the module api_connection"""
    # parser = argparse.ArgumentParser(description="Help to get data from given date")
    # parser.add_argument('--date',type=datetime,help='Enter date for pull data', default=datetime.date())
    # args = parser.parse_args()
    pull_data = PullDataFromMetaWeatherApi()  #(args.date)
    city_woeid = pull_data.get_weather_information()
    # pull_data.get_data_from_api(city_woeid)
    # pull_data.upload_to_s3()
    

if __name__ == '__main__':
    main()
        