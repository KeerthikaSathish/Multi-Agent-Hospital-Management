import pandas as pd
from supervisor import Supervisor

doctors = pd.read_csv(r"data/doctors.csv")
absence = pd.read_csv(r"data/doctor_absences.csv")
patients = pd.read_csv(r"data/patients.csv")

supervisor = Supervisor(doctors, absence, patients)
supervisor.run_day()
