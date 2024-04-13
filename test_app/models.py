'''from azure.cosmos import CosmosClient, exceptions

# Initialize the Cosmos client
endpoint = "your_cosmosdb_uri"
key = "your_cosmosdb_key"
client = CosmosClient(endpoint, key)

# Select the database and container (collection) within your Cosmos DB account
database_name = 'your_database_name'
container_name = 'your_container_name'
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

class PatientRecord:
    def __init__(self,  name, latitude, longitude, heart_rate_bpm, pulse, spo2, bp_systolic, bp_diastolic,
                 step_counter, skin_temperature, nursing_home, gender, photo, phone_number):
        # Same as before
        self.Name = name
        self.Latitude = latitude
        self.Longitude = longitude
        self.Heart_Rate_BPM = heart_rate_bpm
        self.Pulse = pulse
        self.SPO2 = spo2
        self.BP_Systolic = bp_systolic
        self.BP_Diastolic = bp_diastolic
        self.Step_Counter = step_counter
        self.Skin_Temperature = skin_temperature
        self.Nursing_Home = nursing_home
        self.Gender = gender
        self.Photo = photo
        self.Phone_Number = phone_number

    def __str__(self):
        return f"PatientRecord(Name={self.Name}, Latitude={self.Latitude}, " \
               f"Longitude={self.Longitude}, Heart_Rate_BPM={self.Heart_Rate_BPM}, Pulse={self.Pulse}, " \
               f"SPO2={self.SPO2}, BP_Systolic={self.BP_Systolic}, BP_Diastolic={self.BP_Diastolic}, " \
               f"Step_Counter={self.Step_Counter}, Skin_Temperature={self.Skin_Temperature}, " \
               f"Nursing_Home={self.Nursing_Home}, Gender={self.Gender}, Photo={self.Photo}, " \
               f"Phone_Number={self.Phone_Number})"

def get_active_patients(steps_threshold=10000):
    try:
        # Query the container for all items
        query = f"SELECT * FROM c WHERE c.Step_Counter > {steps_threshold}"
        items = list(container.query_items(query=query, enable_cross_partition_query=True))

        # Process retrieved items into PatientRecord objects
        patient_records = []
        for item in items:
            patient_instance = PatientRecord(
                name=item['Name'],
                latitude=item['Latitude'],
                longitude=item['Longitude'],
                heart_rate_bpm=item['Heart_Rate_BPM'],
                pulse=item['Pulse'],
                spo2=item['SPO2'],
                bp_systolic=item['BP_Systolic'],
                bp_diastolic=item['BP_Diastolic'],
                step_counter=item['Step_Counter'],
                skin_temperature=item['Skin_Temperature'],
                nursing_home=item['Nursing_Home'],
                gender=item['Gender'],
                photo=item['Photo'],
                phone_number=item['Phone_Number']
            )
            patient_records.append(patient_instance)

        return patient_records

    except exceptions.CosmosHttpResponseError as e:
        print(f"Error fetching records: {e}")
'''




# model.py
from airtable import Airtable

AIRTABLE_API_KEY = 'pat7hpgmy2itPqWrX.da8a874efe149fc7f8569d6297d44973b6175731bb489123aa14de17b35686ae'
AIRTABLE_BASE_ID = 'app2WlcjTHxf5aCIZ'
AIRTABLE_TABLE_NAME = 'smartwatch_data'

# Create an Airtable object
airtable = Airtable(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, AIRTABLE_API_KEY)

class PatientRecord:
    def __init__(self,  name, latitude, longitude, heart_rate_bpm, pulse, spo2, bp_systolic, bp_diastolic,
                 step_counter, skin_temperature, nursing_home, gender, photo, phone_number):
        self.Name = name
        self.Latitude = latitude
        self.Longitude = longitude
        self.Heart_Rate_BPM = heart_rate_bpm
        self.Pulse = pulse
        self.SPO2 = spo2
        self.BP_Systolic = bp_systolic
        self.BP_Diastolic = bp_diastolic
        self.Step_Counter = step_counter
        self.Skin_Temperature = skin_temperature
        self.Nursing_Home = nursing_home
        self.Gender = gender
        self.Photo = photo
        self.Phone_Number = phone_number

    def __str__(self):
        return f"PatientRecord(Name={self.Name}, Latitude={self.Latitude}, " \
               f"Longitude={self.Longitude}, Heart_Rate_BPM={self.Heart_Rate_BPM}, Pulse={self.Pulse}, " \
               f"SPO2={self.SPO2}, BP_Systolic={self.BP_Systolic}, BP_Diastolic={self.BP_Diastolic}, " \
               f"Step_Counter={self.Step_Counter}, Skin_Temperature={self.Skin_Temperature}, " \
               f"Nursing_Home={self.Nursing_Home}, Gender={self.Gender}, Photo={self.Photo}, " \
               f"Phone_Number={self.Phone_Number})"

'''
def get_active_patients(steps_threshold=10000):
    
    try:
        records = airtable.get_all()
        #print(records)  # Add this line to print records
        #patient_records = [PatientRecord(**record['fields']) for record in records]

        patient_records = []

        for record in records:
            fields_data = record['fields']
            patient_instance = PatientRecord(
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
            
        active_patients = [patient for patient in patient_records if patient.Step_Counter > steps_threshold]
        return active_patients
    except Exception as e:
        print(f"Error fetching records: {e}")

    


'''

















