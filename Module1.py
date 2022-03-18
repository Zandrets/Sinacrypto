#Librerias
import tkinter as tk
from tkinter import CENTER, ttk
import tkinter.font as tkFont
import pandas as pd

#VENTANA
class Database():
    def __init__(self, database):
        #Funcionalidades de ventana
        database.title('Test window')
        width=1500
        height=600
        screenwidth = database.winfo_screenwidth()
        screenheight = database.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        database.geometry(alignstr)
        #Style
        style=ttk.Style(database)
        style.theme_use("vista")
        style.configure("Treeview", background="black", fieldbackground="black", foreground="white")
        #TABLA DE HASH
        algoritmos_hash=pd.DataFrame(pd.read_csv('sistemas_hash.csv'))
        hash_columns=algoritmos_hash.columns.values
        hash_tree=ttk.Treeview(database, columns=list(hash_columns))
        rowLabels = algoritmos_hash.index.tolist()
        hash_tree.column("#0", width=50)
        hash_tree.heading("#0", text='id', anchor=CENTER)
        for x in range(len(hash_columns)):
            hash_tree.column(hash_columns[x], width=150)
            hash_tree.heading(hash_columns[x], text=str(hash_columns[x]), anchor=CENTER)
        for i in range(len(algoritmos_hash)):
            hash_tree.insert('', i, text=rowLabels[i], values=algoritmos_hash.iloc[i,:].tolist())
        hash_tree['displaycolumns']=list(hash_columns)
        #TABLA DE LLAVES
        algoritmos_llaves=pd.DataFrame(pd.read_csv('sistemas_llaves.csv'))
        llaves_columns=algoritmos_llaves.columns.values
        llaves_tree=ttk.Treeview(database, columns=list(llaves_columns))
        rowLabels = algoritmos_llaves.index.tolist()
        llaves_tree.column("#0", width=50)
        llaves_tree.heading("#0", text='id', anchor=CENTER)
        for x in range(len(llaves_columns)):
            llaves_tree.column(llaves_columns[x], width=150)
            llaves_tree.heading(llaves_columns[x], text=str(llaves_columns[x]), anchor=CENTER)
        for i in range(len(algoritmos_llaves)):
            llaves_tree.insert('', i, text=rowLabels[i], values=algoritmos_llaves.iloc[i,:].tolist())
        llaves_tree['displaycolumns']=list(llaves_columns)
        #Module Radio buttons
        GRadio_524=tk.Button(database)
#        GRadio_524["font"] = tkFont.Font(family='Times',size=10)
#        GRadio_524["fg"] = "#333333"
#        GRadio_524["justify"] = "center"
        GRadio_524["text"] = "Alg. de llaves"
        GRadio_524.place(x=20,y=70,width=85,height=25)
        GRadio_524["command"] = lambda : self.llaves_button(llaves_tree, hash_tree)

        GRadio_685=tk.Button(database)
#        GRadio_685["font"] = tkFont.Font(family='Times',size=10)
#        GRadio_685["fg"] = "#333333"
#        GRadio_685["justify"] = "center"
        GRadio_685["text"] = "Alg. de hash"
        GRadio_685.place(x=135,y=70,width=85,height=25)
        GRadio_685["command"] = lambda : self.hash_button(hash_tree, llaves_tree)
        
    def hash_button(self, view, destruct):
        view.pack()
        destruct.forget()
    def llaves_button(self,view, destruct):
        view.pack()
        destruct.forget()
#MAIN
if __name__ == "__main__":
    database = tk.Tk()
    project = Database(database)
    database.mainloop()