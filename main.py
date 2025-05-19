# main.py

from services import ContactBook
from models import Contact

def menu():
    """
    Muestra el menú principal de la aplicación de consola.
    """
    book = ContactBook()
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Editar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        choice = input("Selecciona una opción: ")

        if choice == '1':
            name = input("Nombre: ")
            email = input("Correo electrónico: ")
            phone = input("Teléfono: ")
            contact = Contact(name, email, phone)
            book.add_contact(contact)

        elif choice == '2':
            book.list_contacts()

        elif choice == '3':
            book.list_contacts_with_ids()
            try:
                contact_id = int(input("Ingresa el ID del contacto a editar: "))
                book.edit_contact_by_id(contact_id)
            except ValueError:
                print("ID inválido.")

        elif choice == '4':
            book.list_contacts_with_ids()
            try:
                contact_id = int(input("Ingresa el ID del contacto a eliminar: "))
                book.delete_contact_by_id(contact_id)
            except ValueError:
                print("ID inválido.")

        elif choice == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    menu()
