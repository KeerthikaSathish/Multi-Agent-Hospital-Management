# Project Title:

## Multi-Agent Hospital Management System

### Objective:

To automate hospital scheduling and patient assignment using a multi-agent system, ensuring that doctors’ absences are handled, patients are optimally assigned, and daily reports are generated efficiently.

### Data Files
1.	doctor_absences.csv: absence_id, doctor_id, date, reason, duration_days, emergency_backup
2.	doctors.csv: doctor_id, name, specialization, level, max_patients_per_day, experience_years, shift_start, shift_end, department
3.	patients.csv: patient_id, name, preferred_doctor, specialization, urgency, date, appointment_time, status, age, gender, condition, wait_time_minutes

### Multi-Agent Architecture
•	The system is designed using separate agents for specific tasks:
1.	Absence Agent: Handles doctor availability, considers absences, and includes emergency backup doctors.
2.	Assignment Agent: Assigns patients to doctors based on specialization and preferred doctor.
3.	Backup Agent: Redirects patients if the assigned doctor is unavailable.
4.	Reporting Agent: Generates a daily schedule report in CSV format.







patient_id	name	preferred_doctor	specialization	urgency	date	appointment_time	status	age

