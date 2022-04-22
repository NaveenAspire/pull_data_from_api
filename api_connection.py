
# Not completed

"""This module that pull data from the api and upload to in s3."""
from datetime import datetime
import requests
import argparse
import json
import os


# response = requests.get('https://www.metaweather.com/api/location/44418/2013/4/27/')
# print(response.json())

class PullDataFromApi:
    def __init__(self,pull_date) -> None:
        """This is the init method of the class of PullDataFromApi"""
        self.pull_date = pull_date

    def get_woeid_by_city(self):
        """This method used to get the woeid of city from api"""
        pass
    
    def get_data_from_api(self,city_woeid):
        """This method pull data from api using woeid of the city with date"""
        pass
    
    def upload_to_s3(self):
        """This method used to upload the file to s3 which data got from api"""
        pass
    
def main():
    """This is the main method for the module api_connection"""
    parser = argparse.ArgumentParser(description="Help to get data from given date")
    parser.add_argument('--date',type=datetime,help='Enter date for pull data', default=datetime.date())
    args = parser.parse_args()
    pull_data = PullDataFromApi(args.date)
    city_woeid = pull_data.get_woeid_by_city()
    pull_data.get_data_from_api(city_woeid)
    pull_data.upload_to_s3()
    

if __name__ == '__main__':
    main()
        