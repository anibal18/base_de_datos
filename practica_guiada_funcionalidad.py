from tkinter import messagebox
import sqlite3
import webbrowser 
import practica_guiada


class base_de_datos():
				
				def __init__(self):
	    					self.mibase=""
	    					self.micursor=""

	
				def crear_base_menu(self ):#con esta función se crea la base de datos.
							
							try:
										print(type(self.mibase))
										self.mibase=sqlite3.connect("clientes")
										self.micursor=self.mibase.cursor()
										self.micursor.execute('''CREATE TABLE INFORMACION (ID INTEGER PRIMARY KEY AUTOINCREMENT , 
										NOMBRE VARCHAR(50) , APELLIDO VARCHAR(50) , CONTRASEÑA VARCHAR(50) ,
										DIRECCION VARCHAR(50)  ,COMENTARIOS VARCHAR(200))''')
										self.mibase.commit()
										print(type(self.mibase))
							except:
										self.aviso=messagebox.showwarning("Advertencia" , "La BBDD fue creada con anterioridad")

				def salir_base_menu(self):#con esta funcion se puede salir de la aplicación
							self.salir=messagebox.askokcancel("Salir" , "Deseas salir de la aplicación")
							if self.salir:
										self.mibase.close()
										practica_guiada.miraiz.destroy()

				def ID_stringvar_base_menu(self):#con esta función se deja el registro en blanco. 
							self.mibase=sqlite3.connect("clientes")
							self.micursor=self.mibase.cursor()
							self.advertencia=messagebox.askokcancel("Advertencia" , "Reiniciaras el formulario")
							if self.advertencia:
										practica_guiada.ID_stringvar.set(" ")
										practica_guiada.nombre_stringvar.set(" ")
										practica_guiada.apellido_stringvar.set(" ")
										practica_guiada.contraseña_stringvar.set(" ")
										practica_guiada.direccion_stringvar.set(" ")
										practica_guiada.comentarios_text.delete("1.0" , "end")


				def crear_registro(self):#con esta función se insertan registros en la tabla. 
							self.mibase=sqlite3.connect("clientes")
							self.micursor=self.mibase.cursor()
							self.advertencia_registro=messagebox.askokcancel("Información" , "Agregara registros a la base de datos")
							self.informacion2=[ (practica_guiada.nombre_stringvar.get() ), (practica_guiada.apellido_stringvar.get() ), (practica_guiada.contraseña_stringvar.get()) ,(practica_guiada.direccion_stringvar.get() ),( practica_guiada.comentarios_text.get("1.0" , "end"))] #
							if self.advertencia_registro:
										print(type(self.mibase))
										self.micursor.execute("INSERT INTO INFORMACION VALUES(NULL , ? , ?, ? , ? , ?)", self.informacion2)
										self.mibase.commit()
										self.advertencia_registro=messagebox.showinfo("BBDD" , "Se han agregado registros satisfactoriamente")
							self.micursor.execute("SELECT ID FROM INFORMACION")
							self.lista_ID=self.micursor.fetchall()
							self.ultimo_ID=self.lista_ID[len(self.lista_ID)-1]
							self.penultimo_ID=self.lista_ID[len(self.lista_ID)-2]
							self.contador=1
							self.resta=self.ultimo_ID[0]-self.penultimo_ID[0]
							print(type(self.resta))
							print(self.resta)


							if self.resta>1:
										print("siiiiiis")
										self.micursor.execute("UPDATE INFORMACION SET ID=ID+1-'" + str(self.resta) + "'where ID >" +  str(self.penultimo_ID[0]))
										self.mibase.commit()

				def leer_registro(self):#con esta funcion se pueden ver los registro de la base de datos en el formulario.
							self.contador=0
							self.mibase=sqlite3.connect("clientes")
							self.micursor=self.mibase.cursor()
							self.micursor.execute("SELECT * FROM  INFORMACION")
							verconsulta=self.micursor.fetchmany(int(practica_guiada.ID_stringvar.get()))
							self.op_registro=len(verconsulta)
							print(self.op_registro)
							print(verconsulta[self.op_registro-1])
							self.op_registro2=verconsulta[self.op_registro-1]
							for i in verconsulta[self.op_registro-1]:
										practica_guiada.ID_stringvar.set(self.op_registro2[0])
										practica_guiada.nombre_stringvar.set(self.op_registro2[1])
										practica_guiada.apellido_stringvar.set(self.op_registro2[2])
										practica_guiada.contraseña_stringvar.set(self.op_registro2[3])
										practica_guiada.direccion_stringvar.set(self.op_registro2[4])
										if self.contador==0:
													self.contador+=1
													practica_guiada.comentarios_text.insert(1.0 ,self.op_registro2 [5])

				def actualizar_registro(self):#con esta función se pueden actualizar los registros de la base de datos. 
							self.mibase=sqlite3.connect("clientes")
							self.micursor=self.mibase.cursor()		
							self.micursor.execute("UPDATE INFORMACION SET NOMBRE='" + practica_guiada.nombre_stringvar.get() + 
							"',APELLIDO='" + practica_guiada.apellido_stringvar.get() + "',CONTRASEÑA='" + practica_guiada.contraseña_stringvar.get() +
							"',DIRECCION='" + practica_guiada.direccion_stringvar.get() + 
							"',COMENTARIOS='"+ practica_guiada.comentarios_text.get("1.0" , "end") +
							"'WHERE ID=" + practica_guiada.ID_stringvar.get())
							self.mibase.commit()
							self.aviso=messagebox.showinfo("BBDD","Se han actualizado los datos correctamente.")

				def borrar_registro(self):#con esta funcion se pueden borrar los registros de la base de datos 
							self.mibase=sqlite3.connect("clientes")
							self.micursor=self.mibase.cursor()
							self.micursor.execute("DELETE FROM INFORMACION   WHERE ID=" + practica_guiada.ID_stringvar.get())
							self.info=messagebox.askokcancel("ADVERTENCIA" , " Borrar registro de la base de datos")
							if self.info:
										self.micursor.execute("UPDATE INFORMACION SET ID=ID-1 WHERE ID > " + practica_guiada.ID_stringvar.get())
										self.mibase.commit()
										self.info=messagebox.showinfo("BBDD" , "Informacion borrada exitosamente")
							else:
										self.info=messagebox.showinfo("INFORMACION" , "No se han borrado datos de la base de datos.")

				def ayuda_menu_doc_python(self):#con esta funcion se abre la doc oficial de python (webbrowser) en internet.
							self.directorio='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
							self.controlador=webbrowser.get(self.directorio)
							self.navegador=self.controlador.open_new("https://docs.python.org/3/library/webbrowser.html" )

				def ayuda_menu_doc_tkinter(self):#con esta funcion se abre la doc oficial de python (tkinter) en internet.
							self.controlador=webbrowser.get(self.directorio)
							self.navegador2=self.controlador.open_new("https://docs.python.org/3/library/tkinter.html")

				def acerca_de(self):#con esta funcion vemos un pequeño resumen de quien creo el programa y con que lenguaje.
							self.descrip=messagebox.showinfo("INFORMACION" , "Programa creado en PYTHON , por Anibal Gonzalez ")

				def siguiente_registro(self):#con esta funcion podemos ver el registro siguiente al anterior de la base de datos con un click.
							self.nuevo_id=practica_guiada.ID_stringvar.get()
							self.nuevo_id=int(self.nuevo_id)+1
							practica_guiada.ID_stringvar.set(" ")
							practica_guiada.nombre_stringvar.set(" ")
							practica_guiada.apellido_stringvar.set(" ")
							practica_guiada.contraseña_stringvar.set(" ")
							practica_guiada.direccion_stringvar.set(" ")
							practica_guiada.comentarios_text.delete("1.0" , "end")
							practica_guiada.ID_stringvar.set(self.nuevo_id)
							self.leer_registro()

				def anterior_registro(self):#con esta funcion podemos ver el registro anterio al actual de la base de datos con un click.
							self.viejo_id=practica_guiada.ID_stringvar.get()
							self.viejo_id=int(self.viejo_id)-1
							practica_guiada.ID_stringvar.set(" ")
							practica_guiada.nombre_stringvar.set(" ")
							practica_guiada.apellido_stringvar.set(" ")
							practica_guiada.contraseña_stringvar.set(" ")
							practica_guiada.direccion_stringvar.set(" ")
							practica_guiada.ID_stringvar.set(self.viejo_id)
							self.leer_registro()

mibase_datos=base_de_datos()

