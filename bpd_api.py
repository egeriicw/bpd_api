
import json
import requests
from config import *

def bpd_analyze_peers(payload_data):

    bpd_analyze_peers_url = BPD_API_BASEURL + '/peers/'

    # '22206','22301','22302','22304','22305','22311','22314'

    payload = {
	    'filters': payload_data,
	    'auto_bin': False,
	    'eui_type': 'total_site_consumption'
    }

    ###################
    # Example payload # 
    ###################
    # payload = {
	   #  'filters': {
	   #      'state': ['VA'],
	   #      'classification_type': ['Commercial'],
	   #      'zip_code': ['22206','22301','22302','22304','22305','22311','22314']
	   #  },
	   #  'auto_bin': False,
	   #  'eui_type': 'total_site_consumption'
    # }

    response = requests.post(bpd_analyze_peers_url, data=json.dumps(payload), headers=BPD_API_HEADERS)

    return response.text


def bpd_analyze_counts_per_states(payload_data):
    bpd_analyze_counts_per_states_url = BPD_API_BASEURL + '/counts-per-states/'

    payload = {'filters': payload_data}

    response = requests.post(bpd_analyze_counts_per_states_url, data=json.dumps(payload), headers=BPD_API_HEADERS)

    return response.text

def bdp_analyze_compare_eui(payload_data, building_system, from_technology, to_technology):
    bpd_analyze_compare_eui_url = BPD_API_BASEURL + '/compare/eui/'

    payload = {
	    'filters': payload_data,
	    'building_system': building_system,
	    'from': from_technology,
	    'to': to_technology
    }

    response = requests.post(bpd_analyze_compare_eui_url, data=json.dumps(payload), headers=BPD_API_HEADERS)

    return response.text



def bpd_construct_filter(payload_data):

    classification_type = ['Commercial', 'Residential']
    facility_type = ['Agricultural','Commercial - Uncategorized','Convenience store','Convenience store with gas station','Data Center', 'Education - College or university','Education - Elementary or middle school','Education - High school','Education - Other classroom','Education - Preschool or daycare','Education - Uncategorized','Food Sales','Food Service  - Other','Food Service  - Restaurant or cafeteria','Food Service - Bakery','Food Service - Fast food','Food Service - Uncategorized','Grocery store or food market','Health Care - Inpatient','Health Care - Outpatient Clinic','Health Care - Outpatient Diagnostic','Health Care - Outpatient Uncategorized','Health Care - Uncategorized','Industrial','Laboratory','Lodging -  Hotel','Lodging - Dormitory or fraternity/sorority','Lodging - Motel or inn','Lodging - Other','Lodging - Uncategorized','Nursing Home','Office  - Administrative or Professional','Office - Bank or other financial','Office - Government','Office - Medical non diagnostic','Office - Mixed use','Office - Other','Office - Uncategorized','Other','Parking Garage','Public Assembly - Arena','Public Assembly - Drama theater','Public Assembly - Entertainment/culture','Public Assembly - Large Hall','Public Assembly - Library','Public Assembly - Movie Theater','Public Assembly - Recreation','Public Assembly - Social/meeting','Public Assembly - Uncategorized','Public Safety - Courthouse','Public Safety - Fire or police station','Public Safety - Uncategorized','Religious worship','Residential','Retail - Big Box (> 50K sf)','Retail - Enclosed mall','Retail - Other than mall','Retail - Small Box (< 50K sf)','Retail - Strip shopping mall','Retail - Uncategorized','Retail - Vehicle dealership/showroom','Service  - Industrial shop','Service -  Post office or postal center','Service -  Repair shop','Service - Art/Video/Photography Studio','Service - Dry-cleaning or Laundry','Service - Other service','Service - Uncategorized','Service - Vehicle service/repair shop','Transportation Terminal','Vacant','Warehouse - Distribution or Shipping center','Warehouse - Non-refrigerated','Warehouse - Refrigerated','Warehouse - Self-storage','Warehouse - Uncategorized','2-4 Unit Building','5+ Unit Building','Apartment Unit','Manufactured Home','Multifamily - Condominiums','Multifamily - Uncategorized','Other','Single Family - Attached','Single Family - Detached','Single Family - Uncategorized','Unknown']
    floor_area = None 		# range (square meters)
    year_built = None 		# range
    hours_occupied = None	# range (0 to 168)
    number_of_people = None	# range
    climate_zone = ['1A Very Hot - Humid (Miami-FL)','2A Hot - Humid (Houston-TX)','2B Hot - Dry (Phoenix-AZ)','3A Warm - Humid (Memphis-TN)','3B Warm - Dry (El Paso-TX)','3C Warm - Marine (San Francisco-CA)','4A Mixed - Humid (Baltimore-MD)','4B Mixed - Dry (Albuquerque-NM)','4C Mixed - Marine (Salem-OR)','5A Cool - Humid (Chicago-IL)','5B Cool - Dry (Boise-ID)','6A Cold - Humid (Burlington-VT)','6B Cold -Dry (Helena-MT)','7 Very Cold (Duluth-MN)','8 Subarctic (Fairbanks-AK)']
    state = ['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','PR']
    zip_code = ['22206','22301','22302','22304','22305','22311','22314']
    lighting = ['Compact Fluorescent','Fluorescent - T12','Fluorescent - T5','Fluorescent - T8','Fluorescent - Uncategorized','Halogen','High intensity discharge (HID)','Incandescent','LED','Mercury Vapor','Metal Halide','Other Or Combination','Sodium - High Pressure','Sodium - Low Pressure','Unknown']		
    heating = ['Boiler - Hot Water','Boiler - Steam','Boiler - Uncategorized','Central Heating','District Hot Water','District Steam','Furnace','Heat Pump - Air Source','Heat Pump - Ground Source','Heat Pump - Uncategorized','Heat Pump - Water Loop','No Heating','Other Or Combination','PTAC','Perimeter Baseboard','Radiator','Resistance Heating','Unknown']
    cooling = ['Central Air Conditioning','Chiller - Absorption','Chiller - Engine Driven','Chiller - Turbine Driven','Chiller - Uncategorized','Condenser','Cooling Tower - Closed','Cooling Tower - Open','Cooling Tower - Uncategorized','District Chilled Water','Evaporative Cooler','Heat Pump - Air Source','Heat Pump - Ground Source','Heat Pump - Uncategorized','Heat Pump - Water Loop','No cooling','Other Or Combination','PTAC','Packaged Direct Expansion','Split AC System','Unknown']
    window_glass_type = ['Clear','High Performance','Low-e','Other Or Combination','Reflective','Tinted','Unknown']
    window_glass_layers = ['Double-pane','Multi-layered','Other Or Combination','Single-pane','Triple-pane','Unknown']
    air_flow_control = ['Constant Volume','Unknown','Variable Volume']		
    wall_insulation_r_value = None # range (0 to 80)
    roof_ceiling = ['Asphalt/fiberglass/other shingles','Built-up','Concrete','Cool Roof','Metal surfacing','Other Or Combination','Plastic/rubber/synthetic sheeting','Slate or tile shingles','Unknown','Wood shingles/shakes/other wood']

if __name__ == "__main__":
    
    payload = {'state': ['VA'],'classification_type': ['Commercial'],'zip_code': ['22206','22301','22302','22304','22305','22311','22314']}

    print bpd_analyze_peers(payload)
    print bpd_analyze_counts_per_states(payload)
    #print bpd_analyze_compare_eui(payload, '')




    	# classification_type:
		# -	Commercial
		# -	Residential

		# facility_type:
		# -	Agricultural
		# -	Commercial - Uncategorized
		# -	Convenience store
		# -	Convenience store with gas station
		# -	Data Center
		# -	Education - College or university
		# -	Education - Elementary or middle school
		# -	Education - High school
		# -	Education - Other classroom
		# -	Education - Preschool or daycare
		# -	Education - Uncategorized
		# -	Food Sales
		# -	Food Service  - Other
		# -	Food Service  - Restaurant or cafeteria
		# -	Food Service - Bakery
		# -	Food Service - Fast food
		# 	Food Service - Uncategorized
		# 	Grocery store or food market
		# 	Health Care - Inpatient
		# 	Health Care - Outpatient Clinic
		# 	Health Care - Outpatient Diagnostic
		# 	Health Care - Outpatient Uncategorized
		# 	Health Care - Uncategorized
		# 	Industrial
		# 	Laboratory
		# 	Lodging -  Hotel
		# 	Lodging - Dormitory or fraternity/sorority
		# 	Lodging - Motel or inn
		# 	Lodging - Other
		# 	Lodging - Uncategorized
		# 	Nursing Home
		# 	Office  - Administrative or Professional
		# 	Office - Bank or other financial
		# 	Office - Government
		# 	Office - Medical non diagnostic
		# 	Office - Mixed use
		# 	Office - Other
		# 	Office - Uncategorized
		# 	Other
		# 	Parking Garage
		# 	Public Assembly - Arena
		# 	Public Assembly - Drama theater
		# 	Public Assembly - Entertainment/culture
		# 	Public Assembly - Large Hall
		# 	Public Assembly - Library
		# 	Public Assembly - Movie Theater
		# 	Public Assembly - Recreation
		# 	Public Assembly - Social/meeting
		# 	Public Assembly - Uncategorized
		# 	Public Safety - Courthouse
		# 	Public Safety - Fire or police station
		# 	Public Safety - Uncategorized
		# 	Religious worship
		# 	Residential
		# 	Retail - Big Box (> 50K sf)
		# 	Retail - Enclosed mall
		# 	Retail - Other than mall
		# 	Retail - Small Box (< 50K sf)
		# 	Retail - Strip shopping mall
		# 	Retail - Uncategorized
		# 	Retail - Vehicle dealership/showroom
		# 	Service  - Industrial shop
		# 	Service -  Post office or postal center
		# 	Service -  Repair shop
		# 	Service - Art/Video/Photography Studio
		# 	Service - Dry-cleaning or Laundry
		# 	Service - Other service
		# 	Service - Uncategorized
		# 	Service - Vehicle service/repair shop
		# 	Transportation Terminal
		# 	Vacant
		# 	Warehouse - Distribution or Shipping center
		# 	Warehouse - Non-refrigerated
		# 	Warehouse - Refrigerated
		# 	Warehouse - Self-storage
		# 	Warehouse - Uncategorized
		# 	2-4 Unit Building
		# 	5+ Unit Building
		# 	Apartment Unit
		# 	Manufactured Home
		# 	Multifamily - Condominiums
		# 	Multifamily - Uncategorized
		# 	Other
		# 	Single Family - Attached
		# 	Single Family - Detached
		# 	Single Family - Uncategorized
		# 	Unknown
		
		# floor_area
		# 	range (square meters)
		
		# year_built
		# 	range
		
		# hours_occupied
		# 	range (0 to 168)
		
		# number_of_people
		# 	range
		
		# climate_zone
		# 	1A Very Hot - Humid (Miami-FL)
		# 	2A Hot - Humid (Houston-TX)
		# 	2B Hot - Dry (Phoenix-AZ)
		# 	3A Warm - Humid (Memphis-TN)
		# 	3B Warm - Dry (El Paso-TX)
		# 	3C Warm - Marine (San Francisco-CA)
		# 	4A Mixed - Humid (Baltimore-MD)
		# 	4B Mixed - Dry (Albuquerque-NM)
		# 	4C Mixed - Marine (Salem-OR)
		# 	5A Cool - Humid (Chicago-IL)
		# 	5B Cool - Dry (Boise-ID)
		# 	6A Cold - Humid (Burlington-VT)
		# 	6B Cold -Dry (Helena-MT)
		# 	7 Very Cold (Duluth-MN)
		# 	8 Subarctic (Fairbanks-AK)
		
		# state
		# 	AL
		# 	AK
		# 	AZ
		# 	AR
		# 	CA
		# 	CO
		# 	CT
		# 	DE
		# 	DC
		# 	FL
		# 	GA
		# 	HI
		# 	ID
		# 	IL
		# 	IN
		# 	IA
		# 	KS
		# 	KY
		# 	LA
		# 	ME
		# 	MD
		# 	MA
		# 	MI
		# 	MN
		# 	MS
		# 	MO
		# 	MT
		# 	NE
		# 	NV
		# 	NH
		# 	NJ
		# 	NM
		# 	NY
		# 	NC
		# 	ND
		# 	OH
		# 	OK
		# 	OR
		# 	PA
		# 	RI
		# 	SC
		# 	SD
		# 	TN
		# 	TX
		# 	UT
		# 	VT
		# 	VA
		# 	WA
		# 	WV
		# 	WI
		# 	WY
		# 	PR
		
		# zip_code
		# 	JSON list of zip codes as strings (see example above)
		
		# lighting
		# 	Compact Fluorescent
		# 	Fluorescent - T12
		# 	Fluorescent - T5
		# 	Fluorescent - T8
		# 	Fluorescent - Uncategorized
		# 	Halogen
		# 	High intensity discharge (HID)
		# 	Incandescent
		# 	LED
		# 	Mercury Vapor
		# 	Metal Halide
		# 	Other Or Combination
		# 	Sodium - High Pressure
		# 	Sodium - Low Pressure
		# 	Unknown
		
		# heating
		# 	Boiler - Hot Water
		# 	Boiler - Steam
		# 	Boiler - Uncategorized
		# 	Central Heating
		# 	District Hot Water
		# 	District Steam
		# 	Furnace
		# 	Heat Pump - Air Source
		# 	Heat Pump - Ground Source
		# 	Heat Pump - Uncategorized
		# 	Heat Pump - Water Loop
		# 	No Heating
		# 	Other Or Combination
		# 	PTAC
		# 	Perimeter Baseboard
		# 	Radiator
		# 	Resistance Heating
		# 	Unknown
		
		# cooling
		# 	Central Air Conditioning
		# 	Chiller - Absorption
		# 	Chiller - Engine Driven
		# 	Chiller - Turbine Driven
		# 	Chiller - Uncategorized
		# 	Condenser
		# 	Cooling Tower - Closed
		# 	Cooling Tower - Open
		# 	Cooling Tower - Uncategorized
		# 	District Chilled Water
		# 	Evaporative Cooler
		# 	Heat Pump - Air Source
		# 	Heat Pump - Ground Source
		# 	Heat Pump - Uncategorized
		# 	Heat Pump - Water Loop
		# 	No cooling
		# 	Other Or Combination
		# 	PTAC
		# 	Packaged Direct Expansion
		# 	Split AC System
		# 	Unknown
		
		# window_glass_type
		# 	Clear
		# 	High Performance
		# 	Low-e
		# 	Other Or Combination
		# 	Reflective
		# 	Tinted
		# 	Unknown
		
		# window_glass_layers
		# 	Double-pane
		# 	Multi-layered
		# 	Other Or Combination
		# 	Single-pane
		# 	Triple-pane
		# 	Unknown
		
		# air_flow_control
		# 	Constant Volume
		# 	Unknown
		# 	Variable Volume
		
		# wall_insulation_r_value
		# 	range (0 to 80)
		
		# roof_ceiling
		# 	Asphalt/fiberglass/other shingles
		# 	Built-up
		# 	Concrete
		# 	Cool Roof
		# 	Metal surfacing
		# 	Other Or Combination
		# 	Plastic/rubber/synthetic sheeting
		# 	Slate or tile shingles
		# 	Unknown
		# 	Wood shingles/shakes/other wood