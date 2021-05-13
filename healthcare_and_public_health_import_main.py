from hifld_json_functions import hifld_dataframe

from healthready_csv_functions import healthready_dataframe

from mariadb_functions import table_exists, mariadb_write

def main():


    """
    Hospital Data imports module from ornl_json_functions
    """

    source = {'health.hospitals': 'https://opendata.arcgis.com/datasets/6ac5e325468c4cb9b905f1728d6fbf0f_0.geojson', 
    'health.public_health_departments': 'https://opendata.arcgis.com/datasets/1b919b0ff5f44d05bcb374591206f757_0.geojson',
    'health.urgent_care_facilities': 'https://opendata.arcgis.com/datasets/335ccc7c0684453fad69d8a64bc89192_0.geojson', 
    'health.va_admin_medical_facilities': 'https://opendata.arcgis.com/datasets/f11d7d153bfb408f85bd029b2dac9298_0.geojson'}

    for table in source:

        if table_exists(table) == True:

            print(f'Table: "{table}" exists')

        else:

            #print(f'Creating Table: {table}')

            resultsdf = hifld_dataframe(source[table])

            #print(resultsdf)
            results = mariadb_write(table, resultsdf)

            print(results)

    """
    Pharmacy Data imports uses healthready_csv_functions module
    """

    source2 = {'health.pharmacies': 'http://rxopen.org/api/v1/map/download/facility'}

    for table in source2:

        if table_exists(table) == True:

            print(f'Table: "{table}" exists')

        else:

            #print(f'Creating Table: {table}')

            resultsdf = healthready_dataframe(source2[table])

            #print(resultsdf)
            results = mariadb_write(table, resultsdf)

            print(results)

if __name__ == '__main__':
    main()
