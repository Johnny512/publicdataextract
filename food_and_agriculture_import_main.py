from hifld_json_functions import hifld_dataframe

from mariadb_functions import create_db, table_exists, mariadb_write

def main():

    """
    This executes functions related to Food and Agriculture from HIFLD datasets
    """

    source = {'food.poultry_processing_facilities': 'https://opendata.arcgis.com/datasets/55d907e8c03649cd996a99bea1c4fe07_0.geojson',
              'food.public_refrigerated_warehouses': 'https://opendata.arcgis.com/datasets/22c3961adfdb4a8daffdc2d6277b9633_0.geojson'}

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
