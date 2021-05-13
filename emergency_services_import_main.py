from hifld_json_functions import hifld_dataframe

from mariadb_functions import table_exists, mariadb_write

def main():

    source = {'emergency.american_red_cross_chapter_facilities': 'https://opendata.arcgis.com/datasets/432f35312f0849f697b263f3d753e5ed_0.geojson', 
    'emergency.american_red_cross_headquarters': 'https://opendata.arcgis.com/datasets/90780ba531ac42f9824c8bd1a00f219d_0.geojson', 
    'emergency.american_red_cross_regions': 'https://opendata.arcgis.com/datasets/922ca1db135540e48943a870877bef70_2.geojson', 
    'emergency.ems_stations': 'https://opendata.arcgis.com/datasets/362c9480f12e4587b6a502f9ceedccde_0.geojson', 
    'emergency.fema_recovery_offices': 'https://opendata.arcgis.com/datasets/05a88d9d954d4ec68d21794b382b2df3_1.geojson', 
    'emergency.fema_regional_offices': 'https://opendata.arcgis.com/datasets/6622aa77740944a29a31ddfd8e913317_0.geojson', 
    'emergency.fema_regions': 'https://opendata.arcgis.com/datasets/5f6207ccb91d4ae48124018ffaec04bf_2.geojson', 
    'emergency.fire_stations': 'https://opendata.arcgis.com/datasets/0ccaf0c53b794eb8ac3d3de6afdb3286_0.geojson', 
    'emergency.hurricane_evacuation_routes': 'https://opendata.arcgis.com/datasets/3331d09be1684c3d8053a0b71edb54d2_0.geojson', 
    'emergency.local_emergency_ops_centers': 'https://opendata.arcgis.com/datasets/874798faedc74358bac9bbe1867af3c7_0.geojson', 
    'emergency.national_shelter_system_facilities': 'https://opendata.arcgis.com/datasets/bcaf5fdb3db24c78afee52d4c8a02748_5.geojson', 
    'emergency.911_service_area_boundaries': 'https://opendata.arcgis.com/datasets/d47bd3b0796f48d488d63c9917d25100_0.geojson', 
    'emergency.state_emergency_ops_centers': 'https://opendata.arcgis.com/datasets/1a7559aff4844505a1c78efc46368112_0.geojson'}

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
