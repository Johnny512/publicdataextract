"""
These functions import csv data from Healthcare Ready API url for example Pharmacy data
http://rxopen.org/api/v1/map/download/facility

"""

#import csv module
import csv, requests

import pandas as pd

def healthready_dataframe(url):
    """
    Download .csv data from API then convert to DataFrame
    """
    try:
        r = requests.get(url, allow_redirects=True)
        if r.status_code == 200:
            with open('textData.txt', 'wt') as file:
                file.write(r.text)
    except:
        return 'Download not successful'

    #convert text file to csv
    pharmcsv = pd.read_csv("textData.txt",delimiter=',',encoding='latin1')

    #convert csv to dataframe
    df = pd.DataFrame(pharmcsv)

    return df