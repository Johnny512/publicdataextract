from hifld_json_functions import hifld_dataframe

from mariadb_functions import mariadb_write, table_exists

def main():

    source = {'energy.biodiesel_plants': 'https://opendata.arcgis.com/datasets/20db0061f0bb4eaaa02942e8818c0f79_0.geojson', 
    'energy.bottom_wells': 'https://opendata.arcgis.com/datasets/de71df03a4ed4578851638e8910c0108_0.geojson', 
    'energy.control_areas': 'https://opendata.arcgis.com/datasets/02602aecc68d4e0a90bf65e818155f60_0.geojson', 
    'energy.electric_holding_company_areas': 'https://opendata.arcgis.com/datasets/42e8e0c7a3194ab0a42604e5a2cb63ef_0.geojson', 
    'energy.electric_planning_areas': 'https://opendata.arcgis.com/datasets/7d35521e3b2c48ab8048330e14a4d2d1_0.geojson', 
    'energy.electric_power_transmission_lines': 'https://opendata.arcgis.com/datasets/70512b03fe994c6393107cc9946e5c22_0.geojson', 
    'energy.electric_retail_service_territories': 'https://opendata.arcgis.com/datasets/c4fd0b01c2544a2f83440dab292f0980_0.geojson', 
    'energy.electric_substations': 'https://opendata.arcgis.com/datasets/755e8c8ae15a4c9abfceca7b2e95fb9a_0.geojson', 
    'energy.epa_frs_power_plants': 'https://opendata.arcgis.com/datasets/21698d59fa9b4110902b4fc2851426d9_12.geojson', 
    'energy.ethanol_plants': 'https://opendata.arcgis.com/datasets/489eb0a8ed7e4ebab624c8c4acca7569_0.geojson', 
    'energy.ethanol_transloading_facilities': 'https://opendata.arcgis.com/datasets/a520ff2ec6a040ffa38beca431f42d27_0.geojson', 
    'energy.ferc_regions': 'https://opendata.arcgis.com/datasets/ae9bc057efa44f23bde91a2cb8e996db_0.geojson', 
    'energy.generating_units': 'https://opendata.arcgis.com/datasets/14b5a08efaec446ba7aa0121220141fa_0.geojson', 
    'energy.hydrocarbon_gas_liquid_pipelines': 'https://opendata.arcgis.com/datasets/7e0df431f6994399ae48c6a03e29f060_0.geojson', 
    'energy.indepenent_system_operators': 'https://opendata.arcgis.com/datasets/9d1099b016e5482c900d657f06f3ac80_0.geojson', 
    'energy.lng_import_exports_and_terminals': 'https://opendata.arcgis.com/datasets/57baedf9075f42c5b966607a9caa8616_0.geojson', 
    'energy.natural_gas_compressor_stations': 'https://opendata.arcgis.com/datasets/cb4ea4a90a5e4849860d0d56058c2f75_0.geojson', 
    'energy.natural_gas_import_export': 'https://opendata.arcgis.com/datasets/c4dd08fed90744a2acb4d95be0c5b792_0.geojson',
    'energy.natural_gas_local_dist_service_territories': 'https://opendata.arcgis.com/datasets/a3d48c142f88433ab77aa755a56aa07a_0.geojson', 
    'energy.natural_gas_pipelines': 'https://opendata.arcgis.com/datasets/f44e00fce8b943f69a40a2324cf49dfd_0.geojson', 
    'energy.natural_gas_processings_and_plants': 'https://opendata.arcgis.com/datasets/ca984888f8154c63bf3a023f0a1f9ac2_0.geojson', 
    'energy.natural_gas_receipt_delivery_points': 'https://opendata.arcgis.com/datasets/6e01edc178ea4b7e9cec874e206248a2_0.geojson', 
    'energy.natural_gas_storage_facilities': 'https://opendata.arcgis.com/datasets/dfbff0ff802d4a64b13af1f81fac54cf_0.geojson', 
    'energy.nerc_regions': 'https://opendata.arcgis.com/datasets/6b2af23c67f04f4cb01d88c61aaf558a_0.geojson', 
    'energy.nerc_reliability_coordinators': 'https://opendata.arcgis.com/datasets/ee47fbb73fc04d609510f340e1c1952c_0.geojson', 
    'energy.oil_and_natural_gas_fields': 'https://opendata.arcgis.com/datasets/b7bfd5a75537493d894140bd9527337e_0.geojson', 
    'energy.oil_and_natural_gas_interconnects': 'https://opendata.arcgis.com/datasets/749f935c235f4a5eac0db20493a63e7f_0.geojson', 
    'energy.oil_and_natural_gas_platforms': 'https://opendata.arcgis.com/datasets/d6403a49d5cd428ebe67a1fa7fd69a40_0.geojson', 
    'energy.oil_and_natural_gas_wells': 'https://opendata.arcgis.com/datasets/17c5ed5a6bd44dd0a52c616a5b0cacca_0.geojson', 
    'energy.ocs_drilling_platforms': 'https://opendata.arcgis.com/datasets/eb03e987f5524504838f6a4501fe5453_0.geojson', 
    'energy.ocs_natural_gas_wells': 'https://opendata.arcgis.com/datasets/ecf85c4e074745cfae5fce7baac4ada9_1.geojson', 
    'energy.petroleum_ports': 'https://opendata.arcgis.com/datasets/16aafe11156d4ce591c6c054e94fffca_0.geojson', 
    'energy.petroleum_terminals': 'https://opendata.arcgis.com/datasets/7841aba67178425cbf33995fc914e2fe_0.geojson', 
    'energy.pol_pumping_stations': 'https://opendata.arcgis.com/datasets/eb91d583a04042e7a5aff0b72bad0ef9_0.geojson', 
    'energy.power_plants': 'https://opendata.arcgis.com/datasets/ee0263bd105d41599be22d46107341c3_0.geojson'}

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
