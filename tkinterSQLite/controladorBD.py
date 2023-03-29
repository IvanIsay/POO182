from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion= sqlite3.connect("C:/Users/lOkY/Documents/GitHub/POO182/tkinterSQLite/DBUsuarios.db")
            print("Conectado a la BD")
            return conexion
        except sqlite3.OperationalError:
            print("No se puedo Conectar")
            
    def guardarUsuario(self,nom,cor,con):
        
        #1. llamamo el metodo conexion 
        conx= self.conexionBD()
        
        #2. Validar vacios
        if( nom == "" or cor== "" or con ==""):
            messagebox.showwarning("Aguas!!", "Formulario incompleto")
            conx.close()
        else:
            # 3. realizar Insert a BD
            
            #4. Preparamos las varibles necesarias
            cursor= conx.cursor()
            conH= self.encriptarContra(con)
            datos=(nom,cor,conH)
            sqlInsert="insert into tbRegsitrados(nombre,correo,contra) values(?,?,?)"
            
            #5. Ejecutamos el Insert y cerramos la conexion
            cursor.execute(sqlInsert,datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Exito", "Usuario guardado")
                  
    def encriptarContra(self,con):
        
        # 1.preparamos la contraseña y  la sal  para Hash
        conPlana=con
        conPlana= conPlana.encode() #converir a bytes
        sal= bcrypt.gensalt()
        
        #encriptamos
        conHa= bcrypt.hashpw(conPlana,sal)
        print(conHa)
        
        # regresamos la contraseña encriptada
        return conHa
    
    def consultarUsuario(self,id):
        
        #1. realizar conexion BD
        conx= self.conexionBD()
        
        #2.vericar que el id Vacio
        if(id == ""):
            messagebox.showwarning("Cuidado","Escribe un Identificador")
            conx.close()
        else:
            #3. proceder a  la consulta
            try:
                #4.preparamos lo necesario
                cursor= conx.cursor()
                sqlSelect= "select * from tbRegsitrados where id= "+id
                
                #5. Ejecutamos,Guardamos la consulta y cerramos conexion
                cursor.execute(sqlSelect)
                RSusuario=cursor.fetchall()
                conx.close()
                return RSusuario
                
            except sqlite3.OperationalError:
                print("Error de consulta")