
import tkinter as tk
import re
from tkinter import messagebox
import mysql.connector as mysqlCon


def insertRegistry(nombre, apellido, edad, estatura, telefono, genero):
    try:
        connection = mysqlCon.connect(
            host = "localhost",
            port = "3306",
            user = "root",
            password = "1234567",
            database = "dato"
        )
        cursor = connection.cursor()
        query = "insert into tabla (nombre, apellido, telefono, estatura, edad, genero) values (%s, %s, %s, %s, %s, %s)"
        values = (nombre, apellido, telefono, estatura, edad, genero)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("info", "datos guardados")
    except mysqlCon.Error as err:
        messagebox.showerror("Error", f"error para guardar: {err}")


def clear():
  tbName.delete(0,tk.END)
  tbLastName.delete(0,tk.END)
  tbHeight.delete(0,tk.END)
  tbPhone.delete(0,tk.END)
  tbAge.delete(0,tk.END)
  varGender.set(0)
  	

def isValidInt(val):
    try:
      int(val)
      return True
    except ValueError:
      return False

def isValidFloat(val):
    try:
      float(val)
      return True
    except ValueError:
      return False
  
def isValidPhone(val):
     return val.isdigit() and len(val) == 10

def isValidText(val):
   return bool(re.match("^[a-zA-Z\s]+$", val))


def save():
  nombre = tbName.get()
  apellido = tbLastName.get()
  edad   = tbAge.get()
  telefono = tbPhone.get()
  estatura = tbHeight.get()
  genero = ""
  if varGender.get() == 1:
    genero = "Hombre"
  elif varGender.get() == 2:
    genero = "Mujer"
  
  
  if(isValidInt(edad) and isValidFloat(estatura) and isValidPhone(telefono) and isValidText(nombre) and isValidText(apellido)):
    
      insertRegistry(nombre, apellido, edad, estatura, telefono, genero)

      
      data = "nombre: " + nombre + "\napellido: " + apellido + "\nedad: " + edad + "\ntelefono: " + telefono + "\nestatura: " + estatura + "\nGender: " + genero
      with open("3O2024Data.txt", "a") as file:
        file.write(data + "\n\n")
    
      messagebox.showinfo("Info" + "Data saved succesfully\n\n", data)
  else:
     messagebox.showerror("Error", "Couldn't save data\n\nBadFormat")
     
  
  clear();  



window = tk.Tk()
window.geometry("480x640")
window.title("Form")

varGender = tk.IntVar()

lbName = tk.Label(window, text="Nombre: ")
lbName.pack()
tbName = tk.Entry()
tbName.pack()
lbLastName = tk.Label(window, text="Apellido:")
lbLastName.pack()
tbLastName = tk.Entry()
tbLastName.pack()
lbAge = tk.Label(window, text="Edad:")
lbAge.pack()
tbAge = tk.Entry()
tbAge.pack()
lbPhone = tk.Label(window, text= "Telefono:")
lbPhone.pack()
tbPhone = tk.Entry()
tbPhone.pack()
lbHeight = tk.Label(window, text="Estatura:")
lbHeight.pack()
tbHeight = tk.Entry()
tbHeight.pack()
lbGender = tk.Label(window, text="Genero:")
lbGender.pack()
rbMale = tk.Radiobutton(window, text = "Hombre", variable=varGender, value=1)
rbMale.pack()
rbFemale = tk.Radiobutton(window, text = "Mujer", variable=varGender, value=2)
rbFemale.pack()

btnClear = tk.Button(window, text = "Limpiar valores", command=clear)
btnClear.pack()
btnSave  = tk.Button(window, text = "Guardar Valores", command=save)
btnSave.pack()


window.mainloop()