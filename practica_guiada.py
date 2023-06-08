
from tkinter import * 
from tkinter import messagebox
from practica_guiada_funcionalidad import *

miraiz=Tk()


#frame 

miframe=Frame( miraiz )
miframe.pack()






barramenu=Menu(miraiz )
miraiz.config(menu=barramenu )

#crearcion de menu para bbdd
opcion_bbdd=Menu(barramenu , tearoff=0)
opcion_bbdd.add_command(label="crear" , command=mibase_datos.crear_base_menu)
opcion_bbdd.add_command(label="salir" , command=mibase_datos.salir_base_menu)

barramenu.add_cascade(label="BBDD" , menu=opcion_bbdd)

#creacion de menu para borrar

opcion_borrar=Menu(barramenu ,tearoff=0)
opcion_borrar.add_command(label="borrar informarcion" ,command=mibase_datos.ID_stringvar_base_menu)
barramenu.add_cascade(label="BORRAR" , menu=opcion_borrar)

#creacion de menu para CRUD

opcion_crud=Menu(barramenu , tearoff=0)
opcion_crud.add_command(label="crear", command=mibase_datos.crear_registro)
opcion_crud.add_command(label="leer" , command=mibase_datos.leer_registro)
opcion_crud.add_separator()
opcion_crud.add_command(label="actualizar" , command=mibase_datos.actualizar_registro)
opcion_crud.add_command(label="borrar" , command=mibase_datos.borrar_registro)
barramenu.add_cascade(label="CRUD" , menu=opcion_crud)

# creacion de menu para ayuda

opcion_ayuda=Menu(barramenu , tearoff=0)
opcion_ayuda.add_command(label="acerca de" , command=mibase_datos.acerca_de)
sub_menu_ayuda=Menu(opcion_ayuda , tearoff=0)
sub_menu_ayuda.add_command(label="documentacion python " , command=mibase_datos.ayuda_menu_doc_python)
sub_menu_ayuda.add_command(label="documentacion tkinter" , command=mibase_datos.ayuda_menu_doc_tkinter)
opcion_ayuda.add_cascade(label="ayuda" , menu=sub_menu_ayuda)
barramenu.add_cascade(label="AYUDA" , menu=opcion_ayuda)



#creacion de label y entry
ID_stringvar=StringVar()
nombre_stringvar=StringVar()
apellido_stringvar=StringVar()
contraseña_stringvar=StringVar()
direccion_stringvar=StringVar()



id=Label( miframe , text="id")
id.grid(row=1  , column=0 , padx=10)
id_entry=Entry(miframe, textvariable=ID_stringvar )
id_entry.grid(row=1 , column=1)



nombre=Label(miframe , text="nombre")
nombre.grid(row=2 , column=0 ,padx=10 , pady=10)
nombre_entry=Entry(miframe ,textvariable=nombre_stringvar)
nombre_entry.grid(row=2 , column=1 ,padx=10 , pady=10)

apellido=Label(miframe , text="apellido")
apellido.grid(row=3 , column=0 , padx=10 , pady=10)
apellido_entry=Entry(miframe,textvariable=apellido_stringvar)
apellido_entry.grid(row=3 , column=1 , padx=10 , pady=10)

contraseña=Label(miframe , text="contraseña")
contraseña.grid(row=4 , column=0 , padx=10 , pady=10)
contraseña_entry=Entry(miframe,textvariable=contraseña_stringvar)
contraseña_entry.grid(row=4 , column=1 , padx=10 , pady=10)
contraseña_entry.config(show="*")

direccion=Label(miframe , text="dirección")
direccion.grid(row=5, column=0 , padx=10 ,pady=10)
direccion_entry=Entry(miframe,textvariable=direccion_stringvar)
direccion_entry.grid(row=5, column=1 , padx=10 ,pady=10)


comentarios=Label(miframe , text="comentarios")
comentarios.grid(row=6 , column=0 , padx=10 , pady=10)
comentarios_text=Text(miframe , width=20, height=5 )


#comentarios_text.place(x=90 , y=190)
comentarios_text.grid(row=6, column=1, padx=10 , pady=10)
#creacion de scrollbar

scrollvert=Scrollbar(miframe , command=comentarios_text.yview)
scrollvert.grid(row=6 ,column=2 , sticky="nsew")
comentarios_text.config(yscrollcommand=scrollvert.set)



#creacion de segundo frame 

miframe2=Frame(miraiz)
miframe2.pack()


#creacion de boton crear 

boton_crear=Button(miframe2, text="crear" , width=4 , command=mibase_datos.crear_registro)
boton_crear.grid(row=1 , column=0 , sticky="e", padx=10 ,pady=10)

# creacion de boton leer

boton_leer=Button(miframe2 , text="leer"  , width=3 , command=mibase_datos.leer_registro)
boton_leer.grid(row=1,column=1, sticky="e" , padx=10 ,pady=10)


#creacion de boton actualizar
boton_actualizar=Button(miframe2 , text="actualizar"  , width=7 , command=mibase_datos.actualizar_registro)
boton_actualizar.grid(row=1 ,column=2 , sticky="e", padx=10 ,pady=10)

#creacion de boton actualizar
boton_borrar=Button(miframe2 , text="borrar"  , width=4 , command=mibase_datos.borrar_registro)
boton_borrar.grid(row=1 ,column=3 , sticky="e", padx=10 ,pady=10)

#creacion de un tercer frame()
miframe3=Frame(miraiz)
miframe3.pack( side="top" , anchor= "s")


#creacion del boton siguiente

boton_siguiente=Button(miframe3 , text="siguiente" , width=6  ,command=mibase_datos.siguiente_registro)
boton_siguiente.grid(row=1 , column=4  )

#creacion del boton anterior 

boto_anterior=Button(miframe3 , text="anterior" , width=6, command=mibase_datos.anterior_registro)
boto_anterior.grid(row=1 , column=3  ,padx=10 , pady=10)




miraiz.mainloop()
