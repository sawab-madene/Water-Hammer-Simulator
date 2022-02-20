# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 05:40:15 2020

@author: hp
"""
# %%bibliotheques
import tkinter as tk
from tkinter import ttk
import math 
import numpy 
import sympy
import sys
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import xlsxwriter
# %% zoom function
def zoom(combobox,Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,Z_ch,Qorf,Hair,Vair,position,x):   
    choice=combobox.get()
    if choice== "- Charge hydraulique H(m)":
            window=tk.Tk()
            window.state('zoomed')
            window.title(choice)
            window.iconbitmap(r'photos\images.ico')
            fig =Figure (figsize=(16,11), dpi=140)
            ax = fig.add_subplot(111) 
            fig.subplots_adjust( wspace=1.4, hspace=1)
            ax.grid(True)
            ax.plot(Time,(H[1:,position]))
            ax.plot(Time,H[1:,position],'b')
            ax.set_xlabel('Temps [s]')
            ax.set_ylabel('Charge hydraulique H(m)')
            ax.set_title("H(t) x=%s"%x)
            graph = FigureCanvasTkAgg(fig,master=window)
            graph.get_tk_widget().pack()
    if choice== "- Pression(m)":
            window=tk.Tk()
            window.state('zoomed')
            window.title(choice)
            window.iconbitmap(r'photos\images.ico')
            fig =Figure (figsize=(16,11), dpi=140)
            ax = fig.add_subplot(111) 
            fig.subplots_adjust( wspace=1.4, hspace=1)
            ax.grid(True)
            ax.plot(Time,h[1:,position])
            ax.set_xlabel("Temps [s]")
            ax.set_ylabel("pression (m)")
            ax.set_title("Pression (t) de x=%s"%x)
            graph = FigureCanvasTkAgg(fig,master=window)
            graph.get_tk_widget().pack()
    if choice== "- Enveloppe H(x)":
            window=tk.Tk()
            window.state('zoomed')
            window.title(choice)
            window.iconbitmap(r'photos\images.ico')
            fig =Figure (figsize=(16,11), dpi=140)
            ax = fig.add_subplot(111) 
            fig.subplots_adjust( wspace=1.4, hspace=1)
            ax.grid(True)
            ax.plot(Distance, Hmax, 'r',label='(Hmax)')
            ax.plot(Distance, Hmin, 'b',label='(Hmin)')
            ax.set_xlabel("Distance x[m]")
            ax.set_ylabel("Charge hydraulique H(m)")
            ax.set_title("Enveloppe H(x) ")
            ax.legend()
            graph = FigureCanvasTkAgg(fig,master=window)
            graph.get_tk_widget().pack()
    if choice== "- Enveloppe de pression (m)":
            window=tk.Tk()
            window.state('zoomed')
            window.title(choice)
            window.iconbitmap(r'photos\images.ico')
            fig =Figure (figsize=(16,11), dpi=140)
            ax = fig.add_subplot(111) 
            fig.subplots_adjust( wspace=1.4, hspace=1)
            ax.grid(True)
            ax.plot(Distance, hmax, 'r',label='(hmax)')
            ax.plot(Distance, hmin, 'b',label='(hmin)')
            ax.set_xlabel("Distance x[m]")
            ax.set_ylabel("pression h(m)")
            ax.set_title("Enveloppe pression(x) ") 
            ax.legend()
            graph = FigureCanvasTkAgg(fig,master=window)
            graph.get_tk_widget().pack()
    if choice=="- Débit volumique Q(m3/s)":
            window=tk.Tk()
            window.state('zoomed')
            window.title(choice)
            window.iconbitmap(r'photos\images.ico')
            fig =Figure (figsize=(16,11), dpi=140)
            ax = fig.add_subplot(111) 
            fig.subplots_adjust( wspace=1.4, hspace=1)
            ax.grid(True) 
            ax.plot(Time,Q[1:,position])
            ax.plot(Time,Q[1:,position],'r')
            ax.set_xlabel('Temps [s]')
            ax.set_ylabel('Débit volumique Q(m3/s)')        
            ax.set_title("Q(t) de x=%s"%x)  
            graph = FigureCanvasTkAgg(fig,master=window)
            graph.get_tk_widget().pack()
    if choice=="- debit d'orifice Qorifice(t) du reservoir d'air ":
            window=tk.Tk()
            window.state('zoomed')
            window.title(choice)
            window.iconbitmap(r'photos\images.ico')
            fig =Figure (figsize=(16,11), dpi=140)
            ax = fig.add_subplot(111) 
            fig.subplots_adjust( wspace=1.4, hspace=1)
            ax.grid(True)
            ax.plot(Time,Qorf[1:,])
            ax.set_xlabel("Temps [s]")
            ax.plot(Time,Qorf[1:,],'r')
            ax.set_ylabel("Qorf [m^3/s]")
            ax.set_title("Qorifice(t) du reservoir d'air ")  
            graph = FigureCanvasTkAgg(fig,master=window)
            graph.get_tk_widget().pack()
    if choice== "- Z(t) du reservoir d'air ":
            window=tk.Tk()
            window.state('zoomed')
            window.title(choice)
            window.iconbitmap(r'photos\images.ico')
            fig =Figure (figsize=(16,11), dpi=140)
            ax = fig.add_subplot(111) 
            fig.subplots_adjust( wspace=1.4, hspace=1)
            ax.grid(True)
            ax.plot(Time,Z_ch[1:])
            ax.set_xlabel("Temps [s]")
            ax.plot(Time,Z_ch[1:],'b')
            ax.set_ylabel("Z_ch [m]")
            ax.set_title("Z(t) du reservoir d'air ")
            graph = FigureCanvasTkAgg(fig,master=window)
            graph.get_tk_widget().pack()
    if choice== "- Volume d'air Vair(t) du reservoir d'air ":
            window=tk.Tk()
            window.state('zoomed')
            window.title(choice)
            window.iconbitmap(r'photos\images.ico')
            fig =Figure (figsize=(16,11), dpi=140)
            ax = fig.add_subplot(111) 
            fig.subplots_adjust( wspace=1.4, hspace=1)
            ax.grid(True)
            ax.plot(Time,Vair[1:])
            ax.set_xlabel("Temps [s]")
            ax.plot(Time,Vair[1:],'b')
            ax.set_ylabel("Vair [m3]")
            ax.set_title("Vair(t) du reservoir d'air ")
            graph = FigureCanvasTkAgg(fig,master=window)
            graph.get_tk_widget().pack()
    if choice=="- Charge hydraulique d'air Hair(t) du reservoir d'air ":
            window=tk.Tk()
            window.state('zoomed')
            window.title(choice)
            window.iconbitmap(r'photos\images.ico')
            fig =Figure (figsize=(16,11), dpi=140)
            ax = fig.add_subplot(111) 
            fig.subplots_adjust( wspace=1.4, hspace=1)
            ax.grid(True)
            ax.plot(Time,Hair[1:])
            ax.set_xlabel("Temps [s]")
            ax.plot(Time,Hair[1:],'b')
            ax.set_ylabel("Hair [m]")
            ax.set_title("Hair(t) du reservoir d'air ")
            graph = FigureCanvasTkAgg(fig,master=window)
            graph.get_tk_widget().pack()
                             
                                
# %% calcul [reservoir-conduite-vanne]+cheminee d'equilbre
def result(Hres,k,L,D,a,f,n,Z0,Z1,Dc,Vairch,Vooair,Hooair,Corf_inflow,Corf_outflow,M,Q0,tf,T):
    """calcule des paramtres"""
    g=9.81                     
    mgas=1.2                   #exposant m 
    eps=0.0001                 #tolerance de la methode newton
    Hb=10                      #pression atmospherique
    A=(math.pi*D**2)/4
    Ac=(math.pi*Dc**2)/4
    R=f/(2*D*A)
    Ca=g*A/a
    dx=L/n
    dt=dx/a
    n1=round((L-M)/dx)
    m=round(T/dt)
    """initialisation"""
    H=numpy.zeros((m+2,n+2))
    Hmax=numpy.zeros(n+2)  
    Hmin=numpy.zeros(n+2)
    hmax=numpy.zeros(n+2)  
    hmin=numpy.zeros(n+2)
    Q=numpy.zeros((m+2,n+2))
    h=numpy.zeros((m+2,n+2))
    Cp=numpy.zeros((m+1,n+2))
    Cn=numpy.zeros((m+1,n+2))
    Z_ch=numpy.zeros(m+2)
    Qorf=numpy.zeros(m+2)
    horf=numpy.zeros(m+2)
    Vair=numpy.zeros(m+2)
    Hair=numpy.zeros(m+2)
    Distance=numpy.zeros(n+2)
    Time=numpy.zeros(m+1)
    for j in range(m):
        Time[j+1]=Time[j]+dt
    for j in range(n+1):
        if j==n1:
            Distance[j+1]=Distance[j]
        else:
            Distance[j+1]=Distance[j]+dx
    """ symbols"""
    Zp=sympy.Symbol('Zp',real=True)
    """calcul""" 
    for i in range (m+2):
        for j in range(n+2):
            if i==0:                           #regime permanent
                if j<=n1:
                    Q[i][j]=Q0
                    H[i][j]=Hres-((1+k+(f*j*dx/D))*(Q[i][j]**2/(2*g*A**2)))
                    h[i][j]=H[i][j]-(Z0+((Z0-Z1)/L)*(dx*j))   
                else:
                    if j==n1+1:
                        Q[i][j]=Q[i][j-1]
                        H[i][j]=H[i][j-1]
                        h[i][j]=h[i][j-1]
                    else:
                        Q[i][j]=Q0
                        H[i][j]=Hres-((1+k+(f*(j-1)*dx/D))*(Q[i][j]**2/(2*g*A**2)))
                        h[i][j]=H[i][j]-(Z0+((Z0-Z1)/L)*(dx*(j-1)))
                Qorf[i]=0
                horf[i]=0
                if Hooair=='None':
                    Voair=float(Vooair)
                    Hoair=H[i][n1]-((Vairch-Voair)/Ac)+Hb             
                if Vooair=='None':
                    Hoair=float(Hooair)
                    Voair=Vairch-(H[i][n1]+Hb-Hoair)*Ac
                    
                Hair[i]=Hoair
                Vair[i]=Voair                   
                Z_ch[i]=H[i][n1]-Hair[i]+Hb     
                Cst=Hair[i]*Vair[i]**mgas
        
            elif i==1:                         #le regime a t=0
                Q[i][j]=Q[0][j]
                H[i][j]=H[0][j]
                h[i][j]=h[0][j]
            
                Qorf[i]=0
                horf[i]=0
                Hair[i]=Hair[0]
                Vair[i]=Vair[0]
                Z_ch[i]=Z_ch[0]
        
            else:                              #regime transitoir
                if j==0:# resvoir amont
                    k1=(Ca*(1+k))/(2*g*A**2)
                    if n1==0: #si le rservoir se trouve en niveau de la vanne
                        Cn[i-1][j]=Q[i-1][j+2]-Ca*H[i-1][j+2]-R*dt*Q[i-1][j+2]*abs(Q[i-1][j+2])
                    else:    
                        Cn[i-1][j]=Q[i-1][j+1]-Ca*H[i-1][j+1]-R*dt*Q[i-1][j+1]*abs(Q[i-1][j+1])
                    Q[i][j]=(-1+math.sqrt(1+4*k1*(Cn[i-1][j]+Ca*Hres)))/(2*k1)
                    if Q[i][j]>=0:
                        H[i][j]=Hres-(1+k)*((Q[i][j])**2)/(2*g*A**2)
                        h[i][j]=H[i][j]-(Z0+((Z0-Z1)/L)*(dx*j))
                    else:
                        H[i][j]=Hres-(1-k)*((Q[i][j])**2)/(2*g*A**2)
                        h[i][j]=H[i][j]-(Z0+((Z0-Z1)/L)*(dx*j))

                
                elif (j==n+1 and n1!=n):# vanne aval
                    if tf==0:#Dead END
                        tau=0   
                    elif (i-1)*dt<tf:  # Vanne avec temp de fermetue
                        tau=1-(((i-1)*dt)/tf)
                    else:
                        tau=0
                   
                    Cp[i-1][j]=Q[i-1][j-1]+Ca*H[i-1][j-1]-R*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                    Cv=((tau*Q[0][j])**2)/(Ca*H[0][j])
                    Q[i][j]=0.5*(-Cv+math.sqrt(Cv**2+4*Cp[i-1][j]*Cv))
                    H[i][j]=(Cp[i-1][j]-Q[i][j])/Ca
                    h[i][j]=H[i][j]-(Z0+((Z0-Z1)/L)*(dx*(j-1)))  
                
                elif (j==n and n1==n):# si le reservoir d'air se trouve au niveau de la vanne
                    if tf==0:#Dead END
                        tau=0   
                    elif (i-1)*dt<tf:  # Vanne avec temp de fermetue
                        tau=1-(((i-1)*dt)/tf)
                    else:
                        tau=0
                 
                    Cp[i-1][j]=Q[i-1][j-1]+Ca*H[i-1][j-1]-R*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                    Cv=((tau*Q[0][j])**2)/(Ca*H[0][j])
                    Q[i][j]=0.5*(-Cv+math.sqrt(Cv**2+4*Cp[i-1][j]*Cv))
                    H[i][j]=(Cp[i-1][j]-Q[i][j])/Ca
                    h[i][j]=H[i][j]-(Z0+((Z0-Z1)/L)*(dx*(j-1))) 
                
                elif (j==n1 and n1!=n) :#reservoir d'air amont
                    Cp[i-1][j]=Q[i-1][j-1]+Ca*H[i-1][j-1]-R*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                    Cn[i-1][j+1]=Q[i-1][j+2]-Ca*H[i-1][j+2]-R*dt*Q[i-1][j+2]*abs(Q[i-1][j+2])
                    
                    Qporf=(Zp-Z_ch[i-1])*(Ac/dt)
                    Vpair=Vair[i-1]-Ac*(Zp-Z_ch[i-1])
                    Hp=(Cp[i-1][j]-Cn[i-1][j+1]-Qporf)/(Ca+Ca)
                    Hpair=Cst/(Vpair**mgas)
               
                    f_inflow=Hp-Hpair+Hb-Zp-Corf_inflow*Qporf*abs(Qporf)
                    f_outflow=Hp-Hpair+Hb-Zp-Corf_outflow*Qporf*abs(Qporf)
                    X0=Z_ch[i-1]
                    if Qorf[i-1]>=0:
                        f= sympy.lambdify(Zp, f_inflow)
                        f1=f(X0)
                        df= sympy.lambdify(Zp, sympy.diff(f_inflow))  
                        df1=df(X0)  
                        X1=X0-(f1/df1)
                        for w in range(100): 
                            if (abs(X1-X0)>=eps):
                                X0=X1
                                f1=f(X0)
                                df1=df(X0)
                                X1=X0-(f1/df1)
                            else:
                                Z_ch[i]=X1
                                break
                        if abs(X1-X0)>=eps:
                            print('la methode ne converge pas')
                            sys.exit()
                    else:
                        f= sympy.lambdify(Zp, f_outflow)
                        f1=f(X0)
                        df= sympy.lambdify(Zp, sympy.diff(f_outflow))  
                        df1=df(X0)  
                        X1=X0-(f1/df1)
                        for w in range(100): 
                            if (abs(X1-X0)>=eps):
                                X0=X1
                                f1=f(X0)
                                df1=df(X0)
                                X1=X0-(f1/df1)
                            else: 
                                Z_ch[i]=X1
                                break
                        if abs(X1-X0)>=eps:
                            print('la methode ne converge pas')
                            sys.exit()  
                    Qorf[i]=(Z_ch[i]-Z_ch[i-1])*(Ac/dt)
                    Vair[i]=Vair[i-1]-Ac*(Z_ch[i]-Z_ch[i-1])
                    H[i][j]=(Cp[i-1][j]-Cn[i-1][j+1]-Qorf[i])/(Ca+Ca) 
                    Hair[i]=Cst/(Vair[i]**mgas) 
                    if Qorf[i]>=0:
                        horf [i]=Corf_inflow*Qorf[i]*abs(Qorf[i])
                    else:
                        horf [i]= Corf_outflow*Qorf[i]*abs(Qorf[i])
                    Q[i][j] = Cp[i-1][j]-Ca*H[i][j]
                    h[i][j]=H[i][j]-(Z0+((Z0-Z1)/L)*(dx*j))
                
                elif j==n1+1:#reservoir d'air aval
                    Q[i][j]=Q[i][j-1]-Qorf[i]
                    H[i][j]=H[i][j-1]                 
                    h[i][j]=H[i][j]-(Z0+((Z0-Z1)/L)*(dx*(j-1)))
                else:# noeuds intermediaires
                    if j<=n1:
                        Cn[i-1][j]=Q[i-1][j+1]-Ca*H[i-1][j+1]-R*dt*Q[i-1][j+1]*abs(Q[i-1][j+1])
                        Cp[i-1][j]=Q[i-1][j-1]+Ca*H[i-1][j-1]-R*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                        Q[i][j]=(Cp[i-1][j]+Cn[i-1][j])/2
                        H [i][j]=(Cp[i-1][j]-Cn[i-1][j])/(2*Ca)
                        h[i][j]=H[i][j]-(Z0+((Z0-Z1)/L)*(dx*j))
                    else:
                        Cn[i-1][j]=Q[i-1][j+1]-Ca*H[i-1][j+1]-R*dt*Q[i-1][j+1]*abs(Q[i-1][j+1])
                        Cp[i-1][j]=Q[i-1][j-1]+Ca*H[i-1][j-1]-R*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                        Q[i][j]=(Cp[i-1][j]+Cn[i-1][j])/2
                        H [i][j]=(Cp[i-1][j]-Cn[i-1][j])/(2*Ca)
                        h[i][j]=H[i][j]-(Z0+((Z0-Z1)/L)*(dx*(j-1)))
    """calcule envloppe"""
    for i in range(n+2): 
        Hmin[i]=min(H[:,i])
        hmin[i]=min(h[:,i]) 
        Hmax[i]=max(H[:,i]) 
        hmax[i]=max(h[:,i])
    """modification"""              
    for i in range (m+2):
        if Z_ch[i]<0:
            Z_ch[i]=0
    return(Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,Z_ch,Qorf,Hair,Vair)
# %% affiches les graphes [reservoir-conduite-vanne]        
def display_result(page,canvas,frame,Hres_entry,k_entry,L_entry,D_entry,a_entry,f_entry,n_entry,Z0_entry,Z1_entry,Dc_entry,Vairch_entry,Voair_entry,Hoair_entry,Corf_inflow_entry,Corf_outflow_entry,M_entry,Q0_entry,tf_entry,T_entry,x_entry):
    Hres=float(Hres_entry.get())
    k=float(k_entry.get())
    L=float(L_entry.get())
    D= float(D_entry.get())
    a=float(a_entry.get())
    f= float(f_entry.get())
    n = int(n_entry.get())
    Z0=float(Z0_entry.get())
    Z1=float(Z1_entry.get())
    Dc=float(Dc_entry.get())
    Vairch=float(Vairch_entry.get())
    Voair=Voair_entry.get()
    Hoair=Hoair_entry.get()
    Corf_inflow=float(Corf_inflow_entry.get())
    Corf_outflow=float(Corf_outflow_entry.get())
    M=float(M_entry.get())
    Q0=float(Q0_entry.get())
    tf=float(tf_entry.get())
    T=float(T_entry.get())
    x=float(x_entry.get())
    def x_position(x,dx):
        if x>(L-M):
            p=round(x/dx)+1
        else:
            p=round(x/dx)
        return p
    dx=L/n    
    position=x_position(x,dx)
    Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,Z_ch,Qorf,Hair,Vair=result(Hres,k,L,D,a,f,n,Z0,Z1,Dc,Vairch,Voair,Hoair,Corf_inflow,Corf_outflow,M,Q0,tf,T)
    # zoom les graphe
    aircombobox = ttk.Combobox(page, values=[
                                "- Charge hydraulique H(m)", 
                                "- Pression(m)",
                                "- Enveloppe H(x)",
                                "- Enveloppe de pression (m)",
                                "- Débit volumique Q(m3/s)",
                                "- Z(t) du reservoir d'air ",
                                "- Volume d'air Vair(t) du reservoir d'air ",
                                "- Charge hydraulique d'air Hair(t) du reservoir d'air ",
                                "- debit d'orifice Qorifice(t) du reservoir d'air "],width=35)
    aircombobox.insert(0,'sélectionnez une réponse')
    aircombobox.bind('<<ComboboxSelected>>',lambda event:zoom(aircombobox,Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,Z_ch,Qorf,Hair,Vair,position,x))
    canvas.create_window(140, 260,window=aircombobox)
    canvas.create_text(130,240,text="-ZOOM")
    # plots les graphes sur l'interface graphique
    fig = Figure(figsize=(15,9), dpi=80)
    ax = fig.add_subplot(331) 
    fig.subplots_adjust( wspace=0.3, hspace=0.4)
    ax.grid(True)
    ax.plot(Time,(H[1:,position]))
    ax.plot(Time,H[1:,position],'b')
    ax.set_xlabel('Temps [s]')
    ax.set_ylabel('Charge hydraulique H(m)')
    ax.set_title("H(t) x=%s"%x)
    
    ax = fig.add_subplot(332)
    ax.grid(True)
    ax.plot(Time,h[1:,position])
    ax.set_xlabel("Temps [s]")
    ax.set_ylabel("pression (m)")
    ax.set_title("Pression (t) de x=%s"%x)
          
    ax = fig.add_subplot(333)
    ax.grid(True) 
    ax.plot(Time,Q[1:,position])
    ax.plot(Time,Q[1:,position],'r')
    ax.set_xlabel('Temps [s]')
    ax.set_ylabel('Débit volumique Q(m3/s)')        
    ax.set_title("Q(t) de x=%s"%x)  
    
    ax = fig.add_subplot(334)
    ax.grid(True)
    ax.plot(Time,Qorf[1:,])
    ax.set_xlabel("Temps [s]")
    ax.plot(Time,Qorf[1:,],'r')
    ax.set_ylabel("Qorf [m^3/s]")
    ax.set_title("Qorifice(t) du reservoir d'air ") 
    
    ax = fig.add_subplot(335)
    ax.grid(True)
    ax.plot(Time,Z_ch[1:])
    ax.set_xlabel("Temps [s]")
    ax.plot(Time,Z_ch[1:],'b')
    ax.set_ylabel("Z_ch [m]")
    ax.set_title("Z(t) du reservoir d'air ")
    
    ax = fig.add_subplot(336)
    ax.grid(True)
    ax.plot(Time,Hair[1:])
    ax.set_xlabel("Temps [s]")
    ax.plot(Time,Hair[1:],'b')
    ax.set_ylabel("Hair [m]")
    ax.set_title("Hair(t) du reservoir d'air ")
    
    ax = fig.add_subplot(337)
    ax.grid(True)
    ax.plot(Time,Vair[1:])
    ax.set_xlabel("Temps [s]")
    ax.plot(Time,Vair[1:],'b')
    ax.set_ylabel("Vair [m3]")
    ax.set_title("Vair(t) du reservoir d'air ")
    
    ax = fig.add_subplot(338)
    ax.grid(True)
    ax.plot(Distance, Hmax, 'r',label='(Hmax)')
    ax.plot(Distance, Hmin, 'b',label='(Hmin)')
    ax.set_xlabel("Distance x[m]")
    ax.set_ylabel("Charge hydraulique H(m)")
    ax.set_title("Enveloppe H(x) ")
    ax.legend()
    
    ax = fig.add_subplot(339)
    ax.grid(True)
    ax.plot(Distance, hmax, 'r',label='(hmax)')
    ax.plot(Distance, hmin, 'b',label='(hmin)')
    ax.set_xlabel("Distance x[m]")
    ax.set_ylabel("pression h(m)")
    ax.set_title("Enveloppe pression(x) ") 
    ax.legend()
    graph = FigureCanvasTkAgg(fig,master=frame)
    return(graph)
# %% enregistre les resultas [reservoir-conduite-vanne] +cheminee d'equilbre
def save(Hres_entry,k_entry,L_entry,D_entry,a_entry,f_entry,n_entry,Z0_entry,Z1_entry,Dc_entry,Vairch_entry,Voair_entry,Hoair_entry,Corf_inflow_entry,Corf_outflow_entry,M_entry,Q0_entry,tf_entry,T_entry,x_entry):
    Hres=float(Hres_entry.get())
    k=float(k_entry.get())
    L=float(L_entry.get())
    D= float(D_entry.get())
    a=float(a_entry.get())
    f= float(f_entry.get())
    n = int(n_entry.get())
    Z0=float(Z0_entry.get())
    Z1=float(Z1_entry.get())
    Dc=float(Dc_entry.get())
    Vairch=float(Vairch_entry.get())
    Voair=Voair_entry.get()
    Hoair=Hoair_entry.get()
    Corf_inflow=float(Corf_inflow_entry.get())
    Corf_outflow=float(Corf_outflow_entry.get())
    M=float(M_entry.get())
    Q0=float(Q0_entry.get())
    tf=float(tf_entry.get())
    T=float(T_entry.get())
    dx=L/n
    dt=dx/a
    n1=round((L-M)/dx)
    m=round(T/dt)
    Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,Z_ch,Qorf,Hair,Vair=result(Hres,k,L,D,a,f,n,Z0,Z1,Dc,Vairch,Voair,Hoair,Corf_inflow,Corf_outflow,M,Q0,tf,T)
    workbook = xlsxwriter.Workbook("Réservoir-conduite-vanne avec reservoir d'air.xlsx")
    cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})
    worksheet = workbook.add_worksheet('H(x,t)')
    for  i in range (m+2):
        for j in range (n+3):
            if i==0:
                if j==0:
                    worksheet.write(i,j,'t[s]')
                else:
                    if j==n1+1 or j==n1+2:
                        worksheet.write(i,j,' H[%s m]'%int(Distance[j-1]),cell_format)
                    else:
                        worksheet.write(i,j,' H[%s m]'%int(Distance[j-1]))
            else:
                if j==0:
                    worksheet.write(i,j,Time[i-1])
                else:
                    worksheet.write(i,j,H[i,j-1])
                
    worksheet = workbook.add_worksheet('p(x,t)')
    for  i in range (m+2):
        for j in range (n+3):
            if i==0:
                if j==0:
                    worksheet.write(i,j,'t[s]')
                else:
                    if j==n1+1 or j==n1+2:
                        worksheet.write(i,j,' h[%s m]'%int(Distance[j-1]),cell_format)
                    else:
                        worksheet.write(i,j,' h[%s m]'%int(Distance[j-1]))
            else:
                if j==0:
                    worksheet.write(i,j,Time[i-1])
                else:
                    worksheet.write(i,j,h[i,j-1])            
                    
    worksheet = workbook.add_worksheet('Q(x,t)')
    for  i in range (m+2):
        for j in range (n+3):
            if i==0:
                if j==0:
                    worksheet.write(i,j,'t[s]')
                else:
                    if j==n1+1 or j==n1+2:
                        worksheet.write(i,j,' Q[%s m]'%int(Distance[j-1]),cell_format)
                    else:
                        worksheet.write(i,j,' Q[%s m]'%int(Distance[j-1]))
            else:
                if j==0:
                    worksheet.write(i,j,Time[i-1])
                else:
                    worksheet.write(i,j,Q[i,j-1])   
                
    worksheet = workbook.add_worksheet("les parametres")
    for  i in range (m+2):
        for j in range (5):
            if i==0:
                if j==0:
                    worksheet.set_column(i, j, 25)
                    worksheet.write(i,j,'t[s]')
                elif j==1:
                    worksheet.set_column(i, j, 25)
                    worksheet.write(i,j,"Volume d'air [m3]")
                elif j==2:
                    worksheet.set_column(i, j, 25)
                    worksheet.write(i,j,"pression d'air [m]")
                elif j==3:
                    worksheet.set_column(i, j, 25)
                    worksheet.write(i,j,"niveau d'eau [m]")
                elif j==4:
                    worksheet.set_column(i, j, 34)
                    worksheet.write(i,j,"debit d'orifice du reservoir d'air [m3/s]")
            else:
                if j==0:
                    worksheet.write(i,j,Time[i-1])
                elif j==1:
                    worksheet.write(i,j,Vair[i])
                elif j==2:
                    worksheet.write(i,j,Hair[i])
                elif j==3:
                    worksheet.write(i,j,Z_ch[i])
                elif j==4:
                    worksheet.write(i,j,Qorf[i])  
    worksheet = workbook.add_worksheet('Hmax(x) et hmax(x)')
    for  i in range (4):
        for j in range (n+3):
            if i==0:
                if j==0:
                    pass
                else:
                    if j==n1+1 or j==n1+2:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,' Hmax[%s m]'%int(Distance[j-1]),cell_format)
                    else:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,' Hmax[%s m]'%int(Distance[j-1]))
            elif i==1:
                if j==0:
                   pass
                else:
                    worksheet.set_column(i, j, 15)
                    worksheet.write(i,j,Hmax[j-1])
            elif i==2:
                if j==0:
                    pass
                else:
                    if j==n1+1 or j==n1+2:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,' hmax[%s m]'%int(Distance[j-1]),cell_format)
                    else:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,' hmax[%s m]'%int(Distance[j-1]))
            elif i==3:
                if j==0:
                   pass
                else:
                    worksheet.set_column(i, j, 15)
                    worksheet.write(i,j,hmax[j-1])
                    
    worksheet = workbook.add_worksheet('Hmin(x) et hmin(x)')
    for  i in range (4):
        for j in range (n+3):
            if i==0:
                if j==0:
                    pass
                else:
                    if j==n1+1 or j==n1+2:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,' Hmin[%s m]'%int(Distance[j-1]),cell_format)
                    else:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,' Hmin[%s m]'%int(Distance[j-1]))
            elif i==1:
                if j==0:
                   pass
                else:
                    worksheet.set_column(i, j, 15)
                    worksheet.write(i,j,Hmin[j-1])
            elif i==2:
                if j==0:
                    pass
                else:
                    if j==n1+1 or j==n1+2:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,' hmin[%s m]'%int(Distance[j-1]),cell_format)
                    else:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,' hmin[%s m]'%int(Distance[j-1]))
            elif i==3:
                if j==0:
                   pass
                else:
                    worksheet.set_column(i, j, 15)
                    worksheet.write(i,j,hmin[j-1])    
                    
    workbook.close()  