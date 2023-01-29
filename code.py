import random
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import json

# Import the data from the JSON file
with open('patient_data.json') as json_file:
    patient_data = json.load(json_file)

# Convert the imported data to a DataFrame
patient_df = pd.DataFrame(patient_data)

# Create a new column to store the traffic light status based on the medication given
patient_df['status'] = 'green'
patient_df.loc[patient_df['medication_given'] == 1, 'status'] = 'red'
patient_df.loc[patient_df['medication_given'] == 2, 'status'] = 'yellow'

# Initialize the app
app = dash.Dash()

# Create a dropdown menu to select the room number
room_number_options = [{'label': i, 'value': i} for i in patient_df['room_number'].unique()]
room_number_dropdown = dcc.Dropdown(id='room_number-select', options=room_number_options, value='All')

# Create a scatter plot
scatter_plot = dcc.Graph(id='scatter-plot')

# Create a div to display patient information when clicking on a patient's name
patient_info_div = html.Div(id='patient-info')

# Create the layout of the app
app.layout = html.Div([room_number_dropdown, scatter_plot, patient_info_div])


# Update the scatter plot based on the selected room number
@app.callback(Output('scatter-plot', 'figure'), [Input('room_number-select', 'value')])
def update_scatter_plot(selected_room_number):
    if selected_room_number == 'All':
        filtered_df = patient_df
    else:
        filtered_df = patient_df[patient_df['room_number'] == selected_room_number]
    scatter_plot = px.scatter(filtered_df, x='room_number', y='medication_given', color='status', title='Medication Status by Room Number', color_discrete_map={'green': 'green', 'yellow': 'yellow', 'red': 'red'}, custom_data=['patient_id', 'first_name', 'last_name', 'address', 'gender', 'age', 'medication_1', 'medication_2', 'medication_3', 'admission_date', 'expected_discharge_date'])
    return scatter_plot

# Add a callback to show the patient information when clicking on a patient's name
@app.callback(Output('patient-info', 'children'), [Input('scatter-plot', 'clickData')])
def show_patient_info(clickData):
    if clickData:
        patient_id = clickData['points'][0]['customdata'][0]
        first_name = clickData['points'][0]['customdata'][1]
        last_name = clickData['points'][0]['customdata'][2]
        address = clickData['points'][0]['customdata'][3]
        gender = clickData['points'][0]['customdata'][4]
        age = clickData['points'][0]['customdata'][5]
        medication_1 = clickData['points'][0]['customdata'][6]
        medication_2 = clickData['points'][0]['customdata'][7]
        medication_3 = clickData['points'][0]['customdata'][8]
        admission_date = clickData['points'][0]['customdata'][9]
        expected_discharge_date = clickData['points'][0]['customdata'][10]
        return html.Div([
            html.H3('Patient Information'),
            html.P(f'Patient ID: {patient_id}'),
            html.P(f'Name: {first_name} {last_name}'),
            html.P(f'Address: {address}'),
            html.P(f'Gender: {gender}'),
            html.P(f'Age: {age}'),
            html.P(f'Medications Given: {medication_1}, {medication_2}, {medication_3}'),
            html.P(f'Admission Date: {admission_date}'),
            html.P(f'Expected Discharge Date: {expected_discharge_date}'),
        ])
    else:
        return html.Div([])

# Run the app
if __name__ == '__main__':
    app.run_server()




