
 
import csv
import os

running = True

def load_data():
    if os.path.exists('patients.csv'):
        with open('patients.csv', 'r') as f:
            reader = csv.DictReader(f)
            patients = list(reader)
            for p in patients:
                p['age'] = int(p['age'])
            return patients
    return []

patient_data = load_data()


def save_data():
    with open('patients.csv', 'w', newline='') as f:
        fieldnames = ['patient_id', 'name', 'age', 'gender', 'diagnosis']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(patient_data)

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

def view_menu():
    print("\n======================================")
    print("List Menu:")
    print("1. Add a Patient")
    print("2. View Patients List")
    print("3. Search a Patient")
    print("4. Change Patient's Data")
    print("5. Delete a Patient")
    print("6. Exit Program.")
    print("======================================")

def add_patient():
    patient_id_add  = patient_id()
    name_add        = patient_name()
    age_add         = patient_age()
    gender_add      = patient_gender()
    diagnosis_add   = patient_diagnosis()

    patient_data.append({
        'patient_id': patient_id_add,
        'name'      : name_add,
        'age'       : age_add,
        'gender'    : gender_add,
        'diagnosis' : diagnosis_add
    })
    save_data()
    print(f"Patient '{name_add}' successfully added!")
                
def view_patient():
    print(f"\n{'Index':<8} {'ID':<8} {'Name':<20} {'Age':<5} {'Gender':<10} {'Diagnosis':<15}")
    print("-" * 67) #Six Seven
    for i, patient in enumerate(patient_data):
        print(f"{i:<8} {patient['patient_id']:<8} {patient['name']:<20} {patient['age']:<5} {patient['gender']:<10} {patient['diagnosis']:<15}")


def search_patient():
    print("\n--- Search Patient ---")
    search_id = input("Enter patient ID to search: ").strip()

    result = None
    for p in patient_data:
        if p['patient_id'] == search_id:
            result = p
            break

    if result:
        print(f"\n{'ID':<8} {'Name':<20} {'Age':<5} {'Gender':<10} {'Diagnosis':<15}")
        print("-" * 67)
        print(f"{result['patient_id']:<8} {result['name']:<20} {result['age']:<5} {result['gender']:<10} {result['diagnosis']:<15}")
    else:
        print(f"No patient found with ID '{search_id}'.")


def update_patient():
    print("\n--- Update Patient Data ---")
    view_patient()

    index = int(input("\nEnter the index of the patient to update: "))

    if 0 <= index < len(patient_data):
        patient = patient_data[index]
        print(f"\nUpdating data for: {patient['name']}")
        print("(Press Enter to keep the current value)\n")

        new_id = input(f"New Patient ID [{patient['patient_id']}]: ").strip()
        new_name = input(f"New Name [{patient['name']}]: ").strip()
        new_age = input(f"New Age [{patient['age']}]: ").strip()
        new_gender = input(f"New Gender [{patient['gender']}]: ").strip()
        new_diagnosis = input(f"New Diagnosis [{patient['diagnosis']}]: ").strip()

        if new_id: patient['patient_id'] = new_id
        if new_name: patient['name'] = new_name
        if new_age: patient['age'] = int(new_age)
        if new_gender: patient['gender'] = new_gender
        if new_diagnosis: patient['diagnosis'] = new_diagnosis

        print(f"\nPatient data successfully updated!")
        save_data()
        view_patient()
    else:
        print("Invalid input, please try again.")

def delete_patient():
    print("\n--- Delete Patient ---")
    view_patient()

    index = int(input("\nEnter the index of the patient to delete: "))

    if 0 <= index < len(patient_data):
        removed = patient_data[index]
        delete_confirm = input(f"\nAre you sure you want to delete '{removed['name']}' (ID: {removed['patient_id']})? (y/n): ").strip().lower()
        if delete_confirm == "y":
            patient_data.pop(index)
            save_data()
            print(f"\nPatient '{removed['name']}' successfully deleted!")
            view_patient()
        else:
            print("\n Cancelling deletion")
    else:
        print("Invalid input, please try again.")

while running:
    view_menu()
    menu = int(input("Please input a menu number: "))
    if menu == 1:
        add_patient()
    elif menu == 2:
        view_patient()
    elif menu == 3:
        search_patient() 
    elif menu == 4:
        update_patient()
    elif menu == 5:
        delete_patient()
    elif menu == 6:
        print("Thank you have a great day!")
        running = False
    else:
        print("Invalid input, please try again.")