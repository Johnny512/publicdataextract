"""
These functions work for data from source: Oak Ridge National Laboratory (ORNL)
The data is in json format with the same structure
The API urls follow the same format and same server like: https://opendata.arcgis.com/datasets/f11d7d153bfb408f85bd029b2dac9298_0.geojson
"""
import requests,json

import pandas as pd

from mariadb_functions import mariadb_write, table_exists

def hifld_dataframe(url):
    """
    Returns a clean dataframe from an API. Libraries must be imported in calling script.
    """

    try:
        r = requests.get(url, allow_redirects=True)
        if r.status_code == 200:
            obj1 = json.loads(r.text)
    except:
        return 'Download not successful'

    #Grab the internal list
    obj1_list = obj1['features']

    #Loop through the list and add the internal objects to a new list using the 'properties' key.
    prop_list = []
    for prop_obj in obj1_list:
        prop_list.append(prop_obj['properties'])

    #Create Pandas DataFrame, drop unecessary column and display sample
    df = pd.DataFrame(prop_list)

    return df