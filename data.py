import csv
import os

patient_data = []

def load_data():
    if os.path.exists('patients.csv'):
        with open('patients.csv', 'r') as f:
            reader = csv.DictReader(f)
            patients = list(reader)
            for p in patients:
                p['age'] = int(p['age'])
            return patients
    return []

def save_data():
    with open('patients.csv', 'w', newline='') as f:
        fieldnames = ['patient_id', 'name', 'age', 'gender', 'diagnosis']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(patient_data)