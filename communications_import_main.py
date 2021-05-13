from hifld_json_functions import hifld_dataframe

from mariadb_functions import table_exists, mariadb_write

def main():

    """
    This executes functions related to HIFLD datasets and processes into dataframe then writes to database
    """

    source = {'comm.am_transmission_towers': 'https://opendata.arcgis.com/datasets/8dc622e0d473417b81494c1ee587df50_0.geojson', 
    'comm.antenna_structure_registrate': 'https://opendata.arcgis.com/datasets/a3c6520e6d7942b0abaf569dd721788b_0.geojson', 
    'comm.broadband_and_educational_broadband_service_transmitters': 'https://opendata.arcgis.com/datasets/e268048c26be47efa63cb15e81a25f4b_0.geojson', 
    'comm.cellular_service_areas': 'https://opendata.arcgis.com/datasets/b01aac4aca194b78aba62404ece987bb_0.geojson', 
    'comm.cellular_towers': 'https://opendata.arcgis.com/datasets/0835ba2ed38f494196c14af8407454fb_0.geojson', 
    'comm.fm_transmission_towers': 'https://opendata.arcgis.com/datasets/fc3838297bb844daadb4bebe714bba78_0.geojson', 
    'comm.land_mobile_broadcast_towers': 'https://opendata.arcgis.com/datasets/ec4d868ea1354fc9a85fe35e7db0cffd_0.geojson',
    'comm.land_mobile_commercial_transmission_towers': 'https://opendata.arcgis.com/datasets/4ec3d6fe24124d7597da4c88dfeae678_0.geojson', 
    'comm.land_mobile_private_transmission_towers': 'https://opendata.arcgis.com/datasets/4797be545f7449b4ab7b52b9e5b52ffc_0.geojson', 
    'comm.microwave_service_towers': 'https://opendata.arcgis.com/datasets/ed7eba3a40264dfea65c282af5d8d3c9_0.geojson', 
    'comm.paging_transmission_towers': 'https://opendata.arcgis.com/datasets/98d19dce5c1b443eaaae3288229e103d_0.geojson', 
    'comm.tv_analog_station_transmitters': 'https://opendata.arcgis.com/datasets/05455bf306ed438f84a398e14cdb6d51_0.geojson', 
    'comm.tv_broadcast_contours': 'https://opendata.arcgis.com/datasets/c648514663b64864843ff6b799fb7e24_0.geojson', 
    'comm.tv_digital_station_transmitters': 'https://opendata.arcgis.com/datasets/2bfd434d9263401eadae464a9c26104f_0.geojson'}

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
