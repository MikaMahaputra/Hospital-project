from data import load_data, patient_data
from menu import view_menu, add_patient, view_patient, search_patient, update_patient, delete_patient

patient_data[:] = load_data()

running = True


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