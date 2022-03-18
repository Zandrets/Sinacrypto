import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import pandas as pd

#VENTANA
class menu_database():
    def __init__(self, modata):
        #Funcionalidades de ventana
        modata.title('Test window')
        width=600
        height=400
        screenwidth = modata.winfo_screenwidth()
        screenheight = modata.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        modata.resizable(width=False, height=False)
        #CAMPOS DE TEXTO
        modata.geometry(alignstr)
        algoritmo=ttk.Entry(modata)
        seguridad=ttk.Entry(modata)
        tcifrado=ttk.Entry(modata)
        tdescifrado=ttk.Entry(modata)
        aupes=ttk.Entry(modata)
        comrec=ttk.Entry(modata)
        idd=ttk.Entry(modata)
        algoritmo.place(x=210,y=70,width=360,height=25)
        seguridad.place(x=210,y=100,width=360,height=25)
        tcifrado.place(x=210,y=130,width=360,height=25)
        comrec.place(x=210,y=160,width=360,height=25)
        tdescifrado.place(x=210,y=190,width=360,height=25)
        aupes.place(x=210,y=220,width=360,height=25)
        idd.place(x=210,y=250,width=360,height=25)
        #TEXTO DE AYUDA PARA LOS CAMPOS DE TEXTO
        txt_alg=ttk.Label(modata, text="Algoritmo")
        txt_seg=ttk.Label(modata, text="Seguridad")
        txt_tc=ttk.Label(modata, text="Tiempo de cifrado")
        txt_cr=ttk.Label(modata, text="Consumo de recursos")
        txt_td=ttk.Label(modata, text="Tiempo de descifrado")
        txt_ap=ttk.Label(modata, text="Aumento de peso")
        iddd=ttk.Label(modata, text="ID (modificar/borrar)")
        txt_help=ttk.Label(modata, text="Only use the ID field if you will modify or delete a row, ")
        txt_alg.place(x=15,y=70,width=120,height=25)
        txt_seg.place(x=15,y=100,width=120,height=25)
        txt_tc.place(x=15,y=130,width=120,height=25)
        txt_cr.place(x=15,y=160,width=120,height=25)
        txt_td.place(x=15,y=190,width=120,height=25)
        txt_ap.place(x=15,y=220,width=120,height=25)
        iddd.place(x=15,y=250,width=120,height=25)
        #BOTONES
        GRadio_524=tk.Radiobutton(modata)
#        GRadio_524["font"] = tkFont.Font(family='Times',size=10)
#        GRadio_524["fg"] = "333333"
#        GRadio_524["justify"] = "center"
        GRadio_524["text"] = "Alg. de llaves"
        GRadio_524.place(x=100,y=10,width=85,height=25)
        GRadio_524["command"] = lambda : self.llaves_button(algoritmo, seguridad, tcifrado, comrec, tdescifrado, aupes, iddd, modata)

        GRadio_685=tk.Radiobutton(modata)
#        GRadio_685["font"] = tkFont.Font(family='Times',size=10)
#        GRadio_685["fg"] = "333333"
#        GRadio_685["justify"] = "center"
        GRadio_685["text"] = "Alg. de hash"
        GRadio_685.place(x=400,y=10,width=85,height=25)
        GRadio_685["command"] = lambda : self.hash_button(algoritmo, seguridad, tcifrado, comrec, tdescifrado, aupes,iddd, modata)
#        added= '%s, %s, %s, %s' % (var1, var2, var3, var4)
    def hash_button(self, alg,seg,tc,cr,td,ap,idd,modata):
        mode="hash"
        td["state"]=tk.DISABLED
        ap["state"]=tk.DISABLED
        create=ttk.Button(modata, text="agregar")
        modify=ttk.Button(modata, text="modificar")
        delete=ttk.Button(modata, text="delete")
        create.place(x=80,y=350,width=100,height=30)
        modify.place(x=230,y=350,width=100,height=30)
        delete.place(x=380,y=350,width=100,height=30)
        create["command"]=lambda : self.agregar(alg,seg,tc,cr,td,ap,modata,mode)
        modify["command"]=lambda : self.modificar(idd,alg,seg,tc,cr,td,ap,modata,mode)
        delete["command"]=lambda : self.eliminar(idd,modata,mode)

    def llaves_button(self, alg,seg,tc,cr,td,ap,idd,modata):
        mode="key"
        td["state"]=tk.NORMAL
        ap["state"]=tk.NORMAL
        create=ttk.Button(modata, text="agregar")
        modify=ttk.Button(modata, text="modificar")
        delete=ttk.Button(modata, text="delete")
        create.place(x=80,y=350,width=100,height=30)
        modify.place(x=230,y=350,width=100,height=30)
        delete.place(x=380,y=350,width=100  ,height=30)
        create["command"]=lambda : self.agregar(alg,seg,tc,cr,td,ap,modata,mode)
        modify["command"]=lambda : self.modificar(idd,alg,seg,tc,cr,td,ap,modata,mode)
        delete["command"]=lambda : self.eliminar(idd,modata,mode)

    def modificar(self, alg,seg,tc,cr,td,ap,modata,mode):
        

    def agregar(self, alg,seg,tc,cr,td,ap,modata,mode):
        if mode == "hash":
            algoritmo=alg.get();seguridad=seg.get();tcifrado=tc.get();consum=cr.get()
            if algoritmo!="" and seguridad!="" and tcifrado!="" and consum!="":
                line="%s, %s, %s, %s" % (algoritmo,seguridad,tcifrado,consum)
                file=open("sistemas_hash.csv","a")
                file.write("\n")
                file.write(line)
                file.close
            else:
                print(2)
        if mode == "key":
            algoritmo=alg.get();seguridad=seg.get();tcifrado=tc.get();consum=cr.get();tdescifrado=td.get();aupes=ap.get()
            if algoritmo!="" and seguridad!="" and tcifrado!="" and consum!="" and tdescifrado!="" and aupes!="":
                line="%s, %s, %s, %s, %s, %s" % (algoritmo,seguridad,tcifrado,consum,tdescifrado,aupes)
                file=open("sistemas_llaves.csv","a")
                file.write("\n")
                file.write(line)
                file.close
            else:
                print(2)

    def eliminar(idd,modata,mode):
        if mode == "hash" and idd!="":
            print(1)
        elif mode == "key" and idd!="":
            print(2)
        else:
            print(3)

#MAIN
if __name__ == "__main__":
    root = tk.Tk()
    project = menu_database(root)
    root.mainloop()