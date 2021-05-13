# covid-19 project
## Notes
strategic customers HEB, We don't have all customers mapped. Strategic vs non-strategic. CEO wants to know how many customers are in this critical class locations.

1. Getting public use data of grocery, healthcare, 
2. automate and build mariadb database build a pipleline to 
3. focus on healthcare, food & ag, energy
4. TSP codes indicate they have some critical function that makes them higher priority.
5. I need to know all critical inf that are HealthCare and Public Health Sector.
6. when i have the hospital piece then let him know. Then iterate on other sources for other critical categories.

Steps to create Python Environment:

1. Clone the repository: https://gitlab.one.twcbiz.com/jcastillo02/hifld_import_pub_data_extract.git
2. Create virtual Environment with command: python -m venv env
3. Download all packages with command: pip install requirements.txt

## Resources
* [HIFLD](https://services1.arcgis.com/Hp6G80Pky0om7QvQ/arcgis/rest/services/Hospitals_1/FeatureServer/0/query?outFields=*&where=1%3D1)
   * [Catalog](https://gii.dhs.gov/hifld/content/hifld-data-catalog)
* [Homeland Security Critical Infrastructure](https://www.cisa.gov/identifying-critical-infrastructure-during-covid-19)
* [NYTimes COVID19 Data](https://www.kaggle.com/paultimothymooney/nytimes-covid19-data/download)
   * `kaggle datasets download -d paultimothymooney/nytimes-covid19-data`

## Data Models
``` yaml
-Database Name: healthcare_and_public_health
	-tables:
		-hospitals 
		-pharmacies 
		-public_health_departments
		-urgent_care_facilities 
		-veterans_health_administration_medical_facilities 

-Database name: food_and_agriculture
	-tables:
		-poultry_slaughtering_and_processing_facilities
		-public_refrigerated_warehouses
		
-Database name: communications
	-tables:
		-'am_transmission_towers',
		-'antenna_structure_registrate',
		-'broadband_and_educational_broadband_service_transmitters',
		-'cellular_service_areas',
		-'cellular_towers',
		-'fm_transmission_towers',
		-'land_mobile_broadcast_towers',
		-'land_mobile_commercial_transmission_towers',
		-'land_mobile_private_transmission_towers',
		-'microwave_service_towers',
		-'paging_transmission_towers',
		-'tv_analog_station_transmitters',
		-'tv_broadcast_contours',
		-'tv_digital_station_transmitters'

-Database name: emergency_services
	-tables:
		-american_red_cross_chapter_facilities
		-american_red_cross_headquarters      
		-american_red_cross_regions
		-ems_stations
		-fema_recovery_offices
		-fema_regional_offices
		-fema_regions
		-fire_stations
		-hurricane_evacuation_routes
		-local_emergency_ops_centers
		-national_shelter_system_facilities
		-psap_911_service_area_boundaries
		-state_emergency_ops_centers

-Database name: energy
	-tables:
		-biodiesel_plants
		-bottom_wells
		-control_areas
		-electric_holding_company_areas
		-electric_planning_areas
		-electric_power_transmission_lines
		-electric_retail_service_territories
		-electric_substations
		-epa_frs_power_plants
		-ethanol_plants
		-ethanol_transloading_facilities
		-ferc_regions
		-generating_units
		-hydrocarbon_gas_liquid_pipelines
		-indepenent_system_operators
		-lng_import_exports_and_terminals
		-natural_gas_compressor_stations
		-natural_gas_import_export
		-natural_gas_local_dist_service_territories
		-natural_gas_pipelines
		-natural_gas_processings_and_plants
		-natural_gas_receipt_delivery_points
		-natural_gas_storage_facilities
		-nerc_regions
		-nerc_reliability_coordinators
		-oil_and_natural_gas_fields
		-oil_and_natural_gas_interconnects
		-oil_and_natural_gas_platforms
		-oil_and_natural_gas_wells
		-ocs_drilling_platforms
		-ocs_natural_gas_wells
		-petroleum_ports
		-petroleum_terminals
		-pol_pumping_stations
		-power_plants

Database name: water_supply
	-tables:
		-aquifers
		-dam_lines
		-epa_frs_wastewater_treatment_plant
		-nhd_areas_large_scale
		-nhd_areas_small_scale
		-nhd_flowlines_large_scale
		-nhd_flowlines_small_scale
		-nhd_lines_large_scale
		-nhd_lines_small_scale
		-nhd_point_events
		-nhd_points
		-nhd_waterbodies_large_scale
		-nhd_waterbodies_small_scale
		-reclamation_reservoirs
		-usace_owned_operated_reservoirs
		-watershed_boundary_lines
```