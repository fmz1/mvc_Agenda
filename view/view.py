class View:
    def mostrar_contacto(self, contacto):
        print('******Datos del contacto******')
        print('Nombre: ', contacto.nombre)
        print('Telefono: ', contacto.tel)
        print('Correo: ', contacto.correo)
        print('Direccion: ', contacto.dir)
        print('*****************************')

    def mostrar_contactos(self, contactos):
        print('*****Contactos definidos*****')
        for c in contactos:
            print(c.nombre, c.tel, c.correo, c.dir)
        print('*****************************')

    def agregar_contacto(self, contacto):
        print(contacto.nombre, 'Se agrego a la base de datos')

    def borrar_contacto(self, contacto):
        print(contacto.nombre, 'Se ha borrado de la base de datos')

    def actualizar_contacto(self, id_contacto):
        print(id_contacto, 'Se ha modificado de la base de datos')  

    def contacto_ya_existe(self, id_contacto):
        print(id_contacto, 'YA EXISTE EN LA BASE DE DATOS')

    def contacto_no_existe(self, id_contacto):
        print('EL CONTACTO: ', id_contacto, 'NO EXISTE EN LA BASE DE DATOS')

    # ------------------------ CITAS ----------------------------- #
    def mostrar_cita(self, cita):
        print('*****Datos de la cita*****')
        print('Lugar: ', cita.lugar)
        print('Fecha: ', cita.fecha)
        print('Hora: ', cita.hora)
        print('Asunto: ', cita.asunto)
        print('**************************')

    def mostrar_citas(self, citas):
        print('*****Citas definidas*****')
        for c in citas:
            print(c.lugar, c.fecha, c.hora, c.asunto)
        print('*************************************')

    def agregar_cita(self, cita):
        print(cita.lugar, 'Se agrego a la base de datos')

    def borrar_cita(self, cita):
        print(cita.lugar, 'Se borro de la base de datos')

    def modificar_cita(self, cita_o, cita_n):
        print(cita_o.lugar, 'Se ha modificado de la base de datos')  

    def cita_ya_existe(self, cita):
        print(cita.id_cita, 'YA EXISTE EN LA BASE DE DATOS')

    def cita_no_existe(self, id_cita):
        print(id_cita, 'NO EXISTE EN LA BASE DE DATOS')
        
    # General views
    def start(self):
        print('Esto es un ejemplo de vista sencilla')

    def end(self):
        print('Nos vemos')

    def opcion_no_valida(self):
        print('No selecciono una opcion valida')

    def menu(self):
        print("1.Agregar contacto")
        print('2.Buscar contacto')
        print('3.Actualizar contacto')
        print('4.Borrar contacto')
        print('5.Agregar cita')
        print('6.Buscar cita')
        print('7.Actualizar cita')
        print('8.Borrar cita')
        print('9.Salir')