from data import patient_data

def patient_id():
    while True:
        patient_id_input = input("Insert patient's ID: (id001 for example)").strip()
        if not patient_id_input:
            print("Patient ID cannot be empty!")
        elif any(p['patient_id'] == patient_id_input for p in patient_data):
            print(f"ID '{patient_id_input}' is already taken!")
        else:
            return patient_id_input


def patient_name():
    while True:
        name = input("Insert patient's name: ").strip()
        if not name:
            print("Name cannot be empty!")
        else:
            return name
        
def patient_age():
    while True:
        try:
            age = int(input("Insert patient's age: "))
            if age <= 0:
                print("Age must be more than zero.")
            else:
                return age
        except ValueError:
            print("Invalid age, try again.")


def patient_gender():
    while True:
        gender = input("Specify patient's gender (Male/Female): ").strip().capitalize()
        if gender not in ["Male", "Female"]:
            print("Please try again, gender must be Male/Female.")
        else:
            return gender
        
def patient_diagnosis():
    while True:
        diagnosis = input("Insert patient's diagnosis: ").strip()
        if not diagnosis:
            print("Diagnosis cannot be empty!")
        else:
            return diagnosis
