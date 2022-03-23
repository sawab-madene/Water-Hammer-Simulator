# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 16:49:08 2020

@author: hp
"""
""" bibliotheques"""  
import math 
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image 
from algorithmes import algo1,algo2,algo3,algo4,algo5,algo6,algo7,algo8,algo9          
# %% calculateur de Célérité de l’onde (line_12 to line 1029)
def wave_calculator_window():
    def paramétres(): #paramétres utilisés dans le calcul  de la célérité de l'onde de pression
        #les syntaxes ci dessous sont relatives à l'interface graphique
        top=tk.Toplevel()#nouvelle fenetre
        top.geometry("600x600")
        top.iconbitmap(r"photos\images.ico")
        frame1=tk.Frame(top)
        LabelTrois=tk.Label(top, text='Paramètres utilisés dans les calcules',fg="#0A1172",font=("courrier",20))
        LabelTrois.place(x=40,y=50)
            
        LabelTrois=tk.Label(frame1, text='a: Vitesse de propagation de l’onde de pression en [m/s]',font=("courrier",14))
        LabelTrois.grid(pady=10,row=0,column=1,sticky="W")
        
        LabelTrois=tk.Label(frame1, text='E: Module de Young du matériau de la conduite en [N/m²]',font=("courrier",14))
        LabelTrois.grid(pady=10,row=1,column=1,sticky="W")
        
        LabelTrois=tk.Label(frame1, text='K: Module d’élasticité hydrostatique du fluide en [N/m²]',font=("courrier",14))
        LabelTrois.grid(pady=10,row=2,column=1,sticky="W")
        
        LabelTrois=tk.Label(frame1, text='G: Module de rigidité de la roche en [N/m²]',font=("courrier",14))
        LabelTrois.grid(pady=10,row=3,column=1,sticky="W")
        
        LabelTrois=tk.Label(frame1, text='e: Epaisseur du revêtement en [m]',font=("courrier",14))
        LabelTrois.grid(pady=10,row=4,column=1,sticky="W")
        
        LabelTrois=tk.Label(frame1, text='ʋ: Coefficient de Poisson en [ - ]',font=("courrier",14))
        LabelTrois.grid(pady=10,row=5,column=1,sticky="W")
        
        LabelTrois=tk.Label(frame1, text='D: Diamètre de la conduite en [m]',font=("courrier",14))
        LabelTrois.grid(pady=10,row=6,column=1,sticky="W")
         
        LabelTrois=tk.Label(frame1, text='ρ: Densité du fluide en [kg/m3]',font=("courrier",14))
        LabelTrois.grid(pady=10,row=7,column=1,sticky="W")
        
        frame1.pack(expand=tk.YES)
    
    def Rigide():# Code qui concerne la conduite rigide
        def resultat(): #resultat est une fonction utilisé pour le calcul de la celerité dans le cas d'une conduite régide  
            K = float(K_entry.get())
            ρ=float(ρ_entry.get())
            a=(K/(ρ))**0.5
            a_Label.config(text=float(a),fg='red',font=("courrier",14))
            
        top=tk.Toplevel()#nouvelle fenetre
        top.geometry("400x400")
        top.iconbitmap(r"photos\images.ico")
        top.title("Calculateur de la célérité de l'onde de pression")
        frame1=tk.Frame(top)
        #Valeurs prédifinis
        K1=tk.StringVar()
        K1.set(1500000000)
        
        ρ1=tk.StringVar()
        ρ1.set(900)
         #les syntaxes ci dessous sont relatives à l'interface graphique
        LabelTrois=tk.Label(frame1, text='K [N/m²]',font=("courrier",14))
        LabelTrois.pack()
        K_entry=tk.Entry(frame1,textvariable=K1)
        K_entry.pack()
        
        LabelCinq=tk.Label(frame1, text='ρ  [kg/m3]',padx=10,font=("courrier",14))
        LabelCinq.pack()   
        ρ_entry=tk.Entry(frame1,textvariable=ρ1)
        ρ_entry.pack()
        
        bouton5=tk.Button(frame1, text='Calculer',font=("courrier",14),command=resultat)
        bouton5.pack(pady=30)
        
        LabelCinq=tk.Label(frame1, text=' a [m/s]',padx=10,font=("courrier",14))
        LabelCinq.pack()   
        
        bouton4=tk.Button(top, text='Aide',font=("courrier",12),bg='green',fg='white',command=paramétres)
        bouton4.place(x=0,y=0)
        
        a_Label=tk.Label(frame1)
        a_Label.pack()
        
        frame1.pack(expand=tk.YES)
        
    def tunnel(): # code concernant le tunnel 
        def sans():# code concernant le tennel sans revetement en acier
            def supprimer(): #l'appel de cette fonction supprime les boutons, les labels, les entry pour tout changement de systeme de fixation
                bouton5.destroy()
                bouton.destroy()
                LabelTrois.destroy()
                K_entry.destroy()
                LabelQuatre.destroy()
                E_entry.destroy()
                LabelCinq.destroy()
                ρ_entry.destroy()
                LabelCis.destroy()
                a_Label.destroy()
                
            def resultat(): #resultat est une fonction utilisé pour le calcul de la celerité dans le cas d'un tunnel sans revetment   
                K = float(K_entry.get())
                E = float( E_entry.get())
                ρ=float(ρ_entry.get())
                a=(K/(ρ*(1+(K/E))))**0.5   
                a_Label.config(text=float(a),fg='red',font=("courrier",14))
            #Valeurs prédifinis   
            K1=tk.StringVar()
            K1.set(2270000000)
            E1=tk.StringVar()
            E1.set(50000000000)
            ρ1=tk.StringVar()
            ρ1.set(1025)
             #les syntaxes ci dessous sont relatives à l'interface graphique
            LabelTrois=tk.Label(frame1, text='K [N/m²]',font=("courrier",12))
            LabelTrois.pack()
            K_entry=tk.Entry(frame1,textvariable=K1)
            K_entry.pack()
        
            LabelQuatre=tk.Label(frame1, text='E [N/m²]',padx=10,font=("courrier",12))
            LabelQuatre.pack()    
            E_entry=tk.Entry(frame1,textvariable=E1)
            E_entry.pack()
    
            LabelCinq=tk.Label(frame1, text='ρ [kg/m3]',padx=10,font=("courrier",12))
            LabelCinq.pack()   
            ρ_entry=tk.Entry(frame1,textvariable=ρ1)
            ρ_entry.pack()
            
            bouton5=tk.Button(frame1, text='Calculer',font=("courrier",12),command=resultat)
            bouton5.pack(pady=30,side='left')
            
            bouton=tk.Button(frame1, text='Réinitialiser',font=("courrier",12),command=supprimer)
            bouton.pack(side='right')
            
            LabelCis=tk.Label(frame3, text='a [m/s]',padx=10,font=("courrier",12))
            LabelCis.pack()
            
            bouton4=tk.Button(top, text='Aide',font=("courrier",12),bg='green',fg='white',command=paramétres)
            bouton4.place(x=0,y=0)
               
            a_Label=tk.Label(frame3)
            a_Label.pack()
            
            frame1.pack()
            
        def avec():# code qui concerne le tuennel sans revetement 
            def supprimer():#l'appel de cette fonction supprime les bouton, les labels, les entry pour tout changement de systeme de fixation
                LabelTrois.destroy()
                K_entry.destroy()
                LabelQuatre.destroy()
                E_entry.destroy()
                LabelCis.destroy()
                ρ_entry.destroy()
                Labelsept.destroy()
                D_entry.destroy()
                Label8.destroy()
                e_entry.destroy()
                Label9.destroy()
                G_entry.destroy()
                bouton10.destroy()
                Label11.destroy()
                a_Label.destroy()
                bouton.destroy()
               
            def resultat(): #resultat est une fonction utilisé pour le calcul de la celerité dans le cas d'un tunel avec revetement
                K = float(K_entry.get())
                D=  float(D_entry.get())
                e=  float(e_entry.get())           
                E = float( E_entry.get())
                ρ=float(ρ_entry.get())
                G = float( G_entry.get())
                psi=(D*E)/(G*D+E*e) 
                a=(K/(ρ*(1+(K/E)*psi)))**0.5
                a_Label.config(text=float(a),fg='red',font=("courrier",14))
            #Valeurs prédifinis    
            K1=tk.StringVar()
            K1.set(2270000000)
            E1=tk.StringVar()
            E1.set(206000000000)
            ρ1=tk.StringVar()
            ρ1.set(1025)
            D1=tk.StringVar()
            D1.set(1)
            e1=tk.StringVar()
            e1.set(0.02)
            G1=tk.StringVar()
            G1.set(50000000000)
             #les syntaxes ci dessous sont relatives à l'interface graphique
            LabelTrois=tk.Label(frame1, text='K [N/m²]',font=("courrier",12))
            LabelTrois.pack()
            K_entry=tk.Entry(frame1,textvariable=K1)
            K_entry.pack()
        
            LabelQuatre=tk.Label(frame1, text='E [N/m²]',padx=10,font=("courrier",12))
            LabelQuatre.pack()    
            E_entry=tk.Entry(frame1,textvariable=E1)
            E_entry.pack()
    
            LabelCis=tk.Label(frame1, text='ρ [kg/m3]',padx=10,font=("courrier",12))
            LabelCis.pack()   
            ρ_entry=tk.Entry(frame1,textvariable=ρ1)
            ρ_entry.pack()
            
            Labelsept=tk.Label(frame1, text='D [m]',padx=10,font=("courrier",12))
            Labelsept.pack()   
            D_entry=tk.Entry(frame1,textvariable=D1)
            D_entry.pack()
            
            Label8=tk.Label(frame1, text='e [m]',padx=10,font=("courrier",12))
            Label8.pack()   
            e_entry=tk.Entry(frame1,textvariable=e1)
            e_entry.pack()
            
            Label9=tk.Label(frame1, text='G [N/m²]',font=("courrier",12))
            Label9.pack()
            G_entry=tk.Entry(frame1,textvariable=G1)
            G_entry.pack()
            
            bouton10=tk.Button(frame1, text='Calculer',font=("courrier",12),command=resultat)
            bouton10.pack(pady=30,side='left')
            
            bouton=tk.Button(frame1, text='Réinitialiser',font=("courrier",12),command=supprimer)
            bouton.pack(side='right')
                      
            Label11=tk.Label(frame3, text='a [m/s]',padx=10,font=("courrier",12))
            Label11.pack()
            
            bouton4=tk.Button(top, text='Aide',font=("courrier",12),bg='green',fg='white',command=paramétres)
            bouton4.place(x=0,y=0)
            
            a_Label=tk.Label(frame3)
            a_Label.pack()
            
            frame1.pack()
                      
        top=tk.Toplevel()#nouvelle fenetre
        top.geometry("600x600")
        top.iconbitmap(r"photos\images.ico")
        top.title("Calculateur de la célérité de l'onde de pression")
        frame2=tk.Frame(top)
        frame1=tk.Frame(top)
        frame3=tk.Frame(top)
        
        Label11=tk.Label(frame2, text='Type de tunnel',padx=10,font=("courrier",16),fg='#0A1172')
        Label11.pack()
        
        bouton5=tk.Radiobutton(frame2, text='Tunnel sans revêtement ',value=1,font=("courrier",14),command=sans)
        bouton5.pack(pady=0)
        
        bouton5=tk.Radiobutton(frame2, text='Tunnel avec revêtement ',value=2,font=("courrier",14),command=avec)
        bouton5.pack(pady=0)
        
        frame2.pack()
        frame1.pack()
        frame3.pack()
        
    def autre():# Code concernant les conduites élastiques
        def toute():#le premier systeme de fixation: conduite encastré dans toute sa longeur
            def supprimer():#l'appel de cette fonction supprime les bouton, les labels, les entry pour tout changement de systeme de fixation
                LabelTrois.destroy()
                K_entry.destroy()
                LabelQuatre.destroy()   
                E_entry.destroy()
                 
                LabelCinq.destroy()   
                ρ_entry.destroy()
                Label6.destroy() 
                D_entry.destroy()
                Label7.destroy()   
                e_entry.destroy()
                Label8.destroy()   
                ʋ_entry.destroy()
                bouton10.destroy()
                bouton11.destroy()
                Label12.destroy()
                a_Label.destroy()
                Label13.destroy()
                Label14.destroy()
                                
            def resultat(): #resultat est une fonction utilisé pour le calcul de la celerité dans le cas d'une conduite régide  
                K = float(K_entry.get())
                D=  float(D_entry.get())
                e=  float(e_entry.get())           
                E = float( E_entry.get())
                ρ=float(ρ_entry.get())
                ʋ = float( ʋ_entry.get())
                
                if (D/e)<25:            
                    Label13.pack()
                    psi=2*(1+ʋ)*(((((D/2)+e)**2+(D/2)**2)/(((D/2)+e)**2-(D/2)**2))-((2*ʋ*(D/2)**2)/(((D/2)+e)**2-(D/2)**2)))
                    
                else:
                    Label14.pack()
                    psi=(D/e)*(1-ʋ**2)
                a=(K/(ρ*(1+(K/E)*psi)))**0.5
                a_Label.config(text=float(a),fg='red',font=("courrier",14))
            
            Label13=tk.Label(frame3, text='Paroi epaisse',fg='#0A1172',padx=10,font=("courrier",14))
            Label14=tk.Label(frame3, text='Paroi mince',fg='#0A1172',padx=10,font=("courrier",14))
            #Valeurs prédifinis
            K1=tk.StringVar()
            K1.set(2190000000)
            E1=tk.StringVar()
            E1.set(206000000000)
            ρ1=tk.StringVar()
            ρ1.set(999)
            D1=tk.StringVar()
            D1.set(2)
            e1=tk.StringVar()
            e1.set(0.03)
            ʋ1=tk.StringVar()
            ʋ1.set(0.27)
             #les syntaxes ci dessous sont relatives à l'interface graphique  
            LabelTrois=tk.Label(frame1, text='K [N/m²]',font=("courrier",12))
            LabelTrois.pack()
            K_entry=tk.Entry(frame1,textvariable=K1)
            K_entry.pack()
        
            LabelQuatre=tk.Label(frame1, text='E [N/m²]',padx=10,font=("courrier",12))
            LabelQuatre.pack()    
            E_entry=tk.Entry(frame1,textvariable=E1)
            E_entry.pack()
    
            LabelCinq=tk.Label(frame1, text='ρ [kg/m3]',padx=10,font=("courrier",12))
            LabelCinq.pack()   
            ρ_entry=tk.Entry(frame1,textvariable=ρ1)
            ρ_entry.pack()
            
            Label6=tk.Label(frame1, text='D [m]',padx=10,font=("courrier",12))
            Label6.pack()   
            D_entry=tk.Entry(frame1,textvariable=D1)
            D_entry.pack()
            
            Label7=tk.Label(frame1, text='e [m]',padx=10,font=("courrier",12))
            Label7.pack()   
            e_entry=tk.Entry(frame1,textvariable=e1)
            e_entry.pack()
            
            Label8=tk.Label(frame1, text='ʋ [-]',font=("courrier",12))
            Label8.pack()
            ʋ_entry=tk.Entry(frame1,textvariable=ʋ1)
            ʋ_entry.pack()
            
            bouton10=tk.Button(frame1, text='Calculer',font=("courrier",12),command=resultat)
            bouton10.pack(pady=30,side='left')
            
            bouton11=tk.Button(frame1, text='Réinitialiser',font=("courrier",12),command=supprimer)
            bouton11.pack(side='right')
            
            Label12=tk.Label(frame3, text='a [m/s]',padx=10,font=("courrier",12))
            Label12.pack()
            
            bouton4=tk.Button(top, text='Aide',font=("courrier",12),bg='green',fg='white',command=paramétres)
            bouton4.place(x=0,y=0)
            
            a_Label=tk.Label(frame3)
            a_Label.pack()
            
            frame1.pack()
            
        def partie():#le deuxieme systeme de fixation: conduite encastré dans sa partie supérieur
            def supprimer():#l'appel de cette fonction supprime les bouton, les labels, les entry pour tout changement de systeme de fixation
                LabelTrois.destroy()
                K_entry.destroy()
                LabelQuatre.destroy()   
                E_entry.destroy()
                Label6.destroy()   
                ρ_entry.destroy()
                Label7.destroy()   
                D_entry.destroy()
                Label8.destroy()   
                e_entry.destroy()
                Label9.destroy()
                ʋ_entry.destroy()
                bouton10.destroy()
                bouton11.destroy()
                Label12.destroy()
                a_Label.destroy()
                Label13.destroy()
                Label14.destroy()
                
            def resultat(): # resultat est une fonction utilisé pour le calcul de la célérité de l'onde de pression
                K = float(K_entry.get())
                D=  float(D_entry.get())
                e=  float(e_entry.get())           
                E = float( E_entry.get())
                ρ=float(ρ_entry.get())
                ʋ = float( ʋ_entry.get())
                
                if (D/e)<25:      
                    Label13.pack()
                    psi=2*(((((D/2)+e)**2+1.5*(D/2)**2)/(((D/2)+e)**2-(D/2)**2))-((ʋ*((D/2)+e)**2-3*(D/2)**2)/(((D/2)+e)**2-(D/2)**2)))
                    
                else:              
                    Label14.pack()
                    psi=(D/e)*(1-0.5*ʋ)
                a=(K/(ρ*(1+(K/E)*psi)))**0.5
                a_Label.config(text=float(a),fg='red',font=("courrier",14))
                
            Label13=tk.Label(frame3, text='Paroi epaisse',fg='#0A1172',padx=10,font=("courrier",14))    
            Label14=tk.Label(frame3, text='Paroi mince',fg='#0A1172',padx=10,font=("courrier",14))
            #Valeurs prédifinis 
            K1=tk.StringVar()
            K1.set(2190000000)
            E1=tk.StringVar()
            E1.set(206000000000)
            ρ1=tk.StringVar()
            ρ1.set(999)
            D1=tk.StringVar()
            D1.set(2)
            e1=tk.StringVar()
            e1.set(0.03)
            ʋ1=tk.StringVar()
            ʋ1.set(0.27)
            
            LabelTrois=tk.Label(frame1, text='K [N/m²]',font=("courrier",12))
            LabelTrois.pack()
            K_entry=tk.Entry(frame1,textvariable=K1)
            K_entry.pack()
        
            LabelQuatre=tk.Label(frame1, text='E [N/m²]',padx=10,font=("courrier",12))
            LabelQuatre.pack()    
            E_entry=tk.Entry(frame1,textvariable=E1)
            E_entry.pack()
    
            Label6=tk.Label(frame1, text='ρ [kg/m3]',padx=10,font=("courrier",12))
            Label6.pack()   
            ρ_entry=tk.Entry(frame1,textvariable=ρ1)
            ρ_entry.pack()
            
            Label7=tk.Label(frame1, text='D [m]',padx=10,font=("courrier",12))
            Label7.pack()   
            D_entry=tk.Entry(frame1,textvariable=D1)
            D_entry.pack()
             
            Label8=tk.Label(frame1, text='e [m]',padx=10,font=("courrier",12))
            Label8.pack()   
            e_entry=tk.Entry(frame1,textvariable=e1)
            e_entry.pack()
            
            Label9=tk.Label(frame1, text='ʋ [-]',font=("courrier",12))
            Label9.pack()
            ʋ_entry=tk.Entry(frame1,textvariable=ʋ1)
            ʋ_entry.pack()
            
            bouton10=tk.Button(frame1, text='Calculer',font=("courrier",12),command=resultat)
            bouton10.pack(pady=30,side='left')
            
            bouton11=tk.Button(frame1, text='Réinitialiser',font=("courrier",12),command=supprimer)
            bouton11.pack(side='right')
            
            Label12=tk.Label(frame3, text='a [m/s]',padx=10,font=("courrier",12))
            Label12.pack()
            
            bouton4=tk.Button(top, text='Aide',font=("courrier",12),bg='green',fg='white',command=paramétres)
            bouton4.place(x=0,y=0)
            
            a_Label=tk.Label(frame3)
            a_Label.pack()
                        
        def dilatation():#le troisieme systeme de fixation: conduite avec joint delatation
            def supprimer():#l'appel de cette fonction supprime les bouton, les labels, les entry pour tout changement de systeme de fixation
                LabelTrois.destroy()
                K_entry.destroy()
                LabelQuatre.destroy()   
                E_entry.destroy()
                Label6.destroy()   
                ρ_entry.destroy()
                Label7.destroy()   
                D_entry.destroy()
                Label8.destroy()   
                e_entry.destroy()
                Label9.destroy()
                ʋ_entry.destroy()
                bouton10.destroy()
                bouton11.destroy()
                Label12.destroy()
                a_Label.destroy()
                Label13.destroy()
                Label14.destroy()
                
            def resultat(): # resultat est une fonction utilisé pour le calcul de la célérité de l'onde de pression
                K =float(K_entry.get())
                D=float(D_entry.get())
                e=float(e_entry.get())           
                E =float( E_entry.get())
                ρ=float(ρ_entry.get())
                ʋ = float( ʋ_entry.get())
                
                if (D/e)<25:               
                    Label13.pack()
                    psi=2*(((((D/2)+e)**2+(D/2)**2)/(((D/2)+e)**2-(D/2)**2))+(ʋ))
                    
                else:             
                    Label14.pack()
                    psi=(D/e)
                a=(K/(ρ*(1+(K/E)*psi)))**0.5
                a_Label.config(text=float(a),fg='red',font=("courrier",14))
                
            Label13=tk.Label(frame3, text='Paroi epaisse',fg='#0A1172',padx=10,font=("courrier",14)) 
            Label14=tk.Label(frame3, text='Paroi mince',fg='#0A1172',padx=10,font=("courrier",14))
            #Valeurs prédifinis
            K1=tk.StringVar()
            K1.set(2190000000)
            E1=tk.StringVar()
            E1.set(206000000000)
            ρ1=tk.StringVar()
            ρ1.set(999)
            D1=tk.StringVar()
            D1.set(2)
            e1=tk.StringVar()
            e1.set(0.03)
            ʋ1=tk.StringVar()
            ʋ1.set(0.27)
             #les syntaxes ci dessous sont relatives à l'interface graphique  
            LabelTrois=tk.Label(frame1, text='K [N/m²]',font=("courrier",12))
            LabelTrois.pack()
            K_entry=tk.Entry(frame1,textvariable=K1)
            K_entry.pack()
        
            LabelQuatre=tk.Label(frame1, text='E [N/m²]',padx=10,font=("courrier",12))
            LabelQuatre.pack()    
            E_entry=tk.Entry(frame1,textvariable=E1)
            E_entry.pack()
    
            Label6=tk.Label(frame1, text='ρ [kg/m3]',padx=10,font=("courrier",12))
            Label6.pack()   
            ρ_entry=tk.Entry(frame1,textvariable=ρ1)
            ρ_entry.pack()
            
            Label7=tk.Label(frame1, text='D [m]',padx=10,font=("courrier",12))
            Label7.pack()   
            D_entry=tk.Entry(frame1,textvariable=D1)
            D_entry.pack()
            
            Label8=tk.Label(frame1, text='e [m]',padx=10,font=("courrier",12))
            Label8.pack()   
            e_entry=tk.Entry(frame1,textvariable=e1)
            e_entry.pack()
            
            Label9=tk.Label(frame1, text='ʋ [-]',font=("courrier",12))
            Label9.pack()
            ʋ_entry=tk.Entry(frame1,textvariable=ʋ1)
            ʋ_entry.pack()
            
            bouton10=tk.Button(frame1, text='Calculer',font=("courrier",12),command=resultat)
            bouton10.pack(pady=30,side='left')
            
            bouton11=tk.Button(frame1, text='Réinitialiser',font=("courrier",12),command=supprimer)
            bouton11.pack(side='right')
            
            Label12=tk.Label(frame3, text='a [m/s]',padx=10,font=("courrier",12))
            Label12.pack()
            
            bouton4=tk.Button(top, text='Aide',font=("courrier",12),bg='green',fg='white',command=paramétres)
            bouton4.place(x=0,y=0)
            
            a_Label=tk.Label(frame3)
            a_Label.pack()
            
            frame1.pack()
          #les syntaxes ci dessous sont relatives à l'interface graphique   
        top=tk.Toplevel()#nouvelle fenetre
        top.iconbitmap(r"photos\images.ico")
        top.title("Calculateur de la célérité de l'onde de pression")
        width_value=top.winfo_screenwidth()
        height_value=top.winfo_screenheight()
        top.geometry("%dx%d+0+0" %(width_value, height_value))
        
        frame2=tk.Frame(top)
        frame1=tk.Frame(top)
        frame3=tk.Frame(top)
        
        LabelCinq=tk.Label(frame2, text='Type de fixation de la conduite',padx=10,font=("courrier",16),fg='#0A1172')
        LabelCinq.grid(pady=10,row=0,column=1)
        
        bouton6=tk.Radiobutton(frame2, text='Conduite avec joint de dilatation sur toute sa longueur ',value=1,font=("courrier",14),command=dilatation)
        bouton6.grid(pady=0,row=1,column=1,sticky="W")
        
        bouton5=tk.Radiobutton(frame2, text='Conduite encastrée sur sa partie supérieure',value=2,font=("courrier",14),command=partie)
        bouton5.grid(pady=0,row=2,column=1,sticky="W")
        
        bouton5=tk.Radiobutton(frame2, text='Conduite encastrée sur toute sa longueur',value=3,font=("courrier",14),command=toute)
        bouton5.grid(pady=0,row=3,column=1,sticky="W")
        
        frame2.pack() 
        frame1.pack()
        frame3.pack()
      
    def béton():#Code qui concerne conduite en béton armé
        
        def toute():#le premier systeme de fixation: conduite encastré dans toute sa longeur
            def supprimer():#l'appel de cette fonction supprime les bouton, les labels, les entry pour tout changement de systeme de fixation
                LabelTrois.destroy()
                K_entry.destroy()
                LabelQuatre.destroy()
                E_entry.destroy()
                Label5.destroy()
                ρ_entry.destroy()
                Label6.destroy()
                D_entry.destroy()
                Label7.destroy()
                ec_entry.destroy()
                Label8.destroy()
                ʋ_entry.destroy()
                Label9.destroy()
                ø_entry.destroy()
                Label10.destroy()
                N_entry.destroy()
                bouton11.destroy()
                bouton12.destroy()
                Label13.destroy()
                a_Label.destroy()
            def resultat(): # resultat est une fonction utilisé pour le calcul de la célérité de l'onde de pression
                K = float(K_entry.get())
                D=  float(D_entry.get())
                ec=  float(ec_entry.get())           
                E = float( E_entry.get())
                ρ=float(ρ_entry.get())
                ʋ = float( ʋ_entry.get())
                ø = float(ø_entry.get())
                N =float(N_entry.get())
                
                ls=2*math.pi*((D/2)+(ec/2))/N
                As=N*math.pi*(ø/2)**2
                Er=(22)/(206)
                ee=Er*ec+(As/ls)
    
                if (D/ee)<25:
                    LabelCinq=tk.Label(frame1)
                    LabelCinq.pack()
                    psi=2*(1+ʋ)*(((((D/2)+ee)**2+(D/2)**2)/(((D/2)+ee)**2-(D/2)**2))-((2*ʋ*(D/2)**2)/(((D/2)+ee)**2-(D/2)**2)))
                    
                else:
                    LabelCinq=tk.Label(frame1 )
                    LabelCinq.pack()
                    psi=(D/ee)*(1-ʋ**2)
                a=(K/(ρ*(1+(K/E)*psi)))**0.5
                a_Label.config(text=float(a),fg='red',font=("courrier",14))
            #Valeurs prédifinis    
            K1=tk.StringVar()
            K1.set(2190000000)
            E1=tk.StringVar()
            E1.set(206000000000)
            ρ1=tk.StringVar()
            ρ1.set(999)
            D1=tk.StringVar()
            D1.set(2)
            ec1=tk.StringVar()
            ec1.set(0.1)
            ʋ1=tk.StringVar()
            ʋ1.set(0.125)
            ø1=tk.StringVar()
            ø1.set(0.2)
            N1=tk.StringVar()
            N1.set(6)
             #les syntaxes ci dessous sont relatives à l'interface graphique
            LabelTrois=tk.Label(frame1, text='K [N/m²] ',font=("courrier",12))
            LabelTrois.pack()
            K_entry=tk.Entry(frame1,textvariable=K1)
            K_entry.pack()
        
            LabelQuatre=tk.Label(frame1, text='E [N/m²]',padx=10,font=("courrier",12))
            LabelQuatre.pack()    
            E_entry=tk.Entry(frame1,textvariable=E1)
            E_entry.pack()
    
            Label5=tk.Label(frame1, text='ρ [kg/m3]',padx=10,font=("courrier",12))
            Label5.pack()   
            ρ_entry=tk.Entry(frame1,textvariable=ρ1)
            ρ_entry.pack()
            
            Label6=tk.Label(frame1, text='D [m]',padx=10,font=("courrier",12))
            Label6.pack()   
            D_entry=tk.Entry(frame1,textvariable=D1)
            D_entry.pack()
            
            Label7=tk.Label(frame1, text='ec [m]',padx=10,font=("courrier",12))
            Label7.pack()   
            ec_entry=tk.Entry(frame1,textvariable=ec1)
            ec_entry.pack()
            
            Label8=tk.Label(frame1, text='ʋ [-]',font=("courrier",12))
            Label8.pack()
            ʋ_entry=tk.Entry(frame1,textvariable=ʋ1)
            ʋ_entry.pack()
            
            Label9=tk.Label(frame1, text='ø [m]',font=("courrier",12))
            Label9.pack()
            ø_entry=tk.Entry(frame1,textvariable=ø1)
            ø_entry.pack()
            
            Label10=tk.Label(frame1, text='N',font=("courrier",12))
            Label10.pack()
            N_entry=tk.Entry(frame1,textvariable=N1)
            N_entry.pack()
            
            bouton11=tk.Button(frame1, text='Calculer',font=("courrier",12),command=resultat)
            bouton11.pack(pady=20,side='left')
            
            bouton12=tk.Button(frame1, text='Réinitialiser',font=("courrier",12),command=supprimer)
            bouton12.pack(side='right')
            
            Label13=tk.Label(frame3, text='a [m/s]',padx=10,font=("courrier",12))
            Label13.pack()
            
            bouton4=tk.Button(top, text='Aide',font=("courrier",12),bg='green',fg='white',command=paramétres)
            bouton4.place(x=0,y=0)
            
            a_Label=tk.Label(frame3)
            a_Label.pack()
            
            frame1.pack()
            
        def partie():#le deuxieme systeme de fixation: conduite encastré dans sa partie supérieur
            def supprimer():#l'appel de cette fonction supprime les bouton, les labels, les entry pour tout changement de systeme de fixation
                LabelTrois.destroy()
                K_entry.destroy()
                LabelQuatre.destroy()
                E_entry.destroy()
                Label5.destroy()
                ρ_entry.destroy()
                Label6.destroy()
                D_entry.destroy()
                Label7.destroy()
                ec_entry.destroy()
                Label8.destroy()
                ʋ_entry.destroy()
                Label9.destroy()
                ø_entry.destroy()
                Label10.destroy()
                N_entry.destroy()
                bouton11.destroy()
                bouton12.destroy()
                Label13.destroy()
                a_Label.destroy()
            def resultat(): # resultat est une fonction utilisé pour le calcul de la célérité de l'onde de pression
                K = float(K_entry.get())
                D=  float(D_entry.get())
                ec=  float(ec_entry.get())           
                E = float( E_entry.get())
                ρ=float(ρ_entry.get())
                ʋ = float( ʋ_entry.get())
                ø = float(ø_entry.get())
                N =float(N_entry.get())
                
                
                ls=2*math.pi*((D/2)+(ec/2))/N
                As=N*math.pi*(ø/2)**2
                Er=(22*10**9)/(206*10**9)
                ee=Er*ec+(As/ls)
    
                if (D/ee)<25:
                    LabelCinq=tk.Label(frame1)
                    LabelCinq.pack()
                    psi=2*(((((D/2)+ee)**2+1.5*(D/2)**2)/(((D/2)+ee)**2-(D/2)**2))-((ʋ*((D/2)+ee)**2-3*(D/2)**2)/(((D/2)+ee)**2-(D/2)**2)))
                    
                else:
                    LabelCinq=tk.Label(frame1)
                    LabelCinq.pack()
                    psi=(D/ee)*(1-0.5*ʋ)
                a=(K/(ρ*(1+(K/E)*psi)))**0.5
                a_Label.config(text=float(a),fg='red',font=("courrier",14))
            #Valeurs prédifinis    
            K1=tk.StringVar()
            K1.set(2190000000)
            E1=tk.StringVar()
            E1.set(206000000000)
            ρ1=tk.StringVar()
            ρ1.set(999)
            D1=tk.StringVar()
            D1.set(2)
            ec1=tk.StringVar()
            ec1.set(0.1)
            ʋ1=tk.StringVar()
            ʋ1.set(0.125)
            ø1=tk.StringVar()
            ø1.set(0.2)
            N1=tk.StringVar()
            N1.set(6)
             #les syntaxes ci dessous sont relatives à l'interface graphique   
            LabelTrois=tk.Label(frame1, text='K [N/m²]',font=("courrier",12))
            LabelTrois.pack()
            K_entry=tk.Entry(frame1,textvariable=K1)
            K_entry.pack()
        
            LabelQuatre=tk.Label(frame1, text='E [N/m²]',padx=10,font=("courrier",12))
            LabelQuatre.pack()    
            E_entry=tk.Entry(frame1,textvariable=E1)
            E_entry.pack()
    
            Label5=tk.Label(frame1, text='ρ [kg/m3]',padx=10,font=("courrier",12))
            Label5.pack()   
            ρ_entry=tk.Entry(frame1,textvariable=ρ1)
            ρ_entry.pack()
            
            Label6=tk.Label(frame1, text='D [m]',padx=10,font=("courrier",12))
            Label6.pack()   
            D_entry=tk.Entry(frame1,textvariable=D1)
            D_entry.pack()
            
            Label7=tk.Label(frame1, text='ec [m]',padx=10,font=("courrier",12))
            Label7.pack()   
            ec_entry=tk.Entry(frame1,textvariable=ec1)
            ec_entry.pack()
            
            Label8=tk.Label(frame1, text='ʋ [-]',font=("courrier",14))
            Label8.pack()
            ʋ_entry=tk.Entry(frame1,textvariable=ʋ1)
            ʋ_entry.pack()
            
            Label9=tk.Label(frame1, text='ø [m]',font=("courrier",12))
            Label9.pack()
            ø_entry=tk.Entry(frame1,textvariable=ø1)
            ø_entry.pack()
            
            Label10=tk.Label(frame1, text='N',font=("courrier",12))
            Label10.pack()
            N_entry=tk.Entry(frame1,textvariable=N1)
            N_entry.pack()
            
            bouton11=tk.Button(frame1, text='Calculer',font=("courrier",12),command=resultat)
            bouton11.pack(pady=20,side='left')
            
            bouton12=tk.Button(frame1, text='Réinitialiser',font=("courrier",12),command=supprimer)
            bouton12.pack(side='right')
            
            Label13=tk.Label(frame3, text='a [m/s]',padx=10,font=("courrier",12))
            Label13.pack()
            
            bouton4=tk.Button(top, text='Aide',font=("courrier",12),bg='green',fg='white',command=paramétres)
            bouton4.place(x=0,y=0)
            
            a_Label=tk.Label(frame3)
            a_Label.pack()
            
            frame1.pack()
                   
        def dilatation():#le troisieme systeme de fixation: conduite avec joint de dilataion
            def supprimer():#l'appel de cette fonction supprime les bouton, les labels, les entry pour tout changement de systeme de fixation
                LabelTrois.destroy()
                K_entry.destroy()
                LabelQuatre.destroy()
                E_entry.destroy()
                Label5.destroy()
                ρ_entry.destroy()
                Label6.destroy()
                D_entry.destroy()
                Label7.destroy()
                ec_entry.destroy()
                Label8.destroy()
                ʋ_entry.destroy()
                Label9.destroy()
                ø_entry.destroy()
                Label10.destroy()
                N_entry.destroy()
                bouton11.destroy()
                bouton12.destroy()
                Label13.destroy()
                a_Label.destroy()
                                       
            def resultat(): # resultat est une fonction utilisé pour le calcul de la célérité de l'onde de pression
                K = float(K_entry.get())
                D=  float(D_entry.get())
                ec=  float(ec_entry.get())           
                E = float( E_entry.get())
                ρ=float(ρ_entry.get())
                ʋ = float( ʋ_entry.get())
                ø = float(ø_entry.get())
                N =float(N_entry.get())
                
                ls=(2*math.pi*(D+ec)/2)/N
                As=N*math.pi*(ø/2)**2
                Er=(22*10**9)/(206*10**9)
                ee=Er*ec+(As/ls)
    
                if (D/ee)<25:
                    LabelCinq=tk.Label(frame1)
                    LabelCinq.pack()
                    psi=2*(((((D/2)+ee)**2+(D/2)**2)/(((D/2)+ee)**2-(D/2)**2))+(ʋ))
                    
                else:
                    LabelCinq=tk.Label(frame1)
                    LabelCinq.pack()
                    psi=(D/ee)
                a=(K/(ρ*(1+(K/E)*psi)))**0.5
                a_Label.config(text=float(a),fg='red',font=("courrier",14))
            #Valeurs prédifinis    
            K1=tk.StringVar()
            K1.set(2190000000)
            E1=tk.StringVar()
            E1.set(206000000000)
            ρ1=tk.StringVar()
            ρ1.set(999)
            D1=tk.StringVar()
            D1.set(2)
            ec1=tk.StringVar()
            ec1.set(0.1)
            ʋ1=tk.StringVar()
            ʋ1.set(0.125)
            ø1=tk.StringVar()
            ø1.set(0.2)
            N1=tk.StringVar()
            N1.set(6)
             #les syntaxes ci dessous sont relatives à l'interface graphique
            LabelTrois=tk.Label(frame1, text='K [N/m²] ',font=("courrier",12))
            LabelTrois.pack()
            K_entry=tk.Entry(frame1,textvariable=K1)
            K_entry.pack()
        
            LabelQuatre=tk.Label(frame1, text='E [N/m²]',padx=10,font=("courrier",12))
            LabelQuatre.pack()    
            E_entry=tk.Entry(frame1,textvariable=E1)
            E_entry.pack()
    
            Label5=tk.Label(frame1, text='ρ [kg/m3]',padx=10,font=("courrier",12))
            Label5.pack()   
            ρ_entry=tk.Entry(frame1,textvariable=ρ1)
            ρ_entry.pack()
            
            Label6=tk.Label(frame1, text='D [m]',padx=10,font=("courrier",12))
            Label6.pack()   
            D_entry=tk.Entry(frame1,textvariable=D1)
            D_entry.pack()
            
            Label7=tk.Label(frame1, text='ec [m]',padx=10,font=("courrier",12))
            Label7.pack()   
            ec_entry=tk.Entry(frame1,textvariable=ec1)
            ec_entry.pack()
            
            Label8=tk.Label(frame1, text='ʋ [-]',font=("courrier",12))
            Label8.pack()
            ʋ_entry=tk.Entry(frame1,textvariable=ʋ1)
            ʋ_entry.pack()
            
            Label9=tk.Label(frame1, text='ø [m]',font=("courrier",12))
            Label9.pack()
            ø_entry=tk.Entry(frame1,textvariable=ø1)
            ø_entry.pack()
            
            Label10=tk.Label(frame1, text='N',font=("courrier",12))
            Label10.pack()
            N_entry=tk.Entry(frame1,textvariable=N1)
            N_entry.pack()
            
            bouton11=tk.Button(frame1, text='Calculer',font=("courrier",12),command=resultat)
            bouton11.pack(pady=20,side='left')
            
            bouton12=tk.Button(frame1, text='Réinitialiser',font=("courrier",12),command=supprimer)
            bouton12.pack(side='right')
            
            Label13=tk.Label(frame3, text='a [m/s]',padx=10,font=("courrier",12))
            Label13.pack()
            
            bouton4=tk.Button(top, text='Aide',font=("courrier",12),bg='green',fg='white',command=paramétres)
            bouton4.place(x=0,y=0)
            
            a_Label=tk.Label(frame3)
            a_Label.pack()
            
            frame1.pack()
                             
        top=tk.Toplevel()#nouvelle fenetre
        top.geometry("600x600")
        top.iconbitmap(r"photos\images.ico")
        top.title("Calculateur de la célérité de l'onde de pression")
        width_value=top.winfo_screenwidth()
        height_value=top.winfo_screenheight()
        top.geometry("%dx%d+0+0" %(width_value, height_value))
               
        frame2=tk.Frame(top)
        frame1=tk.Frame(top)
        frame3=tk.Frame(top)
        
        LabelCinq=tk.Label(frame2, text='Type de fixation de la conduite',padx=10,font=("courrier",16),fg='#0A1172')
        LabelCinq.grid(pady=10,row=0,column=1)
        
        bouton6=tk.Radiobutton(frame2, text='Conduite avec joint de dilatation sur toute sa longueur ',value=1,font=("courrier",14),command=dilatation)
        bouton6.grid(pady=0,row=1,column=1,sticky="W")
        
        bouton5=tk.Radiobutton(frame2, text='Conduite encastrée sur sa partie supérieure',value=2,font=("courrier",14),command=partie)
        bouton5.grid(pady=0,row=2,column=1,sticky="W")
        
        bouton5=tk.Radiobutton(frame2, text='Conduite encastrée sur toute sa longueur',value=3,font=("courrier",14),command=toute)
        bouton5.grid(pady=0,row=3,column=1,sticky="W")
              
        frame2.pack() 
        frame1.pack()
        frame3.pack()
        
        frame1.pack()
     #les syntaxes ci dessous sont relatives à l'interface graphique         
    fen = tk.Tk() # fenetre principale du calculateur de célérité de l'onde de pression
    fen.title("Calculateur de la célérité de l'onde de pression")
    fen.geometry("400x500")
    fen.maxsize(400,500)
    fen.iconbitmap(r"photos\images.ico")  
    
    frame=tk.Frame(fen)
    
    labelUn=tk.Label(fen, text="Ecole Nationale Polytechnique",font=("courrier",18))
    labelUn.pack(pady=20)
    
    labelUn=tk.Label(fen, text="Veuillez choisir le type de conduite:",fg='#0A1172',font=("courrier",16))
    labelUn.pack()
    
    bouton2=tk.Button(frame, text='Conduite en béton armé',font=("courrier",14),command=béton)
    bouton2.pack(pady=10)
    
    bouton4=tk.Button(frame, text='     Conduite élastique    ',font=("courrier",14),command=autre)
    bouton4.pack(pady=10)
    
    bouton1=tk.Button(frame, text='      Tunnel en roche    ',padx=10,font=("courrier",14),command=tunnel)
    bouton1.pack(pady=10)
        
    bouton3=tk.Button(frame, text='        Conduite rigide       ',font=("courrier",14),command=Rigide)
    bouton3.pack(pady=10)
           
    labelUn=tk.Label(fen, text="                                                                                  ENP 2019",font=("courrier",10),fg='green')
    labelUn.pack(side='bottom')
    
    frame.pack(expand=tk.YES)
# %% le systeme simple (reservoir conduite vanne) [line 1030 to 1190 ]
def no_protection_type1():
    """ create widgets """
    top=tk.Toplevel()
    top.state('zoomed')
    top.iconbitmap(r'photos\images.ico')
    top.title("Réservoir-conduite-vanne")
    tab=ttk.Notebook(top)

    #button       
    project_B=tk.Button(top,text='Paramètres d’entrée' ,bg='#20A9CE',
                    fg='white',bd=0,font=('Arial',20,'bold'),height=1, width =25) 
    project_B.place(x=400,y=10) 
    
#page1
    page1 =ttk.Frame(tab,width=1330,height=540)
    tab.add(page1,text='Réservoir')
    ##canvas
    canvas1= tk.Canvas(page1,width=1330, height=540,bg='white')
    #entry
    Hresin=tk.StringVar()
    Hresin.set(100)# les valeurs prédéfinies 
    Hres_entry=tk.Entry(page1,textvariable=Hresin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas1.create_window(100, 140,window= Hres_entry)
    
    kin=tk.StringVar()
    kin.set(0.5)# les valeurs prédéfinies 
    k_entry=tk.Entry(page1,textvariable=kin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas1.create_window(100, 200,window=k_entry)

    #text
    canvas1.create_text(330,140, text="- Niveau d’eau dans le réservoir: Hres [m]",fill='black',font=('Arial',12))
    canvas1.create_text(350,200, text='- Coefficient de perte de charge singulière: k[-]',fill='black',font=('Arial',12))
    #images
    inforeservoir_im=Image.open(r'photos\inforeservoir.png')
    inforeservoir_im = ImageTk.PhotoImage(inforeservoir_im.resize((700,300), Image.ANTIALIAS))
    canvas1.create_image(1000, 250, image=inforeservoir_im)
    canvas1.image = inforeservoir_im
#page2    
    page2 =ttk.Frame(tab,width= 1330,height=540)
    tab.add(page2,text='Conduite')
    ##canvas
    canvas2= tk.Canvas(page2,width=1330, height=540,bg='white')
    #images
    pipeinfo_im=Image.open(r'photos\pipeinfo.png')
    pipeinfo_im = ImageTk.PhotoImage(pipeinfo_im.resize((700,500), Image.ANTIALIAS))
    canvas2.create_image(1000, 250, image=pipeinfo_im)
    canvas2.image = pipeinfo_im
    #entry 
    Lin=tk.StringVar()
    Lin.set(1000)# les valeurs prédéfinies 
    L_entry=tk.Entry(page2,textvariable=Lin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas2.create_window(100, 100,window= L_entry)
    
    Din=tk.StringVar()
    Din.set(1)# les valeurs prédéfinies 
    D_entry=tk.Entry(page2,textvariable=Din,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas2.create_window(100, 150,window= D_entry)
    
         
    ain=tk.StringVar()
    ain.set(1000)# les valeurs prédéfinies 
    a_entry=tk.Entry(page2,textvariable=ain,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas2.create_window(100, 200,window= a_entry)
    
    
    fin=tk.StringVar()
    fin.set(0.04)# les valeurs prédéfinies 
    f_entry=tk.Entry(page2,textvariable=fin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas2.create_window(100, 250,window= f_entry)
    
    
    nin=tk.StringVar()
    nin.set(5)# les valeurs prédéfinies 
    n_entry=tk.Entry(page2,textvariable=nin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas2.create_window(100, 300,window= n_entry)
    
    
    Z0in=tk.StringVar()
    Z0in.set(20)# les valeurs prédéfinies 
    Z0_entry=tk.Entry(page2,textvariable=Z0in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas2.create_window(100, 350,window= Z0_entry)
    
           
    Z1in=tk.StringVar()
    Z1in.set(10)# les valeurs prédéfinies 
    Z1_entry=tk.Entry(page2,textvariable=Z1in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas2.create_window(100, 400,window= Z1_entry)
    
    #text
    canvas2.create_text(303,100, text="- Longueur de la conduite: L [m]",fill='black',font=('Arial',12))
    canvas2.create_text(305,150, text='- Diamètre de la conduite: D [m]',fill='black',font=('Arial',12))
    canvas2.create_text(330,200, text='- Célérité de l’onde de pression: a [m/s]',fill='black',font=('Arial',12))
    canvas2.create_text(370,250, text='- Coefficient de frottement de Darcy_Weisbach: f [-]',fill='black',font=('Arial',12))
    canvas2.create_text(380,300, text='- Discrétisation de la conduite: nombre de ségments n',fill='black',font=('Arial',12))
    canvas2.create_text(373,350, text='- Elevation de l’extrimité amont de la conduite: Z0[m]',fill='black',font=('Arial',12))
    canvas2.create_text(365,400, text='- Elevation de l’extrimité aval de la conduite: Z1[m]',fill='black',font=('Arial',12))
    #button  
    wave_calculator_B=tk.Button(page2,text='Calculateur\n de Célérité de l’onde',command=wave_calculator_window,
                                font=('Arial',10,'bold'),bg='green',fg='white',bd=2)
    canvas2.create_window(580 ,200,window=wave_calculator_B)                  
#page3    
    page3=ttk.Frame(tab,width= 1330,height=540)    
    tab.add(page3,text='Vanne')
    ##canvas
    canvas3= tk.Canvas(page3,width=1330, height=540,bg='white')
    ##image
    infovanne_im=Image.open(r'photos\infovanne.png')
    infovanne_im = ImageTk.PhotoImage(infovanne_im.resize((500,300), Image.ANTIALIAS))
    canvas3.create_image(900, 150, image=infovanne_im)
    canvas3.image = infovanne_im
    #entry 
    Q0in=tk.StringVar()
    Q0in.set(0.75)# les valeurs prédéfinies 
    Q0_entry=tk.Entry(page3,textvariable=Q0in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas3.create_window(100, 190,window= Q0_entry)
      
    tfin=tk.StringVar()
    tfin.set(0)# les valeurs prédéfinies 
    tf_entry=tk.Entry(page3,textvariable=tfin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas3.create_window(100, 240,window= tf_entry)
    
    #text
    canvas3.create_text(315,190, text="- Débit initial d’écoulement: Q0 [m3/s]",fill='black',font=('Arial',12))
    canvas3.create_text(320,240, text="- Temps de fermeture de la vanne: tf [s]",fill='black',font=('Arial',12))  
#page4    
    page4=ttk.Frame(tab,width= 1330,height=570)    
    tab.add(page4,text='Exécuter')
    ##canvas
    canvas4= tk.Canvas(page4,width=1330, height=570,bg='white')
    ##frame
    graph_frame=tk.Frame(page4)
    canvas4.create_window(850,270,window=graph_frame)  
    #entry     
    Tin=tk.StringVar()
    Tin.set(50)# les valeurs prédéfinies 
    T_entry=tk.Entry(page4,textvariable=Tin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas4.create_window(80,50,window= T_entry)
        
    xin=tk.StringVar()
    xin.set(0)# les valeurs prédéfinies 
    x_entry=tk.Entry(page4,textvariable=xin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas4.create_window(80,110,window= x_entry)    
    #text
    canvas4.create_text(85,25, text="- Temps de simulation:T [s]",fill='black',font=('Arial',10))
    canvas4.create_text(120,80, text="- Point spatial à partir du réservoir: x [m]",fill='black',font=('Arial',10))
    #button         
    exécuter_B=tk.Button(page4,width=10,text='Exécuter',font=('Arial',12,'bold'),bg='#2AA321',fg='white',bd=2,
command=lambda:algo1.display_result(page4,canvas4,graph_frame,Hres_entry,k_entry,L_entry,D_entry,a_entry,f_entry,n_entry,Z0_entry,Z1_entry,Q0_entry,tf_entry,T_entry,x_entry).get_tk_widget().grid(column=1, row=1))
    canvas4.create_window(80,160,window=exécuter_B)  
    
    enregistrer_B=tk.Button(page4,width=10,text='Enregistrer',font=('Arial',12,'bold'),bg='blue',fg='white',bd=2,
command=lambda:algo1.save(Hres_entry,k_entry,L_entry,D_entry,a_entry,f_entry,n_entry,Z0_entry,Z1_entry,Q0_entry,tf_entry,T_entry,x_entry))
    canvas4.create_window(80 ,210,window=enregistrer_B)  

    """ activate widgets"""     
    canvas1.place(x=0,y=0) 
    canvas2.place(x=0,y=0)
    canvas3.place(x=0,y=0)
    canvas4.place(x=0,y=0)
    tab.place(x=15,y=60)
# %% le systeme simple (reservoir conduite en serie vanne)  [line 1191 to 1382 ]
def no_protection_type2():
    """ create widgets """
    top=tk.Toplevel()
    top.state('zoomed')
    top.iconbitmap(r'photos\images.ico')
    top.title("Réservoir-conduite en serie-vanne")
    tab=ttk.Notebook(top)
    #button       
    project_B=tk.Button(top,text='Paramètres d’entrée' ,bg='#20A9CE',
                    fg='white',bd=0,font=('Arial',20,'bold'),height=1, width =25) 
    project_B.place(x=400,y=10)     
#page1
    page1 =ttk.Frame(tab,width=1330,height=540)
    tab.add(page1,text='Reservoir')
    ##canvas
    canvas1= tk.Canvas(page1,width=1330, height=540,bg='white')
    #entry
    Hresin=tk.StringVar()
    Hresin.set(100)# les valeurs prédéfinies 
    Hres_entry=tk.Entry(page1,textvariable=Hresin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas1.create_window(100, 140,window= Hres_entry)
    
    kin=tk.StringVar()
    kin.set(0.5)# les valeurs prédéfinies 
    k_entry=tk.Entry(page1,textvariable=kin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas1.create_window(100, 200,window=k_entry)

    #text
    canvas1.create_text(328,140, text="- Niveau d’eau dans le réservoir: Hres [m]",fill='black',font=('Arial',12))
    canvas1.create_text(347,200, text='- Coefficient de perte de charge singulière: k[-]',fill='black',font=('Arial',12))
    #images
    inforeservoir_im=Image.open(r'photos\inforeservoir.png')
    inforeservoir_im = ImageTk.PhotoImage(inforeservoir_im.resize((700,300), Image.ANTIALIAS))
    canvas1.create_image(1000, 250, image=inforeservoir_im)
    canvas1.image = inforeservoir_im
#page2    
    page2 =ttk.Frame(tab,width= 1330,height=600)
    tab.add(page2,text='Conduite')
    ##canvas
    canvas2= tk.Canvas(page2,width=1330, height=600,bg='white')
    #frame
    pipe_frame=tk.Frame(canvas2,bg='white')
    canvas2.create_window((8,225),window= pipe_frame,anchor='nw')
    #images
    jonctionpipeinfo_im=Image.open(r'photos\jonctionpipeinfo.png')
    jonctionpipeinfo_im = ImageTk.PhotoImage(jonctionpipeinfo_im.resize((700,500), Image.ANTIALIAS))
    canvas2.create_image(1000, 270, image=jonctionpipeinfo_im)
    canvas2.image = jonctionpipeinfo_im
    #entry 
    nin=tk.StringVar()
    nin.set(2)# les valeurs prédéfinies 
    n_entry=tk.Entry(page2,textvariable=nin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas2.create_window(100, 100,window= n_entry)
    
    fin=tk.StringVar()
    fin.set(0.04)# les valeurs prédéfinies 
    f_entry=tk.Entry(page2,textvariable=fin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas2.create_window(100, 150,window= f_entry)
    
    ncin=tk.StringVar()
    ncin.set('')# les valeurs prédéfinies 
    nc_entry=tk.Entry(page2,textvariable=ncin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas2.create_window(100,200,window= nc_entry)
    
    def pipe(): # conduite est une fonction pour afficher et saisir les caractristiques("D,L,a") de chaque conduite  
        for child in pipe_frame.winfo_children():
            child.destroy()
        nc=int(nc_entry.get())
        # les syntaxes ci dessous sont relatives à l'interface graphique
        mbd=tk.Menubutton (pipe_frame,text='           D[m]         ',font=('Arial',11,'bold'),relief='groove',bg='white')
        mbd.menu=tk.Menu(mbd)
        mbd["menu"]=mbd.menu
        mbd.menu.add_command(label="Diamètre de la conduite")
        mbd.grid(row=14,column=1,sticky="nsew")
        
        mba=tk.Menubutton (pipe_frame,text='          a[m/s]        ',font=('Arial',11,'bold'),relief='groove',bg='#75E25A')
        mba.menu=tk.Menu(mba)
        mba["menu"]=mba.menu
        mba.menu.add_command(label="Célérité de l’onde de pression")
        mba.menu.add_command(label="Exécuter",command=wave_calculator_window)
        mba.grid(row=14,column=2,sticky="W")
        
        mbL=tk.Menubutton (pipe_frame,text='           L[m]          ',font=('Arial',11,'bold'),relief='groove',bg='white')
        mbL.menu=tk.Menu(mbL)
        mbL["menu"]=mbL.menu
        mbL.menu.add_command(label="Longueur de la conduite")
        mbL.grid(row=14,column=3,sticky="W")
        
        mbZ=tk.Menubutton (pipe_frame,text='           Z[m]         ',font=('Arial',11,'bold'),relief='groove',bg='white')
        mbZ.menu=tk.Menu(mbZ)
        mbZ["menu"]=mbZ.menu
        mbZ.menu.add_command(label="Elévation de noued par rapport au Datum")
        mbZ.grid(row=14,column=4,sticky="W")
        global d1
        global a1
        global l1
        global Z1   
        d1=[]
        a1=[]
        l1=[]
        Z1=[]
        #input d:diamètre des conduites ,a:célérite d'onde de pression des conduites , l: longueur des conduites 
        for i in range(0,nc):
                d_entry=tk.Entry(pipe_frame,bg='#C4CCCE')
                d_entry.grid(row=16+i,column=1)
                d1.append(d_entry)
                a_entry=tk.Entry(pipe_frame,bg='#C4CCCE')
                a_entry.grid(row=16+i,column=2)
                a1.append(a_entry)
                l_entry=tk.Entry(pipe_frame,bg='#C4CCCE')
                l_entry.grid(row=16+i,column=3)
                l1.append(l_entry)
        #input les elevations d'extrimité de chaque conduite 
        for i in range(0,nc+1):    
                Z_entry=tk.Entry(pipe_frame,bg='#C4CCCE')
                Z_entry.grid(row=16+i,column=4)
                Z1.append(Z_entry)

    #text
    canvas2.create_text(391,100, text='- Discrétisation de la 1ere  conduite: nombre de ségments n',fill='black',font=('Arial',12))
    canvas2.create_text(365,150, text='- Coefficient de frottement de Darcy_Weisbach: f [-]',fill='black',font=('Arial',12))
    canvas2.create_text(288,200, text='- Nombre de conduites: nc [-]',fill='black',font=('Arial',12))
    #button
    entrer_B=tk.Button(page2,text='Entrer',command=pipe,font=('Arial',10,'bold'),bg='red',fg='white',bd=2,width=20)
    canvas2.create_window(540 ,200,window=entrer_B)              
#page3    
    page3=ttk.Frame(tab,width= 1330,height=540)    
    tab.add(page3,text='Vanne')
    ##canvas
    canvas3= tk.Canvas(page3,width=1330, height=540,bg='white')
    ##image
    infovanne_im=Image.open(r'photos\infovanne.png')
    infovanne_im = ImageTk.PhotoImage(infovanne_im.resize((500,300), Image.ANTIALIAS))
    canvas3.create_image(900, 150, image=infovanne_im)
    canvas3.image = infovanne_im
    #entry 
    Q0in=tk.StringVar()
    Q0in.set(0.75)# les valeurs prédéfinies 
    Q0_entry=tk.Entry(page3,textvariable=Q0in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas3.create_window(100, 190,window= Q0_entry)
      
    tfin=tk.StringVar()
    tfin.set(0)# les valeurs prédéfinies 
    tf_entry=tk.Entry(page3,textvariable=tfin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas3.create_window(100, 240,window= tf_entry)
    
    #text
    canvas3.create_text(315,190, text="- Débit initial d’écoulement: Q0 [m3/s]",fill='black',font=('Arial',12))
    canvas3.create_text(320,240, text="- Temps de fermeture de la vanne: tf [s]",fill='black',font=('Arial',12))  
#page4    
    page4=ttk.Frame(tab,width= 1330,height=540)    
    tab.add(page4,text='Exécuter')
    ##canvas
    canvas4= tk.Canvas(page4,width=1330, height=540,bg='white')
    ##frame
    graph_frame=tk.Frame(page4)
    canvas4.create_window(850,270,window=graph_frame)  
    #entry     
    Tin=tk.StringVar()
    Tin.set(50)# les valeurs prédéfinies 
    T_entry=tk.Entry(page4,textvariable=Tin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas4.create_window(80,50,window= T_entry)
        
    xin=tk.StringVar()
    xin.set(0)# les valeurs prédéfinies 
    x_entry=tk.Entry(page4,textvariable=xin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas4.create_window(80,110,window= x_entry) 
    
    cin=tk.StringVar()
    cin.set(1)# les valeurs prédéfinies 
    c_entry=tk.Entry(page4,textvariable=cin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas4.create_window(80,170,window= c_entry)   
    #text
    canvas4.create_text(85,25, text="- Temps de simulation:T [s]",fill='black',font=('Arial',10))
    canvas4.create_text(120,80, text="- Point spatial à partir du réservoir: x [m]",fill='black',font=('Arial',10))
    canvas4.create_text(118,140, text="- Le point x se trouve dans la conduite \n N°=:",fill='black',font=('Arial',10))
    #button     
    exécuter_B=tk.Button(page4,width=10,text='Exécuter',font=('Arial',12,'bold'),bg='#2AA321',fg='white',bd=2,
command=lambda:algo4.display_result(page4,canvas4, graph_frame,Hres_entry,k_entry,n_entry,nc_entry,f_entry,l1,d1,a1,Z1,Q0_entry,tf_entry,T_entry,x_entry,c_entry).get_tk_widget().grid(row=1,column=1))
    canvas4.create_window(80,210,window=exécuter_B)  
    
    enregistrer_B=tk.Button(page4,width=10,text='Enregistrer',font=('Arial',12,'bold'),bg='blue',fg='white',bd=2,
command=lambda:algo4.save(Hres_entry,k_entry,n_entry,nc_entry,f_entry,l1,d1,a1,Z1,Q0_entry,tf_entry,T_entry,x_entry,c_entry))
    canvas4.create_window(80 ,260,window=enregistrer_B)  

    """ activate widgets"""     
    canvas1.place(x=0,y=0) 
    canvas2.place(x=0,y=0)
    canvas3.place(x=0,y=0)
    canvas4.place(x=0,y=0)
    tab.place(x=15,y=60)
# %% le systeme simple (reservoir-conduite en parallèle-vanne) [line 1383 to 1572]
def no_protection_type3():
    """ create widgets """
    top=tk.Toplevel()
    top.state('zoomed')
    top.iconbitmap(r'photos\images.ico')
    top.title("Réservoir-conduite en parallèle-vanne")
    tab=ttk.Notebook(top)

    #button       
    project_B=tk.Button(top,text='Paramètres d’entrée' ,bg='#20A9CE',
                    fg='white',bd=0,font=('Arial',20,'bold'),height=1, width =25) 
    project_B.place(x=400,y=10)   
#page1
    page1 =ttk.Frame(tab,width=1330,height=540)
    tab.add(page1,text='Reservoir')
    ##canvas
    canvas1= tk.Canvas(page1,width=1330, height=540,bg='white')
    #entry
    Hresin=tk.StringVar()
    Hresin.set(100)# les valeurs prédéfinies 
    Hres_entry=tk.Entry(page1,textvariable=Hresin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas1.create_window(100, 140,window= Hres_entry)
    
    kin=tk.StringVar()
    kin.set(0.5)# les valeurs prédéfinies 
    k_entry=tk.Entry(page1,textvariable=kin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas1.create_window(100, 200,window=k_entry)

    #text
    canvas1.create_text(330,140, text="- Niveau d’eau dans le réservoir: Hres [m]",fill='black',font=('Arial',12))
    canvas1.create_text(350,200, text='- Coefficient de perte de charge singulière: k[-]',fill='black',font=('Arial',12))
    #images
    inforeservoir_im=Image.open(r'photos\inforeservoir.png')
    inforeservoir_im = ImageTk.PhotoImage(inforeservoir_im.resize((700,300), Image.ANTIALIAS))
    canvas1.create_image(1000, 250, image=inforeservoir_im)
    canvas1.image = inforeservoir_im
#page2    
    page2 =ttk.Frame(tab,width= 1330,height=600)
    tab.add(page2,text='Conduite et Vanne')
    ##canvas
    canvas2= tk.Canvas(page2,width=1330, height=600,bg='white')
    #frame
    pipe_frame=tk.Frame(canvas2,bg='white')
    canvas2.create_window((10,290),window= pipe_frame,anchor='nw')
    #images
    branchpipeinfo_im=Image.open(r'photos\branchpipeinfo.png')
    branchpipeinfo_im = ImageTk.PhotoImage(branchpipeinfo_im.resize((700,500), Image.ANTIALIAS))
    canvas2.create_image(1000, 270, image=branchpipeinfo_im)
    canvas2.image = branchpipeinfo_im
    #entry
    Q0in=tk.StringVar()
    Q0in.set(0.75)# les valeurs prédéfinies 
    Q0_entry=tk.Entry(page2,textvariable=Q0in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas2.create_window(100, 100,window= Q0_entry)
    
    nin=tk.StringVar()
    nin.set(2)# les valeurs prédéfinies 
    n_entry=tk.Entry(page2,textvariable=nin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas2.create_window(100, 150,window= n_entry)
    
    fin=tk.StringVar()
    fin.set(0.04)# les valeurs prédéfinies 
    f_entry=tk.Entry(page2,textvariable=fin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas2.create_window(100, 200,window= f_entry)    
    
    ncin=tk.StringVar()
    ncin.set('')# les valeurs prédéfinies 
    nc_entry=tk.Entry(page2,textvariable=ncin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=15)
    canvas2.create_window(100,250,window= nc_entry)
    
    def pipe(): # conduite est une fonction pour afficher et saisir les caractristiques("D,L,a") de chaque conduite  
        for child in pipe_frame.winfo_children():
            child.destroy()
        nc=int(nc_entry.get())
        # les syntaxes ci dessous sont relatives à l'interface graphique
        
        mbd=tk.Menubutton (pipe_frame,text='           D[m]         ',font=('Arial',10,'bold'),relief='groove',bg='white',width=15)
        mbd.menu=tk.Menu(mbd)
        mbd["menu"]=mbd.menu
        mbd.menu.add_command(label="Diamètre de la conduite")
        mbd.menu.add_command(label="Premiere ligne pour la conduite principale")
        mbd.grid(row=15,column=1,sticky="W")
        
        mbL=tk.Menubutton (pipe_frame,text='           L[m]          ',font=('Arial',10,'bold'),relief='groove',bg='white',width=15)
        mbL.menu=tk.Menu(mbL)
        mbL["menu"]=mbL.menu
        mbL.menu.add_command(label="Longueur de la conduite")
        mbL.menu.add_command(label="Premiere ligne pour la conduite principale")
        mbL.grid(row=15,column=3,sticky="W")
        
        mbZ=tk.Menubutton (pipe_frame,text='           Z[m]         ',font=('Arial',10,'bold'),relief='groove',bg='white',width=15)
        mbZ.menu=tk.Menu(mbZ)
        mbZ["menu"]=mbZ.menu
        mbZ.menu.add_command(label='Elévation de noued par rapport au Datum' )
        mbZ.menu.add_command(label="Premiere ligne pour la conduite principale")
        mbZ.grid(row=15,column=4,sticky="W")
        
        mbtf=tk.Menubutton (pipe_frame,text='             tf[s]          ',font=('Arial',10,'bold'),relief='groove',bg='white',width=15)
        mbtf.menu=tk.Menu(mbtf)
        mbtf["menu"]=mbtf.menu
        mbtf.menu.add_command(label="Temps de fermeture de la vanne")
        mbtf.grid(row=15,column=5,sticky="W")
        
        mba=tk.Menubutton (pipe_frame,text='          a[m/s]        ',font=('Arial',10,'bold'),relief='groove',bg='#75E25A',width=15)
        mba.menu=tk.Menu(mba)
        mba["menu"]=mba.menu
        mba.menu.add_command(label="Célérité de l’onde de pression")
        mba.menu.add_command(label="Exécuter",command=wave_calculator_window)
        mba.grid(row=15,column=2,sticky="W")
        global d1
        global a1
        global l1
        global Z1
        global tf1          
        d1=[]
        a1=[]
        l1=[]
        Z1=[]
        tf1=[]
        #input d:diamètre des conduites ,a:célérite d'onde de pression des conduites , l: longueur des conduites
        for i in range(0,nc+1):
                d_entry=tk.Entry(pipe_frame,bg='#C4CCCE',width=20)
                d_entry.grid(row=16+i,column=1)
                d1.append(d_entry)
                a_entry=tk.Entry(pipe_frame,bg='#C4CCCE',width=20)
                a_entry.grid(row=16+i,column=2)
                a1.append(a_entry)
                l_entry=tk.Entry(pipe_frame,bg='#C4CCCE',width=20)
                l_entry.grid(row=16+i,column=3)
                l1.append(l_entry)
        for i in range(0,nc+2):    
                Z_entry=tk.Entry(pipe_frame,bg='#C4CCCE',width=20)
                Z_entry.grid(row=16+i,column=4)
                Z1.append(Z_entry)
        for i in range(0,nc):    
                tf_entry=tk.Entry(pipe_frame,bg='#C4CCCE',width=20)
                tf_entry.grid(row=17+i,column=5)
                tf1.append(tf_entry)

    
    #text
    canvas2.create_text(315,100, text="- Débit initial d’écoulement: Q0 [m3/s]",fill='black',font=('Arial',12))
    canvas2.create_text(393,150, text='- Discrétisation de la 1ere  conduite: nombre de ségments n',fill='black',font=('Arial',12))
    canvas2.create_text(362,200, text='- Coefficient de frottement de Darcy_Weisbach: f [-]',fill='black',font=('Arial',12))
    canvas2.create_text(385,250, text='- Nombre de conduites liées à la conduite principale: nc [-]',fill='black',font=('Arial',12))
    #button
    entrer_B=tk.Button(page2,text='Entrer',command=pipe,font=('Arial',10,'bold'),bg='red',fg='white',bd=2,width=10)
    canvas2.create_window(590 ,275,window=entrer_B)      
#page3    
    page3=ttk.Frame(tab,width= 1330,height=540)    
    tab.add(page3,text='Exécuter')
    ##canvas
    canvas3= tk.Canvas(page3,width=1330, height=540,bg='white')
    ##frame
    graph_frame=tk.Frame(page3)
    canvas3.create_window(850,270,window=graph_frame)  
    #entry     
    Tin=tk.StringVar()
    Tin.set(50)# les valeurs prédéfinies 
    T_entry=tk.Entry(page3,textvariable=Tin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas3.create_window(80,50,window= T_entry)
        
    xin=tk.StringVar()
    xin.set(0)# les valeurs prédéfinies 
    x_entry=tk.Entry(page3,textvariable=xin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas3.create_window(80,110,window= x_entry) 
    
    cin=tk.StringVar()
    cin.set(1)# les valeurs prédéfinies 
    c_entry=tk.Entry(page3,textvariable=cin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas3.create_window(80,170,window= c_entry)   
    #text
    canvas3.create_text(85,25, text="- Temps de simulation:T [s]",fill='black',font=('Arial',10))
    canvas3.create_text(120,80, text="- Point spatial à partir du réservoir: x [m]",fill='black',font=('Arial',10))
    canvas3.create_text(117,140, text="- Le point x se trouve dans la conduite \n N°=:",fill='black',font=('Arial',10))
    #button       
    exécuter_B=tk.Button(page3,width=10,text='Exécuter',font=('Arial',12,'bold'),bg='#2AA321',fg='white',bd=2,
command=lambda:algo7.display_result(page3,canvas3,graph_frame,Hres_entry,k_entry,Q0_entry,n_entry,f_entry,nc_entry,l1,d1,a1,Z1,tf1,c_entry,T_entry,x_entry).grid(row=1,column=1))
    canvas3.create_window(80,210,window=exécuter_B)  
    
    enregistrer_B=tk.Button(page3,width=10,text='Enregistrer',font=('Arial',12,'bold'),bg='blue',fg='white',bd=2,
command=lambda:algo7.save(Hres_entry,k_entry,Q0_entry,n_entry,f_entry,nc_entry,l1,d1,a1,Z1,tf1,c_entry,T_entry,x_entry))
    canvas3.create_window(80 ,260,window=enregistrer_B)  

    """ activate widgets"""     
    canvas1.place(x=0,y=0) 
    canvas2.place(x=0,y=0)
    canvas3.place(x=0,y=0)
    tab.place(x=15,y=60)
# %% le systeme simple (reservoir conduite vanne)+chemine d'equilibre [line 1573 to 1748]
def surgetank_type1():
    """ create widgets """
    top=tk.Toplevel()
    top.state('zoomed')
    top.iconbitmap(r'photos\images.ico')
    top.title("Réservoir-conduite-vanne avec protection (cheminée d'équilibre) ")
    tab=ttk.Notebook(top)

    #button       
    project_B=tk.Button(top,text='Paramètres d’entrée' ,bg='#20A9CE',
                    fg='white',bd=0,font=('Arial',20,'bold'),height=1, width =25) 
    project_B.place(x=400,y=10)     
#page1
    page1 =ttk.Frame(tab,width=1330,height=540)
    tab.add(page1,text='Reservoir')
    ##canvas
    canvas1= tk.Canvas(page1,width=1330, height=540,bg='white')
    #entry
    Hresin=tk.StringVar()
    Hresin.set(100)# les valeurs prédéfinies 
    Hres_entry=tk.Entry(page1,textvariable=Hresin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10)
    canvas1.create_window(70, 140,window= Hres_entry)
    
    kin=tk.StringVar()
    kin.set(0.5)# les valeurs prédéfinies 
    k_entry=tk.Entry(page1,textvariable=kin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10)
    canvas1.create_window(70, 200,window=k_entry)
    #text
    canvas1.create_text(273,140, text="- Niveau d’eau dans le réservoir: Hres [m]",fill='black',font=('Arial',12))
    canvas1.create_text(290,200, text='- Coefficient de perte de charge singulière: k[-]',fill='black',font=('Arial',12))
    #images
    inforeservoir_im=Image.open(r'photos\inforeservoir.png')
    inforeservoir_im = ImageTk.PhotoImage(inforeservoir_im.resize((700,300), Image.ANTIALIAS))
    canvas1.create_image(1000, 250, image=inforeservoir_im)
    canvas1.image = inforeservoir_im
#page2    
    page2 =ttk.Frame(tab,width= 1330,height=540)
    tab.add(page2,text='Conduite')
    ##canvas
    canvas2= tk.Canvas(page2,width=1330, height=540,bg='white')
    #images
    pipeinfo_im=Image.open(r'photos\pipeinfo.png')
    pipeinfo_im = ImageTk.PhotoImage(pipeinfo_im.resize((700,500), Image.ANTIALIAS))
    canvas2.create_image(1000, 250, image=pipeinfo_im)
    canvas2.image = pipeinfo_im
    #entry 
    Lin=tk.StringVar()
    Lin.set(1000)# les valeurs prédéfinies 
    L_entry=tk.Entry(page2,textvariable=Lin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10)
    canvas2.create_window(70, 100,window= L_entry)
    
    Din=tk.StringVar()
    Din.set(1)# les valeurs prédéfinies 
    D_entry=tk.Entry(page2,textvariable=Din,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10)
    canvas2.create_window(70, 150,window= D_entry)
             
    ain=tk.StringVar()
    ain.set(1000)# les valeurs prédéfinies 
    a_entry=tk.Entry(page2,textvariable=ain,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10)
    canvas2.create_window(70, 200,window= a_entry)
        
    fin=tk.StringVar()
    fin.set(0.04)# les valeurs prédéfinies 
    f_entry=tk.Entry(page2,textvariable=fin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10)
    canvas2.create_window(70, 250,window= f_entry)
        
    nin=tk.StringVar()
    nin.set(5)# les valeurs prédéfinies 
    n_entry=tk.Entry(page2,textvariable=nin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10)
    canvas2.create_window(70, 300,window= n_entry)
        
    Z0in=tk.StringVar()
    Z0in.set(20)# les valeurs prédéfinies 
    Z0_entry=tk.Entry(page2,textvariable=Z0in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10)
    canvas2.create_window(70, 350,window= Z0_entry)
               
    Z1in=tk.StringVar()
    Z1in.set(10)# les valeurs prédéfinies 
    Z1_entry=tk.Entry(page2,textvariable=Z1in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10)
    canvas2.create_window(70, 400,window= Z1_entry)    
    #text
    canvas2.create_text(243,100, text="- Longueur de la conduite: L [m]",fill='black',font=('Arial',12))
    canvas2.create_text(245,150, text='- Diamètre de la conduite: D [m]',fill='black',font=('Arial',12))
    canvas2.create_text(270,200, text='- Célérité de l’onde de pression: a [m/s]',fill='black',font=('Arial',12))
    canvas2.create_text(310,250, text='- Coefficient de frottement de Darcy_Weisbach: f [-]',fill='black',font=('Arial',12))
    canvas2.create_text(320,300, text='- Discrétisation de la conduite: nombre de ségments n',fill='black',font=('Arial',12))
    canvas2.create_text(315,350, text='- Elevation de l’extrimité amont de la conduite: Z0[m]',fill='black',font=('Arial',12))
    canvas2.create_text(307,400, text='- Elevation de l’extrimité aval de la conduite: Z1[m]',fill='black',font=('Arial',12))
    #button  
    wave_calculator_B=tk.Button(page2,text='Calculateur\n de Célérité de l’onde',command=wave_calculator_window,
                                font=('Arial',10,'bold'),bg='green',fg='white',bd=2)
    canvas2.create_window(520 ,200,window=wave_calculator_B)                  
#page3    
    page3=ttk.Frame(tab,width= 1330,height=540)    
    tab.add(page3,text='Vanne')
    ##canvas
    canvas3= tk.Canvas(page3,width=1330, height=540,bg='white')
    ##image
    infovanne_im=Image.open(r'photos\infovanne.png')
    infovanne_im = ImageTk.PhotoImage(infovanne_im.resize((500,300), Image.ANTIALIAS))
    canvas3.create_image(900, 150, image=infovanne_im)
    canvas3.image = infovanne_im
    #entry 
    Q0in=tk.StringVar()
    Q0in.set(0.75)# les valeurs prédéfinies 
    Q0_entry=tk.Entry(page3,textvariable=Q0in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10)
    canvas3.create_window(70, 190,window= Q0_entry)
      
    tfin=tk.StringVar()
    tfin.set(0)# les valeurs prédéfinies 
    tf_entry=tk.Entry(page3,textvariable=tfin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10)
    canvas3.create_window(70, 240,window= tf_entry)    
    #text
    canvas3.create_text(260,190, text="- Débit initial d’écoulement: Q0 [m3/s]",fill='black',font=('Arial',12))
    canvas3.create_text(265,240, text="- Temps de fermeture de la vanne: tf [s]",fill='black',font=('Arial',12)) 
#page4
    page4=ttk.Frame(tab,width= 1330,height=540) 
    tab.add(page4,text="Cheminée d'équilibre")
    ##canvas
    canvas4= tk.Canvas(page4,width=1330, height=540,bg='white')
    ##image
    surgetankinfo_im=Image.open(r'photos\surgetank info.png')
    surgetankinfo_im = ImageTk.PhotoImage(surgetankinfo_im.resize((700,500), Image.ANTIALIAS))
    canvas4.create_image(900,250, image=surgetankinfo_im)
    canvas4.image = surgetankinfo_im
    #entry     
    Dsin=tk.StringVar()
    Dsin.set(2)# les valeurs prédéfinies 
    Ds_entry=tk.Entry(page4,textvariable=Dsin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10)
    canvas4.create_window(70,140,window= Ds_entry)
        
    Min=tk.StringVar()
    Min.set(200)# les valeurs prédéfinies 
    M_entry=tk.Entry(page4,textvariable=Min,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10)
    canvas4.create_window(70,180,window= M_entry)
    #text
    canvas4.create_text(250,140, text="- Diamètre de la cheminée: Ds[m]",fill='black',font=('Arial',12))
    canvas4.create_text(312,180, text="- Position de la cheminée à partir du réservoir: M[m]",fill='black',font=('Arial',12))   
#page5    
    page5=ttk.Frame(tab,width=1330,height=700)    
    tab.add(page5,text='Exécuter')
    ##canvas
    canvas5= tk.Canvas(page5,width=1330, height=540,bg='white')
    ##frame
    graph_frame=tk.Frame(page5)
    canvas5.create_window(820,300,window=graph_frame)  
    #entry     
    Tin=tk.StringVar()
    Tin.set(50)# les valeurs prédéfinies 
    T_entry=tk.Entry(page5,textvariable=Tin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas5.create_window(80,50,window= T_entry)
        
    xin=tk.StringVar()
    xin.set(0)# les valeurs prédéfinies 
    x_entry=tk.Entry(page5,textvariable=xin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas5.create_window(80,110,window= x_entry)    
    #text
    canvas5.create_text(85,25, text="- Temps de simulation:T [s]",fill='black',font=('Arial',9))
    canvas5.create_text(115,80, text="- Point spatial à partir du réservoir: x [m]",fill='black',font=('Arial',9))
    #button         
    exécuter_B=tk.Button(page5,width=10,text='Exécuter',font=('Arial',12,'bold'),bg='#2AA321',fg='white',bd=2,
command=lambda:algo2.display_result(page5,canvas5,graph_frame,Hres_entry,k_entry,L_entry,D_entry,a_entry,f_entry,n_entry,Z0_entry,Z1_entry,Ds_entry,M_entry,Q0_entry,tf_entry,T_entry,x_entry).get_tk_widget().grid(column=1, row=1))
    canvas5.create_window(80,160,window=exécuter_B)  
    
    enregistrer_B=tk.Button(page5,width=10,text='Enregistrer',font=('Arial',12,'bold'),bg='blue',fg='white',bd=2,
command=lambda:algo2.save(Hres_entry,k_entry,L_entry,D_entry,a_entry,f_entry,n_entry,Z0_entry,Z1_entry,Ds_entry,M_entry,Q0_entry,tf_entry,T_entry,x_entry))
    canvas5.create_window(80 ,210,window=enregistrer_B)  

    """ activate widgets"""     
    canvas1.place(x=0,y=0) 
    canvas2.place(x=0,y=0)
    canvas3.place(x=0,y=0)
    canvas4.place(x=0,y=0)
    canvas5.place(x=0,y=0)
    tab.place(x=15,y=60)
# %% le systeme simple (reservoir conduite en serie vanne)+chemine d'equilibre [line 1749 to 1972]
def surgetank_type2():
    """ create widgets """
    top=tk.Toplevel()
    top.state('zoomed')
    top.iconbitmap(r'photos\images.ico')
    top.title("Réservoir-conduite en serie-vanne avec protection (cheminée d'équilibre) ")
    tab=ttk.Notebook(top)

    #button       
    project_B=tk.Button(top,text='Paramètres d’entrée' ,bg='#20A9CE',
                    fg='white',bd=0,font=('Arial',20,'bold'),height=1, width =25) 
    project_B.place(x=400,y=10)     
#page1
    page1 =ttk.Frame(tab,width=1330,height=540)
    tab.add(page1,text='Reservoir')
    ##canvas
    canvas1= tk.Canvas(page1,width=1330, height=540,bg='white')
    #entry
    Hresin=tk.StringVar()
    Hresin.set(100)# les valeurs prédéfinies 
    Hres_entry=tk.Entry(page1,textvariable=Hresin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas1.create_window(100, 140,window= Hres_entry)
    
    kin=tk.StringVar()
    kin.set(0.5)# les valeurs prédéfinies 
    k_entry=tk.Entry(page1,textvariable=kin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas1.create_window(100, 200,window=k_entry)
    #text
    canvas1.create_text(330,140, text="- Niveau d’eau dans le réservoir: Hres [m]",fill='black',font=('Arial',12))
    canvas1.create_text(350,200, text='- Coefficient de perte de charge singulière: k[-]',fill='black',font=('Arial',12))
    #images
    inforeservoir_im=Image.open(r'photos\inforeservoir.png')
    inforeservoir_im = ImageTk.PhotoImage(inforeservoir_im.resize((700,300), Image.ANTIALIAS))
    canvas1.create_image(1000, 250, image=inforeservoir_im)
    canvas1.image = inforeservoir_im
#page2    
    page2 =ttk.Frame(tab,width= 1330,height=600)
    tab.add(page2,text='Conduite')
    ##canvas
    canvas2= tk.Canvas(page2,width=1330, height=600,bg='white')
    #frame
    pipe_frame=tk.Frame(canvas2,bg='white')
    canvas2.create_window((8,225),window= pipe_frame,anchor='nw')
    #images
    jonctionpipeinfo_im=Image.open(r'photos\jonctionpipeinfo.png')
    jonctionpipeinfo_im = ImageTk.PhotoImage(jonctionpipeinfo_im.resize((700,500), Image.ANTIALIAS))
    canvas2.create_image(1000, 270, image=jonctionpipeinfo_im)
    canvas2.image = jonctionpipeinfo_im
    #entry 
    nin=tk.StringVar()
    nin.set(2)# les valeurs prédéfinies 
    n_entry=tk.Entry(page2,textvariable=nin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 100,window= n_entry)
    
    fin=tk.StringVar()
    fin.set(0.04)# les valeurs prédéfinies 
    f_entry=tk.Entry(page2,textvariable=fin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 150,window= f_entry)
    
    ncin=tk.StringVar()
    ncin.set('')# les valeurs prédéfinies 
    nc_entry=tk.Entry(page2,textvariable=ncin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100,200,window= nc_entry)
    
    def pipe(): # conduite est une fonction pour afficher et saisir les caractristiques("D,L,a") de chaque conduite  
        for child in pipe_frame.winfo_children():
            child.destroy()
        nc=int(nc_entry.get())
        # les syntaxes ci dessous sont relatives à l'interface graphique
        mbd=tk.Menubutton (pipe_frame,text='           D[m]         ',font=('Arial',11,'bold'),relief='groove',bg='white')
        mbd.menu=tk.Menu(mbd)
        mbd["menu"]=mbd.menu
        mbd.menu.add_command(label="Diamètre de la conduite")
        mbd.grid(row=14,column=1,sticky="nsew")
        
        mba=tk.Menubutton (pipe_frame,text='          a[m/s]        ',font=('Arial',11,'bold'),relief='groove',bg='#75E25A')
        mba.menu=tk.Menu(mba)
        mba["menu"]=mba.menu
        mba.menu.add_command(label="Célérité de l’onde de pression")
        mba.menu.add_command(label="Exécuter",command=wave_calculator_window)
        mba.grid(row=14,column=2,sticky="W")
        
        mbL=tk.Menubutton (pipe_frame,text='           L[m]          ',font=('Arial',11,'bold'),relief='groove',bg='white')
        mbL.menu=tk.Menu(mbL)
        mbL["menu"]=mbL.menu
        mbL.menu.add_command(label="Longueur de la conduite")
        mbL.grid(row=14,column=3,sticky="W")
        
        mbZ=tk.Menubutton (pipe_frame,text='           Z[m]         ',font=('Arial',11,'bold'),relief='groove',bg='white')
        mbZ.menu=tk.Menu(mbZ)
        mbZ["menu"]=mbZ.menu
        mbZ.menu.add_command(label="Elévation de noued par rapport au Datum")
        mbZ.grid(row=14,column=4,sticky="W")
        global d1
        global a1
        global l1
        global Z1
        d1=[]
        a1=[]
        l1=[]
        Z1=[]
       
        #input d:diamètre des conduites ,a:célérite d'onde de pression des conduites , l: longueur des conduites 
        for i in range(0,nc):
                d_entry=tk.Entry(pipe_frame,bg='#C4CCCE')
                d_entry.grid(row=16+i,column=1)
                d1.append(d_entry)
                a_entry=tk.Entry(pipe_frame,bg='#C4CCCE')
                a_entry.grid(row=16+i,column=2)
                a1.append(a_entry)
                l_entry=tk.Entry(pipe_frame,bg='#C4CCCE')
                l_entry.grid(row=16+i,column=3)
                l1.append(l_entry)
        #input les elevations d'extrimité de chaque conduite 
        for i in range(0,nc+1):    
                Z_entry=tk.Entry(pipe_frame,bg='#C4CCCE')
                Z_entry.grid(row=16+i,column=4)
                Z1.append(Z_entry)
       
    
    #text
    canvas2.create_text(390,100, text='- Discrétisation de la 1ere  conduite: nombre de ségments n',fill='black',font=('Arial',12))
    canvas2.create_text(362,150, text='- Coefficient de frottement de Darcy_Weisbach: f [-]',fill='black',font=('Arial',12))
    canvas2.create_text(285,200, text='- Nombre de conduites: nc [-]',fill='black',font=('Arial',12))
    #button
    entrer_B=tk.Button(page2,text='Entrer',command=pipe,font=('Arial',10,'bold'),bg='red',fg='white',bd=2,width=20)
    canvas2.create_window(540 ,200,window=entrer_B)                 
#page3    
    page3=ttk.Frame(tab,width= 1330,height=540)    
    tab.add(page3,text='Vanne')
    ##canvas
    canvas3= tk.Canvas(page3,width=1330, height=540,bg='white')
    ##image
    infovanne_im=Image.open(r'photos\infovanne.png')
    infovanne_im = ImageTk.PhotoImage(infovanne_im.resize((500,300), Image.ANTIALIAS))
    canvas3.create_image(900, 150, image=infovanne_im)
    canvas3.image = infovanne_im
    #entry 
    Q0in=tk.StringVar()
    Q0in.set(0.75)# les valeurs prédéfinies 
    Q0_entry=tk.Entry(page3,textvariable=Q0in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas3.create_window(100, 190,window= Q0_entry)
      
    tfin=tk.StringVar()
    tfin.set(0)# les valeurs prédéfinies 
    tf_entry=tk.Entry(page3,textvariable=tfin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas3.create_window(100, 240,window= tf_entry)    
    #text
    canvas3.create_text(315,190, text="- Débit initial d’écoulement: Q0 [m3/s]",fill='black',font=('Arial',12))
    canvas3.create_text(320,240, text="- Temps de fermeture de la vanne: tf [s]",fill='black',font=('Arial',12)) 
#page4
    page4=ttk.Frame(tab,width= 1330,height=700) 
    tab.add(page4,text="Cheminée d'équilibre")
    ##canvas
    canvas4= tk.Canvas(page4,width=1330, height=540,bg='white')
    ##image
    surgetankinfo_im=Image.open(r'photos\joncsurgetank info.png')
    surgetankinfo_im = ImageTk.PhotoImage(surgetankinfo_im.resize((700,500), Image.ANTIALIAS))
    canvas4.create_image(950,250, image=surgetankinfo_im)
    canvas4.image = surgetankinfo_im
    #entry     
    Dsin=tk.StringVar()
    Dsin.set(2)# les valeurs prédéfinies 
    Ds_entry=tk.Entry(page4,textvariable=Dsin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas4.create_window(100,140,window= Ds_entry)
        
    Min=tk.StringVar()
    Min.set(200)# les valeurs prédéfinies 
    M_entry=tk.Entry(page4,textvariable=Min,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas4.create_window(100,180,window= M_entry)
    
    c1in=tk.StringVar()
    c1in.set(1)# les valeurs prédéfinies 
    c1_entry=tk.Entry(page4,textvariable=c1in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas4.create_window(100,220,window= c1_entry)
    #text
    canvas4.create_text(303,140, text="- Diamètre de la cheminée: Ds[m]",fill='black',font=('Arial',12))
    canvas4.create_text(365,180, text="- Position de la cheminée à partir du réservoir: M[m]",fill='black',font=('Arial',12))
    canvas4.create_text(380,220, text="- La cheminée d’équilibre se trouve dans la conduite N°=",fill='black',font=('Arial',12))
    
#page5    
    page5=ttk.Frame(tab,width= 1330,height=580)    
    tab.add(page5,text='Exécuter')
    ##canvas
    canvas5= tk.Canvas(page5,width=1330, height=580,bg='white')
    ##frame
    graph_frame=tk.Frame(page5,bg='white')
    canvas5.create_window(820,300,window=graph_frame)     
    #entry     
    Tin=tk.StringVar()
    Tin.set(50)# les valeurs prédéfinies 
    T_entry=tk.Entry(page5,textvariable=Tin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas5.create_window(80,50,window= T_entry)
        
    xin=tk.StringVar()
    xin.set(0)# les valeurs prédéfinies 
    x_entry=tk.Entry(page5,textvariable=xin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas5.create_window(80,110,window= x_entry) 
    
    cin=tk.StringVar()
    cin.set(1)# les valeurs prédéfinies 
    c_entry=tk.Entry(page5,textvariable=cin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas5.create_window(80,170,window= c_entry)   
    #text
    canvas5.create_text(88,25, text="- Temps de simulation:T [s]",fill='black',font=('Arial',10))
    canvas5.create_text(125,80, text="- Point spatial à partir du réservoir: x [m]",fill='black',font=('Arial',10))
    canvas5.create_text(123,140, text="- Le point x se trouve dans la conduite \n N°=:",fill='black',font=('Arial',10))
    #button               
    exécuter_B=tk.Button(page5,width=10,text='Exécuter',font=('Arial',12,'bold'),bg='#2AA321',fg='white',bd=2,
command=lambda:algo5.display_result(page5,canvas5,graph_frame,Hres_entry,k_entry,n_entry,nc_entry,f_entry,l1,d1,a1,Z1,Q0_entry,tf_entry,Ds_entry,M_entry,c1_entry,T_entry,x_entry,c_entry).get_tk_widget().grid(row=1,column=1))
    canvas5.create_window(80,210,window=exécuter_B)  
    
    enregistrer_B=tk.Button(page5,width=10,text='Enregistrer',font=('Arial',12,'bold'),bg='blue',fg='white',bd=2,
command=lambda:algo5.save(Hres_entry,k_entry,n_entry,nc_entry,f_entry,l1,d1,a1,Z1,Q0_entry,tf_entry,Ds_entry,M_entry,c1_entry,T_entry,x_entry,c_entry))
    canvas5.create_window(80 ,260,window=enregistrer_B) 

    """ activate widgets"""     
    canvas1.place(x=0,y=0) 
    canvas2.place(x=0,y=0)
    canvas3.place(x=0,y=0)
    canvas4.place(x=0,y=0)
    canvas5.place(x=0,y=0)
    tab.place(x=15,y=60)  
# %% le systeme simple (reservoir conduite-en-parallèle vanne)+cheminee d'equilibre [line 1973 to 2191]
def surgetank_type3():
    """ create widgets """
    top=tk.Toplevel()
    top.state('zoomed')
    top.iconbitmap(r'photos\images.ico')
    top.title("Réservoir-conduite en parallèle-vanne avec protection (cheminée d'équilibre)")
    tab=ttk.Notebook(top)

    #button       
    project_B=tk.Button(top,text='Paramètres d’entrée' ,bg='#20A9CE',
                    fg='white',bd=0,font=('Arial',20,'bold'),height=1, width =25) 
    project_B.place(x=400,y=10) 
    
#page1
    page1 =ttk.Frame(tab,width=1330,height=540)
    tab.add(page1,text='Reservoir')
    ##canvas
    canvas1= tk.Canvas(page1,width=1330, height=540,bg='white')
    #entry
    Hresin=tk.StringVar()
    Hresin.set(100)# les valeurs prédéfinies 
    Hres_entry=tk.Entry(page1,textvariable=Hresin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas1.create_window(100, 140,window= Hres_entry)
    
    kin=tk.StringVar()
    kin.set(0.5)# les valeurs prédéfinies 
    k_entry=tk.Entry(page1,textvariable=kin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas1.create_window(100, 200,window=k_entry)

    #text
    canvas1.create_text(330,140, text="- Niveau d’eau dans le réservoir: Hres [m]",fill='black',font=('Arial',12))
    canvas1.create_text(348,200, text='- Coefficient de perte de charge singulière: k[-]',fill='black',font=('Arial',12))
    #images
    inforeservoir_im=Image.open(r'photos\inforeservoir.png')
    inforeservoir_im = ImageTk.PhotoImage(inforeservoir_im.resize((700,300), Image.ANTIALIAS))
    canvas1.create_image(1000, 250, image=inforeservoir_im)
    canvas1.image = inforeservoir_im
#page2    
    page2 =ttk.Frame(tab,width= 1330,height=600)
    tab.add(page2,text='Conduite et Vanne')
    ##canvas
    canvas2= tk.Canvas(page2,width=1330, height=600,bg='white')
    #frame
    pipe_frame=tk.Frame(canvas2,bg='white')
    canvas2.create_window((10,290),window= pipe_frame,anchor='nw')
    #images
    branchpipeinfo_im=Image.open(r'photos\branchpipeinfo.png')
    branchpipeinfo_im = ImageTk.PhotoImage(branchpipeinfo_im.resize((700,500), Image.ANTIALIAS))
    canvas2.create_image(1000, 270, image=branchpipeinfo_im)
    canvas2.image = branchpipeinfo_im
    #entry
    Q0in=tk.StringVar()
    Q0in.set(0.75)# les valeurs prédéfinies 
    Q0_entry=tk.Entry(page2,textvariable=Q0in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 100,window= Q0_entry)
    
    nin=tk.StringVar()
    nin.set(2)# les valeurs prédéfinies 
    n_entry=tk.Entry(page2,textvariable=nin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 150,window= n_entry)
    
    fin=tk.StringVar()
    fin.set(0.04)# les valeurs prédéfinies 
    f_entry=tk.Entry(page2,textvariable=fin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 200,window= f_entry)    
    
    ncin=tk.StringVar()
    ncin.set('')# les valeurs prédéfinies 
    nc_entry=tk.Entry(page2,textvariable=ncin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100,250,window= nc_entry)
    
    def pipe(): # conduite est une fonction pour afficher et saisir les caractristiques("D,L,a") de chaque conduite  
        for child in pipe_frame.winfo_children():
            child.destroy()
        nc=int(nc_entry.get())
        # les syntaxes ci dessous sont relatives à l'interface graphique
        
        mbd=tk.Menubutton (pipe_frame,text='           D[m]         ',font=('Arial',10,'bold'),relief='groove',bg='white',width=15)
        mbd.menu=tk.Menu(mbd)
        mbd["menu"]=mbd.menu
        mbd.menu.add_command(label="Diamètre de la conduite")
        mbd.menu.add_command(label="Premiere ligne pour la conduite principale")
        mbd.grid(row=15,column=1,sticky="W")
        
        mbL=tk.Menubutton (pipe_frame,text='           L[m]          ',font=('Arial',10,'bold'),relief='groove',bg='white',width=15)
        mbL.menu=tk.Menu(mbL)
        mbL["menu"]=mbL.menu
        mbL.menu.add_command(label="Longueur de la conduite")
        mbL.menu.add_command(label="Premiere ligne pour la conduite principale")
        mbL.grid(row=15,column=3,sticky="W")
        
        mbZ=tk.Menubutton (pipe_frame,text='           Z[m]         ',font=('Arial',10,'bold'),relief='groove',bg='white',width=15)
        mbZ.menu=tk.Menu(mbZ)
        mbZ["menu"]=mbZ.menu
        mbZ.menu.add_command(label='Elévation de noued par rapport au Datum' )
        mbZ.menu.add_command(label="Premiere ligne pour la conduite principale")
        mbZ.grid(row=15,column=4,sticky="W")
        
        mbtf=tk.Menubutton (pipe_frame,text='             tf[s]          ',font=('Arial',10,'bold'),relief='groove',bg='white',width=15)
        mbtf.menu=tk.Menu(mbtf)
        mbtf["menu"]=mbtf.menu
        mbtf.menu.add_command(label="Temps de fermeture de la vanne")
        mbtf.grid(row=15,column=5,sticky="W")
        
        mba=tk.Menubutton (pipe_frame,text='          a[m/s]        ',font=('Arial',10,'bold'),relief='groove',bg='#75E25A',width=15)
        mba.menu=tk.Menu(mba)
        mba["menu"]=mba.menu
        mba.menu.add_command(label="Célérité de l’onde de pression")
        mba.menu.add_command(label="Exécuter",command=wave_calculator_window)
        mba.grid(row=15,column=2,sticky="W")
        global d1
        global a1
        global l1
        global Z1
        global tf1        
        d1=[]
        a1=[]
        l1=[]
        Z1=[]
        tf1=[]
        #input d:diamètre des conduites ,a:célérite d'onde de pression des conduites , l: longueur des conduites
        for i in range(0,nc+1):
                d_entry=tk.Entry(pipe_frame,bg='#C4CCCE',width=20)
                d_entry.grid(row=16+i,column=1)
                d1.append(d_entry)
                a_entry=tk.Entry(pipe_frame,bg='#C4CCCE',width=20)
                a_entry.grid(row=16+i,column=2)
                a1.append(a_entry)
                l_entry=tk.Entry(pipe_frame,bg='#C4CCCE',width=20)
                l_entry.grid(row=16+i,column=3)
                l1.append(l_entry)
        for i in range(0,nc+2):    
                Z_entry=tk.Entry(pipe_frame,bg='#C4CCCE',width=20)
                Z_entry.grid(row=16+i,column=4)
                Z1.append(Z_entry)
        for i in range(0,nc):    
                tf_entry=tk.Entry(pipe_frame,bg='#C4CCCE',width=20)
                tf_entry.grid(row=17+i,column=5)
                tf1.append(tf_entry)    
    #text
    canvas2.create_text(315,100, text="- Débit initial d’écoulement: Q0 [m3/s]",fill='black',font=('Arial',12))
    canvas2.create_text(390,150, text='- Discrétisation de la 1ere  conduite: nombre de ségments n',fill='black',font=('Arial',12))
    canvas2.create_text(362,200, text='- Coefficient de frottement de Darcy_Weisbach: f [-]',fill='black',font=('Arial',12))
    canvas2.create_text(385,250, text='- Nombre de conduites liées à la conduite principale: nc [-]',fill='black',font=('Arial',12))
    #button
    entrer_B=tk.Button(page2,text='Entrer',command=pipe,font=('Arial',10,'bold'),bg='red',fg='white',bd=2,width=10)
    canvas2.create_window(590 ,275,window=entrer_B)                 
#page3
    page3=ttk.Frame(tab,width= 1330,height=600) 
    tab.add(page3,text="Cheminée d'équilibre")
    ##canvas
    canvas3= tk.Canvas(page3,width=1330, height=600,bg='white')
    ##image
    branchsurgetankinfo_im=Image.open(r'photos\branchsurge tankinfo.png')
    branchsurgetankinfo_im = ImageTk.PhotoImage(branchsurgetankinfo_im.resize((700,500), Image.ANTIALIAS))
    canvas3.create_image(950,300, image=branchsurgetankinfo_im)
    canvas3.image = branchsurgetankinfo_im
    #entry     
    Dsin=tk.StringVar()
    Dsin.set(2)# les valeurs prédéfinies 
    Ds_entry=tk.Entry(page3,textvariable=Dsin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas3.create_window(100,140,window= Ds_entry)
        
    Min=tk.StringVar()
    Min.set(200)# les valeurs prédéfinies 
    M_entry=tk.Entry(page3,textvariable=Min,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas3.create_window(100,180,window= M_entry)
    
    c1in=tk.StringVar()
    c1in.set(1)# les valeurs prédéfinies 
    c1_entry=tk.Entry(page3,textvariable=c1in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas3.create_window(100,220,window= c1_entry)
    #text
    canvas3.create_text(305,140, text="- Diamètre de la cheminée: Ds[m]",fill='black',font=('Arial',12))
    canvas3.create_text(345,180, text="- Position de la cheminée à partir d'extrémité \n gauche de conduite: M[m]",fill='black',font=('Arial',12))
    canvas3.create_text(385,220, text="- La cheminée d’équilibre se trouve dans la conduite N°=",fill='black',font=('Arial',12))
#page4    
    page4=ttk.Frame(tab,width= 1330,height=580)    
    tab.add(page4,text='Exécuter')
    ##canvas
    canvas4= tk.Canvas(page4,width=1330, height=580,bg='white')
    ##frame
    graph_frame=tk.Frame(page4,bg='white')
    canvas4.create_window(830,300,window=graph_frame)  
    #entry     
    Tin=tk.StringVar()
    Tin.set(50)# les valeurs prédéfinies 
    T_entry=tk.Entry(page4,textvariable=Tin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas4.create_window(80,50,window= T_entry)
        
    xin=tk.StringVar()
    xin.set(0)# les valeurs prédéfinies 
    x_entry=tk.Entry(page4,textvariable=xin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas4.create_window(80,110,window= x_entry) 
    
    cin=tk.StringVar()
    cin.set(1)# les valeurs prédéfinies 
    c_entry=tk.Entry(page4,textvariable=cin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas4.create_window(80,170,window= c_entry)   
    #text
    canvas4.create_text(90,25, text="- Temps de simulation:T [s]",fill='black',font=('Arial',10))
    canvas4.create_text(185,80, text="- Point spatial à partir d'extrémité gauche de conduite: x [m]",fill='black',font=('Arial',10))
    canvas4.create_text(125,140, text="- Le point x se trouve dans la conduite \n N°=:",fill='black',font=('Arial',10))
    #button      
    exécuter_B=tk.Button(page4,width=10,text='Exécuter',font=('Arial',12,'bold'),bg='#2AA321',fg='white',bd=2,
command=lambda:algo8.display_result(page4,canvas4,graph_frame,Hres_entry,k_entry,Q0_entry,n_entry,f_entry,nc_entry,l1,d1,a1,Z1,tf1,Ds_entry,M_entry,c1_entry,c_entry,T_entry,x_entry).grid(row=1,column=1))
    canvas4.create_window(80,210,window=exécuter_B)  
    
    enregistrer_B=tk.Button(page4,width=10,text='Enregistrer',font=('Arial',12,'bold'),bg='blue',fg='white',bd=2,
command=lambda:algo8.save(Hres_entry,k_entry,Q0_entry,n_entry,f_entry,nc_entry,l1,d1,a1,Z1,tf1,Ds_entry,M_entry,c1_entry,c_entry,T_entry,x_entry))
    canvas4.create_window(80 ,260,window=enregistrer_B)  

    """ activate widgets"""     
    canvas1.place(x=0,y=0) 
    canvas2.place(x=0,y=0)
    canvas3.place(x=0,y=0)
    canvas4.place(x=0,y=0)
    tab.place(x=15,y=60)      
# %% le systeme simple (reservoir conduite vanne)+Reservoir d'air line[2192 to 2420 ]
def airchamber_type1():
    """ create widgets """
    top=tk.Toplevel()
    top.state('zoomed')
    top.iconbitmap(r'photos\images.ico')
    top.title("Réservoir-conduite-vanne avec protection (Reservoir d'air) ")
    tab=ttk.Notebook(top)
    #button       
    project_B=tk.Button(top,text='Paramètres d’entrée' ,bg='#20A9CE',
                    fg='white',bd=0,font=('Arial',20,'bold'),height=1, width =25) 
    project_B.place(x=400,y=10)     
#page1
    page1 =ttk.Frame(tab,width=1330,height=540)
    tab.add(page1,text='Réservoir')
    ##canvas
    canvas1= tk.Canvas(page1,width=1330, height=540,bg='white')
    #entry
    Hresin=tk.StringVar()
    Hresin.set(100)# les valeurs prédéfinies 
    Hres_entry=tk.Entry(page1,textvariable=Hresin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas1.create_window(100, 140,window= Hres_entry)
    
    kin=tk.StringVar()
    kin.set(0.5)# les valeurs prédéfinies 
    k_entry=tk.Entry(page1,textvariable=kin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas1.create_window(100, 200,window=k_entry)
    #text
    canvas1.create_text(330,140, text="- Niveau d’eau dans le réservoir: Hres [m]",fill='black',font=('Arial',12))
    canvas1.create_text(350,200, text='- Coefficient de perte de charge singulière: k[-]',fill='black',font=('Arial',12))
    #images
    inforeservoir_im=Image.open(r'photos\inforeservoir.png')
    inforeservoir_im = ImageTk.PhotoImage(inforeservoir_im.resize((700,300), Image.ANTIALIAS))
    canvas1.create_image(1000, 250, image=inforeservoir_im)
    canvas1.image = inforeservoir_im
#page2    
    page2 =ttk.Frame(tab,width= 1330,height=540)
    tab.add(page2,text='Conduite')
    ##canvas
    canvas2= tk.Canvas(page2,width=1330, height=540,bg='white')
    #images
    pipeinfo_im=Image.open(r'photos\pipeinfo.png')
    pipeinfo_im = ImageTk.PhotoImage(pipeinfo_im.resize((700,500), Image.ANTIALIAS))
    canvas2.create_image(1000, 250, image=pipeinfo_im)
    canvas2.image = pipeinfo_im
    #entry 
    Lin=tk.StringVar()
    Lin.set(1000)# les valeurs prédéfinies 
    L_entry=tk.Entry(page2,textvariable=Lin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 100,window= L_entry)
    
    Din=tk.StringVar()
    Din.set(1)# les valeurs prédéfinies 
    D_entry=tk.Entry(page2,textvariable=Din,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 150,window= D_entry)
             
    ain=tk.StringVar()
    ain.set(1000)# les valeurs prédéfinies 
    a_entry=tk.Entry(page2,textvariable=ain,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 200,window= a_entry)
        
    fin=tk.StringVar()
    fin.set(0.04)# les valeurs prédéfinies 
    f_entry=tk.Entry(page2,textvariable=fin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 250,window= f_entry)
        
    nin=tk.StringVar()
    nin.set(5)# les valeurs prédéfinies 
    n_entry=tk.Entry(page2,textvariable=nin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 300,window= n_entry)
        
    Z0in=tk.StringVar()
    Z0in.set(20)# les valeurs prédéfinies 
    Z0_entry=tk.Entry(page2,textvariable=Z0in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 350,window= Z0_entry)
               
    Z1in=tk.StringVar()
    Z1in.set(10)# les valeurs prédéfinies 
    Z1_entry=tk.Entry(page2,textvariable=Z1in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 400,window= Z1_entry)    
    #text
    canvas2.create_text(298,100, text="- Longueur de la conduite: L [m]",fill='black',font=('Arial',12))
    canvas2.create_text(300,150, text='- Diamètre de la conduite: D [m]',fill='black',font=('Arial',12))
    canvas2.create_text(325,200, text='- Célérité de l’onde de pression: a [m/s]',fill='black',font=('Arial',12))
    canvas2.create_text(365,250, text='- Coefficient de frottement de Darcy_Weisbach: f [-]',fill='black',font=('Arial',12))
    canvas2.create_text(375,300, text='- Discrétisation de la conduite: nombre de ségments n',fill='black',font=('Arial',12))
    canvas2.create_text(370,350, text='- Elevation de l’extrimité amont de la conduite: Z0[m]',fill='black',font=('Arial',12))
    canvas2.create_text(362,400, text='- Elevation de l’extrimité aval de la conduite: Z1[m]',fill='black',font=('Arial',12))
    #button  
    wave_calculator_B=tk.Button(page2,text='Calculateur\n de Célérité de l’onde',command=wave_calculator_window,
                                font=('Arial',10,'bold'),bg='green',fg='white',bd=2)
    canvas2.create_window(570 ,200,window=wave_calculator_B)                  
#page3    
    page3=ttk.Frame(tab,width= 1330,height=540)    
    tab.add(page3,text='Vanne')
    ##canvas
    canvas3= tk.Canvas(page3,width=1330, height=540,bg='white')
    ##image
    infovanne_im=Image.open(r'photos\infovanne.png')
    infovanne_im = ImageTk.PhotoImage(infovanne_im.resize((500,300), Image.ANTIALIAS))
    canvas3.create_image(900, 150, image=infovanne_im)
    canvas3.image = infovanne_im
    #entry 
    Q0in=tk.StringVar()
    Q0in.set(0.75)# les valeurs prédéfinies 
    Q0_entry=tk.Entry(page3,textvariable=Q0in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas3.create_window(100, 190,window= Q0_entry)
      
    tfin=tk.StringVar()
    tfin.set(0)# les valeurs prédéfinies 
    tf_entry=tk.Entry(page3,textvariable=tfin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas3.create_window(100, 240,window= tf_entry)    
    #text
    canvas3.create_text(315,190, text="- Débit initial d’écoulement: Q0 [m3/s]",fill='black',font=('Arial',12))
    canvas3.create_text(320,240, text="- Temps de fermeture de la vanne: tf [s]",fill='black',font=('Arial',12)) 
#page4
    page4=ttk.Frame(tab,width= 1330,height=540) 
    tab.add(page4,text="Réservoir d'air ")
    ##canvas
    canvas4= tk.Canvas(page4,width=1330, height=540,bg='white')
    ##image
    airchamberinfo_im=Image.open(r'photos\airchamber info.png')
    airchamberinfo_im = ImageTk.PhotoImage(airchamberinfo_im.resize((700,500), Image.ANTIALIAS))
    canvas4.create_image(950,250, image=airchamberinfo_im)
    canvas4.image = airchamberinfo_im
    #entry     
    Dcin=tk.StringVar()
    Dcin.set(0.5)# les valeurs prédéfinies 
    Dc_entry=tk.Entry(page4,textvariable=Dcin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas4.create_window(100, 100,window= Dc_entry)
        
    Vairchin=tk.StringVar()
    Vairchin.set(4)# les valeurs prédéfinies 
    Vairch_entry=tk.Entry(page4,textvariable=Vairchin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas4.create_window(100, 150,window= Vairch_entry)
    
    Voairin=tk.StringVar()
    Voairin.set('')# les valeurs prédéfinies
    Voair_entry=tk.Entry(page4,textvariable=Voairin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10,state='disabled')                     
    canvas4.create_window(75, 250,window= Voair_entry)
    
    Hoairin=tk.StringVar()
    Hoairin.set('')# les valeurs prédéfinies 
    Hoair_entry=tk.Entry(page4,textvariable=Hoairin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10,state='disabled')
    canvas4.create_window(200, 250,window= Hoair_entry)
    
    def airselecte(V_entry,H_entry,Hin,Vin,combobox):
        if combobox.get()=="- Le volume d'air initiale:voair[m3]":
                 V_entry.config(state='normal')
                 Vin.set(0.5)# les valeurs prédéfinies
                 H_entry.config(state='disabled')
                 Hin.set('None')

        if combobox.get()=="- La pression d'air initiale: Hoair[m]":
                 H_entry.config(state='normal') 
                 Hin.set(96)
                 V_entry.config(state='disabled')
                 Vin.set('None')
                 
                   
    Corf_inflowin=tk.StringVar()
    Corf_inflowin.set(0.5)# les valeurs prédéfinies 
    Corf_inflow_entry=tk.Entry(page4,textvariable=Corf_inflowin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas4.create_window(100, 300,window= Corf_inflow_entry)
               
    Corf_outflowin=tk.StringVar()
    Corf_outflowin.set(0.3)# les valeurs prédéfinies 
    Corf_outflow_entry=tk.Entry(page4,textvariable=Corf_outflowin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas4.create_window(100, 350,window=Corf_outflow_entry)  
    
    Min=tk.StringVar()
    Min.set(200)# les valeurs prédéfinies 
    M_entry=tk.Entry(page4,textvariable=Min,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas4.create_window(100, 400,window= M_entry)
    ##combobox
    aircombobox = ttk.Combobox(page4, values=[
                                    "- Le volume d'air initiale:voair[m3]", 
                                    "- La pression d'air initiale: Hoair[m]"],width=35)
    aircombobox.insert(0,'sélectionnez une réponse')
    aircombobox.bind('<<ComboboxSelected>>',lambda event:airselecte(Voair_entry,Hoair_entry,Hoairin,Voairin,aircombobox))
    canvas4.create_window(130, 200,window=aircombobox)
    #text
    canvas4.create_text(310,100, text="- Diamètre de reservoir d'air: Dc[m]",fill='black',font=('Arial',12))
    canvas4.create_text(340,145, text="- Le volume totale du rervoir d'air: vairch[m3]",fill='black',font=('Arial',12))
    canvas4.create_text(343,200 ,text="- Sélectionnez une réponse",fill='black',font=('Arial',12))
    canvas4.create_text(70,220 ,text="- Le volume d'air",fill='black',font=('Arial',12))
    canvas4.create_text(210,220,text="- La pression d'air",fill='black',font=('Arial',12))
    canvas4.create_text(370,300, text="- Coef perte de charge d'orifice (inflow):Corf_inflow[-]",fill='black',font=('Arial',12))
    canvas4.create_text(380,350, text="- Coef perte de charge d'orifice (outflow):Corf_outflow[-]",fill='black',font=('Arial',12))
    canvas4.create_text(345,400, text="- Position de reservoir à partir de  vanne: M[m]",fill='black',font=('Arial',12))
    
#page5    
    page5=ttk.Frame(tab,width=1330,height=700)    
    tab.add(page5,text='Exécuter')
    ##canvas
    canvas5= tk.Canvas(page5,width=1330, height=540,bg='white')
    ##frame
    graph_frame=tk.Frame(page5)
    canvas5.create_window(820,300,window=graph_frame)  
    #entry     
    Tin=tk.StringVar()
    Tin.set(50)# les valeurs prédéfinies 
    T_entry=tk.Entry(page5,textvariable=Tin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas5.create_window(80,50,window= T_entry)
        
    xin=tk.StringVar()
    xin.set(0)# les valeurs prédéfinies 
    x_entry=tk.Entry(page5,textvariable=xin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas5.create_window(80,110,window= x_entry)

    #text
    canvas5.create_text(80,25, text="- Temps de simulation:T [s]",fill='black',font=('Arial',9))
    canvas5.create_text(110,80, text="- Point spatial à partir du réservoir: x [m]",fill='black',font=('Arial',9))
    #button         
    exécuter_B=tk.Button(page5,width=10,text='Exécuter',font=('Arial',12,'bold'),bg='#2AA321',fg='white',bd=2,
command=lambda:algo3.display_result(page5,canvas5,graph_frame,Hres_entry,k_entry,L_entry,D_entry,a_entry,f_entry,n_entry,Z0_entry,Z1_entry,Dc_entry,Vairch_entry,Voair_entry,Hoair_entry,Corf_inflow_entry,Corf_outflow_entry,M_entry,Q0_entry,tf_entry,T_entry,x_entry).get_tk_widget().grid(column=1, row=1))
    canvas5.create_window(80,160,window=exécuter_B)  
    
    enregistrer_B=tk.Button(page5,width=10,text='Enregistrer',font=('Arial',12,'bold'),bg='blue',fg='white',bd=2,
command=lambda:algo3.save(Hres_entry,k_entry,L_entry,D_entry,a_entry,f_entry,n_entry,Z0_entry,Z1_entry,Dc_entry,Vairch_entry,Voair_entry,Hoair_entry,Corf_inflow_entry,Corf_outflow_entry,M_entry,Q0_entry,tf_entry,T_entry,x_entry))
    canvas5.create_window(80 ,210,window=enregistrer_B)  

    """ activate widgets"""     
    canvas1.place(x=0,y=0) 
    canvas2.place(x=0,y=0)
    canvas3.place(x=0,y=0)
    canvas4.place(x=0,y=0)
    canvas5.place(x=0,y=0)
    tab.place(x=15,y=60)  
# %% le systeme simple (reservoir conduite en serie vanne)+Reservoir d'air [line 2421 to 2692]
def airchamber_type2():
    """ create widgets """
    top=tk.Toplevel()
    top.state('zoomed')
    top.iconbitmap(r'photos\images.ico')
    top.title("Réservoir-conduite en serie -vanne avec protection (Reservoir d'air) ")
    tab=ttk.Notebook(top)
    #button       
    project_B=tk.Button(top,text='Paramètres d’entrée' ,bg='#20A9CE',
                    fg='white',bd=0,font=('Arial',20,'bold'),height=1, width =25) 
    project_B.place(x=400,y=10)     
#page1
    page1 =ttk.Frame(tab,width=1330,height=540)
    tab.add(page1,text='Réservoir')
    ##canvas
    canvas1= tk.Canvas(page1,width=1330, height=540,bg='white')
    #entry
    Hresin=tk.StringVar()
    Hresin.set(100)# les valeurs prédéfinies 
    Hres_entry=tk.Entry(page1,textvariable=Hresin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas1.create_window(100, 140,window= Hres_entry)
    
    kin=tk.StringVar()
    kin.set(0.5)# les valeurs prédéfinies 
    k_entry=tk.Entry(page1,textvariable=kin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas1.create_window(100, 200,window=k_entry)
    #text
    canvas1.create_text(330,140, text="- Niveau d’eau dans le réservoir: Hres [m]",fill='black',font=('Arial',12))
    canvas1.create_text(350,200, text='- Coefficient de perte de charge singulière: k[-]',fill='black',font=('Arial',12))
    #images
    inforeservoir_im=Image.open(r'photos\inforeservoir.png')
    inforeservoir_im = ImageTk.PhotoImage(inforeservoir_im.resize((700,300), Image.ANTIALIAS))
    canvas1.create_image(1000, 250, image=inforeservoir_im)
    canvas1.image = inforeservoir_im
#page2    
    page2 =ttk.Frame(tab,width= 1330,height=600)
    tab.add(page2,text='Conduite')
    ##canvas
    canvas2= tk.Canvas(page2,width=1330, height=600,bg='white')
    #frame
    pipe_frame=tk.Frame(canvas2,bg='white')
    canvas2.create_window((8,225),window= pipe_frame,anchor='nw')
    #images
    jonctionpipeinfo_im=Image.open(r'photos\jonctionpipeinfo.png')
    jonctionpipeinfo_im = ImageTk.PhotoImage(jonctionpipeinfo_im.resize((700,500), Image.ANTIALIAS))
    canvas2.create_image(1000, 270, image=jonctionpipeinfo_im)
    canvas2.image = jonctionpipeinfo_im
    #entry 
    nin=tk.StringVar()
    nin.set(2)# les valeurs prédéfinies 
    n_entry=tk.Entry(page2,textvariable=nin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 100,window= n_entry)
    
    fin=tk.StringVar()
    fin.set(0.04)# les valeurs prédéfinies 
    f_entry=tk.Entry(page2,textvariable=fin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 150,window= f_entry)
    
    ncin=tk.StringVar()
    ncin.set('')# les valeurs prédéfinies 
    nc_entry=tk.Entry(page2,textvariable=ncin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100,200,window= nc_entry)
    
    def pipe(): # conduite est une fonction pour afficher et saisir les caractristiques("D,L,a") de chaque conduite  
        for child in pipe_frame.winfo_children():
            child.destroy()
        nc=int(nc_entry.get())
        # les syntaxes ci dessous sont relatives à l'interface graphique
        mbd=tk.Menubutton (pipe_frame,text='           D[m]         ',font=('Arial',11,'bold'),relief='groove',bg='white')
        mbd.menu=tk.Menu(mbd)
        mbd["menu"]=mbd.menu
        mbd.menu.add_command(label="Diamètre de la conduite")
        mbd.grid(row=14,column=1,sticky="nsew")
        
        mba=tk.Menubutton (pipe_frame,text='          a[m/s]        ',font=('Arial',11,'bold'),relief='groove',bg='#75E25A')
        mba.menu=tk.Menu(mba)
        mba["menu"]=mba.menu
        mba.menu.add_command(label="Célérité de l’onde de pression")
        mba.menu.add_command(label="Exécuter",command=wave_calculator_window)
        mba.grid(row=14,column=2,sticky="W")
        
        mbL=tk.Menubutton (pipe_frame,text='           L[m]          ',font=('Arial',11,'bold'),relief='groove',bg='white')
        mbL.menu=tk.Menu(mbL)
        mbL["menu"]=mbL.menu
        mbL.menu.add_command(label="Longueur de la conduite")
        mbL.grid(row=14,column=3,sticky="W")
        
        mbZ=tk.Menubutton (pipe_frame,text='           Z[m]         ',font=('Arial',11,'bold'),relief='groove',bg='white')
        mbZ.menu=tk.Menu(mbZ)
        mbZ["menu"]=mbZ.menu
        mbZ.menu.add_command(label="Elévation de noued par rapport au Datum")
        mbZ.grid(row=14,column=4,sticky="W")
        global d1
        global a1
        global l1
        global Z1
        d1=[]
        a1=[]
        l1=[]
        Z1=[]
        #input d:diamètre des conduites ,a:célérite d'onde de pression des conduites , l: longueur des conduites 
        for i in range(0,nc):
                d_entry=tk.Entry(pipe_frame,bg='#C4CCCE')
                d_entry.grid(row=16+i,column=1)
                d1.append(d_entry)
                a_entry=tk.Entry(pipe_frame,bg='#C4CCCE')
                a_entry.grid(row=16+i,column=2)
                a1.append(a_entry)
                l_entry=tk.Entry(pipe_frame,bg='#C4CCCE')
                l_entry.grid(row=16+i,column=3)
                l1.append(l_entry)
        #input les elevations d'extrimité de chaque conduite 
        for i in range(0,nc+1):    
                Z_entry=tk.Entry(pipe_frame,bg='#C4CCCE')
                Z_entry.grid(row=16+i,column=4)
                Z1.append(Z_entry)  
    #text
    canvas2.create_text(390,100, text='- Discrétisation de la 1ere  conduite: nombre de ségments n',fill='black',font=('Arial',12))
    canvas2.create_text(362,150, text='- Coefficient de frottement de Darcy_Weisbach: f [-]',fill='black',font=('Arial',12))
    canvas2.create_text(285,200, text='- Nombre de conduites: nc [-]',fill='black',font=('Arial',12))
    #button
    entrer_B=tk.Button(page2,text='Entrer',command=pipe,font=('Arial',10,'bold'),bg='red',fg='white',bd=2,width=20)
    canvas2.create_window(520 ,200,window=entrer_B)                             
#page3    
    page3=ttk.Frame(tab,width= 1330,height=540)    
    tab.add(page3,text='Vanne')
    ##canvas
    canvas3= tk.Canvas(page3,width=1330, height=540,bg='white')
    ##image
    infovanne_im=Image.open(r'photos\infovanne.png')
    infovanne_im = ImageTk.PhotoImage(infovanne_im.resize((500,300), Image.ANTIALIAS))
    canvas3.create_image(900, 150, image=infovanne_im)
    canvas3.image = infovanne_im
    #entry 
    Q0in=tk.StringVar()
    Q0in.set(0.75)# les valeurs prédéfinies 
    Q0_entry=tk.Entry(page3,textvariable=Q0in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas3.create_window(100, 190,window= Q0_entry)
      
    tfin=tk.StringVar()
    tfin.set(0)# les valeurs prédéfinies 
    tf_entry=tk.Entry(page3,textvariable=tfin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas3.create_window(100, 240,window= tf_entry)    
    #text
    canvas3.create_text(315,190, text="- Débit initial d’écoulement: Q0 [m3/s]",fill='black',font=('Arial',12))
    canvas3.create_text(320,240, text="- Temps de fermeture de la vanne: tf [s]",fill='black',font=('Arial',12)) 
#page4
    page4=ttk.Frame(tab,width= 1330,height=540) 
    tab.add(page4,text="Réservoir d'air ")
    ##canvas
    canvas4= tk.Canvas(page4,width=1330, height=540,bg='white')
    ##image
    jonctairchamberinfo_im=Image.open(r'photos\jonctairchamber info.png')
    jonctairchamberinfo_im = ImageTk.PhotoImage(jonctairchamberinfo_im.resize((700,500), Image.ANTIALIAS))
    canvas4.create_image(950,250, image=jonctairchamberinfo_im)
    canvas4.image = jonctairchamberinfo_im
    #entry     
    Dcin=tk.StringVar()
    Dcin.set(0.5)# les valeurs prédéfinies 
    Dc_entry=tk.Entry(page4,textvariable=Dcin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas4.create_window(100, 100,window= Dc_entry)
        
    Vairchin=tk.StringVar()
    Vairchin.set(4)# les valeurs prédéfinies 
    Vairch_entry=tk.Entry(page4,textvariable=Vairchin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas4.create_window(100, 150,window= Vairch_entry)
    
    Voairin=tk.StringVar()
    Voairin.set('')# les valeurs prédéfinies
    Voair_entry=tk.Entry(page4,textvariable=Voairin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10,state='disabled')                     
    canvas4.create_window(75, 250,window= Voair_entry)
    
    Hoairin=tk.StringVar()
    Hoairin.set('')# les valeurs prédéfinies 
    Hoair_entry=tk.Entry(page4,textvariable=Hoairin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10,state='disabled')
    canvas4.create_window(200, 250,window= Hoair_entry)
    
    def airselecte(V_entry,H_entry,Hin,Vin,combobox):
        if combobox.get()=="- Le volume d'air initiale:voair[m3]":
                 V_entry.config(state='normal')
                 Vin.set(0.5)# les valeurs prédéfinies
                 H_entry.config(state='disabled')
                 Hin.set('None')

        if combobox.get()=="- La pression d'air initiale: Hoair[m]":
                 H_entry.config(state='normal') 
                 Hin.set(96)
                 V_entry.config(state='disabled')
                 Vin.set('None')
                 
                   
    Corf_inflowin=tk.StringVar()
    Corf_inflowin.set(0.5)# les valeurs prédéfinies 
    Corf_inflow_entry=tk.Entry(page4,textvariable=Corf_inflowin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas4.create_window(100, 300,window= Corf_inflow_entry)
               
    Corf_outflowin=tk.StringVar()
    Corf_outflowin.set(0.3)# les valeurs prédéfinies 
    Corf_outflow_entry=tk.Entry(page4,textvariable=Corf_outflowin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas4.create_window(100, 350,window=Corf_outflow_entry)  
    
    Min=tk.StringVar()
    Min.set(200)# les valeurs prédéfinies 
    M_entry=tk.Entry(page4,textvariable=Min,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas4.create_window(100, 400,window= M_entry)
    
    c1in=tk.StringVar()
    c1in.set(2)# les valeurs prédéfinies 
    c1_entry=tk.Entry(page4,textvariable=c1in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas4.create_window(100, 450,window= c1_entry)
       
    ##combobox
    aircombobox = ttk.Combobox(page4, values=[
                                    "- Le volume d'air initiale:voair[m3]", 
                                    "- La pression d'air initiale: Hoair[m]"],width=35)
    aircombobox.insert(0,'sélectionnez une réponse')
    aircombobox.bind('<<ComboboxSelected>>',lambda event:airselecte(Voair_entry,Hoair_entry,Hoairin,Voairin,aircombobox))
    canvas4.create_window(130, 200,window=aircombobox)
    #text
    canvas4.create_text(308,100, text="- Diamètre de reservoir d'air: Dc[m]",fill='black',font=('Arial',12))
    canvas4.create_text(340,145, text="- Le volume totale du rervoir d'air: vairch[m3]",fill='black',font=('Arial',12))
    canvas4.create_text(342,200 ,text="- Sélectionnez une réponse",fill='black',font=('Arial',12))
    canvas4.create_text(73,220 ,text="- Le volume d'air",fill='black',font=('Arial',12))
    canvas4.create_text(208,220,text="- La pression d'air",fill='black',font=('Arial',12))
    canvas4.create_text(373,300, text="- Coef perte de charge d'orifice (inflow):Corf_inflow[-]",fill='black',font=('Arial',12))
    canvas4.create_text(379,350, text="- Coef perte de charge d'orifice (outflow):Corf_outflow[-]",fill='black',font=('Arial',12))
    canvas4.create_text(345,400, text="- Position de reservoir à partir de vanne: M[m]",fill='black',font=('Arial',12))
    canvas4.create_text(330,455, text="- Le reservoir se trouve dans la conduite \n N°=: C1[-]",fill='black',font=('Arial',12))    
#page5    
    page5=ttk.Frame(tab,width= 1330,height=615)    
    tab.add(page5,text='Exécuter')
    ##canvas
    canvas5= tk.Canvas(page5,width=1330, height=615,bg='white')
    ##frame
    graph_frame=tk.Frame(page5,bg='white')
    canvas5.create_window(840,300,window=graph_frame)    
    #entry     
    Tin=tk.StringVar()
    Tin.set(50)# les valeurs prédéfinies 
    T_entry=tk.Entry(page5,textvariable=Tin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas5.create_window(80,50,window= T_entry)
        
    xin=tk.StringVar()
    xin.set(0)# les valeurs prédéfinies 
    x_entry=tk.Entry(page5,textvariable=xin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas5.create_window(80,110,window= x_entry) 
    
    cin=tk.StringVar()
    cin.set(1)# les valeurs prédéfinies 
    c_entry=tk.Entry(page5,textvariable=cin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas5.create_window(80,180,window= c_entry)   
    #text
    canvas5.create_text(85,25, text="- Temps de simulation:T [s]",fill='black',font=('Arial',10))
    canvas5.create_text(120,80, text="- Point spatial à partir du réservoir: x [m]",fill='black',font=('Arial',10))
    canvas5.create_text(118,145, text="- Le point x se trouve dans la conduite \n N°=: C[-]",fill='black',font=('Arial',10))
    #button                      
    exécuter_B=tk.Button(page5,width=10,text='Exécuter',font=('Arial',12,'bold'),bg='#2AA321',fg='white',bd=2,
command=lambda:algo6.display_result(page5,canvas5,graph_frame,Hres_entry,k_entry,n_entry,f_entry,nc_entry,l1,d1,a1,Z1,Q0_entry,tf_entry,Dc_entry,Vairch_entry,Voair_entry,Hoair_entry,Corf_inflow_entry,Corf_outflow_entry,M_entry,c1_entry,c_entry,T_entry,x_entry).grid(column=1, row=1))
    canvas5.create_window(80,220,window=exécuter_B)  
    
    enregistrer_B=tk.Button(page5,width=10,text='Enregistrer',font=('Arial',12,'bold'),bg='blue',fg='white',bd=2,
command=lambda:algo6.save(Hres_entry,k_entry,n_entry,f_entry,nc_entry,l1,d1,a1,Z1,Q0_entry,tf_entry,Dc_entry,Vairch_entry,Voair_entry,Hoair_entry,Corf_inflow_entry,Corf_outflow_entry,M_entry,c1_entry,c_entry,T_entry,x_entry))
    canvas5.create_window(80 ,270,window=enregistrer_B)  

    """ activate widgets"""     
    canvas1.place(x=0,y=0) 
    canvas2.place(x=0,y=0)
    canvas3.place(x=0,y=0)
    canvas4.place(x=0,y=0)
    canvas5.place(x=0,y=0)
    tab.place(x=15,y=60)  
# %% le systeme simple (reservoir conduite-en-parallèle vanne)+cheminee d'equilibre [line 2693 to 2965]
def airchamber_type3():
    """ create widgets """
    top=tk.Toplevel()
    top.state('zoomed')
    top.iconbitmap(r'photos\images.ico')
    top.title("Réservoir-conduite en parallèle-vanne avec protection (reservoir d'air)")
    tab=ttk.Notebook(top)

    #button       
    project_B=tk.Button(top,text='Paramètres d’entrée' ,bg='#20A9CE',
                    fg='white',bd=0,font=('Arial',20,'bold'),height=1, width =25) 
    project_B.place(x=400,y=10) 
    
#page1
    page1 =ttk.Frame(tab,width=1330,height=700)
    tab.add(page1,text='Réservoir')
    ##canvas
    canvas1= tk.Canvas(page1,width=1330, height=700,bg='white')
    #entry
    Hresin=tk.StringVar()
    Hresin.set(100)# les valeurs prédéfinies 
    Hres_entry=tk.Entry(page1,textvariable=Hresin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas1.create_window(100, 140,window= Hres_entry)
    
    kin=tk.StringVar()
    kin.set(0.5)# les valeurs prédéfinies 
    k_entry=tk.Entry(page1,textvariable=kin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas1.create_window(100, 200,window=k_entry)

    #text
    canvas1.create_text(330,140, text="- Niveau d’eau dans le réservoir: Hres [m]",fill='black',font=('Arial',12))
    canvas1.create_text(348,200, text='- Coefficient de perte de charge singulière: k[-]',fill='black',font=('Arial',12))
    #images
    inforeservoir_im=Image.open(r'photos\inforeservoir.png')
    inforeservoir_im = ImageTk.PhotoImage(inforeservoir_im.resize((700,300), Image.ANTIALIAS))
    canvas1.create_image(1000, 250, image=inforeservoir_im)
    canvas1.image = inforeservoir_im
#page2    
    page2 =ttk.Frame(tab,width= 1330,height=600)
    tab.add(page2,text='Conduite et Vanne')
    ##canvas
    canvas2= tk.Canvas(page2,width=1330, height=600,bg='white')
    #frame
    pipe_frame=tk.Frame(canvas2,bg='white')
    canvas2.create_window((10,290),window= pipe_frame,anchor='nw')
    #images
    branchpipeinfo_im=Image.open(r'photos\branchpipeinfo.png')
    branchpipeinfo_im = ImageTk.PhotoImage(branchpipeinfo_im.resize((700,500), Image.ANTIALIAS))
    canvas2.create_image(1000, 270, image=branchpipeinfo_im)
    canvas2.image = branchpipeinfo_im
    #entry
    Q0in=tk.StringVar()
    Q0in.set(0.75)# les valeurs prédéfinies 
    Q0_entry=tk.Entry(page2,textvariable=Q0in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 100,window= Q0_entry)
    
    nin=tk.StringVar()
    nin.set(2)# les valeurs prédéfinies 
    n_entry=tk.Entry(page2,textvariable=nin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 150,window= n_entry)
    
    fin=tk.StringVar()
    fin.set(0.04)# les valeurs prédéfinies 
    f_entry=tk.Entry(page2,textvariable=fin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100, 200,window= f_entry)    
    
    ncin=tk.StringVar()
    ncin.set('')# les valeurs prédéfinies 
    nc_entry=tk.Entry(page2,textvariable=ncin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas2.create_window(100,250,window= nc_entry)
    
    def pipe(): # conduite est une fonction pour afficher et saisir les caractristiques("D,L,a") de chaque conduite  
        for child in pipe_frame.winfo_children():
            child.destroy()
        nc=int(nc_entry.get())
        # les syntaxes ci dessous sont relatives à l'interface graphique
        
        mbd=tk.Menubutton (pipe_frame,text='           D[m]         ',font=('Arial',10,'bold'),relief='groove',bg='white',width=15)
        mbd.menu=tk.Menu(mbd)
        mbd["menu"]=mbd.menu
        mbd.menu.add_command(label="Diamètre de la conduite")
        mbd.menu.add_command(label="Premiere ligne pour la conduite principale")
        mbd.grid(row=15,column=1,sticky="W")
        
        mbL=tk.Menubutton (pipe_frame,text='           L[m]          ',font=('Arial',10,'bold'),relief='groove',bg='white',width=15)
        mbL.menu=tk.Menu(mbL)
        mbL["menu"]=mbL.menu
        mbL.menu.add_command(label="Longueur de la conduite")
        mbL.menu.add_command(label="Premiere ligne pour la conduite principale")
        mbL.grid(row=15,column=3,sticky="W")
        
        mbZ=tk.Menubutton (pipe_frame,text='           Z[m]         ',font=('Arial',10,'bold'),relief='groove',bg='white',width=15)
        mbZ.menu=tk.Menu(mbZ)
        mbZ["menu"]=mbZ.menu
        mbZ.menu.add_command(label='Elévation de noued par rapport au Datum' )
        mbZ.menu.add_command(label="Premiere ligne pour la conduite principale")
        mbZ.grid(row=15,column=4,sticky="W")
        
        mbtf=tk.Menubutton (pipe_frame,text='             tf[s]          ',font=('Arial',10,'bold'),relief='groove',bg='white',width=15)
        mbtf.menu=tk.Menu(mbtf)
        mbtf["menu"]=mbtf.menu
        mbtf.menu.add_command(label="Temps de fermeture de la vanne")
        mbtf.grid(row=15,column=5,sticky="W")
        
        mba=tk.Menubutton (pipe_frame,text='          a[m/s]        ',font=('Arial',10,'bold'),relief='groove',bg='#75E25A',width=15)
        mba.menu=tk.Menu(mba)
        mba["menu"]=mba.menu
        mba.menu.add_command(label="Célérité de l’onde de pression")
        mba.menu.add_command(label="Exécuter",command=wave_calculator_window)
        mba.grid(row=15,column=2,sticky="W")
        global d1
        global a1
        global l1
        global Z1
        global tf1    
        d1=[]
        a1=[]
        l1=[]
        Z1=[]
        tf1=[]
        #input d:diamètre des conduites ,a:célérite d'onde de pression des conduites , l: longueur des conduites
        for i in range(0,nc+1):
                d_entry=tk.Entry(pipe_frame,bg='#C4CCCE',width=20)
                d_entry.grid(row=16+i,column=1)
                d1.append(d_entry)
                a_entry=tk.Entry(pipe_frame,bg='#C4CCCE',width=20)
                a_entry.grid(row=16+i,column=2)
                a1.append(a_entry)
                l_entry=tk.Entry(pipe_frame,bg='#C4CCCE',width=20)
                l_entry.grid(row=16+i,column=3)
                l1.append(l_entry)
        for i in range(0,nc+2):    
                Z_entry=tk.Entry(pipe_frame,bg='#C4CCCE',width=20)
                Z_entry.grid(row=16+i,column=4)
                Z1.append(Z_entry)
        for i in range(0,nc):    
                tf_entry=tk.Entry(pipe_frame,bg='#C4CCCE',width=20)
                tf_entry.grid(row=17+i,column=5)
                tf1.append(tf_entry) 
    #text
    canvas2.create_text(315,100, text="- Débit initial d’écoulement: Q0 [m3/s]",fill='black',font=('Arial',12))
    canvas2.create_text(392,150, text='- Discrétisation de la 1ere  conduite: nombre de ségments n',fill='black',font=('Arial',12))
    canvas2.create_text(362,200, text='- Coefficient de frottement de Darcy_Weisbach: f [-]',fill='black',font=('Arial',12))
    canvas2.create_text(385,250, text='- Nombre de conduites liées à la conduite principale: nc [-]',fill='black',font=('Arial',12))
    #button
    entrer_B=tk.Button(page2,text='Entrer',command=pipe,font=('Arial',10,'bold'),bg='red',fg='white',bd=2,width=10)
    canvas2.create_window(590 ,275,window=entrer_B)              
#page3
    page3=ttk.Frame(tab,width= 1330,height=540) 
    tab.add(page3,text="Reservoir d'air ")
    ##canvas
    canvas3= tk.Canvas(page3,width=1330, height=540,bg='white')
    ##image
    branchairchamberinfo_im=Image.open(r'photos\branchair chamberinfo.png')
    branchairchamberinfo_im = ImageTk.PhotoImage(branchairchamberinfo_im.resize((680,400), Image.ANTIALIAS))
    canvas3.create_image(950,250, image=branchairchamberinfo_im)
    canvas3.image = branchairchamberinfo_im

    #entry     
    Dcin=tk.StringVar()
    Dcin.set(0.5)# les valeurs prédéfinies 
    Dc_entry=tk.Entry(page3,textvariable=Dcin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas3.create_window(100, 100,window= Dc_entry)
        
    Vairchin=tk.StringVar()
    Vairchin.set(4)# les valeurs prédéfinies 
    Vairch_entry=tk.Entry(page3,textvariable=Vairchin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas3.create_window(100, 150,window= Vairch_entry)
    
    Voairin=tk.StringVar()
    Voairin.set('')# les valeurs prédéfinies
    Voair_entry=tk.Entry(page3,textvariable=Voairin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10,state='disabled')                     
    canvas3.create_window(75, 250,window= Voair_entry)
    
    Hoairin=tk.StringVar()
    Hoairin.set('')# les valeurs prédéfinies 
    Hoair_entry=tk.Entry(page3,textvariable=Hoairin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'),width=10,state='disabled')
    canvas3.create_window(200, 250,window= Hoair_entry)
    
    def airselecte(V_entry,H_entry,Hin,Vin,combobox):
        if combobox.get()=="- Le volume d'air initiale:voair[m3]":
                 V_entry.config(state='normal')
                 Vin.set(0.5)# les valeurs prédéfinies
                 H_entry.config(state='disabled')
                 Hin.set('None')

        if combobox.get()=="- La pression d'air initiale: Hoair[m]":
                 H_entry.config(state='normal') 
                 Hin.set(96)
                 V_entry.config(state='disabled')
                 Vin.set('None')
                 
                   
    Corf_inflowin=tk.StringVar()
    Corf_inflowin.set(0.5)# les valeurs prédéfinies 
    Corf_inflow_entry=tk.Entry(page3,textvariable=Corf_inflowin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas3.create_window(100, 300,window= Corf_inflow_entry)
               
    Corf_outflowin=tk.StringVar()
    Corf_outflowin.set(0.3)# les valeurs prédéfinies 
    Corf_outflow_entry=tk.Entry(page3,textvariable=Corf_outflowin,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas3.create_window(100, 350,window=Corf_outflow_entry)  
    
    Min=tk.StringVar()
    Min.set(200)# les valeurs prédéfinies 
    M_entry=tk.Entry(page3,textvariable=Min,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas3.create_window(100, 400,window= M_entry)
    
    c1in=tk.StringVar()
    c1in.set(2)# les valeurs prédéfinies 
    c1_entry=tk.Entry(page3,textvariable=c1in,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'), width =15)
    canvas3.create_window(100, 450,window= c1_entry)
       
    ##combobox
    aircombobox = ttk.Combobox(page3, values=[
                                    "- Le volume d'air initiale:voair[m3]", 
                                    "- La pression d'air initiale: Hoair[m]"],width=35)
    aircombobox.insert(0,'sélectionnez une réponse')
    aircombobox.bind('<<ComboboxSelected>>',lambda event:airselecte(Voair_entry,Hoair_entry,Hoairin,Voairin,aircombobox))
    canvas3.create_window(130, 200,window=aircombobox)
    #text
    canvas3.create_text(308,100, text="- Diamètre de reservoir d'air: Dc[m]",fill='black',font=('Arial',12))
    canvas3.create_text(340,145, text="- Le volume totale du rervoir d'air: vairch[m3]",fill='black',font=('Arial',12))
    canvas3.create_text(342,200 ,text="- Sélectionnez une réponse",fill='black',font=('Arial',12))
    canvas3.create_text(73,220 ,text="- Le volume d'air",fill='black',font=('Arial',12))
    canvas3.create_text(208,220,text="- La pression d'air",fill='black',font=('Arial',12))
    canvas3.create_text(373,300, text="- Coef perte de charge d'orifice (inflow):Corf_inflow[-]",fill='black',font=('Arial',12))
    canvas3.create_text(379,350, text="- Coef perte de charge d'orifice (outflow):Corf_outflow[-]",fill='black',font=('Arial',12))
    canvas3.create_text(335,400, text="- Position de reservoir à partir d'extrémité \n  droite de conduite: M[m]",fill='black',font=('Arial',12))
    canvas3.create_text(330,455, text="- Le reservoir se trouve dans la conduite \n N°=: C1[-]",fill='black',font=('Arial',12))
#page4    
    page4=ttk.Frame(tab,width= 1330,height=615)    
    tab.add(page4,text='Exécuter')
    ##canvas
    canvas4= tk.Canvas(page4,width=1330, height=615,bg='white')
    ##frame
    graph_frame=tk.Frame(page4,bg='white')
    canvas4.create_window(840,300,window=graph_frame)  
    #entry     
    Tin=tk.StringVar()
    Tin.set(50)# les valeurs prédéfinies 
    T_entry=tk.Entry(page4,textvariable=Tin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas4.create_window(80,50,window= T_entry)
        
    xin=tk.StringVar()
    xin.set(0)# les valeurs prédéfinies 
    x_entry=tk.Entry(page4,textvariable=xin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas4.create_window(80,110,window= x_entry) 
    
    cin=tk.StringVar()
    cin.set(1)# les valeurs prédéfinies 
    c_entry=tk.Entry(page4,textvariable=cin,width=10,bg='#C4CCCE',fg='black',font=('Arial',15,'bold'))
    canvas4.create_window(80,170,window= c_entry)   
    #text
    canvas4.create_text(85,25, text="- Temps de simulation:T [s]",fill='black',font=('Arial',10))
    canvas4.create_text(180,80, text="- Point spatial à partir d'extrémité gauche de conduite: x [m]",fill='black',font=('Arial',10))
    canvas4.create_text(120,140, text="- Le point x se trouve dans la conduite \n N°=:",fill='black',font=('Arial',10))
    #button       
    exécuter_B=tk.Button(page4,width=10,text='Exécuter',font=('Arial',12,'bold'),bg='#2AA321',fg='white',bd=2,
command=lambda:algo9.display_result(page4,canvas4,graph_frame,Hres_entry,k_entry,Q0_entry,n_entry,f_entry,nc_entry,l1,d1,a1,Z1,tf1,Dc_entry,Vairch_entry,Voair_entry,Hoair_entry,Corf_inflow_entry,Corf_outflow_entry,M_entry,c1_entry,c_entry,T_entry,x_entry).grid(row=1,column=1))
    canvas4.create_window(80,210,window=exécuter_B)  
    
    enregistrer_B=tk.Button(page4,width=10,text='Enregistrer',font=('Arial',12,'bold'),bg='blue',fg='white',bd=2,
command=lambda:algo9.save(Hres_entry,k_entry,Q0_entry,n_entry,f_entry,nc_entry,l1,d1,a1,Z1,tf1,Dc_entry,Vairch_entry,Voair_entry,Hoair_entry,Corf_inflow_entry,Corf_outflow_entry,M_entry,c1_entry,c_entry,T_entry,x_entry))
    canvas4.create_window(80 ,260,window=enregistrer_B)  

    """ activate widgets"""     
    canvas1.place(x=0,y=0) 
    canvas2.place(x=0,y=0)
    canvas3.place(x=0,y=0)
    canvas4.place(x=0,y=0)
    tab.place(x=15,y=60)      
# %% choisir l'element de protection [line 2966 to 3112]
def with_without_protection1():
    """ create widgets """
    top=tk.Toplevel()
    top.state('zoomed')
    top.iconbitmap(r'photos\images.ico')
    top.title("Réservoir-conduite-vanne")
    w, h = top.winfo_screenwidth(),top.winfo_screenheight()
    
    ##canvas
    canvas= tk.Canvas(top,width=w, height=h,bg='white')  
    canvas1=tk.Canvas(top,width=400, height=800,bg='#20A9CE')  
##images
    button_im=Image.open(r'photos\main button.png')
    button_im=tk.PhotoImage(file=r'photos\main button.png',master=canvas)
    canvas.image0 = button_im
    
    X_im=Image.open(r'photos\x.png')
    X_im = ImageTk.PhotoImage(X_im.resize((130,120), Image.ANTIALIAS))
    canvas.create_image(600, 100, image=X_im)
    canvas.image1 = X_im
    
    surge_tank_im=Image.open(r'photos\surge tank.png')
    surge_tank_im = ImageTk.PhotoImage(surge_tank_im.resize((130,120), Image.ANTIALIAS))
    canvas.create_image(600, 300, image=surge_tank_im)
    canvas.image2 = surge_tank_im
    
    air_chamber_im=Image.open(r'photos\air chamber.png')
    air_chamber_im = ImageTk.PhotoImage(air_chamber_im.resize((130,120), Image.ANTIALIAS))
    canvas.create_image(600, 500, image=air_chamber_im)
    canvas.image3 =air_chamber_im
##buttons
    project_B=tk.Button(top,text='Réservoir-conduite-vanne ' ,bg='white',
                    fg='#20A9CE',bd=0,font=('Arial',15,'bold'),height=1, width =25)
    button1=tk.Button(top,image=button_im,text="Sans Protection",compound="center",command=no_protection_type1,
                      font=('Arial',11,'bold'),height=60, width =300,bd=0,fg='#3961AB')
    button2=tk.Button(top,image=button_im,text="Avec Protection (cheminée d’équilibre )",compound="center",command=surgetank_type1,
                      font=('Arial',11,'bold'),height=60, width =300,bd=0,fg='#3961AB')
    button3=tk.Button(top,image=button_im,text="Avec protection (Reservoir d'air )" , compound="center",command=airchamber_type1,
                      font=('Arial',11,'bold'),height=60, width =300,bd=0,fg='#3961AB')
                      
    canvas.create_window(200 ,50,window=project_B)
    canvas.create_window(900 ,100,window=button1)
    canvas.create_window(900 ,300,window=button2)
    canvas.create_window(900 ,500,window=button3)

    """ activate widgets"""    
    canvas.place(x=-1.5,y=-1.5) 
    canvas1.place(x=-1.5,y=-1.5) 
    
def with_without_protection2():
    """ create widgets """
    top=tk.Toplevel()
    top.state('zoomed')
    top.iconbitmap(r'photos\images.ico')
    top.title("Réservoir-multi jonctions")
    w, h = top.winfo_screenwidth(),top.winfo_screenheight()
    
    ##canvas
    canvas= tk.Canvas(top,width=w, height=h,bg='white')  
    canvas1=tk.Canvas(top,width=400, height=800,bg='#20A9CE')  
##images
    button_im=Image.open(r'photos\main button.png')
    button_im=tk.PhotoImage(file=r'photos\main button.png',master=canvas)
    canvas.image0 = button_im
    
    X_im=Image.open(r'photos\x.png')
    X_im = ImageTk.PhotoImage(X_im.resize((130,120), Image.ANTIALIAS))
    canvas.create_image(600, 100, image=X_im)
    canvas.image1 = X_im
    
    surge_tank_im=Image.open(r'photos\surge tank.png')
    surge_tank_im = ImageTk.PhotoImage(surge_tank_im.resize((130,120), Image.ANTIALIAS))
    canvas.create_image(600, 300, image=surge_tank_im)
    canvas.image2 = surge_tank_im
    
    air_chamber_im=Image.open(r'photos\air chamber.png')
    air_chamber_im = ImageTk.PhotoImage(air_chamber_im.resize((130,120), Image.ANTIALIAS))
    canvas.create_image(600, 500, image=air_chamber_im)
    canvas.image3 =air_chamber_im
##buttons
    project_B=tk.Button(top,text='Réservoir-multi jonctions ' ,bg='white',
                    fg='#20A9CE',bd=0,font=('Arial',15,'bold'),height=1, width =25)
    button1=tk.Button(top,image=button_im,text="Sans Protection",compound="center",font=('Arial',11,'bold'),
                     command= no_protection_type2, height=60, width =300,bd=0,fg='#3961AB')
    button2=tk.Button(top,image=button_im,text="Avec Protection (cheminée d’équilibre )",compound="center",font=('Arial',11,'bold'),
                      command=surgetank_type2,height=60, width =300,bd=0,fg='#3961AB')
    button3=tk.Button(top,image=button_im,text="Avec protection (Reservoir d'air )" , compound="center",font=('Arial',11,'bold'),
                      command=airchamber_type2,height=60, width =300,bd=0,fg='#3961AB')
                      
    canvas.create_window(200 ,50,window=project_B)
    canvas.create_window(900 ,100,window=button1)
    canvas.create_window(900 ,300,window=button2)
    canvas.create_window(900 ,500,window=button3)

    """ activate widgets"""    
    canvas.place(x=-1.5,y=-1.5) 
    canvas1.place(x=-1.5,y=-1.5)  
    
def with_without_protection3():
    """ create widgets """
    top=tk.Toplevel()
    top.state('zoomed')
    top.iconbitmap(r'photos\images.ico')
    top.title("Réservoir-multi branchements")
    w, h = top.winfo_screenwidth(),top.winfo_screenheight()
    
    ##canvas
    canvas= tk.Canvas(top,width=w, height=h,bg='white')  
    canvas1=tk.Canvas(top,width=400, height=800,bg='#20A9CE')  
##images
    button_im=Image.open(r'photos\main button.png')
    button_im=tk.PhotoImage(file=r'photos\main button.png',master=canvas)
    canvas.image0 = button_im
    
    X_im=Image.open(r'photos\x.png')
    X_im = ImageTk.PhotoImage(X_im.resize((130,120), Image.ANTIALIAS))
    canvas.create_image(600, 100, image=X_im)
    canvas.image1 = X_im
    
    surge_tank_im=Image.open(r'photos\surge tank.png')
    surge_tank_im = ImageTk.PhotoImage(surge_tank_im.resize((130,120), Image.ANTIALIAS))
    canvas.create_image(600, 300, image=surge_tank_im)
    canvas.image2 = surge_tank_im
    
    air_chamber_im=Image.open(r'photos\air chamber.png')
    air_chamber_im = ImageTk.PhotoImage(air_chamber_im.resize((130,120), Image.ANTIALIAS))
    canvas.create_image(600, 500, image=air_chamber_im)
    canvas.image3 =air_chamber_im
##buttons
    project_B=tk.Button(top,text='Réservoir-multi branchements ' ,bg='white',
                    fg='#20A9CE',bd=0,font=('Arial',15,'bold'),height=1, width =25)
    button1=tk.Button(top,image=button_im,text="Sans Protection",compound="center",font=('Arial',11,'bold'),
                      command=no_protection_type3,height=60, width =300,bd=0,fg='#3961AB')
    button2=tk.Button(top,image=button_im,text="Avec Protection (cheminée d’équilibre )",compound="center",font=('Arial',11,'bold'),
                      command=surgetank_type3,height=60, width =300,bd=0,fg='#3961AB')
    button3=tk.Button(top,image=button_im,text="Avec protection (Reservoir d'air )" , compound="center",font=('Arial',11,'bold'),
                     command=airchamber_type3, height=60, width =300,bd=0,fg='#3961AB')
                      
    canvas.create_window(200 ,50,window=project_B)
    canvas.create_window(900 ,100,window=button1)
    canvas.create_window(900 ,300,window=button2)
    canvas.create_window(900 ,500,window=button3)

    """ activate widgets"""    
    canvas.place(x=-1.5,y=-1.5) 
    canvas1.place(x=-1.5,y=-1.5)      
# %% type de systeme(simple,en serie,en parallele) [line 3113 to 3160 ]
def system_type():
    """ create widgets """
    top=tk.Toplevel()
    top.state('zoomed')
    top.iconbitmap(r'photos\images.ico')
    top.title("Nouveau Projet")
    w, h = top.winfo_screenwidth(),top.winfo_screenheight()
##canvas
    canvas= tk.Canvas(top,width=w, height=h,bg='white')  
    canvas1=tk.Canvas(top,width=400, height=800,bg='#20A9CE')  
##images
    button_im=Image.open(r'photos\main button.png')
    button_im=tk.PhotoImage(file=r'photos\main button.png',master=canvas)
    canvas.image0 = button_im
    
    type1_im=Image.open(r'photos\h1.png')
    type1_im=tk.PhotoImage(file=r'photos\h1.png',master=canvas)
    canvas.create_image(600, 100, image=type1_im)
    canvas.image1 = type1_im
    
    type2_im=Image.open(r'photos\h2.png')
    type2_im=tk.PhotoImage(file=r'photos\h2.png',master=canvas)
    canvas.create_image(600, 300, image=type2_im)
    canvas.image2 = type2_im
    
    type3_im=Image.open(r'photos\h3.png')
    type3_im=tk.PhotoImage(file=r'photos\h3.png',master=canvas)
    canvas.create_image(600, 500, image=type3_im)
    canvas.image3 =type3_im
##buttons
    project_B=tk.Button(top,text='Nouveau Projet ' ,bg='white',
                    fg='#20A9CE',bd=0,font=('Arial',15,'bold'),height=1, width =25)
    button1=tk.Button(top,image=button_im,text="Réservoir-conduite-vanne",command=with_without_protection1, 
                      compound="center",font=('Arial',15,'bold'),height=60, width =300,bd=0,fg='#3961AB')
    button2=tk.Button(top,image=button_im,text="Réservoir-multi jonctions",command=with_without_protection2,
                      compound="center",font=('Arial',15,'bold'),height=60, width =300,bd=0,fg='#3961AB')
    button3=tk.Button(top,image=button_im,text="Réservoir-multi branchements",command=with_without_protection3,
                      compound="center",font=('Arial',15,'bold'),height=60, width =300,bd=0,fg='#3961AB')
                      
    canvas.create_window(200 ,50,window=project_B)
    canvas.create_window(900 ,100,window=button1)
    canvas.create_window(900 ,300,window=button2)
    canvas.create_window(900 ,500,window=button3)

    """ activate widgets"""    
    canvas.place(x=-1.5,y=-1.5) 
    canvas1.place(x=-1.5,y=-1.5) 
# %% les information [line 3161 to 3196]
def about_us():
    """ create widgets """
    top=tk.Toplevel()
    top.state('zoomed')
    top.iconbitmap(r'photos\images.ico')
    top.title("À propos")
    w, h = top.winfo_screenwidth(),top.winfo_screenheight()
##canvas
    canvas= tk.Canvas(top,width=w, height=h,bg='white')                      
    """ activate widgets"""    
    canvas.place(x=-1.5,y=-1.5) 
