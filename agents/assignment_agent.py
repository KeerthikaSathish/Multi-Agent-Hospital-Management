import pandas as pd

doctors = pd.read_csv(r"data/doctors.csv")
class Assignment:
    def __init__(self, doctors_df, patients_df):
        self.doctors = doctors_df
        self.patients = patients_df

    def assign_patients(self):
        assignments = []
        for _, patient in self.patients.iterrows():
            candidates = self.doctors[self.doctors['specialization'] == patient['specialization']]
            if patient['preferred_doctor'] in candidates['doctor_id'].values:
                assigned_doc = patient['preferred_doctor']
            elif not candidates.empty:
                assigned_doc = candidates.iloc[0]['doctor_id']
            else:
                assigned_doc = None
            assignments.append((patient['patient_id'], assigned_doc))
        return assignments