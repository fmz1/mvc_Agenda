from .contacto import Contacto
from .cita import Cita
from view.view import View

class Model:
    def __init__(self):
        self.contactos = []
        self.citas = []
        
    def buscar_id(self, id_contacto):
        for c in self.contactos:
            if c.id_contacto == id_contacto:
                return True, c
        return False, 0

    def buscar_id_cita(self, id_cita):
        for c in self.citas:
            if c.id_cita == id_cita:
                return True, c
        return False, 0

    #-------------------------Contacto methods---------------------------#
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        e, c = self.buscar_id(id_contacto)
        if not e:
            c = Contacto(id_contacto, nombre, tel, correo, dir)
            self.contactos.append(c)
            return True, c
        return False, 0

        #if not self.buscar_id(id_contacto)[0]:
        #    c = Contacto(id_contacto, nombre, tel, correo, dir)
        #    self.contactos.append(c)
        #    return True
        #return False

    def leer_contactos(self, id_contacto):
        e, c = self.buscar_id(id_contacto)
        return e, c

    def leer_todos_contactos(self):
        return self.contactos

    def actualizar_contacto(self, id_contacto, n_nombre = '', n_tel = '', n_correo = '', n_dir = ''):
        e, c = self.buscar_id(id_contacto)
        if e:
            if n_nombre != '':
                c.nombre = n_nombre
            if n_tel != '':
                c.tel = n_tel
            if n_correo != '':
                c.correo = n_correo
            if n_dir != '':
                c.dir = dir
            return True
        return False

    def borrar_contacto(self, id_contacto):
        e, c = self.buscar_id(id_contacto)
        if e:
            self.contactos.remove(Contacto)
            lista_temp = [c for c in self.citas if c.id_contacto == id_contacto]
            for c in lista_temp:
                self.citas.remove(c)
            return True, Contacto
        return False, 0

    def leer_contactos_letra(self, letra):
        lista = [c for c in self.contactos if c.nombre.lower().startswith(letra.lower())]
        '''lista = []
            for i in self.contactos:
                if c.nombre[0].lower() == letra.lower()
                if letra.nombre.lower().startswith(letra):
                    lista.append(c) '''
        
        return lista

    #----------------------------Cita methods----------------------------#
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        if not self.buscar_id_cita(id_cita)[0]:
            ci = Cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
            self.citas.append(ci)
            return True
        return False

    def leer_cita(self, id_cita):
        e, c = self.buscar_id_cita(id_cita)
        if e:
            return c
        return False

    def actualizar_Cita(self, id_cita, id_ncontacto = '', n_lugar = '', n_fecha = '', n_hora = '', n_asunto = ''):
        e, c = self.buscar_id_cita(id_cita)
        if e:
            if id_ncontacto != '':
                c.id_contacto = id_ncontacto
            if n_lugar != '':
                c.lugar = n_lugar
            if n_fecha != '':
                c.fecha = n_fecha
            if n_hora != '':
                c.hora = n_hora
            if n_asunto != '':
                c.asunto = n_asunto
            return True
        return False

    def borrar_cita(self, id_cita):
        e, c = self.buscar_id_cita(id_cita)
        if e:
            self.citas.remove(c)
            return True
        return False

    def buscar_cita(self, fecha):
        lista = [c for c in self.citas if c.fecha == fecha]
        '''lista = []
            for c in self.citas:
            if c.fecha == fecha:
                lista.append(c)
            return lista'''

        return lista