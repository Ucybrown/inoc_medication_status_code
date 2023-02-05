import unittest
import json
import pandas as pd

# Import the data from the JSON file
with open('patient_data.json') as json_file:
    patient_data = json.load(json_file)

# Convert the imported data to a DataFrame
patient_df = pd.DataFrame(patient_data)

class TestDashApp(unittest.TestCase):
    def test_update_scatter_plot(self):
        # Test that the scatter plot updates correctly based on the selected room number
        selected_room_number = '102'
        filtered_df = patient_df[patient_df['room_number'] == selected_room_number]
        scatter_plot = update_scatter_plot(selected_room_number)
        self.assertEqual(scatter_plot['data'][0]['x'], filtered_df['room_number'].tolist())

    def test_show_patient_info(self):
        # Test that the patient information is displayed correctly when clicking on a patient's name
        clickData = {'points': [{'customdata': [1, 'John', 'Doe', '123 Main St', 'Male', 30, 'Medication 1', 'Medication 2', 'Medication 3', '2022-01-01', '2022-01-10']}]}
        patient_info = show_patient_info(clickData)
        self.assertEqual(patient_info[1]['children'], 'Patient ID: 1')
        self.assertEqual(patient_info[2]['children'], 'Name: John Doe')
        self.assertEqual(patient_info[3]['children'], 'Address: 123 Main St')
        self.assertEqual(patient_info[4]['children'], 'Gender: Male')
        self.assertEqual(patient_info[5]['children'], 'Age: 30')
        self.assertEqual(patient_info[6]['children'], 'Medications Given: Medication 1, Medication 2, Medication 3')
        self.assertEqual(patient_info[7]['children'], 'Admission Date: 2022-01-01')
        self.assertEqual(patient_info[8]['children'], 'Expected Discharge Date: 2022-01-10')

if _name_ == '_main_':
    unittest.main()
