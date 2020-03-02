from model.contacto import Contacto 
from model.model import Model
from view.view import View
from controller.controller import Controller

'''
m = Model()
m.agregar_contacto(1, 'Francisco Zárate', '473-162-1246', 'fm.zaratelopez@ugto.mx', 'Juan Rojas Gonzales')
m.agregar_contacto(2, 'Carlos Canno', '464-145-1835', 'cano@hotmail.com', 'Bulcano')
m.agregar_contacto(3, 'Conathan Hernandez', '464-132-1235', 'jonathan@gmail.com', 'Arteaga no 6')

m.agregar_cita(1, 1, 'Dicis', '17/02/2020', '15:30', 'Sistemas')
m.agregar_cita(2, 2, 'Escuela', '20/11/2020', '20:30', 'NLP')
m.agregar_cita(3, 1, 'Centro', '18/03/2020', '13:30', 'Trabajo')

#s = m.buscar_contacto('C')
#for c in s:
#    print(c.nombre, c.tel)

v = View()
s = m.leer_contactos(1)
v.mostrar_contacto(s)
c = m.leer_contactos(2)
v.mostrar_contacto(c)

f, c = m.buscar_contacto('C')
if f:
    v.borrar_contacto(c)
else:
    v.contacto_no_existe(1)'''

#s = m.leer_todos_contactos()
#v.mostrar_contactos(s)

cont = Controller()
cont.start()
cont.menu()