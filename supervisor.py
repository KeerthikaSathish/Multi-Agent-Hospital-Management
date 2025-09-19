from agents.absence_agent import Absence
from agents.assignment_agent import Assignment
from agents.backup_agent import Backup
from agents.reporting_agent import Reporting

class Supervisor:
    def __init__(self, doctors_df, absences_df, patients_df):
        self.doctors = doctors_df
        self.absences = absences_df
        self.patients = patients_df

    def run_day(self):
        # Step 1: Absence handling
        available_doctors = Absence(self.doctors, self.absences).available_doctors()
        
        # Step 2: Patient assignment
        assignments = Assignment(available_doctors, self.patients).assign_patients()
        
        # Step 3: Backup redirection
        final_assignments = Backup(available_doctors, assignments).redirect_patients()
        
        # Step 4: Generate report
        Reporting(available_doctors, self.patients, final_assignments).generate_csv_report()
        print("Daily schedule report generated.")
