from locust import HttpUser, TaskSet, task
import json

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.load_data()
        
    def load_data(self):
        with open('patient_data.json') as json_file:
            self.patient_data = json.load(json_file)
    
    @task(1)
    def view_patient_data(self):
        room_number = self.patient_data['room_number'][0]
        self.client.get("/update_scatter_plot?room_number=" + str(room_number))

class WebsiteUser(HttpUser):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

#  locust -f locustfile.py --host=http://localhost:8050
# http://localhost:8089/

# Result:

# With user test from 1- 250, The response time is within acceptable limits. This indicates that the application is able to handle the load and provide a good user experience.

# After testing with 250 users, The response time is significantly longer than expected. This could indicate that the application is not able to handle the load and the user experience may be impacted. In this case, you may need to optimize the code or increase the resources available to the application.