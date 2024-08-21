# Sección del administrador 
# • El administrador debe estar creado directamente en el código. Se debe crear un usuario 
# (nombre) y una contraseña para el administrador. 
# • Se conoce como CRUD al mantenimiento de información dentro de los sistemas, por 
# sus siglas en ingles se denominan Cread, Read, Update y Delete. 
# Perfiles 
# • El sistema debe contar con los siguientes perfiles de acceso para los usuarios, los 
# cuales responden a roles y permisos que deberán ser definidos. 
# o Ciudadano: corresponde a cualquier ciudadano del país que cuente con licencia 
# de conducir.  
# o Oficial de Tránsito: corresponde a los oficiales de tránsito debidamente 
# autorizados para ejercer su oficio en el país. 
# o Oficina del Juzgado: corresponde a los colaboradores de las oficinas de 
# juzgado de tránsito encargados de atender los temas de colisiones. 
# o Administrador: corresponde a los encargados principales de la aplicación, que 
# velarán por el buen funcionamiento y control de la herramienta. 
# 3 
# Estados 
# • Los estados en los que puede estar un evento son: 
# o Abierto: estará por defecto cuando un Ciudadano cree un nuevo evento.  
# o Por aprobar: cuando esté logueado como Oficial de Tránsito puede pasar el 
# estado de Abierto a Por aprobar.  
# o Completo: cuando esté logueado como Oficina del Juzgado puede pasar el 
# estado de Por aprobar a Completo.  
# CRUD de provincias y cantones 
# • El sistema debe permitir gestionar provincias y cantones. 
# • Se deben crear por defecto 4 provincias y cada una de ellas, tiene 2 cantones. 
# • No se puede eliminar provincias ni cantones que ya están asignados a un evento. 
# • Queda a criterio de cada equipo de trabajo el cómo almacenan esta información. 
# Reportes 
# 1. Mostrar todos los cantones ordenados alfabéticamente. 
# 2. Mostrar todas las personas registradas, ordenadas por la edad ascendentemente. La 
# información que se debe mostrar es la edad, el nombre y el perfil con que se registró. 
# 3. Mostrar la cantidad de hombres y de mujeres registrados en el sistema. 
# 4. Mostrar la cantidad de hombres de acuerdo con una provincia en específico. 
# 5. Mostrar la cantidad de mujeres de acuerdo con un cantón en específico. 
# 6. Mostrar todos los vehículos ordenados por tipo, en donde deben salir en este orden: 
# moto, automóvil, bus y camión. La información que se debe mostrar es la placa y la 
# marca. 
# 7. Mostrar todos los eventos donde la multa sea mayor de los 45 mil colones, siempre y 
# cuando el estado del evento sea por aprobar. La información que se muestra es el 
# código del evento, el nombre del oficial de tránsito y el valor de la multa.  
# 8. Mostrar todos los eventos con estado Completo, los datos que se imprimen son: Nombre 
# del ciudadano, Número de parte, Lugar del choque (provincia y cantón), Estado, Fecha 
# y hora. Deben estar ordenados ascendentemente por la fecha. La información se debe 
# obtener del archivo. 
# 9. Mostrar los eventos con estado Abierto de acuerdo con una hora específica. Por 
# ejemplo, si se coloca la hora 9:00:00, deben salir todos los eventos Abiertos que están 
# antes de esa hora, los posteriores a las 9:00:00 no deben salir.  
# 10. Mostrar la provincia con mayores incidentes y la de menor incidentes. La información 
# que se debe mostrar es el nombre de la provincia y la cantidad de incidentes. 
# 4 
# Sección de los usuarios 
# Registro al sistema 
# • Esta sección es para que los usuarios se puedan registrar al sistema, los perfiles que 
# se pueden registrar aquí son: Ciudadano, Oficial de Tránsito y Oficina del Juzgado. 
# • En esta sección no se permite el uso de archivos para gestionar la información. 
# • Solo se pueden registrar personas que sean mayores de edad. 
# • No puede haber personas repetidas, lo cual se debe validar por medio de la cédula del 
# ciudadano. 
# • Un mismo ciudadano (cédula) no puede tener más de un tipo de perfil.  
# • La información que se debe gestionar de los usuarios que se van a registrar es la 
# siguiente: 
# Campo 
# Descripción 
# Cédula 
# Nombre 
# Fecha de nacimiento 
# Cédula de la persona. 
# Nombre de la persona. 
# Se coloca el día, mes y año de nacimiento. 
# Edad 
# Debe ser autogenerada, a partir de la fecha de nacimiento. 
# Sexo 
# Lugar de residencia 
# Tipo de usuario 
# Género de la persona (Masculino o Femenino). 
# De acuerdo con la provincia y cantón que indique. 
# Si es ciudadano, oficial de tránsito u oficina del juzgado. 
# Contraseña 
# Contraseña que permite el acceso al sistema. 
# Inicio de sesión 
# • Ningún usuario de los perfiles que existen, puede acceder a secciones que no le 
# corresponden. 
# • Si se loguea como Administrador únicamente puede acceder a la sección de 
# administración del sistema. Puede cerrar sesión (salir). 
# • Si se loguea como Ciudadano solo puede tener acceso a la sección de CRUD evento 
# ciudadano o al CRUD vehículos. Puede cerrar sesión (salir). 
# • Si se loguea como Oficial de Tránsito solo puede tener acceso a la sección de CRUD 
# evento oficial de tránsito. Puede cerrar sesión (salir). 
# • Si se loguea como Oficina del Juzgado solo puede tener acceso a la sección de CRUD 
# evento oficina del juzgado. Puede cerrar sesión (salir). 
# • Para iniciar sesión (login) se suministrará Cédula y Contraseña, el sistema deberá 
# detectar de manera automática el tipo de usuario (administrador, ciudadano, oficial de 
# tránsito, oficina de juzgado).  
# 5 
# CRUD vehículos 
# • Para gestionar la información de este CRUD no se puede usar archivos. 
# • Solo los usuarios que sean de tipo Ciudadano tienen acceso a este CRUD. 
# • Un ciudadano puede tener N vehículos asociados. 
# • Cuando se registran vehículos, se debe validar que no exista placas repetidas. 
# • La información que se debe gestionar de los vehículos es la siguiente: 
# Campo 
# Descripción 
# Cédula 
# Placa 
# Año 
# Cédula del ciudadano al que pertenece el vehículo. 
# Placa del vehículo, debe ser alfanumérica (JMH-200)  
# Año del vehículo. 
# Marca 
# Marca del vehículo (Nissan, Hyundai, Toyota, entre otros) 
# Color 
# Tipo 
# Color del vehículo que se registra. 
# Tipo de vehículo (Moto, automóvil, bus o camión) 
# CRUD evento ciudadano 
# • Se entiende evento como un incidente o infracción que se está registrando por alguna 
# colisión de uno de los vehículos del ciudadano. 
# • Para gestionar la información de este CRUD no se puede usar archivos. 
# • Solo los usuarios que sean de tipo Ciudadano tienen acceso a este CRUD. 
# • Lo primero que debe aparecer para crear un evento nuevo, es la lista de vehículos que 
# pertenece al ciudadano que está logueado en el sistema. La información que se muestra 
# de los vehículos es el número de placa del mismo. 
# • Cada vehículo puede tener únicamente un evento asociado, no importa el estado en 
# que esté el evento, solo puede tener uno. 
# • Debe especificar el lugar donde se produjo el incidente, para esto se muestra las 
# provincias y luego sus respectivos cantones. 
# • El ciudadano puede consultar todos los eventos que ha creado, sin importar en el estado 
# en que se encuentre el mismo. 
# • Cuando el usuario requiera modificar el evento, puede hacer cambios en todos los 
# campos excepto en el código y el estado. 
# • Se puede eliminar un evento si y solo si, el estado del mismo es Abierto. 
# • La información que se almacena de los eventos que corresponden al ciudadano es: 
# Campo 
# Descripción 
# Código 
# Nombre de usuario 
# Lugar del incidente 
# Código del evento. Se genera con random de 1 a 5. 
# Nombre del ciudadano que registra el evento. 
# Provincia y cantón donde se produjo el incidente. 
# Placa 
# Corresponde a la placa del vehículo. 
# Estado del incidente 
# En este momento es Abierto, se registra desde el código. 
# 6 
# Fecha y hora del sistema. 
# Fecha y hora 
# Multa 
# Monto a cobrar por el incidente (ver tabla de incidentes) 
# • Ejemplo: Código: 21313, Nombre de usuario: Roberto, Lugar del incidente: Alajuela / 
# Ciudad Quesada, Placa: 12345, Estado: Abierto, Fecha: 05/08/2018 – 08:00:00, Multa: 
# 70000. 
# Tabla de incidentes: 
# • Depende del tipo de vehículo que produjo el incidente, se cobra una multa la cual 
# corresponde al valor de la multa más el impuesto. 
# • En caso que el vehículo sea de un año menor al 2000, se le adiciona al total de la multa 
# un 10%. 
# • Para generar esta información de la multa, se debe realizar en una función propia y 
# exclusiva que retorne el valor total de la multa. 
# • La información de la siguiente tabla debe estar almacenada en un archivo. 
# Tipo Vehículo 
# Valor de la Multa 
# Moto 
# Impuesto 
# 10000 
# Automóvil 
# 25000 
# 15% 
# Bus 
# 30% 
# 45000 
# Camión 
# 65000 
# 45% 
# 70% 
# Evento oficial de tránsito 
# • El Oficial de Tránsito puede cargar la lista de eventos creados por los Ciudadanos, pero 
# no los puede editar. Solo puede ver los eventos con estado Abierto y que haya 
# transcurrido 30 segundos después de registrado el evento. Por ejemplo, si el evento el 
# Ciudadano lo registró a las 8:00:00, y si el Oficial de Tránsito accede a la lista a las 
# 8:00:10, el evento no debe salir, pero si accede a la lista a las 8:00:30 o posterior, el 
# evento si debe salir. 
# • Lo único que el Oficial de Tránsito puede hacer es incluir el número de parte, el cual es 
# numérico. 
# • Acá el estado debe cambiar de Abierto a Por aprobar. Este cambio de estado debe ser 
# desde el código fuente, o sea, el usuario no debe hacerlo desde pantalla. 
# • Se debe modificar la información del evento que estaba creado, en donde las únicas 
# modificaciones son: agregar el nombre del oficial de tránsito, el número de parte, 
# además de cambiar el estado de Abierto a Por aprobar, la fecha y hora actual (se toma 
# del sistema).  
# • Ejemplo: Código: 21313, Nombre de usuario: Roberto, Lugar del incidente: Alajuela / 
# Ciudad Quesada, Placa: 12345, Nombre del Oficial: Carlos, Número de parte: 234, 
# Estado: Por aprobar, Fecha: 05/08/2018 – 08:04:00, Multa: 70000. 
# 7 
# Evento oficina del juzgado 
# • La Oficina del Juzgado puede cargar la lista de eventos creados por Ciudadanos y con 
# los datos que el Oficial de Tránsito incluyó, o sea, todos los eventos en estado Por 
# aprobar, pero no los puede editar. 
# • Lo único que la Oficina del Juzgado puede hacer es incluir el número de registro. 
# • Acá el estado debe cambiar de Por aprobar a Completo. Este cambio de estado debe 
# ser desde el código fuente, o sea, el usuario no debe hacerlo desde pantalla. 
# • Se debe modificar la información del evento que estaba creado, en donde las únicas 
# modificaciones son: agregar el nombre de la persona de oficina del juzgado, agregar el 
# número de registro, además de cambiar el estado de Por aprobar a Completo, la fecha 
# y hora actual (se toma del sistema).  
# • Ejemplo: Código: 21313, Nombre de usuario: Roberto, Lugar del incidente: Alajuela / 
# Ciudad Quesada, Placa: 12345, Nombre del Oficial: Carlos, Número de parte: 234, 
# Nombre Oficina del Juzgado: Laura, Número de registro: 872, Estado: Completo, Fecha: 
# 05/08/2018 – 08:08:00, Multa: 70000. 
# • En este punto, cuando el evento cambia de estado a completo, si se debe guardar toda 
# la información anterior en un archivo



from os import system  # Import the system function
from datetime import datetime  # Import the datetime module
import random  # Import the random module


def calcularEdad(fechaNacimiento):  # Function to calculate the user's age
        fechaNacimiento = datetime.strptime(fechaNacimiento, "%d/%m/%Y") 
        fechaActual = datetime.today()  # Get the current date
        edad = fechaActual.year - fechaNacimiento.year - ((fechaActual.month, fechaActual.day) < (fechaNacimiento.month, fechaNacimiento.day))
        return edad


listUsuarios = [
    {"cedula": "admin", 
     "nombre": "David", 
     "perfil": "Administrador", 
     "edad": "19", 
     "contraseña": "admin"},

    {"cedula": "1", 
    "nombre": "Roberto",
    "fechaNacimiento": "05/08/2018",
    "edad": "20",
    "sexo": "Masculino",
    "provincia": "Cartago",
    "canton": "Turrialba",
    "perfil": "Ciudadano", 
    "contraseña": "12345"},

    {"cedula": "2", 
    "nombre": "Luis",
    "fechaNacimiento": "05/08/2018",
    "edad": "20",
    "sexo": "Masculino",
    "provincia": "Alajuela",
    "canton": "San Carlos",
    "perfil": "Ciudadano", 
    "contraseña": "12345"},

    {"cedula": "3", 
    "nombre": "Carlos",
    "fechaNacimiento": "08/01/2005",
    "edad": "20",
    "sexo": "Masculino",
    "provincia": "Alajuela",
    "canton": "San Carlos",
    "perfil": "Oficial", 
    "contraseña": "12345"},

    {"cedula": "4", 
    "nombre": "Pedro",
    "fechaNacimiento": "08/01/2003",
    "edad": "20",
    "sexo": "Femenino",
    "provincia": "Alajuela",
    "canton": "San Carlos",
    "perfil": "Juzgado",
    "contraseña": "12345"}
]



provinciasCantones = {"Alajuela": ["San Carlos", "Upala"],
                      "Cartago": ["La Union", "Turrialba"],
                      "Guanacaste": ["Cañas", "Abangares"],
                      "Heredia": ["Belen", "Las Flores"]}


listVehiculos = []  # List to store vehicle information

listEventos = []  # List to store event information





def mostrarCantonesAlfabeticamente():  # Function to display the list of cantones in alphabetical order
    system("cls")
    print("Cantones ordenados alfabéticamente:")

    listCantones = [canton for cantones in provinciasCantones.values() for canton in cantones]  # Create a list of all cantons in alphabetical order

    listCantones.sort()  # Sort the list of cantons alphabetically

    for canton in listCantones:  # Loop through the list of cantons to display the information
        print(f"- {canton}")
    system("pause")


def mostrarPersonas():  # Function to display all registered users, sorted by age in ascending order
    system("cls")
    print("Personas:")

    
    usuarios_a_mostrar = listUsuarios[1:]  # Omit the first user from the list

    
    
    edades = {int(persona['edad']) for persona in usuarios_a_mostrar}  # Convierte edad a entero y usa un conjunto para eliminar duplicados


    edades_ordenadas = sorted(edades)




    contador = 1  # Initialize the counter
    personasMostradas = []  # List to store the users already displayed

    for edad in edades_ordenadas:  # Loop through the list of users by age
        for persona in usuarios_a_mostrar:  # Loop through the list of users to check if the user's age matches the current age
            if edad == persona['edad'] and persona['nombre'] not in [p['nombre'] for p in personasMostradas]:
                print(f"{contador}. {persona['nombre']}")
                print(f"Edad: {persona['edad']}")
                print(f"Perfil: {persona['perfil']}")
                print()
                personasMostradas.append(persona)  # Add the user to the list of users already displayed
                contador += 1  # Increment the counter

    system("pause")


def mostrarCantidadPorGenero():  # Function to display the number of users by gender
    system("cls")
    print("Cantidad de Usuarios por Género:")

    
    cantidadHombres = 0  # Initialize the counters
    cantidadMujeres = 0

    
    for persona in listUsuarios:  # Loop through the list of users to count the number of each gender
        if 'sexo' in persona:
            if persona['sexo'].capitalize() == 'Masculino':  # Check if the user's gender is male
                cantidadHombres += 1
            elif persona['sexo'].capitalize() == 'Femenino':
                cantidadMujeres += 1

    
    print(f"Hombres: {cantidadHombres}")
    print(f"Mujeres: {cantidadMujeres}")

    system("pause")


def mostrarCantidadHombresPorProvincia():  # Function to display the number of males by province
    system("cls")
    print("Cantidad de Hombres por Provincia:")

    
    hombresProvincia = {provincia: 0 for provincia in provinciasCantones}  # Initialize a dictionary to count males by province

    
    for persona in listUsuarios:   # Loop through the list of users to count the number of males by province
        if 'provincia' in persona and persona['sexo'].capitalize() == 'Masculino':
            provincia = persona['provincia'].title()  # Ensure that the province is in the same format
            if provincia in hombresProvincia:  # Check if the province is in the dictionary
                hombresProvincia[provincia] += 1  # Increment the count

    
    for provincia, cantidad in hombresProvincia.items():  # Loop through the dictionary to display the results
        print(f"Hombres en {provincia}: {cantidad}")

    system("pause")



def mostrarCantidadMujeresPorCanton():  # Function to display the number of females by canton
    system("cls")
    print("Cantidad de Mujeres por Cantón:")

    
    mujeresCanton = {}  # Initialize a dictionary to count females by canton
    
    
    for provincia, cantones in provinciasCantones.items():  # Loop through the province-canton dictionary to initialize the dictionary with cantons
        for canton in cantones:  # Loop through the list of cantons to initialize the dictionary with females
            mujeresCanton[canton] = 0  # Initialize the count for each canton

    
    for persona in listUsuarios:  # Loop through the list of users to count the number of females by canton
        if 'canton' in persona and 'sexo' in persona and persona['sexo'].capitalize() == 'Femenino':
            canton = persona['canton'].title()  # Ensure that the canton is in the same format
            if canton in mujeresCanton:
                mujeresCanton[canton] += 1  # Increment the count

    
    for canton, cantidad in mujeresCanton.items():  # Loop through the dictionary to display the results
        print(f"Mujeres en {canton}: {cantidad}") 

    system("pause")



def mostrarVehiculosOrdenados():  # Function to display all vehicles ordered by type, where they should be displayed in this order: motor, automobile, bus, and car
    system("cls")
    print("Vehiculos ordenados por tipo:")
    print()
    if listVehiculos:  # Check if there are any vehicles in the list
        
        ordenTipo = ["Moto", "Automovil", "Bus", "Camion"]
        
        
        listVehiculosOrdenados = sorted(listVehiculos, key=lambda v: ordenTipo.index(v["tipo"]))  # Sort the list of vehicles based on the specified order
        
        
        for vehiculo in listVehiculosOrdenados:  # Loop through the sorted list of vehicles to display the information
            print(f"Tipo: {vehiculo['tipo']}")
            print(f"Placa: {vehiculo['placa']}")
            print(f"Marca: {vehiculo['marca']}")
            print()

    system("pause")



def mostrarEventosConMultaMayorA45k():  # Function to display events with a multa greater than 45,000 colones and in the "Por Aprobar" state
    try:
        system("cls")
        
        
        if listEventos:  # Check if there are any events in the list
            
            eventosFiltrados = [e for e in listEventos if e["multa"] > 45000 and e["estado"] == "Por Aprobar"]  # Filter events with a multa greater than 45,000 colones and in the "Por Aprobar" state
            
            
            if eventosFiltrados:  # Check if there are any events that meet the conditions
                
                for evento in eventosFiltrados:  # Loop through the filtered events to display the information
                    print(f"Código del Evento: {evento['codigo']}")
                    print(f"Nombre del Oficial de Tránsito: {evento['nombreOficial']}")
                    print(f"Valor de la Multa: {evento['multa']}")
                    print()
            else:  # If there are no events that meet the conditions
                print("No hay eventos con multa mayor a 45,000 colones y estado Por Aprobar!")

        else:  # If there are no events in the list
            print("No hay eventos para mostrar")
            
        system("pause")
    
    except ValueError:  # If an error occurs, try again
        system("cls")
        print(f"Se ha producido un error, intente nuevamente")
        system("pause")






def mostrarlistadoEventosCompletos():  # Function to display completed events
    system("cls")
    for e in listEventos:  # Loop through the list of events to display the information
        if e["estado"] == "Completo":  # Check if the event is in the "Completo" state
            print(f"Nombre del ciudadano: {e['nombre']}")
            print(f"Numero de parte: {e['numeroParte']}")
            print(f"Lugar del choque provincia: {e['provincia']}")
            print(f"Lugar del choque cantón: {e['canton']}")
            print(f"Estado: {e['estado']}")
            print(f"Fecha: {e['fecha']}")
            print(f"Hora: {e['hora']}")
            print(f"Multa: {e['multa']}")
            print()

    system("pause") 




def crudProvinciasCantones(i):  # Function to display the CRUD menu for provinces and cantons
    print("1. Mostrar cantones ordenados alfabéticamente.")
    print("2. Mostrar todas las personas registradas, ordenadas por la edad ascendentemente. ")
    print("3. Mostrar la cantidad de hombres y de mujeres registrados.")
    print("4. Mostrar la cantidad de hombres de acuerdo con una provincia en específico.")
    print("5. Mostrar la cantidad de mujeres de acuerdo con un cantón en específico.")
    print("6. Mostrar todos los vehículos ordenados por tipo.")
    print("7. Mostrar todos los eventos con multa mayor a 45mil y estado Por Aprobar.")            
    print("8. Mostrar todos los eventos con estado Completo.")
    print("9. Salir")

    opcion = int(input("Ingrese la opción deseada: "))  # Prompt the user to select an option from the menu
    if opcion == 1:
        mostrarCantonesAlfabeticamente()
    elif opcion == 2:
        mostrarPersonas()
    elif opcion == 3:
        mostrarCantidadPorGenero()
    elif opcion == 4:
        mostrarCantidadHombresPorProvincia()
    elif opcion == 5:
        mostrarCantidadMujeresPorCanton()
    elif opcion == 6:
        mostrarVehiculosOrdenados()
    elif opcion == 7:
        mostrarEventosConMultaMayorA45k()
    elif opcion == 8:
       mostrarlistadoEventosCompletos()
    elif opcion == 9:
         menuAdmin(i)



def verUsuariosRegistrados():  # Function to display the list of registered users
    system("cls")
    contador = 1  # Initialize the counter
    print("--- Usuarios Registrados ---")
    print()
    if listUsuarios[1:]:  # Check if there are any users in the list except the first one
        for usuario in listUsuarios[1:]:  # Loop through the list of users except the first one to display the information
                print(f"{contador}. {usuario['nombre']}")
                print(f"Cedula: {usuario['cedula']}")
                print(f"Fecha Nacimiento: {usuario['fechaNacimiento']}")
                print(f"Edad: {usuario['edad']}")
                print(f"Sexo: {usuario['sexo']}")
                print(f"Provincia: {usuario['provincia']}")
                print(f"Cantón: {usuario['canton']}")
                print(f"Perfil: {usuario['perfil']}")
                print()
                contador += 1
    else:  # If there are no users in the list except the first one
        system("cls")
        print("No hay usuarios registrados!")

    system("pause")


def modificarUsuarios(i):  # Function to modify registered users
    system("cls")
    
    cedulaAModificar = input ("Ingrese la cedula del usuario a modificar: ").lower()  # Prompt the user to enter the user's cedula to modify

    for x in listUsuarios:  # Loop through the list of users to check if the user's cedula matches the input cedula
        if x["cedula"] == cedulaAModificar:  # Check if the input cedula matches the user's cedula
            nombre = input("Ingrese su nuevo nombre: ").capitalize()
            cedula = input("Ingrese su nuevo cédula: ").lower()
                    
            while True:  # Loop to validate the user's date of birth
                try:  # Try to validate the user's date of birth
                    fechaNacimiento = input("Ingrese su nueva fecha de nacimiento (dia/mes/año): ")
                    edad = calcularEdad(fechaNacimiento)
                    break
                except ValueError:
                    print()
                    print("Ingrese la fecha de nacimiento en el formato correcto")
                    system("pause")
                    print()
            
            if edad >= 18:
                pass
            else:
                system("cls")
                print("Debe ser mayor de edad para registrarse!")
                system("pause")
                menuInicioSesion()
            
            while True:  # Loop to validate the user's sex
                try:
                    sexo = input("Ingrese su nuevo sexo (Masculino o Femenino): ").capitalize()
                    if sexo == "Masculino" or sexo == "Femenino":
                        break
                    
                except ValueError:
                    system("cls")
                    print("Ingrese el sexo en el formato correcto!")
                    system("pause")    
            
            
            while True:  # Loop to validate the user's residence province
                try:
                    mostrarProvincias()
                    provincia = input("Ingrese su nueva provincia de residencia: ").title()
                    if provincia in provinciasCantones.keys():
                        print()
                        break
                    else:
                        system("cls")
                        print("La provincia ingresada no existe!")
                        system("pause")

                except ValueError:
                    system("cls")
                    print("Ingrese una de las provincias mostradas en pantalla!")
                    system("pause")
                    mostrarProvincias()

            
            while True:  # Loop to validate the user's residence canton
                try:  # Try to validate the user's residence canton
                    cantonesProvincia = provinciasCantones[provincia]
                    
                    print(f"Los cantones disponibles en {provincia} son:")
                    for canton in cantonesProvincia:
                        print(f"- {canton}")
                    
                    canton = input("Ingrese su nuevo cantón de residencia: ").title()
                    if canton in cantonesProvincia:
                        break    
                    else:
                        system("cls")
                        print("El cantón ingresado no existe!")
                        system("pause")

                except ValueError:
                    system("cls")
                    print("Ingrese uno de los cantones mostrados en pantalla!")
                    system("pause")

            while True:  # Loop to validate the user's profile
                try:
                    perfil = input("Ingrese su nuevo perfil (Ciudadano, Oficial o Juzgado): ").capitalize()
                    if perfil == "Ciudadano" or perfil == "Oficial" or perfil == "Juzgado":
                        break
                    
                except ValueError:
                    system("cls")
                    print("Ingrese el tipo de perfil (Ciudadano, Oficial o Juzgado) en el formato correcto!")
                    system("pause")
            
            contraseña = input("Ingrese la nueva contraseña: ").lower()  # Prompt the user to enter their new password
            
            x["cedula"] = cedula
            x["nombre"] = nombre
            x["fechaNacimiento"] = fechaNacimiento
            x["edad"] = edad
            x["sexo"] = sexo
            x["provincia"] = provincia
            x["canton"] = canton
            x["perfil"] = perfil
            x["contraseña"] = contraseña

            print("Usuario modificado con éxito")
            system("pause")
            menuUsuario(i)

    else:
        system("cls")
        print("La cedula ingresada no pertenece a ningun usuario registrado!")
        system("pause")
        menuUsuario(i)
    

def eliminarUsuarios(i):  # Function to delete registered users
    system("cls")
    cedulaAEliminar = input ("Ingrese la cedula del usuario a eliminar: ").lower()

    for x in listUsuarios:  # Loop through the list of users to check if the user's cedula matches the input cedula
        if x["cedula"] == cedulaAEliminar:
            listUsuarios.remove(x)
            print("Usuario eliminado con éxito")
            system("pause")
            menuUsuario(i)
    else:  # If the input cedula does not match any user's cedula
        system("cls")
        print("La cedula ingresada no pertenece a ningun usuario registrado!")
        system("pause")
        menuUsuario(i)



def mostrarEventosAdmin(i):  # Function to display the list of events for the Administrator
    system("cls")
    print("Lista de eventos actuales:")
    print()
    if listEventos:  # Check if there are any events in the list
        for e in listEventos:
            print(f"Codigo: {e['codigo']}")
            print(f"Nombre: {e['nombre']}")
            print(f"Provincia: {e['provincia']}")
            print(f"Cantón: {e['canton']}")
            print(f"Placa: {e['placa']}")
            print(f"Nombre del Oficial: {e['nombreOficial']}")
            print(f"Numero de Parte: {e['numeroParte']}")
            print(f"Nombre del Juzgado: {e['nombreJuzgado']}")
            print(f"Numero de Registro: {e['numeroRegistro']}")
            print(f"Estado: {e['estado']}")
            print(f"Fecha: {e['fecha']}")
            print(f"Hora: {e['hora']}")
            print(f"Multa: {e['multa']}")
            print()
        system("pause")

    else:
        system("cls")
        print("No hay eventos registrados en el sistema.")
        system("pause")
        menuCiudadano(i)


def modificarEventosAdmin(i):  # Function to modify events for the Administrator
    system("cls")

    while True:  # Loop to continuously prompt the user until they enter a valid input
            try:
                placa = input("Digite el número de placa del vehiculo del incidente a modificar en el formato (AAA000): ").upper()  # Prompt the user to enter the vehicle's plate number in the correct format
                if len(placa) == 6 and placa[:3].isalpha() and placa[3:].isdigit():  # Check if the input placa is in the correct format
                    placa = placa[:3] + "-" + placa[3:]  
                    
                    
                    for u in listVehiculos:  # Loop through the list of vehicles to check if the input placa is associated with a vehicle
                        if placa == u["placa"]:
                            break

                    else:
                        system("cls")
                        print(f"La placa ingresada no está asociada a ningun vehiculo registrado!")
                        system("pause")
                        return
                      
                    break
                    
                else:
                    raise ValueError
                
            except ValueError:
                system("cls")

                print("Ingrese la placa en el formato correcto: (AAA000)!")
                system("pause")

    for e in listEventos:  # Loop through the list of events to check if the input placa is associated with an event
        if e['placa'] == placa:  # Check if the input placa is associated with an event
            while True:  # Loop to continuously prompt the user until they enter a valid input
                try:  # Try to validate the user's input
                    mostrarProvincias()
                    provinciaSeleccionada = input("Ingrese su provincia de residencia: ").title()
                    if provinciaSeleccionada in provinciasCantones.keys():
                        print()
                        break
                    else:  # If the input province is not in the province-canton dictionary
                        system("cls")
                        print("La provincia ingresada no existe!")
                        system("pause")

                except ValueError:
                    system("cls")
                    print("Ingrese una de las provincias mostradas en pantalla!")
                    system("pause")
                    mostrarProvincias()

            while True:  # Loop to continuously prompt the user until they enter a valid input
                try:  # Try to validate the user's residence canton
                    cantonesProvincia = provinciasCantones[provinciaSeleccionada]
                    
                    print(f"Los cantones disponibles en {provinciaSeleccionada} son:")
                    for canton in cantonesProvincia:
                        print(f"- {canton}")
                    
                    cantonSeleccionado = input("Ingrese su cantón de residencia: ").title()  # Prompt the user to enter their residence canton
                    if cantonSeleccionado in cantonesProvincia:
                        break
                    else:
                        system("cls")
                        print("El cantón ingresado no existe!")
                        system("pause")

                except ValueError:
                    system("cls")
                    print("Ingrese uno de los cantones mostrados en pantalla!")
                    system("pause")


            while True:  # Loop to continuously prompt the user until they enter a valid input
                try:    # Try to validate the user's input
                    placa = input("Digite el nuevo número de placa del vehiculo del incidente en el formato (AAA000): ").upper()
                    if len(placa) == 6 and placa[:3].isalpha() and placa[3:].isdigit():
                        placaNueva = placa[:3] + "-" + placa[3:]
                        
                        
                        for u in listVehiculos:  # Loop through the list of vehicles to check if the input placa is associated with a vehicle
                            if placaNueva == u["placa"]:
                                break

                        else:
                            system("cls")
                            print(f"La placa ingresada no está asociada a ningun vehiculo registrado!")
                            system("pause")
                            return
                        

                        break
                        
                    else:
                        raise ValueError
                    
                except ValueError:  # If the user enters an invalid input
                    system("cls")

                    print("Ingrese la placa en el formato correcto: (AAA000)!")
                    system("pause")


            e['canton'] = cantonSeleccionado
            e['provincia'] = provinciaSeleccionada
            e['placa'] = placaNueva
            e['fecha'] = datetime.today().strftime("%d/%m/%Y")
            e['hora'] = datetime.today().strftime("%H:%M:%S")

            system("cls")
            print("Evento modificado con éxito!")
            system("pause")
            break

        else:  # If the event does not exist
            system("cls")
            print(f"No existe un evento de {i['nombre']} con ese código!")
            system("pause")




def menuAdmin(i):  # Function to display the menu for the Administrator
    while True:  # Loop to continuously display the menu until the user chooses to exit
        try:  # Try to display the menu
            system("cls")
            print(f"---Menú de Administrador--- (Logueado como: {i["perfil"]}  Usuario: {i["nombre"]}))")
            print()
            print("1. CRUD Provincias y Cantones")
            print("2. Ver usuarios Registrados")
            print("3. Modificar Usuarios")
            print("4. Eliminar Usuarios")
            print("5. Ver eventos")
            print("6. Modificar Eventos")
            print("7. Salir")
            print()

            opcion = int(input("Ingrese la opción deseada: "))  # Prompt the user to select an option from the menu

            if opcion == 1:
                crudProvinciasCantones()
            
            elif opcion == 2:
                verUsuariosRegistrados()

            elif opcion == 3:
                modificarUsuarios(i)

            elif opcion == 4:
                eliminarUsuarios(i)

            elif opcion == 5:
                mostrarEventosAdmin(i)

            elif opcion == 6:
                modificarEventosAdmin(i)

            elif opcion ==7:
                menuInicioSesion()

        
            else:  # If the user enters an invalid option
                system("cls")
                print("Opción no válida, digite una de las opciones mostradas en pantalla")
                system("pause")
        

        except ValueError:
            print("Digite un valor valido!")




def registrarVehiculo(i):  # Function to register a new vehicle
    system("cls")
    dictVehiculos = {}  # Initialize an empty dictionary to store the vehicle information

    dictVehiculos['cedulaDueño'] = i["cedula"]  # Set the vehicle's owner's cedula

    while True:  # Loop to continuously prompt the user until they enter a valid input
        try:  # Try to validate the user's input
            placa = input("Digite el número de placa en el formato (AAA000): ").upper()  # Prompt the user to enter the vehicle's plate number in the correct format
            if len(placa) == 6 and placa[:3].isalpha() and placa[3:].isdigit():  # Check if the input placa is in the correct format
                dictVehiculos["placa"] = placa[:3] + "-" + placa[3:]

                for k in listVehiculos:  # Loop through the list of vehicles to check if the input placa is associated with a vehicle
                    if k["placa"] == dictVehiculos["placa"]:
                        system("cls")
                        print("Ya existe un vehiculo asociado a esa placa!")
                        system("pause")
                        menuUsuario(i)
                        break
                else:
                    break
            else:
                raise ValueError
            
        except ValueError:
            system("cls")
            print("Ingrese la placa en el formato correcto: (AAA000)!")
            system("pause")


    while True:  # Loop to continuously prompt the user until they enter a valid input
        try:  # Try to validate the user's input
            dictVehiculos['año'] = int(input("Ingrese el año del vehículo: "))
            break
        except ValueError:
            system("cls")
            print("Ingrese el año en numeros enteros!")
            system("pause")

    dictVehiculos['marca'] = input("Ingrese la marca del vehículo: ").capitalize()
    dictVehiculos['color'] = input("Ingrese el color del vehículo: ").capitalize()

    while True:  # Loop to continuously prompt the user until they enter a valid input
        try:  # Try to validate the user's input
            dictVehiculos['tipo'] = input ("Ingrese el tipo de vehículo (Moto, Automovil, Bus o Camion) sin tildes: ").capitalize()
            if dictVehiculos['tipo'] == "Moto" or dictVehiculos['tipo'] == "Automovil" or dictVehiculos['tipo'] == "Bus" or dictVehiculos['tipo'] == "Camion":
                break
        except ValueError:
            system("cls")
            print("Ingrese el tipo de vehículo (Moto, Automovil, Bus o Camion) sin tildes!")
            system("pause")

    listVehiculos.append(dictVehiculos)  # Add the vehicle to the list

    system("cls")
    print("Vehiculo guardado exitosamente!")
    system("pause")
    menuUsuario(i)

def mostrarVehiculosUsuario(i):  # Function to display the list of vehicles associated with the user
    try:  # Try to display the list of vehicles
        system("cls")

        if listVehiculos:   # Check if there are any vehicles in the list
            listVehiculosUsuario = [m for m in listVehiculos if m["cedulaDueño"] == i["cedula"]]

            if listVehiculosUsuario:  # Check if there are any vehicles associated with the user
                print(f"Vehículos registrados de {i['nombre']}:")

                for m in listVehiculosUsuario:  # Loop through the list of vehicles associated with the user to display the information
                    print(f"Placa: {m['placa']}")
            
            else:  # If there are no vehicles associated with the user
                system("cls")
                print(f"{i['nombre']} no tiene vehículos registrados, favor registre sus vehículos!")
                system("pause")
                menuCiudadano(i)
            print()

        else:  # If there are no vehicles in the list
            system("cls")
            print("No hay vehículos registrados en el sistema.")
            system("pause")
            menuCiudadano(i)
    
    except ValueError:
        menuCiudadano(i)

def mostrarProvincias():  # Function to display the list of provinces
    print("Provincias:")
    for provincias, cantones in provinciasCantones.items():
            print(f" -{provincias}")

def mostrarCantones():  # Function to display the list of cantons
    print("Cantones:")
    for provincias, cantones in provinciasCantones.items():  # Loop through the province-canton dictionary to display the list of cantons
        for canton in cantones:
            print(f" -{canton}")

def calcularMulta(tipoVehiculo,añoVehiculo):  # Function to calculate the total amount of the incident
    try:  # Try to calculate the total amount of the incident
        system("cls")
        dicMultas = {}  # Initialize an empty dictionary to store the incident's information
        
        with open('tablaIncidentes.txt', 'r') as file:  # Open the file in read mode
            for line in file:
                tipo, valores = line.strip().split(': ')  # Split the line into two parts: the incident type and the values
                valorMulta, impuesto = valores.split(', ')  # Split the values into two parts: the base amount and the tax
                dicMultas[tipo.lower()] = {
                    'valorMulta': int(valorMulta),
                    'impuesto': float(impuesto)
                }

        
        tipoVehiculo = tipoVehiculo.lower()  # Convert the input tipoVehiculo to lowercase
        if tipoVehiculo in dicMultas:  # Check if the input tipoVehiculo is in the dictionary
            multaBase = dicMultas[tipoVehiculo]['valorMulta']
            impuesto = dicMultas[tipoVehiculo]['impuesto']

        else:  # If the input tipoVehiculo is not in the dictionary
            raise ValueError("Tipo de vehículo no reconocido")
        
        
        valorMulta = multaBase + (multaBase * impuesto)  # Calculate the total amount of the incident

        
        if añoVehiculo < 2000:  # Check if the year is before 2000
            valorMulta *= 1.10

        return round(valorMulta, 2)  # Round the result to two decimal places
    
    except ValueError:
        system("cls")
        print("Se ha producido un error, intente nuevamente")
        system("pause")

def crearEvento(i):  # Function to create a new event
    system("cls")
    mostrarVehiculosUsuario(i)  # Display the list of vehicles associated with the user
    print()

    dictVehiculosEvento = {}  # Initialize an empty dictionary to store the event information
    listVehiculosUsuario = [m for m in listVehiculos if m["cedulaDueño"] == i["cedula"]]  # Filter the list of vehicles to only include vehicles associated with the user

    dictVehiculosEvento["codigo"] = random.randint(1,5)  # Generate a random code for the event
    dictVehiculosEvento["nombre"] = i["nombre"]  # Set the event's name to the user's name
    
    while True:  # Loop to continuously prompt the user until they enter a valid input
        try:  # Try to validate the user's input
            placa = input("Digite el número de placa del vehiculo del incidente en el formato (AAA000): ").upper()  # Prompt the user to enter the vehicle's plate number in the correct format
            if len(placa) == 6 and placa[:3].isalpha() and placa[3:].isdigit():
                dictVehiculosEvento["placa"] = placa[:3] + "-" + placa[3:]
                
                
                for u in listVehiculosUsuario:  # Loop through the list of vehicles to check if the input placa is associated with a vehicle

                    if dictVehiculosEvento["placa"] == u["placa"]:  # Check if the input placa is associated with a vehicle
                        tipoVehiculo = u["tipo"]
                        añoVehiculo = u["año"]
                        break

                else:  # If the input placa is not associated with a vehicle
                    system("cls")
                    print(f"La placa ingresada no está asociada a ningun vehiculo de {i['nombre']}")
                    system("pause")
                    return
                
                # Validamos si ya existe un evento con esta placa
                for e in listEventos:  # Loop through the list of events to check if the input placa is associated with an event
                    if dictVehiculosEvento["placa"] == e["placa"]:
                        system("cls")
                        print("Ya existe un evento asociado a ese vehículo!")
                        system("pause")
                        return  
                break
                
            else:  # If the input placa is not associated with an event
                raise ValueError
            
        except ValueError:  # If the user enters an invalid input
            system("cls")
            mostrarVehiculosUsuario(i)
            print("Ingrese la placa en el formato correcto: (AAA000)!")
            system("pause")

    system("cls")

    
    while True:  # Loop to continuously prompt the user until they enter a valid input
        try:  # Try to validate the user's residence province
            mostrarProvincias()
            provinciaSeleccionada = input("Ingrese la provincia del incidente: ").title()  # Prompt the user to enter the province in the correct format
            if provinciaSeleccionada in provinciasCantones.keys():  # Check if the input province is in the province-canton dictionary
                print()
                break
            else:  # If the input province is not in the province-canton dictionary
                system("cls")
                print("La provincia ingresada no existe!")
                system("pause")

        except ValueError:  # If the user enters an invalid input
            system("cls")
            print("Ingrese una de las provincias mostradas en pantalla!")
            system("pause")
            mostrarProvincias()

    
    while True:  # Loop to continuously prompt the user until they enter a valid input
        try:  # Try to validate the user's residence canton
            cantonesProvincia = provinciasCantones[provinciaSeleccionada]
            
            print(f"Los cantones disponibles en {provinciaSeleccionada} son:")
            for canton in cantonesProvincia:  # Loop through the list of cantons in the selected province
                print(f"- {canton}")
            
            cantonSeleccionado = input("Ingrese el cantón del incidente: ").title()  # Prompt the user to enter the canton in the correct format
            if cantonSeleccionado in cantonesProvincia:  # Check if the input canton is in the cantons list
                break
            else:  # If the input canton is not in the cantons list
                system("cls")
                print("El cantón ingresado no existe!")
                system("pause")

        except ValueError:  # If the user enters an invalid input
            system("cls")
            print("Ingrese uno de los cantones mostrados en pantalla!")
            system("pause")

    dictVehiculosEvento["provincia"] = provinciaSeleccionada
    dictVehiculosEvento["canton"] = cantonSeleccionado
    dictVehiculosEvento["nombreOficial"] = "Pendiente"
    dictVehiculosEvento["numeroParte"] = 0
    dictVehiculosEvento["nombreJuzgado"] = "Pendiente"
    dictVehiculosEvento["numeroRegistro"] = 0
    dictVehiculosEvento["estado"] = "Abierto"
    dictVehiculosEvento["fecha"] = datetime.today().strftime("%d/%m/%Y")
    dictVehiculosEvento["hora"] = datetime.today().strftime("%H:%M:%S")
    dictVehiculosEvento["multa"] = calcularMulta(tipoVehiculo, añoVehiculo)

    listEventos.append(dictVehiculosEvento)  # Add the event to the list
    system("cls")
    print("Evento creado con éxito!")

    system("pause")
    menuUsuario(i)
    
def consultarEventos(i):  # Function to view the events associated with a specific user
    system("cls")

    eventosUsuario = [e for e in listEventos if e['nombre'] == i["nombre"]]  # Filter the list of events to only include events associated with the user

    if eventosUsuario:  # Check if there are any events associated with the user
        system("cls")
        print(f"Eventos para el usuario {i["nombre"]}:")
        print()
        for e in eventosUsuario:  # Loop through the list of events to display the information
            print(f"Codigo: {e['codigo']}")
            print(f"Nombre: {e['nombre']}")
            print(f"Provincia: {e['provincia']}")
            print(f"Cantón: {e['canton']}")
            print(f"Placa: {e['placa']}")
            print(f"Nombre del oficial: {e['nombreOficial']}")
            print(f"Numero de Parte: {e['numeroParte']}")
            print(f"Nombre del Juzgado: {e['nombreJuzgado']}")
            print(f"Numero de Registro: {e['numeroRegistro']}")
            print(f"Estado: {e['estado']}")
            print(f"Fecha: {e['fecha']}")
            print(f"Hora: {e['hora']}")
            print(f"Multa: {e['multa']}")
            print()
    else:  # If the user does not have any events registered
        system("cls")
        print(f"El usuario {i['nombre']} no tiene eventos registrados.")
        system("pause")
        menuCiudadano(i)

    system("pause")

def modificarEventos(i):  # Function to modify a specific event
    system("cls")
    eventosUsuario = [e for e in listEventos if e['nombre'] == i["nombre"]]  # Filter the list of events to only include events associated with the user
    listVehiculosUsuario = [m for m in listVehiculos if m["cedulaDueño"] == i["cedula"]]  # Filter the list of vehicles to only include vehicles associated with the user

    while True:   # Loop to continuously prompt the user until they enter a valid input
            try:
                placa = input("Digite el número de placa del vehiculo del incidente a modificar en el formato (AAA000): ").upper() 
                if len(placa) == 6 and placa[:3].isalpha() and placa[3:].isdigit():
                    placa = placa[:3] + "-" + placa[3:]
                    
                    
                    for u in listVehiculosUsuario:  # Loop through the list of vehicles to check if the input placa is associated with a vehicle
                        if placa == u["placa"]:
                            break

                    else:  # If the input placa is not associated with a vehicle
                        system("cls")
                        print(f"La placa ingresada no está asociada a ningun vehiculo de {i['nombre']}")
                        system("pause")
                        return
                      
                    break
                    
                else:  # If the input placa is not associated with a vehicle
                    raise ValueError
                
            except ValueError:  # If the user enters an invalid input
                system("cls")
                mostrarVehiculosUsuario(i)
                print("Ingrese la placa en el formato correcto: (AAA000)!")
                system("pause")

    for e in eventosUsuario:  # Loop through the list of events to check if the input placa is associated with an event
        if e['placa'] == placa:  # Check if the input placa is associated with an event
            while True:  # Loop to continuously prompt the user until they enter a valid input
                try:
                    mostrarProvincias()
                    provinciaSeleccionada = input("Ingrese su provincia de residencia: ").title()
                    if provinciaSeleccionada in provinciasCantones.keys():
                        print()
                        break
                    else:  # If the input province is not in the province-canton dictionary
                        system("cls")
                        print("La provincia ingresada no existe!")
                        system("pause")

                except ValueError:  # If the user enters an invalid input
                    system("cls")
                    print("Ingrese una de las provincias mostradas en pantalla!")
                    system("pause")
                    mostrarProvincias()

            while True:  # Loop to continuously prompt the user until they enter a valid input
                try:  # Try to validate the user's residence canton
                    cantonesProvincia = provinciasCantones[provinciaSeleccionada]
                    
                    print(f"Los cantones disponibles en {provinciaSeleccionada} son:")
                    for canton in cantonesProvincia:
                        print(f"- {canton}")
                    
                    cantonSeleccionado = input("Ingrese su cantón de residencia: ").title()
                    if cantonSeleccionado in cantonesProvincia:
                        break
                    else:
                        system("cls")
                        print("El cantón ingresado no existe!")
                        system("pause")

                except ValueError:
                    system("cls")
                    print("Ingrese uno de los cantones mostrados en pantalla!")
                    system("pause")

            mostrarVehiculosUsuario(i)  # Display the list of vehicles associated with the user
            while True:  # Loop to continuously prompt the user until they enter a valid input
                try:
                    placa = input("Digite el nuevo número de placa del vehiculo del incidente en el formato (AAA000): ").upper()
                    if len(placa) == 6 and placa[:3].isalpha() and placa[3:].isdigit():
                        placaNueva = placa[:3] + "-" + placa[3:]
                        
                        
                        for u in listVehiculosUsuario:  # Loop through the list of vehicles to check if the input placa is associated with a vehicle

                            if placaNueva == u["placa"]:
                                break

                        else:  # If the input placa is not associated with a vehicle
                            system("cls")
                            print(f"La placa ingresada no está asociada a ningun vehiculo de {i['nombre']}")
                            system("pause")
                            return
                        
                        
                        for e in listEventos:  # Loop through the list of events to check if the input placa is associated with an event
                            if placaNueva == e["placa"]:
                                system("cls")
                                print("Ya existe un evento asociado a ese vehículo!")
                                system("pause")
                                return
                        break
                        
                    else:
                        raise ValueError
                    
                except ValueError:  # If the user enters an invalid input
                    system("cls")
                    mostrarVehiculosUsuario(i)
                    print("Ingrese la placa en el formato correcto: (AAA000)!")
                    system("pause")


            e['canton'] = cantonSeleccionado
            e['provincia'] = provinciaSeleccionada
            e['placa'] = placaNueva
            e['fecha'] = datetime.today().strftime("%d/%m/%Y")
            e['hora'] = datetime.today().strftime("%H:%M:%S")

            system("cls")
            print("Evento modificado con éxito!")
            system("pause")
            break

        else:  # If the event does not exist
            system("cls")
            print(f"No existe un evento de {i['nombre']} con ese código!")
            system("pause")

def eliminarEventos(i):  # Function to delete a specific event
    try:  # Try to delete the event
        system("cls")
        listVehiculosUsuario = [m for m in listVehiculos if m["cedulaDueño"] == i["cedula"]] 

        while True:  # Loop to continuously prompt the user until they enter a valid input
            try:
                placa = input("Digite el número de placa del vehiculo del incidente a eliminar en el formato (AAA000): ").upper()
                if len(placa) == 6 and placa[:3].isalpha() and placa[3:].isdigit():
                    placa = placa[:3] + "-" + placa[3:]
                    
                    
                    for u in listVehiculosUsuario:  # Loop through the list of vehicles to check if the input placa is associated with a vehicle
                        if placa == u["placa"]:
                            break
                    
                    else:  # If the input placa is not associated with a vehicle
                        system("cls")    
                        print(f"La placa ingresada no está asociada a ningun vehiculo de {i['nombre']}")
                        system("pause")
                        return
                    
                    
                    for e in listEventos:  # Loop through the list of events to check if the input placa is associated with an event
                        if not placa == e["placa"]:
                            system("cls")
                            print("No existe un evento asociado a esa placa!")
                            system("pause")
                            return  
                    break
                    
                else:
                    raise ValueError
                
            except ValueError:  # If the user enters an invalid input
                system("cls")
                mostrarVehiculosUsuario(i)
                print("Ingrese la placa en el formato correcto: (AAA000)!")
                system("pause")
        

        for r in listEventos:  # Loop through the list of events to check if the input placa is associated with an event
            if r["placa"] == placa:
                if r["estado"] == "Abierto":
                    system("cls")
                    listEventos.remove(r)  # Remove the event from the list
                    print("Evento eliminado exitosamente!")
                    system("pause")

                else:  # If the event is not in the "Abierto" state
                    system("cls")
                    print("No se puede eliminar un evento con un estado que no sea abierto")
                    system("pause")

                    

            else:  # If the input placa is not associated with an event
                system("cls")
                print(f"La placa ingresada no está asociada a ningun vehiculo de {i['nombre']}")
                system("pause")
                menuUsuario(i)
        
    except ValueError:
        system("cls")
        print("Se ha producido un error inesperado, favor intente nuevamente!")
        system("pause")
                 
def menuCiudadano(i):  # Function to display the menu for the Ciudadan
    while True:  # Loop to continuously display the menu until the user chooses to exit
        try:
            system("cls")
            print(f"---Menú de Ciudadano--- (Logueado como: {i["perfil"]}  Usuario: {i["nombre"]})")
            print()
            print("1. Registrar vehiculo")
            print("2. Crear Evento")
            print("3. Consultar Eventos")
            print("4. Modificar Eventos")
            print("5. Eliminar Eventos")
            print("6. Salir")
            print()



            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                registrarVehiculo(i)
            elif opcion == 2:
                crearEvento(i)
            elif opcion == 3:
                consultarEventos(i)
            elif opcion == 4:
                modificarEventos(i)
            elif opcion == 5:
                eliminarEventos(i)
            elif opcion == 6:
                menuInicioSesion()

            else:  # If the user enters an invalid option
                system("cls")
                print("Opción no válida, digite una de las opciones mostradas en pantalla")
                system("pause")
    
        except ValueError:  # If the user enters an invalid option
            system("cls")
            print("Digite una de las opciones mostradas en pantalla!")
            system("pause")

    

        
#Funciones del menu Oficial
def cargarListaOficial(i):  # Function to load the list of events for the Office of the Judge
    system("cls")
    if listEventos:
        eventos_abiertos = []   # List to store events in the "Abierto" state

        for o in listEventos:  # Loop through the list of events to check if the event is in the "Abierto" state
            if o["estado"] == "Abierto":
                eventos_abiertos.append(o)  # Add the event to the list if it is in the "Abierto" state

        if eventos_abiertos:  # Check if there are any events in the "Abierto" state
            print("Eventos de todos los usuarios con estado Abierto:")
            print()
            for e in eventos_abiertos:  # Loop through the list of events in the "Abierto" state
                print(f"Codigo: {e['codigo']}")
                print(f"Nombre: {e['nombre']}")
                print(f"Provincia: {e['provincia']}")
                print(f"Cantón: {e['canton']}")
                print(f"Placa: {e['placa']}")
                print(f"Estado: {e['estado']}")
                print(f"Fecha: {e['fecha']}")
                print(f"Hora: {e['hora']}")
                print(f"Multa: {e['multa']}")
                print()
            system("pause")
        else:  # If there are no events in the "Abierto" state
            print("No hay eventos con el estado Abierto para mostrar!")
            system("pause")
        
        menuOficial(i)

    else:  # If there are no events in the "Abierto" state
        system("cls")
        print("No hay eventos registrados en el sistema!")
        system("pause")
        menuCiudadano(i)






def modificarInformacionEventoOficial(i):  # Function to modify the information of a specific event for the Office of the Judge
    system("cls")
    while True:  # Loop to continuously prompt the user until they enter a valid input
            try:
                placa = input("Digite el número de placa del vehiculo del incidente a modificar en el formato (AAA000): ").upper() 
                if len(placa) == 6 and placa[:3].isalpha() and placa[3:].isdigit():  # Check if the input placa is in the correct format
                    placa = placa[:3] + "-" + placa[3:] 
                    
                    
                    for u in listVehiculos:  # Loop through the list of vehicles to check if the input placa is associated with a vehicle
                        if placa == u["placa"]:
                            break

                    else:  # If the input placa is not associated with a vehicle
                        system("cls")
                        print(f"La placa ingresada no está asociada a ningun vehiculo")
                        system("pause")
                        return
                    break
                    
                else:
                    raise ValueError
                
            except ValueError:
                system("cls")
                print("Ingrese la placa en el formato correcto: (AAA000)!")
                system("pause")

    for e in listEventos:  # Loop through the list of events to check if the input placa is associated with an event
        if e['placa'] == placa:
            e["nombreOficial"] = i["nombre"]  # Update the event's office name
            while True:  # Loop to continuously prompt the user until they enter a valid input
                try:
                    e["numeroParte"] = int (input("Ingrese el numero de parte: "))
                    break
                except ValueError:
                    system("cls")
                    print("El numero de parte debe de ser un numero entero")
                    system("pause")
            e["estado"] = "Por Aprobar"
            e['fecha'] = datetime.today().strftime("%d/%m/%Y")
            e['hora'] = datetime.today().strftime("%H:%M:%S")

            system("cls")
            print("Evento modificado con éxito!")
            system("pause")
            menuOficial(i)
            break

    else:
        system("cls")
        print(f"No existe un evento de {i['nombre']} con ese código!")
        system("pause")

def menuOficial(i):  # Function to display the menu for the Office of the Judge
    while True:  # Loop to continuously display the menu until the user chooses to exit
        try:
            system("cls")
            print(f"---Menú de Oficial de Tránsito --- (Logueado como: {i["perfil"]}  Usuario: {i["nombre"]})")
            print()
            print("1. Cargar lista de eventos")
            print("2. Modificar evento")
            print("3. Salir")
            print()

            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                cargarListaOficial(i)

            elif opcion == 2:
                modificarInformacionEventoOficial(i)

            elif opcion == 3:
                menuInicioSesion()

            else:
                system("cls")
                print("Digite una de las opciones mostradas en pantalla!")
                system("pause")
    
        except ValueError:
            system("cls")
            print("Digite un valor valido!")
            system("pause")
            menuOficial(i)







def cargarListaJuzgado(i):  # Function to load the list of events for the Judge Office
    system("cls")
    if listEventos:
        for o in listEventos:  # Loop through the list of events to check if the event is in the "Por Aprobar" state
            if o["estado"] == "Por Aprobar":  # Check if the event is in the "Por Aprobar" state
                system("cls")
                print(f"Eventos de todos los usuarios con estado Por Aprobar:")
                print()
                for e in listEventos:  # Loop through the list of events in the "Por Aprobar" state
                    print(f"Codigo: {e['codigo']}")
                    print(f"Nombre: {e['nombre']}")
                    print(f"Provincia: {e['provincia']}")
                    print(f"Cantón: {e['canton']}")
                    print(f"Placa: {e['placa']}")
                    print(f"Nombre del Oficial: {e['nombreOficial']}")
                    print(f"Numero de Parte: {e['numeroParte']}")
                    print(f"Estado: {e['estado']}")
                    print(f"Fecha: {e['fecha']}")
                    print(f"Hora: {e['hora']}")
                    print(f"Multa: {e['multa']}")
                    print()
                system("pause")
                menuJuzgado(i)
            else:  # If there are no events in the "Por Aprobar" state
                system("cls")
                print("No hay eventos con el estado Por Aprobar para mostrar!")
                system("pause")
                menuJuzgado(i)
    else:   # If there are no events in the "Por Aprobar" state
        system("cls")
        print(f"No hay eventos registrados en el sistema!")
        system("pause")
        menuCiudadano(i)




def guardarListado(lineasc):  # Function to save the list of events to a file
    with open(f"eventosCompletos.txt", "w") as file:  # Open the file in write mode
        file.write(lineasc)  # Write the content to the file
    print("Listado de eventos guardado")




def txtInformes():  # Function to save the data to a txt file
    fecha = datetime.today().strftime("%d-%m-%Y")  # Format the current date as dd-mm-yyyy
    hora = datetime.today().strftime("%H:%M:%S")  # Format the current time as hh:mm:ss
    numeroInforme = 1   # Initialize the number of the report
    
    listado = f"Fecha de informe: {fecha}, hora del informe: {hora}\n" 
    listado += f"Numero de informe: {numeroInforme}\n"
    for h in listEventos:  # Loop through the list of events to add the information to the report
        listado += (f"Codigo: {h['codigo']}\n"
                    f"Nombre: {h['nombre']}\n"
                    f"Provincia: {h['provincia']}\n"
                    f"Cantón: {h['canton']}\n"
                    f"Placa: {h['placa']}\n"
                    f"Nombre del Oficial: {h['nombreOficial']}\n"
                    f"Numero de Parte: {h['numeroParte']}\n"
                    f"Nombre del Juzgado: {h['nombreJuzgado']}\n"
                    f"Numero de Registro: {h['numeroRegistro']}\n"
                    f"Estado: {h['estado']}\n"
                    f"Fecha: {h['fecha']}\n"
                    f"Hora: {h['hora']}\n"
                    f"Multa: {h['multa']}\n")
        numeroInforme +=1

    guardarListado(listado)




def modificarInformaciónDeEventoJuzgado(i):  # Function to modify the information of a specific event for the Judge Office
    system("cls")
    while True:  # Loop to continuously prompt the user until they enter a valid input
            try:
                placa = input("Digite el número de placa del vehiculo del incidente a modificar en el formato (AAA000): ").upper()  # Prompt the user to enter the vehicle's plate number in the correct format
                if len(placa) == 6 and placa[:3].isalpha() and placa[3:].isdigit():  # Check if the input placa is in the correct format
                    placa = placa[:3] + "-" + placa[3:]  # Remove the first three characters and the last three characters from the input placa
                    
                    
                    for u in listVehiculos:  # Loop through the list of vehicles to check if the input placa is associated with a vehicle
                        if placa == u["placa"]:
                            break

                    else:
                        system("cls")
                        print(f"La placa ingresada no está asociada a ningun vehiculo")
                        system("pause")
                        return
                    break
                    
                else:
                    raise ValueError
                
            except ValueError:
                system("cls")
                print("Ingrese la placa en el formato correcto: (AAA000)!")
                system("pause")

    for e in listEventos:  # Loop through the list of events to check if the input placa is associated with an event
        if e['placa'] == placa:
            e["nombreJuzgado"] = i["nombre"]  # Update the event's judge office name
            while True:  # Loop to continuously prompt the user until they enter a valid input
                try:  # Try to validate the user's input
                    e["numeroRegistro"] = int (input("Ingrese el numero de registro: "))
                    break
                except ValueError:
                    system("cls")
                    print("El numero de registro debe de ser un numero entero")
                    system("pause")

            e["estado"] = "Completo"
            e['fecha'] = datetime.today().strftime("%d/%m/%Y")
            e['hora'] = datetime.today().strftime("%H:%M:%S")

            
            txtInformes()  # Save the data to the txt file

            system("cls")
            print("Evento modificado con éxito!")
            system("pause")
            menuJuzgado(i)
            break

        else:
            system("cls")
            print(f"No existe un evento de {i['nombre']} con ese código!")
            system("pause")

def menuJuzgado(i):  # Function to display the menu for the Judge Office
    while True:  # Loop to continuously display the menu until the user chooses to exit
        try:
            system("cls")
            print(f"---Menú de Oficina del Juzgado --- (Logueado como: {i["perfil"]}  Usuario: {i["nombre"]})")
            print()
            print("1. Cargar lista de eventos")
            print("2. Modificar evento") 
            print("3. Salir")
            print()

            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                cargarListaJuzgado(i)

            elif opcion == 2:
                modificarInformaciónDeEventoJuzgado(i)

            elif opcion == 3:
                menuInicioSesion()

            else:
                system("cls")
                print("Digite una de las opciones mostradas en pantalla!")
                system("pause")

    
        except ValueError:
            system("cls")
            print("Digite un valor valido!")
            system("pause")
            menuJuzgado(i)











def menuUsuario(i):  # Function to display the menu for the user
    if i["perfil"] == "Administrador":
        menuAdmin(i)

    elif i["perfil"] == "Ciudadano":
        menuCiudadano(i)
    
    elif i["perfil"] == "Oficial":
        menuOficial(i)

    elif i["perfil"] == "Juzgado":
        menuJuzgado(i)

    else:
        print("Perfil no reconocido!")








def iniciarSesion():  # Function to log in the user
    try:  # Try to log in the user
        system("cls")
        cedula = input("Ingrese su cédula: ").lower()
        contraseña = input("Ingrese su contraseña: ").lower()

        for i in listUsuarios:  # Loop through the list of users to check if the user exists
            if i["cedula"] == cedula:  # Check if the user's cedula matches the input cedula
                if i["contraseña"] == contraseña:  # Check if the user's password matches the input password
                    system("cls")
                    print(f"Bienvenido/a {i['nombre']}, su perfil es {i['perfil']} y ha iniciado sesión correctamente!")
                    system("pause")
                    menuUsuario(i)
                    break

                else:  # If the user's password does not match the input password
                    print("Contraseña incorrecta")
                    system("pause")
                    menuInicioSesion()
        else:         
            print("Usuario no registrado")
            system("pause")

    except ValueError:
        system("cls")
        print("Ingrese un valor válido")
        system("pause")



def registrarse():  # Function to register a new user
    try:  # Try to register the user
        system("cls")
        cedula = input("Ingrese su cédula: ").lower()

        for x in listUsuarios:  # Loop through the list of users to check if the user already exists
            if x["cedula"] == cedula:
                print("Cédula ya registrada!")
                system("pause")
                menuInicioSesion()

        nombre = input("Ingrese su nombre: ").capitalize() 

        while True:  # Loop to validate the user's date of birth
            try:  # Try to validate the user's date of birth
                fechaNacimiento = input("Ingrese su fecha de nacimiento (dia/mes/año): ")
                edad = calcularEdad(fechaNacimiento)
                break
            except ValueError:
                print()
                print("Ingrese la fecha de nacimiento en el formato correcto")
                system("pause")
                print()
        
        if edad >= 18:  # Check if the user is at least 18 years old
            pass
        else:
            system("cls")
            print("Debe ser mayor de edad para registrarse!")
            system("pause")
            menuInicioSesion()

        
        while True:  # Loop to validate the user's sex
            try:
                sexo = input("Ingrese su sexo (Masculino o Femenino): ").capitalize()
                if sexo == "Masculino" or sexo == "Femenino":
                    break
                
            except ValueError:
                system("cls")
                print("Ingrese el sexo en el formato correcto!")
                system("pause")
        
        
        while True:  # Loop to validate the user's province
            try:
                mostrarProvincias()
                provincia = input("Ingrese su provincia de residencia: ").title()
                if provincia in provinciasCantones.keys():
                    print()
                    break
                else:
                    system("cls")
                    print("La provincia ingresada no existe!")
                    system("pause")

            except ValueError:
                system("cls")
                print("Ingrese una de las provincias mostradas en pantalla!")
                system("pause")
                mostrarProvincias()

        #Validar que el cantón elegido exista en el diccionario de provincias y cantones
        while True:
            try:
                cantonesProvincia = provinciasCantones[provincia]
                
                print(f"Los cantones disponibles en {provincia} son:")
                for canton in cantonesProvincia:
                    print(f"- {canton}")
                
                canton = input("Ingrese su cantón de residencia: ").title()  # Prompt the user to enter their residence canton
                if canton in cantonesProvincia:
                    break
                else:  # If the input canton is not in the cantons list
                    system("cls")
                    print("El cantón ingresado no existe!")
                    system("pause")

            except ValueError:
                system("cls")
                print("Ingrese uno de los cantones mostrados en pantalla!")
                system("pause")



        while True:  # Loop to validate the user's profile
            try:
                perfil = input("Ingrese su perfil (Ciudadano, Oficial o Juzgado): ").capitalize()
                if perfil == "Ciudadano" or perfil == "Oficial" or perfil == "Juzgado":
                    break
                
            except ValueError:
                system("cls")
                print("Ingrese el tipo de perfil (Ciudadano, Oficial o Juzgado) en el formato correcto!")
                system("pause")

        contraseña = input("Ingrese su contraseña: ").lower()  # Prompt the user to enter their password
        

        listUsuarios.append({"cedula": cedula, "nombre": nombre, "fechaNacimiento": fechaNacimiento, "edad": edad, "sexo": sexo, "provincia": provincia, "canton": canton, "perfil": perfil, "contraseña": contraseña})
        print("Usuario registrado con éxito")
        system("pause")

    except ValueError:
        system("cls")
        print("Ingrese un valor válido")
        system("pause")



def menuInicioSesion():  # Function to display the menu for the user to log in
    while True:  # Loop to continuously display the menu until the user chooses to exit
        try:
            system("cls")
            print("---Bienvenido al sistema de Eventos – Colisión de Vehículos---")
            print()
            print("1. Iniciar Sesión")
            print("2. Registrar Usuario")
            print("3. Salir")
            print()

            opcion = int(input("Seleccione una opción: "))  # Prompt the user to select an option from the menu
            if opcion == 1:
                iniciarSesion()
            elif opcion == 2:
                registrarse()
            elif opcion == 3:
                exit()
                
            else:
                system("cls")
                print("Opción no válida, digite una de las opciones mostradas en pantalla")
                system("pause")

        except ValueError:
            system("cls")
            print("Opción no válida, digite una de las opciones mostradas en pantalla")
            system("pause")
