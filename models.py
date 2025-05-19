# models.py

class Contact:
    """
    Clase que representa un contacto con nombre, email y teléfono.
    """
    def __init__(self, name, email, phone):
        self.name = name.strip()
        self.email = email.strip()
        self.phone = phone.strip()

    def to_list(self):
        """
        Convierte el contacto a lista (útil para guardar en CSV).
        """
        return [self.name, self.email, self.phone]
