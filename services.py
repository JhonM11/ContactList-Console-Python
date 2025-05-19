# services.py

import csv
import os
from tabulate import tabulate
from models import Contact

class ContactBook:
    """
    Clase que maneja la lógica de la agenda de contactos.
    """
    def __init__(self, filename="ListContact.csv"):
        self.filename = filename
        self.contacts = []
        self._load_contacts()

    def _load_contacts(self):
        """
        Carga los contactos desde el archivo CSV o lo crea si no existe.
        """
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Email', 'Phone'])
        else:
            with open(self.filename, mode='r', newline='') as f:
                reader = csv.DictReader(f)
                self.contacts = [Contact(row['Name'], row['Email'], row['Phone']) for row in reader]

    def _save_contacts(self):
        """
        Guarda los contactos en el archivo CSV.
        """
        with open(self.filename, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Email', 'Phone'])
            for contact in self.contacts:
                writer.writerow(contact.to_list())

    def add_contact(self, contact):
        """
        Agrega un nuevo contacto si no existe uno con el mismo nombre.
        """
        if self.find_contact_by_name(contact.name):
            print("Ya existe un contacto con ese nombre.")
            return
        self.contacts.append(contact)
        self._save_contacts()
        print("Contacto agregado exitosamente.")

    def list_contacts(self):
        """
        Lista los contactos sin mostrar ID, usando formato tabla.
        """
        if not self.contacts:
            print("No hay contactos registrados.")
            return

        table = [[c.name, c.email, c.phone] for c in self.contacts]
        headers = ["Nombre", "Correo electrónico", "Teléfono"]
        print("\n" + tabulate(table, headers=headers, tablefmt="grid"))

    def list_contacts_with_ids(self):
        """
        Lista los contactos mostrando un ID (empezando en 1) en tabla.
        """
        if not self.contacts:
            print("No hay contactos registrados.")
            return

        table = []
        for idx, contact in enumerate(self.contacts, start=1):
            table.append([idx, contact.name, contact.email, contact.phone])

        headers = ["ID", "Nombre", "Correo electrónico", "Teléfono"]
        print("\n" + tabulate(table, headers=headers, tablefmt="fancy_grid"))

    def find_contact_by_name(self, name):
        """
        Busca un contacto por nombre (ignorando mayúsculas).
        """
        return next((c for c in self.contacts if c.name.lower() == name.lower()), None)

    def edit_contact_by_id(self, contact_id):
        """
        Edita un contacto por su ID (índice + 1).
        Permite cambiar nombre, correo y teléfono.
        """
        real_index = contact_id - 1
        if not (0 <= real_index < len(self.contacts)):
            print("ID no válido.")
            return

        contact = self.contacts[real_index]
        print(f"\nEditando a: {contact.name} | {contact.email} | {contact.phone}")

        new_name = input("Nuevo nombre (Enter para mantener): ").strip()
        new_email = input("Nuevo correo electrónico (Enter para mantener): ").strip()
        new_phone = input("Nuevo número de teléfono (Enter para mantener): ").strip()

        contact.name = new_name if new_name else contact.name
        contact.email = new_email if new_email else contact.email
        contact.phone = new_phone if new_phone else contact.phone

        self._save_contacts()
        print("Contacto actualizado exitosamente.")

    def delete_contact_by_id(self, contact_id):
        """
        Elimina un contacto por su ID (índice + 1).
        """
        real_index = contact_id - 1
        if not (0 <= real_index < len(self.contacts)):
            print("ID no válido.")
            return

        contact = self.contacts[real_index]
        confirm = input(f"¿Estás seguro de eliminar a {contact.name}? (s/n): ").lower()
        if confirm == 's':
            self.contacts.pop(real_index)
            self._save_contacts()
            print("Contacto eliminado exitosamente.")
        else:
            print("Eliminación cancelada.")
