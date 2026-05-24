patient_data = [
    {
        'patient_id': 'id001',
        'name': 'Agus Putra',
        'age': 22,
        'gender': 'Male',
        'diagnosis': 'Cold'
    },

    {
        'patient_id': 'id002',
        'name': 'Bob Builderman',
        'age': 35,
        'gender': 'Male',
        'diagnosis': 'Asthma'
    },

    {
        'patient_id': 'id003',
        'name': 'Tiara Citra',
        'age': 20,
        'gender': 'Female',
        'diagnosis': 'Flu'
    }
]
 
running = True

def view_menu():
    print("\n======================================")
    print("List Menu:")
    print("1. Add a Patient")
    print("2. View Patients List")
    print("3. Change Patient's Data")
    print("4. Delete a Patient")
    print("5. Exit Program.")
    print("======================================")

def add_patient():
    patient_id_add  = input("Insert patient's ID: ")
    name_add        = input("Insert patient's name: ")
    age_add         = int(input("Insert patient's age: "))
    gender_add      = input("Specify patient's gender (Male/Female): ")
    diagnosis_add   = input("Insert patient's diagnosis: ")

    patient_data.append({
        'patient_id': patient_id_add,
        'name'      : name_add,
        'age'       : age_add,
        'gender'    : gender_add,
        'diagnosis' : diagnosis_add
    })
    print(f"Patient '{name_add}' successfully added!")
                
def view_patient():
    print(f"\n{'Index':<8} {'ID':<8} {'Name':<20} {'Age':<5} {'Gender':<10} {'Diagnosis':<15}")
    print("-" * 67) #Six Seven
    for i, patient in enumerate(patient_data):
        print(f"{i:<8} {patient['patient_id']:<8} {patient['name']:<20} {patient['age']:<5} {patient['gender']:<10} {patient['diagnosis']:<15}")

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
        view_patient()
    else:
        print("Invalid input, please try again.")

def delete_patient():
    print("\n--- Delete Patient ---")
    view_patient()

    index = int(input("\nEnter the index of the patient to delete: "))

    if 0 <= index < len(patient_data):
        removed = patient_data.pop(index)
        print(f"\nPatient '{removed['name']}' successfully deleted!")
        view_patient()
    else:
        print("Invalid input, please try again.")

while running:
    view_menu()
    menu = int(input("Please input a menu number:\n"))
    if menu == 1:
        add_patient()
    elif menu == 2:
        view_patient()
    elif menu == 3:
        update_patient()
    elif menu == 4:
        delete_patient()
    elif menu == 5:
        print("Thank you have a great day!")
        running = False
    else:
        print("Invalid input, please try again.")