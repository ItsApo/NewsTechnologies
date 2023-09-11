users = {}  # Diccionario para almacenar los usuarios registrados

def register():
    print("Registro:")
    email_or_phone = input("Ingresar Telefono o correo: ")
    name = input("Ingresa el nombre: ")
    password = input("Ingresa la contraseña: ")
    validation = int(input("Ingresa el resultado de ((2+5)*4): "))
    
    if validation == (2 + 5) * 4:
        # Agrega los datos del usuario al diccionario
        users[email_or_phone] = {"name": name, "password": password}
        print("Registro exitoso")
    else:
        print("No se ha podido realizar el registro.")

def login():
    print("Inicio de sesión:")
    email_or_phone = input("Ingresa el teléfono o el email: ")
    password = input("Ingresa tu contraseña: ")
    
    # Verifica si el usuario existe en el diccionario y si la contraseña es correcta
    if email_or_phone in users and users[email_or_phone]["password"] == password:
        print(f"Bienvenido {users[email_or_phone]['name']}")
    else:
        print("No se ha podido ingresar.")

while True:
    print("\nMenú:")
    print("1. Registrar")
    print("2. Iniciar sesión")
    print("3. Salir")
    
    choice = input("Selecciona una opción: ")
    
    if choice == "1":
        register()  # Llama a la función para registrar un usuario
    elif choice == "2":
        login()     # Llama a la función para iniciar sesión
    elif choice == "3":
        print("Hasta luego!")
        break
    else:
        print("Opción no válida. Ingresa 1, 2 o 3.")
