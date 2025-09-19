class Backup:
    def __init__(self, doctors_df, assignments):
        self.doctors = doctors_df
        self.assignments = assignments

    def redirect_patients(self):
        # Redirect patients if assigned doctor is None
        redirected = []
        for patient_id, doc_id in self.assignments:
            if doc_id is None:
                # Assign first available doctor of same specialization
                doc_id = self.doctors.iloc[0]['doctor_id']
            redirected.append((patient_id, doc_id))

        return redirected
