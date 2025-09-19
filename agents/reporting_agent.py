import csv
import pandas as pd

class Reporting:
    def __init__(self, doctors_df, patients_df, assignments):
        self.doctors = doctors_df
        self.patients = patients_df
        self.assignments = assignments

    def generate_csv_report(self, filepath='reports/daily_schedule.csv'):
        with open(filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['patient_id', 'patient_name', 'assigned_doctor', 'specialization'])
            for patient_id, doc_id in self.assignments:
                patient_name = self.patients.loc[self.patients['patient_id']==patient_id, 'name'].values[0]
                doctor_name = self.doctors.loc[self.doctors['doctor_id']==doc_id, 'name'].values[0]
                specialization = self.doctors.loc[self.doctors['doctor_id']==doc_id, 'specialization'].values[0]
                writer.writerow([patient_id, patient_name, doctor_name, specialization])
