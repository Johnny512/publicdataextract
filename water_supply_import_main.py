from hifld_json_functions import hifld_dataframe

from mariadb_functions import table_exists, mariadb_write

def main():

    source = {'water.aquifers': 'https://opendata.arcgis.com/datasets/d2ce672fda1f44089af659b629d11458_0.geojson',
    'water.dam_lines': 'https://opendata.arcgis.com/datasets/128ad6541ace4bf8b7a12a395ba9d8b9_0.geojson',
    'water.epa_frs_wastewater_treatment_plant': 'https://opendata.arcgis.com/datasets/4b9bac25263047c19e617d7bd7b30701_0.geojson',
    'water.nhd_areas_large_scale': 'https://opendata.arcgis.com/datasets/e12c65d5070d4239b789767dab99d9d3_8.geojson',
    'water.nhd_areas_small_scale': 'https://opendata.arcgis.com/datasets/df32f7bcbbfd4f80b8407d3cf6346373_7.geojson',
    'water.nhd_flowlines_large_scale': 'https://opendata.arcgis.com/datasets/acc809ddc7b245b1a10fe86159eb6556_6.geojson',
    'water.nhd_flowlines_small_scale': 'https://hifld-geoplatform.opendata.arcgis.com/datasets/national-hydrography-dataset-nhd-flowlines-small-scale',
    'water.nhd_lines_large_scale': 'https://opendata.arcgis.com/datasets/d753f0f1896844b59fe9b2355b12a425_3.geojson',
    'water.nhd_lines_small_scale': 'https://opendata.arcgis.com/datasets/881cc3cc4dda4f6e8569d331ede08f81_2.geojson',
    'water.nhd_point_events': 'https://opendata.arcgis.com/datasets/a9faf578e1e94aeeb6e5cb392d834667_1.geojson',
    'water.nhd_points': 'https://opendata.arcgis.com/datasets/9389e2e84b2a4259ad0a0f12077eb51f_0.geojson',
    'water.nhd_waterbodies_large_scale': 'https://opendata.arcgis.com/datasets/dd78ae237fe64b9582b84ad9869c4365_10.geojson',
    'water.nhd_waterbodies_small_scale': 'https://opendata.arcgis.com/datasets/4f95153df421471d825a1137baabcf2f_9.geojson',
    'water.reclamation_reservoirs': 'https://opendata.arcgis.com/datasets/414d6b8603bc418f9fc4ab509e8596ff_0.geojson',
    'water.usace_owned_operated_reservoirs': 'https://opendata.arcgis.com/datasets/e8abf1e31e2644458a9cd62145f9048c_0.geojson',
    'water.watershed_boundary_lines': 'https://opendata.arcgis.com/datasets/b5ecb8870aa747259359f2c92af6c742_0.geojson'}

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