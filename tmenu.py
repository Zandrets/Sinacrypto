import tkinter as tk
import tkinter.font as tkFont
import Module1 as DB
import dmenu as MDB
import matplotlib.pyplot as mpl
from To_Topsis import Topsis
import pandas as pd
import os 
class menu():
    def __init__(self, menu):
        #Window functionalities
        menu.title('Encryption dynamic system')
        width=600
        height=200
        screenwidth = menu.winfo_screenwidth()
        screenheight = menu.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        menu.geometry(alignstr)                                     #Window size
        menu.resizable(width=False, height=False)                   #Window resizable off
        #Module buttons
        database_button=tk.Button(menu)
        ft = tkFont.Font(family='Times',size=10)                    #Font type
        database_button["font"] = ft                                #Button font
        database_button["fg"] = "#000000"                           #Button font color
        database_button["bg"] = "#a21313"                           #Button color
        database_button["justify"] = "center"                       #Button align
        database_button["text"] = "Database"                        #Button text
        database_button.place(x=20,y=20,width=135,height=40)        #Button position and size
        database_button["command"] = self.database_button_command   #Button actions call

        modata_button=tk.Button(menu)
        modata_button["font"] = ft                              #Button font
        modata_button["fg"] = "#000000"                         #Button font color
        modata_button["bg"] = "#a21313"                         #Button color
        modata_button["justify"] = "center"                     #Button align
        modata_button["text"] = "Update database"               #Button text
        modata_button.place(x=180,y=20,width=135,height=40)     #Button position and size
        modata_button["command"] = self.modata_button_command   #Button actions call

        graphics_button=tk.Button(menu)
        ft = tkFont.Font(family='Times',size=10)                    #Font type
        graphics_button["font"] = ft                                #Button font
        graphics_button["fg"] = "#000000"                           #Button font color
        graphics_button["bg"] = "#a21313"                           #Button color
        graphics_button["justify"] = "center"                       #Button align
        graphics_button["text"] = "Graphics"                        #Button text
        graphics_button.place(x=340,y=20,width=135,height=40)       #Button position and size
        graphics_button["command"] = self.graphics_button_command   #Button actions call
        
    def database_button_command(self):                          #Button actions list
        database=tk.Tk()
        prodatat=DB.Database(database)
        database.mainloop()

    def modata_button_command(self):
        modata=tk.Tk()
        pro_mod=MDB.menu_database(modata)
        modata.mainloop()
        
    def graphics_button_command(self):
        topsis=Topsis()
        hash_table=pd.DataFrame(pd.read_csv(os.path.dirname(__file__)+'/'+"sistemas_hash.csv", index_col='Algoritmos'))
        llaves_table=pd.DataFrame(pd.read_csv(os.path.dirname(__file__)+'/'+"sistemas_llaves.csv", index_col='Algoritmos'))
        hashs=topsis.topsis_pipy(hash_table, hash_table, len(hash_table.columns), [3,1,1], ['+','-','-'])
        llaves=topsis.topsis_pipy(llaves_table, llaves_table ,len(llaves_table.columns), [3,1,1,1,1], ['+','-','-','-','-'])
        for i in range(0, hashs.shape[0]):
            mpl.scatter(hashs.iloc[i, 1], hashs.iloc[i, 2])
        mpl.show()
            
        
#MAIN
if __name__ == "__main__":
    root = tk.Tk()
    project = menu(root)
    root.mainloop()