# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 05:57:32 2020

@author: hp
"""
# %% bibliotheques
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
def zoom(combobox,Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,position,n_ch,Z_ch,Qorf,Hair,Vair,c,x):   
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
            ax.plot(Time,(H[c-1][1:,position]))
            ax.plot(Time,H[c-1][1:,position],'b')
            ax.set_xlabel('Temps [s]')
            ax.set_ylabel('Charge hydraulique H(m)')
            ax.set_title("H(t) x=%s la Conduite:%s "%(x,c))
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
            ax.plot(Time,h[c-1][1:,position])
            ax.set_xlabel("Temps [s]")
            ax.set_ylabel("pression (m)")
            ax.set_title("Pression(t) x=%s la Conduite:%s "%(x,c))
            graph = FigureCanvasTkAgg(fig,master=window)
            graph.get_tk_widget().pack()
    if choice== "- Enveloppe H(x)":
            window=tk.Tk()
            window.state('zoomed')
            window.title(choice)
            window.iconbitmap(r'photos\images.ico')
            fig =Figure (figsize=(16,11), dpi=140)
            ax = fig.add_subplot(111) 
            ax.grid(True)
            ax.plot(Distance[c-1], Hmax[c-1], 'r',label='(Hmax)')
            ax.plot(Distance[c-1], Hmin[c-1], 'b',label='(Hmin)')
            ax.set_xlabel("Distance x[m]")
            ax.set_ylabel("Charge hydraulique H(m)")
            ax.set_title("Enveloppede H(x) la Conduite:%s "%(c))
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
            ax.grid(True)
            ax.plot(Distance[c-1], hmax[c-1], 'r',label='(hmax)')
            ax.plot(Distance[c-1], hmin[c-1], 'b',label='(hmin)')
            ax.set_xlabel("Distance x[m]")
            ax.set_ylabel("pression h(m)")
            ax.set_title("Enveloppe de Pression(x) la Conduite:%s "%(c)) 
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
            ax.grid(True) 
            ax.plot(Time,Q[c-1][1:,position])
            ax.plot(Time,Q[c-1][1:,position],'r')
            ax.set_xlabel('Temps [s]')
            ax.set_ylabel('Débit volumique Q(m3/s)')        
            ax.set_title("Q(t)  x=%s la Conduite:%s "%(x,c))  
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
            ax.set_title("Qorifice(t) du reservoir d'air " ) 
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
# %% calcul [reservoir-conduite en parallèle-vanne]+reservoir d'air
def result(Hres,k,Q00,n1,f,nc,L,D,a,Z,tf,Dc,M,Vairch,Vooair,Hooair,Corf_inflow,Corf_outflow,c1,c,T,x):
    # calcule des parametres
    g=9.81                                
    mgas=1.2                                 #exposant m 
    eps=0.0001                                #tolerance de la methode newton
    Hb=10                                    #pression atmospherique
    Ac=(math.pi*Dc**2)/4
    
    A=numpy.zeros(nc+1,dtype=float)
    A=(math.pi*D**2)/4
    
    R=numpy.zeros(nc+1,dtype=float)
    R=f/(2*D*A)
    R[R == numpy.inf] = 0
    
    Ca=numpy.zeros(nc+1,dtype=float)
    Ca=(g*A)/a  
    
    Q0=numpy.zeros((nc+1),dtype=float)
    for pipe in range(nc+1):
        if pipe==0:
            Q0[pipe]=Q00
        else:
            Q0[pipe]=Q00*(A[pipe]/(sum(A[1:nc+1])))   
    
    alpha=numpy.zeros(nc+1,dtype=float)     #les pentes des conduite
    for i in range(nc+1): 
        if i==0:
            alpha[i]=(Z[i]-Z[i+1])/L[i]
        else:
            alpha[i]=(Z[1]-Z[i+1])/L[i]  
    
    dx=numpy.zeros(nc+1,dtype=float)       
    for i in range(nc+1):
        if i==0:
            dx[i]=L[i]/n1
            dt=dx[i]/a[i]
        else:
            dx[i]=dt*a[i]
            
    m=int(round(T/dt))
    n=numpy.zeros(nc+1,dtype=int)
    for i in range(nc+1):
        if i==0:
            n[i]=n1
        else:
            n[i]=round(L[i]/dx[i])
    #function
    def find_position(x,c,c1,M,L,dx):
        if c==c1:
            if x<=(L[c-1]-M):
                 p=round(x/dx[c-1])
            else:
                 p=round(x/dx[c-1])+1
        else:       
            p=round(x/dx[c-1])
        return int(p)
    
    def one(c,pipe):
        if pipe==c-1:
            e=1
        else:
            e=0
        return int(e)

    position=find_position(x,c,c1,M,L,dx)
    n_ch=find_position((L[c1-1]-M),c,c1,M,L,dx)
    # calcule des paramtres(suite)
    Time=numpy.zeros(m+1)
    for j in range(m):
        Time[j+1]=Time[j]+dt  
    
    Distance=list(numpy.zeros((nc+1),dtype=list))
    for pipe in range(nc+1):
        Distance[pipe]=numpy.zeros(n[pipe]+1+one(c1,pipe))
    for pipe in range(nc+1):
        for j in range(n[pipe]+one(c1,pipe)):
            if pipe==c1-1:
                if j==n_ch:
                    Distance[pipe][j+1]=Distance[pipe][j]
                else:
                    Distance[pipe][j+1]=Distance[pipe][j]+dx[pipe]
            else:    
                Distance[pipe][j+1]=Distance[pipe][j]+dx[pipe]
    # initialisation
    Q=list(numpy.zeros((nc+1),dtype=list))
    H=list(numpy.zeros((nc+1),dtype=list))
    Hmax=list(numpy.zeros((nc+1),dtype=list))
    Hmin=list(numpy.zeros((nc+1),dtype=list))
    hmax=list(numpy.zeros((nc+1),dtype=list))
    hmin=list(numpy.zeros((nc+1),dtype=list))
    h=list(numpy.zeros((nc+1),dtype=list))
    Cp=list(numpy.zeros((nc+1),dtype=list))
    Cn=list(numpy.zeros((nc+1),dtype=list))
    for pipe in range(nc+1):
        H[pipe]=numpy.zeros((m+2,n[pipe]+1+one(c1,pipe)),dtype=float)
        Q[pipe]=numpy.zeros((m+2,n[pipe]+1+one(c1,pipe)),dtype=float)
        h[pipe]=numpy.zeros((m+2,n[pipe]+1+one(c1,pipe)),dtype=float) 
        Cp[pipe]=numpy.zeros((m+1,n[pipe]+1+one(c1,pipe)),dtype=float)
        Cn[pipe]=numpy.zeros((m+1,n[pipe]+1+one(c1,pipe)),dtype=float)
        Hmax[pipe]=numpy.zeros(n[pipe]+1+one(c1,pipe),dtype=float)
        Hmin[pipe]=numpy.zeros(n[pipe]+1+one(c1,pipe),dtype=float)   
        hmax[pipe]=numpy.zeros(n[pipe]+1+one(c1,pipe),dtype=float)
        hmin[pipe]=numpy.zeros(n[pipe]+1+one(c1,pipe),dtype=float)   
    Z_ch=numpy.zeros(m+2)
    Qorf=numpy.zeros(m+2)
    horf=numpy.zeros(m+2)
    Vair=numpy.zeros(m+2)
    Hair=numpy.zeros(m+2)
    #symbols
    Zp=sympy.Symbol('Zp',real=True)
    #calcul
    for i in range (m+2):
        if i==0:#regime permanent
            for pipe in range(nc+1):
                for j in range(n[pipe]+1+one(c1,pipe)):
                    if pipe==c1-1:#la conduite du reservoir d'air
                        if j<=n_ch:
                            Q[pipe][i][j]=Q0[pipe]
                            if pipe==0:
                                H[pipe][i][j]=Hres-((k+1+(f*j*dx[pipe]/D[pipe]))*(Q[pipe][i][j]**2/(2*g*A[pipe]**2)))
                            else:
                                H[pipe][i][j]=H[0][i][n[0]]-((f*j*dx[pipe]/D[pipe])*(Q[pipe][i][j]**2/(2*g*A[pipe]**2)))
                            h[pipe][i][j]=H[pipe][i][j]-(Z[0]+(alpha[pipe]*j*dx[pipe])+(alpha[0]*L[0]))
                        else:
                            if j==n_ch+1:
                                Q[pipe][i][j]=Q[pipe][i][j-1]
                                H[pipe][i][j]=H[pipe][i][j-1]
                                h[pipe][i][j]=h[pipe][i][j-1]
                            else:    
                                Q[pipe][i][j]=Q0[pipe]
                                if pipe==0:
                                    H[pipe][i][j]=Hres-((k+1+(f*(j-1)*dx[pipe]/D[pipe]))*(Q[pipe][i][j]**2/(2*g*A[pipe]**2)))
                                else:
                                    H[pipe][i][j]=H[0][i][n[0]]-((f*(j-1)*dx[pipe]/D[pipe])*(Q[pipe][i][j]**2/(2*g*A[pipe]**2)))
                                h[pipe][i][j]=H[pipe][i][j]-(Z[0]+(alpha[pipe]*(j-1)*dx[pipe])+(alpha[0]*L[0]))
                    else:
                        Q[pipe][i][j]=Q0[pipe]
                        if pipe==0:
                            H[pipe][i][j]=Hres-((k+1+(f*j*dx[pipe]/D[pipe]))*(Q[pipe][i][j]**2/(2*g*A[pipe]**2)))
                        else:
                            H[pipe][i][j]=H[0][i][n[0]+one(c1,0)]-((f*j*dx[pipe]/D[pipe])*(Q[pipe][i][j]**2/(2*g*A[pipe]**2)))
                        h[pipe][i][j]=H[pipe][i][j]-(Z[0]+(alpha[pipe]*j*dx[pipe])+(alpha[0]*L[0]))
                    # si un diametre=0 et on divise par 0 on trouve nan
                    if numpy.isnan(H[pipe][i][j])==True:
                        H[pipe][i][j]= 0
                    if numpy.isnan(h[pipe][i][j])==True:
                        h[pipe][i][j]= 0
                    if numpy.isnan(Q[pipe][i][j])==True:
                        Q[pipe][i][j]= 0 
            Qorf[i]=0
            horf[i]=0 
            if Hooair=='None':
                    Voair=float(Vooair)
                    Hoair=H[c1-1][i][n_ch]-((Vairch-Voair)/Ac)+Hb             
            if Vooair=='None':
                    Hoair=float(Hooair)
                    Voair=Vairch-(H[c1-1][i][n_ch]+Hb-Hoair)*Ac
            Hair[i]=Hoair
            Vair[i]=Voair                
            Z_ch[i]=H[c1-1][i][n_ch]-Hair[i]+Hb     
            Cst=Hair[i]*Vair[i]**mgas 
                         
        
        elif i==1: #le regime a t=0
            for pipe in range(nc+1):     
                for j in range(n[pipe]+1+one(c1,pipe)):
                    if j!=n[pipe]+one(c1,pipe):
                        Q[pipe][i][j]=Q[pipe][0][j]
                        H [pipe][i][j]=H[pipe][0][j]
                        h[pipe][i][j]=h[pipe][0][j]
                    else:
                        if pipe!=0:
                            Q[pipe][i][j]=Q0[pipe]
                            H[pipe][i][j]=H[pipe][0][j]
                            h[pipe][i][j]=h[pipe][0][j]      
                        else:
                            Q[pipe][i][j]=Q[pipe][0][j]
                            H[pipe][i][j]=H[pipe][0][j]
                            h[pipe][i][j]=h[pipe][0][j]
            if n_ch==n[c1-1] :# si le reservoir d'air se trouve au niveau de la vanne
                Q[c1-1][i][n_ch]=Q[c1-1][i][n[c1-1]+1]
                H[c1-1][i][n_ch]=H[c1-1][i][n[c1-1]+1]
                h[c1-1][i][n_ch]=h[c1-1][i][n[c1-1]+1]          
            Qorf[i]=0
            horf[i]=0
            Hair[i]=Hair[0]
            Vair[i]=Vair[0]
            Z_ch[i]=Z_ch[0]                    
        else:#regime transitoir
            for pipe in range(nc+1):
                    for j in range(n[pipe]+1+one(c1,pipe)):
                        if pipe==c1-1:#la conduite du reservoir d'air
                            if j<=n_ch:
                                if j==0 and pipe==0:# resvoir amont
                                    k1=(Ca[pipe]*(1+k))/(2*g*A[pipe]**2)
                                    if c1==1 and n_ch==0:
                                        Cn[pipe][i-1][j]=Q[pipe][i-1][j+2]-Ca[pipe]*H[pipe][i-1][j+2]-R[pipe]*dt*Q[pipe][i-1][j+2]*abs(Q[pipe][i-1][j+2])
                                    else:
                                        Cn[pipe][i-1][j]=Q[pipe][i-1][j+1]-Ca[pipe]*H[pipe][i-1][j+1]-R[pipe]*dt*Q[pipe][i-1][j+1]*abs(Q[pipe][i-1][j+1])
                                    Q[pipe][i][j]=(-1+math.sqrt(1+4*k1*(Cn[pipe][i-1][j]+Ca[pipe]*Hres)))/(2*k1)
                                    if Q[pipe][i][j]>=0:
                                        H[pipe][i][j]=Hres-(1+k)*((Q[pipe][i][j])**2)/(2*g*A[pipe]**2)
                                        h[pipe][i][j]=H[pipe][i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                                    else:
                                        H[pipe][i][j]=Hres-(1-k)*((Q[pipe][i][j])**2)/(2*g*A[pipe]**2)
                                        h[pipe][i][j]=H[pipe][i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                                        
                                elif j==0 and pipe!=0:#le pt de jonction aval
                                    Cn[pipe][i-1][j]=Q[pipe][i-1][j+1]-Ca[pipe]*H[pipe][i-1][j+1]-R[pipe]*dt*Q[pipe][i-1][j+1]*abs(Q[pipe][i-1][j+1])
                                    H[pipe][i][j]=H[0][i][n[0]]
                                    Q[pipe][i][j]=Cn[pipe][i-1][j]+Ca[pipe]*H[pipe][i][j]
                                    h[pipe][i][j]=H[pipe][i][j]-(Z[0]+(alpha[pipe]*j*dx[pipe])+(alpha[0]*L[0]))
                                
                                elif j==n_ch and n_ch==n[pipe] and c1!=1 :# le reservoir d'air se trouve au niveau de la vanne
                                        if tf[pipe-1]==0:#Dead END
                                            tau=0   
                                        elif (i-1)*dt<tf[pipe-1]:  # Vanne avec temp de fermetue
                                            tau=1-(((i-1)*dt)/tf[pipe-1])
                                        else:
                                            tau=0
                                        Cp[pipe][i-1][j]=Q[pipe][i-1][j-1]+Ca[pipe]*H[pipe][i-1][j-1]-R[pipe]*dt*Q[pipe][i-1][j-1]*abs(Q[pipe][i-1][j-1])
                                        Cv=((tau*Q[pipe][0][j])**2)/(Ca[pipe]*H[pipe][0][j])
                                        Q[pipe][i][j]=0.5*(-Cv+math.sqrt(Cv**2+4*Cp[pipe][i-1][j]*Cv))
                                        H[pipe][i][j]=(Cp[pipe][i-1][j]-Q[pipe][i][j])/Ca[pipe]
                                        h[pipe][i][j]=H[pipe][i][j]-(Z[0]+(alpha[pipe]*(j-1)*dx[pipe])+(alpha[0]*L[0]))
                                
                                    
                                elif (j==n_ch  and c1!=1 ) :#reservoir d'air amont 
                                    Cp[pipe][i-1][j]=Q[pipe][i-1][j-1]+Ca[pipe]*H[pipe][i-1][j-1]-R[pipe]*dt*Q[pipe][i-1][j-1]*abs(Q[pipe][i-1][j-1])
                                    Cn[pipe][i-1][j+1]=Q[pipe][i-1][j+2]-Ca[pipe]*H[pipe][i-1][j+2]-R[pipe]*dt*Q[pipe][i-1][j+2]*abs(Q[pipe][i-1][j+2])    
                                    Qporf=(Zp-Z_ch[i-1])*(Ac/dt)
                                    Vpair=Vair[i-1]-Ac*(Zp-Z_ch[i-1])
                                    Hp=(Cp[pipe][i-1][j]-Cn[pipe][i-1][j+1]-Qporf)/(Ca[pipe]+Ca[pipe])
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
                                    H[pipe][i][j]=(Cp[pipe][i-1][j]-Cn[pipe][i-1][j+1]-Qorf[i])/(Ca[pipe]+Ca[pipe]) 
                                    Hair[i]=Cst/(Vair[i]**mgas) 
                                    if Qorf[i]>=0:
                                        horf [i]=Corf_inflow*Qorf[i]*abs(Qorf[i])
                                    else:
                                        horf [i]= Corf_outflow*Qorf[i]*abs(Qorf[i])
                                    Q[pipe][i][j]=Cp[pipe][i-1][j]-Ca[pipe]*H[pipe][i][j]
                                    h[pipe][i][j]=H[pipe][i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                                    
                                elif (j==n_ch and c1==1 ) :#reservoir d'air amont dans la conduite pp
                                    Cp[pipe][i-1][j]=Q[pipe][i-1][j-1]+Ca[pipe]*H[pipe][i-1][j-1]-R[pipe]*dt*Q[pipe][i-1][j-1]*abs(Q[pipe][i-1][j-1])
                                    if n_ch==n[0]:
                                        Cn_sum=0
                                        for w in range (1,nc+1):
                                            Cn[w][i-1][0]=Q[w][i-1][1]-Ca[w]*H[w][i-1][1]-R[w]*dt*Q[w][i-1][1]*abs(Q[w][i-1][1])
                                            Cn_sum=Cn_sum+Cn[w][i-1][0]
                                        Cn[pipe][i-1][j+1]=Cn_sum
                                    else: 
                                         Cn[pipe][i-1][j+1]=Q[pipe][i-1][j+2]-Ca[pipe]*H[pipe][i-1][j+2]-R[pipe]*dt*Q[pipe][i-1][j+2]*abs(Q[pipe][i-1][j+2])    
                                    Qporf=(Zp-Z_ch[i-1])*(Ac/dt)
                                    Vpair=Vair[i-1]-Ac*(Zp-Z_ch[i-1])
                                    Hp=(Cp[pipe][i-1][j]-Cn[pipe][i-1][j+1]-Qporf)/(Ca[pipe]+Ca[pipe])
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
                                    H[pipe][i][j]=(Cp[pipe][i-1][j]-Cn[pipe][i-1][j+1]-Qorf[i])/(Ca[pipe]+Ca[pipe]) 
                                    Hair[i]=Cst/(Vair[i]**mgas) 
                                    if Qorf[i]>=0:
                                        horf [i]=Corf_inflow*Qorf[i]*abs(Qorf[i])
                                    else:
                                        horf [i]= Corf_outflow*Qorf[i]*abs(Qorf[i])
                                    Q[pipe][i][j]=Cp[pipe][i-1][j]-Ca[pipe]*H[pipe][i][j]
                                    h[pipe][i][j]=H[pipe][i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                                
                                
                                else:# noeuds intermediaires
                                    Cn[pipe][i-1][j]=Q[pipe][i-1][j+1]-Ca[pipe]*H[pipe][i-1][j+1]-R[pipe]*dt*Q[pipe][i-1][j+1]*abs(Q[pipe][i-1][j+1])
                                    Cp[pipe][i-1][j]=Q[pipe][i-1][j-1]+Ca[pipe]*H[pipe][i-1][j-1]-R[pipe]*dt*Q[pipe][i-1][j-1]*abs(Q[pipe][i-1][j-1])
                                    Q[pipe][i][j]=(Cp[pipe][i-1][j]+Cn[pipe][i-1][j])/2
                                    H[pipe][i][j]=(Cp[pipe][i-1][j]-Cn[pipe][i-1][j])/(2*Ca[pipe])
                                    h[pipe][i][j]=H[pipe][i][j]-(Z[0]+(alpha[pipe]*j*dx[pipe])+(alpha[0]*L[0]))    
                            else:
                                if j==n_ch+1:#reservoir d'air aval
                                    Q[pipe][i][j]=Q[pipe][i][j-1]-Qorf[i]
                                    H[pipe][i][j]=H[pipe][i][j-1]
                                    h[pipe][i][j]=h[pipe][i][j-1]
                                else:
                                    if j==n[pipe]+1 and pipe==0: #ponit de jonction amont
                                        Cn_sum=0
                                        for w in range (1,nc+1):
                                            Cn[w][i-1][0]=Q[w][i-1][1]-Ca[w]*H[w][i-1][1]-R[w]*dt*Q[w][i-1][1]*abs(Q[w][i-1][1])
                                            Cn_sum=Cn_sum+Cn[w][i-1][0]
                                        Cp[pipe][i-1][j]=Q[pipe][i-1][j-1]+Ca[pipe]*H[pipe][i-1][j-1]-R[pipe]*dt*Q[pipe][i-1][j-1]*abs(Q[pipe][i-1][j-1])
                                        H[pipe][i][j]=(Cp[pipe][i-1][j]-Cn_sum)/sum(Ca)
                                        Q[pipe][i][j]=Cp[pipe][i-1][j]-Ca[pipe]*H[pipe][i][j]
                                        h[pipe][i][j]=H[pipe][i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                                    elif j==n[pipe]+1:# vanne aval
                                        if tf[pipe-1]==0:#Dead END
                                            tau=0   
                                        elif (i-1)*dt<tf[pipe-1]:  # Vanne avec temp de fermetue
                                            tau=1-(((i-1)*dt)/tf[pipe-1])
                                        else:
                                            tau=0
                                        Cp[pipe][i-1][j]=Q[pipe][i-1][j-1]+Ca[pipe]*H[pipe][i-1][j-1]-R[pipe]*dt*Q[pipe][i-1][j-1]*abs(Q[pipe][i-1][j-1])
                                        Cv=((tau*Q[pipe][0][j])**2)/(Ca[pipe]*H[pipe][0][j])
                                        Q[pipe][i][j]=0.5*(-Cv+math.sqrt(Cv**2+4*Cp[pipe][i-1][j]*Cv))
                                        H[pipe][i][j]=(Cp[pipe][i-1][j]-Q[pipe][i][j])/Ca[pipe]
                                        h[pipe][i][j]=H[pipe][i][j]-(Z[0]+(alpha[pipe]*(j-1)*dx[pipe])+(alpha[0]*L[0]))
                                    else:# noeuds intermediaires
                                        Cn[pipe][i-1][j]=Q[pipe][i-1][j+1]-Ca[pipe]*H[pipe][i-1][j+1]-R[pipe]*dt*Q[pipe][i-1][j+1]*abs(Q[pipe][i-1][j+1])
                                        Cp[pipe][i-1][j]=Q[pipe][i-1][j-1]+Ca[pipe]*H[pipe][i-1][j-1]-R[pipe]*dt*Q[pipe][i-1][j-1]*abs(Q[pipe][i-1][j-1])
                                        Q[pipe][i][j]=(Cp[pipe][i-1][j]+Cn[pipe][i-1][j])/2
                                        H[pipe][i][j]=(Cp[pipe][i-1][j]-Cn[pipe][i-1][j])/(2*Ca[pipe])
                                        h[pipe][i][j]=H[pipe][i][j]-(Z[0]+(alpha[pipe]*(j-1)*dx[pipe])+(alpha[0]*L[0])) 
                        else:#calcul les autres conduites
                            if j==0 and pipe==0:# resvoir amont
                                k1=(Ca[pipe]*(1+k))/(2*g*A[pipe]**2)
                                Cn[pipe][i-1][j]=Q[pipe][i-1][j+1]-Ca[pipe]*H[pipe][i-1][j+1]-R[pipe]*dt*Q[pipe][i-1][j+1]*abs(Q[pipe][i-1][j+1])
                                Q[pipe][i][j]=(-1+math.sqrt(1+4*k1*(Cn[pipe][i-1][j]+Ca[pipe]*Hres)))/(2*k1)
                                if Q[pipe][i][j]>=0:
                                    H[pipe][i][j]=Hres-(1+k)*((Q[pipe][i][j])**2)/(2*g*A[pipe]**2)
                                    h[pipe][i][j]=H[pipe][i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                                else:
                                    H[pipe][i][j]=Hres-(1-k)*((Q[pipe][i][j])**2)/(2*g*A[pipe]**2)
                                    h[pipe][i][j]=H[pipe][i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                            elif j==0 and pipe!=0:#le pt de jonction aval
                                Cn[pipe][i-1][j]=Q[pipe][i-1][j+1]-Ca[pipe]*H[pipe][i-1][j+1]-R[pipe]*dt*Q[pipe][i-1][j+1]*abs(Q[pipe][i-1][j+1])
                                H[pipe][i][j]=H[0][i][n[0]+one(c1,0)]
                                Q[pipe][i][j]=Cn[pipe][i-1][j]+Ca[pipe]*H[pipe][i][j]
                                h[pipe][i][j]=H[pipe][i][j]-(Z[0]+(alpha[pipe]*j*dx[pipe])+(alpha[0]*L[0]))
                            elif j==n[pipe] and pipe==0:#le pt de jonction amont
                                Cn_sum=0
                                for w in range (1,nc+1):
                                    Cn[w][i-1][0]=Q[w][i-1][1]-Ca[w]*H[w][i-1][1]-R[w]*dt*Q[w][i-1][1]*abs(Q[w][i-1][1])
                                    Cn_sum=Cn_sum+Cn[w][i-1][0]
                                Cp[pipe][i-1][j]=Q[pipe][i-1][j-1]+Ca[pipe]*H[pipe][i-1][j-1]-R[pipe]*dt*Q[pipe][i-1][j-1]*abs(Q[pipe][i-1][j-1])
                                H[pipe][i][j]=(Cp[pipe][i-1][j]-Cn_sum)/sum(Ca)
                                Q[pipe][i][j]=Cp[pipe][i-1][j]-Ca[pipe]*H[pipe][i][j]
                                h[pipe][i][j]=H[pipe][i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                                    
                            elif j==n[pipe]:# vanne aval
                                if tf[pipe-1]==0:#Dead END
                                    tau=0   
                                elif (i-1)*dt<tf[pipe-1]:  # Vanne avec temp de fermetue
                                    tau=1-(((i-1)*dt)/tf[pipe-1])
                                else:
                                    tau=0
                                Cp[pipe][i-1][j]=Q[pipe][i-1][j-1]+Ca[pipe]*H[pipe][i-1][j-1]-R[pipe]*dt*Q[pipe][i-1][j-1]*abs(Q[pipe][i-1][j-1])
                                Cv=((tau*Q[pipe][0][j])**2)/(Ca[pipe]*H[pipe][0][j])
                                Q[pipe][i][j]=0.5*(-Cv+math.sqrt(Cv**2+4*Cp[pipe][i-1][j]*Cv))
                                H[pipe][i][j]=(Cp[pipe][i-1][j]-Q[pipe][i][j])/Ca[pipe]
                                h[pipe][i][j]=H[pipe][i][j]-(Z[0]+(alpha[pipe]*j*dx[pipe])+(alpha[0]*L[0]))
                            else:# noeuds intermediaires
                                Cn[pipe][i-1][j]=Q[pipe][i-1][j+1]-Ca[pipe]*H[pipe][i-1][j+1]-R[pipe]*dt*Q[pipe][i-1][j+1]*abs(Q[pipe][i-1][j+1])
                                Cp[pipe][i-1][j]=Q[pipe][i-1][j-1]+Ca[pipe]*H[pipe][i-1][j-1]-R[pipe]*dt*Q[pipe][i-1][j-1]*abs(Q[pipe][i-1][j-1])
                                Q[pipe][i][j]=(Cp[pipe][i-1][j]+Cn[pipe][i-1][j])/2
                                H[pipe][i][j]=(Cp[pipe][i-1][j]-Cn[pipe][i-1][j])/(2*Ca[pipe])
                                h[pipe][i][j]=H[pipe][i][j]-(Z[0]+(alpha[pipe]*j*dx[pipe])+(alpha[0]*L[0]))    
                        # si un diametre=0 et on divise par 0 on trouve nan
                        if numpy.isnan(H[pipe][i][j])==True:
                            H[pipe][i][j]= 0
                        if numpy.isnan(h[pipe][i][j])==True:
                            h[pipe][i][j]= 0
                        if numpy.isnan(Q[pipe][i][j])==True:
                            Q[pipe][i][j]= 0                            
    #calcule envloppe
    for pipe in range(nc+1):
        for i in range(n[pipe]+one(c1,pipe)+1): 
            Hmin[pipe][i]=min(H[pipe][:,i])  
            Hmax[pipe][i]=max(H[pipe][:,i])  
    for pipe in range(nc+1):
        for i in range(n[pipe]+one(c1,pipe)+1): 
            hmin[pipe][i]=min(h[pipe][:,i])  
            hmax[pipe][i]=max(h[pipe][:,i]) 
    #modification              
    for i in range (m+2):
        if Z_ch[i]<0:
            Z_ch[i]=0    
    return(Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,position,n_ch,Z_ch,Qorf,Hair,Vair)
# %% affiches les graphes [reservoir-conduite en parallèle-vanne]+reservoir d'air
def display_result(page,canvas,frame,Hres_entry,k_entry,Q0_entry,n_entry,f_entry,nc_entry,l1,d1,a1,Z1,tf1,Dc_entry,Vairch_entry,Voair_entry,Hoair_entry,Corf_inflow_entry,Corf_outflow_entry,M_entry,c1_entry,c_entry,T_entry,x_entry):
    Hres=float(Hres_entry.get())
    k=float(k_entry.get())
    f= float(f_entry.get())
    n1 = int(n_entry.get())
    Q00=float(Q0_entry.get())
    T=float(T_entry.get())
    x=float(x_entry.get())
    Dc=float(Dc_entry.get())
    Vairch=float(Vairch_entry.get())
    Vooair=Voair_entry.get()
    Hooair=Hoair_entry.get()
    Corf_inflow=float(Corf_inflow_entry.get())
    Corf_outflow=float(Corf_outflow_entry.get())
    M=float(M_entry.get())
    nc=int(nc_entry.get())
    c=int(c_entry.get())
    c1=int(c1_entry.get())
    D=numpy.zeros(nc+1,dtype=float)
    tf=numpy.zeros(nc,dtype=float)
    L=numpy.zeros(nc+1,dtype=float)
    a=numpy.zeros(nc+1,dtype=float)
    Z=numpy.zeros(nc+2,dtype=float)
    i=0 
    for d_entry in d1:
        D[i]=float(d_entry.get())
        i=i+1  
    i=0
    for l_entry in l1:
        L[i]=float(l_entry.get())
        i=i+1
    i=0
    for a_entry in a1:
        a[i]=float(a_entry.get())
        i=i+1
    i=0
    for Z_entry in Z1:
        Z[i]=float(Z_entry.get())
        i=i+1
    i=0
    for tf_entry in tf1:
        tf[i]=float(tf_entry.get())
        i=i+1
    dx=numpy.zeros(nc+1,dtype=float)       
    for i in range(nc+1):
        if i==0:
            dx[i]=L[i]/n1
            dt=dx[i]/a[i]
        else:
            dx[i]=dt*a[i]
    # message d'erreur
    if c==0 or c>nc+1:
        tk.messagebox.showerror("erreur sur la page'exécuter' ", "la valeur C doit être superieur à 0 et inferieur à %d" %(nc+1))
        for child in frame.winfo_children():
            child.destroy()
        exit(0)
    if c1==0 or c1>nc+1:
        tk.messagebox.showerror("erreur sur la page 'reservoir d_air' ", "la valeur C1 doit être superieur à 0 et inferieur à %d"%(nc+1))
        for child in frame.winfo_children():
            child.destroy()
        exit(0)
    for pipe in range(nc+1):
        if round((L[c1-1]-M)/dx[c1-1])==0 and c1!=1:
            tk.messagebox.showerror("erreur sur la page 'reservoir d_air'", 
                        "remplacer la valeur C1 par 1 et remplacer la valeur M par 0")
            for child in frame.winfo_children():
                 child.destroy()
            exit(0)
    Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,position,n_ch,Z_ch,Qorf,Hair,Vair=result(Hres,k,Q00,n1,f,nc,L,D,a,Z,tf,Dc,M,Vairch,Vooair,Hooair,Corf_inflow,Corf_outflow,c1,c,T,x)
    # zoom les graphe
    aircombobox = ttk.Combobox(page, values=[
                                "- Charge hydraulique H(m)", 
                                "- Pression(m)",
                                "- Enveloppe H(x)",
                                "- Enveloppe de pression (m)",
                                "- Débit volumique Q(m3/s)",
                                "- debit d'orifice Qorifice(t) du reservoir d'air ",
                                "- Z(t) du reservoir d'air ",
                                "- Volume d'air Vair(t) du reservoir d'air ",
                                "- Charge hydraulique d'air Hair(t) du reservoir d'air "],width=35)
    aircombobox.insert(0,'sélectionnez une réponse')
    aircombobox.bind('<<ComboboxSelected>>',lambda event:zoom(aircombobox,Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,position,n_ch,Z_ch,Qorf,Hair,Vair,c,x))
    canvas.create_window(140, 330,window=aircombobox)
    canvas.create_text(130,310,text="-ZOOM")
    # plots les graphes sur l'interface graphique           
    fig = Figure(figsize=(15,9), dpi=80)
    ax = fig.add_subplot(331) 
    fig.subplots_adjust( wspace=0.3, hspace=0.4)
    ax.grid(True)
    ax.plot(Time,(H[c-1][1:,position]))
    ax.plot(Time,(H[c-1][1:,position]),'b')
    ax.set_xlabel('Temps [s]')
    ax.set_ylabel('Charge hydraulique H(m)')
    ax.set_title("H(t) x=%s la Conduite:%s "%(x,c) )
        
    ax = fig.add_subplot(332)
    ax.grid(True)
    ax.plot(Time,h[c-1][1:,position])
    ax.set_xlabel("Temps [s]")
    ax.set_ylabel("pression (m)")
    ax.set_title("pression(t) x=%s la Conduite:%s "%(x,c) )
              
    ax = fig.add_subplot(333)
    ax.grid(True) 
    ax.plot(Time,Q[c-1][1:,position])
    ax.plot(Time,Q[c-1][1:,position],'r')
    ax.set_xlabel('Temps [s]')    
    ax.set_ylabel('Débit volumique Q(m3/s)')        
    ax.set_title("Q(t) x=%s la Conduite:%s "%(x,c) )  
    
    
    ax = fig.add_subplot(334)
    ax.grid(True)
    ax.plot(Time,Qorf[1:,])
    ax.set_xlabel("Temps [s]")
    ax.plot(Time,Qorf[1:,],'r')
    ax.set_ylabel("Qorf [m^3/s]")
    ax.set_title("Qorifice(t) du reservoir d'air " ) 
        
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
    ax.plot(Distance[c-1], Hmax[c-1], 'r',label='(Hmax)')
    ax.plot(Distance[c-1], Hmin[c-1], 'b',label='(Hmin)')
    ax.set_xlabel("Distance x[m]")
    ax.set_ylabel("Charge hydraulique H(m)")
    ax.set_title("Enveloppe de H(x) la Conduite:%s "%(c))
    ax.legend()
        
    ax = fig.add_subplot(339)
    ax.grid(True)
    ax.plot(Distance[c-1], hmax[c-1], 'r',label='(hmax)')
    ax.plot(Distance[c-1], hmin[c-1], 'b',label='(hmin)')
    ax.set_xlabel("Distance x[m]")
    ax.set_ylabel("pression h(m)")
    ax.set_title("Enveloppe de Pression(x) la Conduite:%s "%(c))    
    ax.legend()
    graph = FigureCanvasTkAgg(fig,master=frame)
    return(graph.get_tk_widget())
# %% enregistrer [reservoir-conduite en parallèle-vanne]+reservoir d'air
def one(c,pipe):
    if pipe==c-1:
        e=1
    else:
        e=0
    return int(e)
def save(Hres_entry,k_entry,Q0_entry,n_entry,f_entry,nc_entry,l1,d1,a1,Z1,tf1,Dc_entry,Vairch_entry,Voair_entry,Hoair_entry,Corf_inflow_entry,Corf_outflow_entry,M_entry,c1_entry,c_entry,T_entry,x_entry):
    Hres=float(Hres_entry.get())
    k=float(k_entry.get())
    f= float(f_entry.get())
    n1 = int(n_entry.get())
    Q00=float(Q0_entry.get())
    T=float(T_entry.get())
    x=float(x_entry.get())
    Dc=float(Dc_entry.get())
    Vairch=float(Vairch_entry.get())
    Vooair=Voair_entry.get()
    Hooair=Hoair_entry.get()
    Corf_inflow=float(Corf_inflow_entry.get())
    Corf_outflow=float(Corf_outflow_entry.get())
    M=float(M_entry.get())
    nc=int(nc_entry.get())
    c=int(c_entry.get())
    c1=int(c1_entry.get())
    D=numpy.zeros(nc+1,dtype=float)
    tf=numpy.zeros(nc,dtype=float)
    L=numpy.zeros(nc+1,dtype=float)
    a=numpy.zeros(nc+1,dtype=float)
    Z=numpy.zeros(nc+2,dtype=float)
    i=0 
    for d_entry in d1:
        D[i]=float(d_entry.get())
        i=i+1  
    i=0
    for l_entry in l1:
        L[i]=float(l_entry.get())
        i=i+1
    i=0
    for a_entry in a1:
        a[i]=float(a_entry.get())
        i=i+1
    i=0
    for Z_entry in Z1:
        Z[i]=float(Z_entry.get())
        i=i+1
    i=0
    for tf_entry in tf1:
        tf[i]=float(tf_entry.get())
        i=i+1
    dx=numpy.zeros(nc+1,dtype=float)       
    for i in range(nc+1):
        if i==0:
            dx[i]=L[i]/n1
            dt=dx[i]/a[i]
        else:
            dx[i]=dt*a[i]
    m=int(round(T/dt))                      #time steps 
    n=numpy.zeros(nc+1,dtype=int)
    for i in range(nc+1):
        if i==0:
            n[i]=n1
        else:
            n[i]=round(L[i]/dx[i])
        
    Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,position,n_ch,Z_ch,Qorf,Hair,Vair=result(Hres,k,Q00,n1,f,nc,L,D,a,Z,tf,Dc,M,Vairch,Vooair,Hooair,Corf_inflow,Corf_outflow,c1,c,T,x)
    # enregistrer "excel"         
    workbook = xlsxwriter.Workbook("reservoir-conduite_en_parallèle-vanne+reservoir d'air.xlsx")
    cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})
    cell_format1 = workbook.add_format({'bold': True, 'font_color': 'blue'})
    worksheet = workbook.add_worksheet('H(x,t)')
    for  i in range (m+3):
        for pipe in range(nc+1):
            if pipe==0:
                end=(n[pipe]+1+one(c1,pipe))+1
                for j in range (n[pipe]+2+one(c1,pipe)):
                    if i==0 :
                        if j==1:
                            worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                    elif i==1:
                        if j==0:
                            worksheet.write(i,j,'t[s]')
                        else:
                            if one(c1,pipe)==1:
                                if j==n_ch+1 or j==n_ch+2:
                                    worksheet.write(i,j,' H[%s m]'%int(Distance[pipe][j-1]),cell_format)
                                else:
                                    worksheet.write(i,j,'H[%s m]'%int(Distance[pipe][j-1]))
                            else:
                                worksheet.write(i,j,'H[%s m]'%int(Distance[pipe][j-1]))
                    else:
                        if j==0:
                            worksheet.write(i,j,Time[i-2])
                        else:
                            worksheet.write(i,j,H[pipe][i-1,j-1])
            else:
                start=end+1
                end=start+n[pipe]+1+one(c1,pipe)
                for j in range (start,end):
                    if i==0:
                        if j==start:
                            worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                    elif i==1:
                        if one(c1,pipe)==1:
                            if j==n_ch+start or j==n_ch+1+start:
                                worksheet.write(i,j,' H[%s m]'%int(Distance[pipe][j-start]),cell_format)
                            else:
                                worksheet.write(i,j,'H[%s m]'%int(Distance[pipe][j-start]))
                        else:
                            worksheet.write(i,j,'H[%s m]'%int(Distance[pipe][j-start]))
                    else:
                        worksheet.write(i,j,(H[pipe][i-1,j-start]))
    
    
    worksheet = workbook.add_worksheet('p(x,t)')
    for  i in range (m+3):
        for pipe in range(nc+1):
            if pipe==0:
                end=(n[pipe]+1+one(c1,pipe))+1
                for j in range (n[pipe]+2+one(c1,pipe)):
                    if i==0 :
                        if j==1:
                            worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                    elif i==1:
                        if j==0:
                            worksheet.write(i,j,'t[s]')
                        else:
                            if one(c1,pipe)==1:
                                if j==n_ch+1 or j==n_ch+2:
                                    worksheet.write(i,j,' p[%s m]'%int(Distance[pipe][j-1]),cell_format)
                                else:
                                    worksheet.write(i,j,'p[%s m]'%int(Distance[pipe][j-1]))
                            else:
                                worksheet.write(i,j,'p[%s m]'%int(Distance[pipe][j-1]))
                    else:
                        if j==0:
                            worksheet.write(i,j,Time[i-2])
                        else:
                            worksheet.write(i,j,H[pipe][i-1,j-1])
            else:
                start=end+1
                end=start+n[pipe]+1+one(c1,pipe)
                for j in range (start,end):
                    if i==0:
                        if j==start:
                            worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                    elif i==1:
                        if one(c1,pipe)==1:
                            if j==n_ch+start or j==n_ch+1+start:
                                worksheet.write(i,j,' p[%s m]'%int(Distance[pipe][j-start]),cell_format)
                            else:
                                worksheet.write(i,j,'p[%s m]'%int(Distance[pipe][j-start]))
                        else:
                            worksheet.write(i,j,'p[%s m]'%int(Distance[pipe][j-start]))
                    else:
                        worksheet.write(i,j,(h[pipe][i-1,j-start]))
    
                        
    worksheet = workbook.add_worksheet('Q(x,t)')
    for  i in range (m+3):
        for pipe in range(nc+1):
            if pipe==0:
                end=(n[pipe]+1+one(c1,pipe))+1
                for j in range (n[pipe]+2+one(c1,pipe)):
                    if i==0 :
                        if j==1:
                            worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                    elif i==1:
                        if j==0:
                            worksheet.write(i,j,'t[s]')
                        else:
                            if one(c1,pipe)==1:
                                if j==n_ch+1 or j==n_ch+2:
                                    worksheet.write(i,j,' Q[%s m]'%int(Distance[pipe][j-1]),cell_format)
                                else:
                                    worksheet.write(i,j,'Q[%s m]'%int(Distance[pipe][j-1]))
                            else:
                                worksheet.write(i,j,'Q[%s m]'%int(Distance[pipe][j-1]))
                    else:
                        if j==0:
                            worksheet.write(i,j,Time[i-2])
                        else:
                            worksheet.write(i,j,Q[pipe][i-1,j-1])
            else:
                start=end+1
                end=start+n[pipe]+1+one(c1,pipe)
                for j in range (start,end):
                    if i==0:
                        if j==start:
                            worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                    elif i==1:
                        if one(c1,pipe)==1:
                            if j==n_ch+start or j==n_ch+1+start:
                                worksheet.write(i,j,' Q[%s m]'%int(Distance[pipe][j-start]),cell_format)
                            else:
                                worksheet.write(i,j,'Q[%s m]'%int(Distance[pipe][j-start]))
                        else:
                            worksheet.write(i,j,'Q[%s m]'%int(Distance[pipe][j-start]))
                    else:
                        worksheet.write(i,j,(Q[pipe][i-1,j-start]))
                        
    worksheet = workbook.add_worksheet("les parametres")
    for  i in range (m+2):
        for j in range (5):
            if i==0:
                if j==0:
                    
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
    for  i in range (5):
        for pipe in range(nc+1):
            if pipe==0:
                end=(n[pipe]+1+one(c1,pipe))+1
                for j in range (n[pipe]+2+one(c1,pipe)):
                    if i==0 :
                        if j==1:
                            worksheet.set_column(i, j, 15)
                            worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                    elif i==1:
                        if j==0:
                            pass
                        else:
                            if one(c1,pipe)==1:
                                if j==n_ch+1 or j==n_ch+2:
                                    worksheet.set_column(i, j, 15)
                                    worksheet.write(i,j,' Hmax[%s m]'%int(Distance[pipe][j-1]),cell_format)
                                else:
                                    worksheet.set_column(i, j, 15)
                                    worksheet.write(i,j,'Hmax[%s m]'%int(Distance[pipe][j-1]))
                            else:
                                worksheet.set_column(i, j, 15)
                                worksheet.write(i,j,'Hmax[%s m]'%int(Distance[pipe][j-1]))
                    elif i==2:
                        if j==0:
                            pass
                        else:
                            worksheet.set_column(i, j, 15)
                            worksheet.write(i,j,Hmax[pipe][j-1])
                    elif i==3:
                        if j==0:
                            pass
                        else:
                            if one(c1,pipe)==1:
                                if j==n_ch+1 or j==n_ch+2:
                                    worksheet.set_column(i, j, 15)
                                    worksheet.write(i,j,' hmax[%s m]'%int(Distance[pipe][j-1]),cell_format)
                                else:
                                    worksheet.set_column(i, j, 15)
                                    worksheet.write(i,j,'hmax[%s m]'%int(Distance[pipe][j-1]))
                            else:
                                worksheet.set_column(i, j, 15)
                                worksheet.write(i,j,'hmax[%s m]'%int(Distance[pipe][j-1]))
                    else:
                        if j==0:
                            pass
                        else:
                            worksheet.set_column(i, j, 15)
                            worksheet.write(i,j,hmax[pipe][j-1])
            else:
                start=end+1
                end=start+n[pipe]+1+one(c1,pipe)
                for j in range (start,end):
                    if i==0:
                        if j==start:
                            worksheet.set_column(i, j, 15)
                            worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                    elif i==1:
                        if one(c1,pipe)==1:
                            if j==n_ch+start or j==n_ch+1+start:
                                worksheet.set_column(i, j, 15)
                                worksheet.write(i,j,' Hmax[%s m]'%int(Distance[pipe][j-start]),cell_format)
                            else:
                                worksheet.set_column(i, j, 15)
                                worksheet.write(i,j,'Hmax[%s m]'%int(Distance[pipe][j-start]))
                        else:
                            worksheet.set_column(i, j, 15)
                            worksheet.write(i,j,'Hmax[%s m]'%int(Distance[pipe][j-start]))
                    elif i==2:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,(Hmax[pipe][j-start]))
                    elif i==3:
                        if one(c1,pipe)==1:
                            if j==n_ch+start or j==n_ch+1+start:
                                worksheet.set_column(i, j, 15)
                                worksheet.write(i,j,' hmax[%s m]'%int(Distance[pipe][j-start]),cell_format)
                            else:
                                worksheet.set_column(i, j, 15)
                                worksheet.write(i,j,'hmax[%s m]'%int(Distance[pipe][j-start]))
                        else:
                            worksheet.set_column(i, j, 15)
                            worksheet.write(i,j,'hmax[%s m]'%int(Distance[pipe][j-start]))
                    else:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,(hmax[pipe][j-start]))
    worksheet = workbook.add_worksheet('Hmin(x) et hmin(x)')
    for  i in range (5):
        for pipe in range(nc+1):
            if pipe==0:
                end=(n[pipe]+1+one(c1,pipe))+1
                for j in range (n[pipe]+2+one(c1,pipe)):
                    if i==0 :
                        if j==1:
                            worksheet.set_column(i, j, 15)
                            worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                    elif i==1:
                        if j==0:
                            pass
                        else:
                            if one(c1,pipe)==1:
                                if j==n_ch+1 or j==n_ch+2:
                                    worksheet.set_column(i, j, 15)
                                    worksheet.write(i,j,' Hmin[%s m]'%int(Distance[pipe][j-1]),cell_format)
                                else:
                                    worksheet.set_column(i, j, 15)
                                    worksheet.write(i,j,'Hmin[%s m]'%int(Distance[pipe][j-1]))
                            else:
                                worksheet.set_column(i, j, 15)
                                worksheet.write(i,j,'Hmin[%s m]'%int(Distance[pipe][j-1]))
                    elif i==2:
                        if j==0:
                            pass
                        else:
                            worksheet.set_column(i, j, 15)
                            worksheet.write(i,j,Hmin[pipe][j-1])
                    elif i==3:
                        if j==0:
                            pass
                        else:
                            if one(c1,pipe)==1:
                                if j==n_ch+1 or j==n_ch+2:
                                    worksheet.set_column(i, j, 15)
                                    worksheet.write(i,j,' hmin[%s m]'%int(Distance[pipe][j-1]),cell_format)
                                else:
                                    worksheet.set_column(i, j, 15)
                                    worksheet.write(i,j,'hmin[%s m]'%int(Distance[pipe][j-1]))
                            else:
                                worksheet.set_column(i, j, 15)
                                worksheet.write(i,j,'hmin[%s m]'%int(Distance[pipe][j-1]))
                    else:
                        if j==0:
                            pass
                        else:
                            worksheet.set_column(i, j, 15)
                            worksheet.write(i,j,hmin[pipe][j-1])
            else:
                start=end+1
                end=start+n[pipe]+1+one(c1,pipe)
                for j in range (start,end):
                    if i==0:
                        if j==start:
                            worksheet.set_column(i, j, 15)
                            worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                    elif i==1:
                        if one(c1,pipe)==1:
                            if j==n_ch+start or j==n_ch+1+start:
                                worksheet.set_column(i, j, 15)
                                worksheet.write(i,j,' Hmin[%s m]'%int(Distance[pipe][j-start]),cell_format)
                            else:
                                worksheet.set_column(i, j, 15)
                                worksheet.write(i,j,'Hmin[%s m]'%int(Distance[pipe][j-start]))
                        else:
                            worksheet.set_column(i, j, 15)
                            worksheet.write(i,j,'Hmax[%s m]'%int(Distance[pipe][j-start]))
                    elif i==2:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,(Hmin[pipe][j-start]))
                    elif i==3:
                        if one(c1,pipe)==1:
                            if j==n_ch+start or j==n_ch+1+start:
                                worksheet.set_column(i, j, 15)
                                worksheet.write(i,j,' hmin[%s m]'%int(Distance[pipe][j-start]),cell_format)
                            else:
                                worksheet.set_column(i, j, 15)
                                worksheet.write(i,j,'hmin[%s m]'%int(Distance[pipe][j-start]))
                        else:
                            worksheet.set_column(i, j, 15)
                            worksheet.write(i,j,'hmin[%s m]'%int(Distance[pipe][j-start]))
                    else:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,(hmin[pipe][j-start]))   
    
                        
    workbook.close()             
                    
