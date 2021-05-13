from hifld_json_functions import hifld_dataframe

from mariadb_functions import table_exists, mariadb_write

def main():

    source = {'transport.trails': 'https://opendata.arcgis.com/datasets/2adfa36ed53646409e0f42f86e494730_0.geojson', 
    'transport.aircraft_landing_facilities': 'https://opendata.arcgis.com/datasets/f6c9f71016f7461ba8e260a3a60b92a7_0.geojson', 
    'transport.faa_regions': 'https://opendata.arcgis.com/datasets/33fb3a7400284b9db780307f0d18a5f2_0.geojson', 
    'transport.runways': 'https://opendata.arcgis.com/datasets/518e7315b90f4fff82d4511c7115eef2_0.geojson', 
    'transport.amtrack_stations': 'https://opendata.arcgis.com/datasets/628537f4cf774cde8aa9721212226390_0.geojson',
    'transport.fixed_guideway_transit_stations': 'https://opendata.arcgis.com/datasets/c16416d09be2411ab7c42225c56999d5_0.geojson', 
    'transport.intermodal_passenger_connectivity': 'https://opendata.arcgis.com/datasets/a316a953272a4faf8ae74b426c88d543_0.geojson', 
    'transport.national_bridge_inventory': 'https://opendata.arcgis.com/datasets/a9b05a595ff94f3fa3888d1240545740_0.geojson', 
    'transport.public_transit_routes': 'https://opendata.arcgis.com/datasets/b1e65e78c4c647d18958c99b17622509_0.geojson'}


    for table in source:

        if table_exists(table) == True:

            print(f'Table: "{table}" exists')

        else:

            #print(f'Creating Table: {table}')

            resultsdf = hifld_dataframe(source[table])

            #print(resultsdf)
            results = mariadb_write(table, resultsdf)

            print(results)

if __name__ == '__main__':
    main()
