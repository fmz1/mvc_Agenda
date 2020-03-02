from model.model import Model
from view.view import View

class Controller:
    # Constructor
    def __init__(self):
        self.model = Model()
        self.view = View()

    #Contacto Controllers
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        e, c = self.model.agregar_contacto(id_contacto, nombre, tel, correo, dir)
        if e:
            self.view.agregar_contacto(c)
        else:
            self.view.contacto_ya_existe(c)

    def leer_contacto(self, id_contacto):
        e, c = self.model.leer_contactos(id_contacto)
        if e:
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_todos_contactos(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)

    def actualizar_contacto(self, id_contacto, n_nombre = '', n_tel = '', n_correo = '', n_dir = ''):
        e = self.model.actualizar_contacto(id_contacto, n_nombre, n_tel , n_correo , n_dir )
        if e:
            self.view.actualizar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)

    def borrar_contacto(self, id_contacto):
        e, c = self.model.borrar_contacto(id_contacto)
        if e:
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_contactos_letra(self, letra):
        c = self.model.leer_contactos_letra(letra)
        self.view.mostrar_contactos(c)

    #----------------- Citas Controller ----------------------------#
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        e, c = self.model.agregar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
        if e:
            self.view.agregar_cita(c)
        else:
            self.view.cita_no_existe(c)

    def leer_cita(self, id_cita):
        e, c = self.model.leer_cita(id_cita)
        if e:
            self.view.mostrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)

    def leer_todos_citas(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)

    def actualizar_Cita(self, id_cita, id_ncontacto = '', n_lugar = '', n_fecha = '', n_hora = '', n_asunto = ''):
        e = self.model.actualizar_Cita(id_cita, id_ncontacto, n_lugar, n_fecha, n_hora, n_asunto)
        if e:
            self.view.actualizar_contacto(id_cita)
        else:
            self.view.contacto_no_existe(id_cita)

    def borrar_cita(self, id_cita):
        e, c = self.model.borrar_cita(id_cita)
        if e:
            self.view.borrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)

    def buscar_cita(self, fecha):
        c = self.model.buscar_cita(fecha)
        self.view.mostrar_cita(c)

    # General methods
    def insertar_contactos(self):
        self.agregar_contacto(1, 'Francisco Zárate', '473-162-1246', 'fm.zaratelopez@ugto.mx', 'Juan Rojas Gonzales')
        self.agregar_contacto(2, 'Carlos Canno', '464-145-1835', 'cano@hotmail.com', 'Vulcano')
        self.agregar_contacto(3, 'Jonathan Hernandez', '464-132-1235', 'jonathan@gmail.com', 'Arteaga no 6')
        
        '''
    def insertar_citas(self):
        self.agregar_cita(1, 1, 'Dicis', '17/02/2020', '15:30', 'Sistemas')
        self.agregar_cita(2, 2, 'Escuela', '20/11/2020', '20:30', 'NLP')
        self.agregar_cita(3, 1, 'Centro', '18/03/2020', '13:30', 'Trabajo')
        '''

    def start(self):
        # Display a welcome message
        self.view.start()

        # Insertar data in model
        self.insertar_contactos()
        #self.insertar_citas()
        
        #Show all contacts in DB
        self.leer_todos_contactos()
        #self.leer_contactos_letra('a')

    def write_contact(self):
        id = input("ID: ")
        n = str(input("Ingrese nombre: "))
        t = str(input("Ingrese telefono: "))
        c = str(input("Ingrese correo: "))
        d = str(input("Direccion: "))

        self.agregar_contacto(id, n, t, c, d)

    def search_contacto(self):
        letra = str(input('Ingresa letra a buscar: '))
        self.leer_contactos_letra(letra)

    def delete_contacto(self):
        id = input("Id contacto a borrar: ")
        self.borrar_contacto(id)

    def update_contaco(self):
        print("Si no desea modificar alguna parte del contacto presiona enter")
        id_contacto = input("Inserte el id del contacto que desea modificar:")
        n_nombre = str(input("Inserte el nuevo nombre:"))
        n_tel = str(input("Inserte el nuevo telefono:"))
        n_correo = str(input("Inserte el nuevo correo:"))
        n_dir = str(input("Inserte el nuevo direccion:"))
        self.actualizar_contacto(id_contacto, n_nombre , n_tel , n_correo , n_dir )
    
    def menu(self):
        #Display menu
        self.view.menu()
        o = input('Selecciona una opcion (1-9): ')     

        if o == '1':
            self.write_contact()
        elif o == '2':
            self.search_contacto()
        elif o == '3':
            self.update_contaco()
        elif o == '4':
           pass
        elif o == '5':
            pass
        elif o == '6':
            pass
        elif o == '7':
            pass
        elif o == '8':
            pass
        elif o == '9':
            self.view.end()
        else:
            self.view.opcion_no_valida()