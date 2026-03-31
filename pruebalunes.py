import csv
import os

#archivo
ARCHIVOCSV = 'CUSTOMER_SCHOOL.csv'
CAMPOS = ['id', 'name', 'age', 'course', 'status']

def cargar_datos():
    """It loads the data from the CSV file when the program starts."""
    students = []
    if os.path.exists(ARCHIVOCSV):
        try:
            with open(ARCHIVOCSV, mode='r', newline='', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    # Convert the age to an integer to maintain the correct data type.
                    fila['age'] = int(fila['age'])
                    students.append(fila)
        except Exception as e:
            print(f"Error loading data: {e}")
    return students

def guardar_datos(students):
   #"""Saves the list of dictionaries to the CSV file to persist data between runs."""
    try:
        with open(ARCHIVOCSV, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(students)
    except Exception as e:
        print(f"Error saving data: {e}")

def crear_students(students):

    print("\n--- register new student ---")
    try:
        id_estudiante = input (" Enter the student's (unique) ID : ").strip()       #Remove specific characters—typically whitespace, tabs, or line breaks—from both the beginning and the end of a text string.


        for c in students:
            if c['id'] == id_estudiante:
                print("Error: There is already a student with that ID.")
                return
            
        name = input("Enter the student's name: ").strip()
        age = int(input("Enter the student's age: "))
        course = input("Enter the course or program ").strip().lower()     # Converts a string to lowercase.
        status = input("Enter the status (active/inactive) ").strip().lower()

        nuevo_estudiante={
            'id': id_estudiante,
            'name': name,
            'age': age,
            'course': course,
            'status': status
        }

        students.append(nuevo_estudiante)   
        guardar_datos(students)
        print(" student successfully registered")

    except ValueError:
        print("Error: The age must be a valid integer.")

def listar_students(students):
    #"""Lista todos los estudiantes registrados en consola."""
    print("\n--- Student List---")
    if not students:
        print("There are no students registered in the system.")
        return

    for c in students:
        print(f"Id: {c['id']} | Name: {c['name']} | Age: {c['age']} | Course: {c['course'].capitalize()} | Status: {c['status'].capitalize()}")            #Convert the first letter of a text string to uppercase and automatically transform all other letters to lowercase.

def buscar_students(students):
    """Search for a student by matching ID or name."""
    print("\n--- Search student---")
    termino = input("Enter the ID or name of the student you are looking for: ").strip().lower()

    encontrados = []
    for c in students:
        if termino == c['id'].lower() or termino in c['name'].lower():
            encontrados.append(c)

    if encontrados:
        for c in encontrados:
            print(f"Id: {c['id']} | Name: {c['name']} | Age: {c['age']} | Course: {c['course']} | status: {c['status']}")
    else:
        print("No student was found with that information.")

def actualizar_students(students):
   #Updates the information of an existing student by prompting for the new data.
    print("\n--- Update student---")
    id_buscar = input("Enter the ID of the student you wish to update: ").strip()

    for c in students:
        if c['id'] == id_buscar:
            print(f"student found: {c['name']}. Leave blank if you do not wish to change the field.")
            try:
                new_name = input(f"New Name ({c['name']}): ").strip()
                new_age_str = input(f"New Age ({c['age']}): ").strip()
                new_course = input(f"New Course ({c['course']}): ").strip()
                new_status = input(f"New Status ({c['status']}): ").strip()

                if new_name: c['name'] = new_name
                if new_age_str: c['age'] = int(new_age_str)
                if new_course: c['course'] = new_course.lower()
                if new_status: c['status'] = new_status.lower()

                guardar_datos(students)
                print("Student information successfully updated!")
                return
            except ValueError:
                print("Error: Invalid value entered during the update.")
                return

    print("No student was found with that ID.")

def eliminar_students(students):
    """Remove a student from the system using their ID."""
    print("\n--- Delete student---")
    id_buscar = input("Enter the ID of the student to delete:").strip()

    for i in range(len(students)):
        if students[i]['id'] == id_buscar:
            confirmacion = input(f"Are you sure you want to delete {students[i]['name']}? (s/n): ").strip().lower()
            if confirmacion == 's':
                eliminado = students.pop(i)
                guardar_datos(students)
                print(f"student '{eliminado['name']}' removed from the system.")
            else:
                print("Canceled operation.")
            return

    print("No student was found with that ID.")

def menu():
   #"""Main function that displays the menu in the console and manages interaction."""
    students = cargar_datos()

    while True:
        print("\n" + "="*30)
        print(" STUDENT MANAGEMENT " )
        print("="*30)
        print("1. Create Student")
        print("2. List Students")
        print("3. Search Student ")
        print("4.Update Student List ")
        print("5. Delete Student ")
        print("6. EXIT")

        opcion = input("Select an option:").strip()

        if opcion == '1':
            crear_students(students)
        elif opcion == '2':
            listar_students(students)
        elif opcion == '3':
            buscar_students(students)
        elif opcion == '4':
            actualizar_students(students)
        elif opcion == '5':
            eliminar_students(students)
        elif opcion == '6':
            print("Saving data and logging out. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Execution Point
if __name__ == "__main__":
    menu()                    
