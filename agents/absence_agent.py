import pandas as pd

class Absence:
    def __init__ (self, doctors_df, absence_df):
        self.doctors = doctors_df
        self.absences = absence_df

    def available_doctors(self):
        available = self.doctors[~self.doctors['doctor_id'].isin(self.absences['doctor_id'])]

        # for emergency
        for _, row in self.absences.iterrows():
            backup = row['emergency_backup']
            if backup not in self.doctors['doctor_id'].values:
                backup_doctor = self.doctors[self.doctors['doctor_id'] == backup]
                available = pd.concat([available, backup_doctor])

        return available