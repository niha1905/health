#this works:)

from airtable import Airtable

# Replace these with your Airtable API key, base ID, and table name
AIRTABLE_API_KEY = 'pat7hpgmy2itPqWrX.da8a874efe149fc7f8569d6297d44973b6175731bb489123aa14de17b35686ae'
AIRTABLE_BASE_ID = 'app2WlcjTHxf5aCIZ'
AIRTABLE_TABLE_NAME = 'smartwatch_data'

# Create an Airtable object
airtable = Airtable(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, AIRTABLE_API_KEY)


try:
    records = airtable.get_all()
except Exception as e:
    print(f"Error fetching records: {e}")
'''
# Print the records
for record in records:
    print(record['fields'])
'''
'''first_record = airtable.get_all()[0]

# Print column names
column_names = first_record['fields'].keys()
print("Column Names:")
for column in column_names:
    print(column)
'''
'''
Name
Pulse
Latitude
Longitude
nursing home
Photo
Heart_Rate_BPM
SPO2
Skin_temperature
gender
BP_Diastolic 2
Step_Counter
BP_Systolic
BP_Systolic 2
ID
BP_Diastolic
Phone Number
'''

patient_records = []

for record in records:
    fields_data = record['fields']
    '''patient_instance = PatientRecord(
        name=fields_data.get('Name'),
        latitude=fields_data.get('Latitude'),
        longitude=fields_data.get('Longitude'),
        heart_rate_bpm=fields_data.get('Heart_Rate_BPM'),
        pulse=fields_data.get('Pulse'),
        spo2=fields_data.get('SPO2'),
        bp_systolic=fields_data.get('BP_Systolic'),
        bp_diastolic=fields_data.get('BP_Diastolic'),
        step_counter=fields_data.get('Step_Counter'),
        skin_temperature=fields_data.get('Skin_temperature'),
        nursing_home=fields_data.get('nursing home'),
        gender=fields_data.get('gender'),
        photo=fields_data.get('Photo'),
        phone_number=fields_data.get('Phone Number')
    )
    patient_records.append(patient_instance)
    '''
    print(fields_data.get('Name'))