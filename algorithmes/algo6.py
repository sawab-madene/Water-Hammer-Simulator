# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:01:30 2020

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
def zoom(combobox,Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,position,n_ch,Z_ch,Qorf,Hair,Vair,x,c):   
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
            ax.set_title("H(t) de x=%s la Conduite:%s "%(x,c)) 
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
            ax.set_title("Pression (t) de x=%s la Conduite:%s "%(x,c)) 
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
            ax.set_title("Q(t) de x=%s la Conduite:%s "%(x,c)) 
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
# %% calcul [reservoir-conduite en serie-vanne]+reservoir d'air
def result(Hres,k,n1,f,nc,L,D,a,Z,Q0,tf,Dc,M,Vairch,Vooair,Hooair,Corf_inflow,Corf_outflow,c1,c,T,x):
    g=9.81
    eps=0.0001                               
    Hb=10                                    
    mgas=1.2                                 
    #function
    def find_position(x,c,n,L,M,dx):
        if x<=(sum(L)-M):
            if c-1==0:
                p=round(x/dx[c-1])
            else:
                p=n[c-2]+(c-1)+round((x-sum(L[0:c-1]))/dx[c-1])
        else:
            if c-1==0:
                p=round(x/dx[c-1])+1
            else:
                p=n[c-2]+(c-1)+round((x-sum(L[0:c-1]))/dx[c-1])+1
        return int(p)
    
    def one(c,pipe):
        if pipe<=c1-1:
            if c1-1==pipe:
                e=1
            else:
                e=0
        else:
            e=1
        return int(e)
    def c_corrector(L,M,c,dx,nc):
        for pipe in range(nc):
            if (sum(L)-M)>sum(L[0:pipe]) and (sum(L)-M)<=sum(L[0:pipe+1]):
                nb=round(abs((sum(L)-M)-sum(L[0:pipe]))/dx[pipe])
                length=sum(L[0:pipe])+nb*dx[pipe]
                break
        if round((sum(L)-M)/dx[0])==0:
            length=0
        if length==sum(L[0:c-1]) and length!=0:
            print('"\033[31m ERREUR:',"remplacer la valeur c1 par",c1-1)
            sys.exit()
    # Calcule des paramtres
    Ac=(math.pi*Dc**2)/4
    
    A=numpy.zeros(nc,dtype=float)
    A=(math.pi*D**2)/4
    
    R=numpy.zeros(nc,dtype=float)
    R=f/(2*D*A)
    
    Ca=numpy.zeros(nc,dtype=float)
    Ca=(g*A)/a
    
    dx=numpy.zeros(nc,dtype=float)           #calcule le dx dans chaque conduite
    for i in range(nc): 
        if i==0:
            dx[i]=L[i]/n1
            dt=dx[i]/a[i]
        else:
            dx[i]=dt*a[i]
            
    alpha=numpy.zeros(nc,dtype=float)       #les pentes des conduite 
    for i in range(nc): 
        alpha[i]=(Z[i]-Z[i+1])/L[i]
    
    m=int(round(T/dt))                      #time steps
    n=numpy.zeros(nc,dtype=int)             #nb de segments dans chaque conduite
    for i in range(nc):                     
        if i==0:
            n[i]=n1
        else:
            n[i]=n[i-1]+round(L[i]/dx[i])
    # Calcule des paramtres(suite)
    position=find_position(x,c,n,L,M,dx)      #la position de x
    n_ch=find_position((sum(L)-M),c1,n,L,M,dx)#la position de reservoir d'air         
    Time=numpy.zeros(m+1)        
    for j in range(m):
        Time[j+1]=Time[j]+dt
        
    Distance=numpy.zeros(n[-1]+nc+1)        #la distance des noeuds 
    for pipe in range(nc):
        if pipe==0:
            for j in range(n[pipe]):
                if j==n_ch:
                    Distance[j+1]=Distance[j]
                else:
                    Distance[j+1]=Distance[j]+dx[pipe]
        else:
            for j in range(n[pipe-1]+pipe-1,n[pipe]+pipe+1):
                if j<n_ch:
                    if j==n[pipe-1]+pipe-1:
                     Distance[j+1]=Distance[j]
                    else:
                     Distance[j+1]=Distance[j]+dx[pipe]
                else:
                    if j==n_ch:
                        Distance[j+1]=Distance[j]
                    elif j==n[pipe-1]+pipe:
                        Distance[j+1]=Distance[j]
                    else:
                        Distance[j+1]=Distance[j]+dx[pipe]
                        
    
    # initialisation
    H=numpy.zeros((m+2,n[-1]+nc+1),dtype=float)
    Hmax=numpy.zeros(n[-1]+nc+1,dtype=float)  
    Hmin=numpy.zeros(n[-1]+nc+1,dtype=float)
    hmax=numpy.zeros(n[-1]+nc+1,dtype=float)  
    hmin=numpy.zeros(n[-1]+nc+1,dtype=float)
    Q=numpy.zeros((m+2,n[-1]+nc+1),dtype=float)
    h=numpy.zeros((m+2,n[-1]+nc+1),dtype=float)
    Cp=numpy.zeros((m+1,n[-1]+nc+1),dtype=float)
    Cn=numpy.zeros((m+1,n[-1]+nc+1),dtype=float)
    Z_ch=numpy.zeros(m+2)
    Qorf=numpy.zeros(m+2)
    horf=numpy.zeros(m+2)
    Vair=numpy.zeros(m+2)
    Hair=numpy.zeros(m+2)                    
    # symbols
    Zp=sympy.Symbol('Zp',real=True)
    
    #calcul
    for i in range (m+2):
        if i==0:                                #regime permanent
            for pipe in range(nc):
                if pipe==0:#calcul la conduite n°01
                    for j in range(n[pipe]+1+one(c1,pipe)):
                       if j<=n_ch:
                           Q[i][j]=Q0
                           H[i][j]=Hres-((k+1+(f*j*dx[pipe]/D[pipe]))*(Q[i][j]**2/(2*g*A[pipe]**2)))
                           h[i][j]=H[i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                       else:
                           if j==n_ch+1:
                               Q[i][j]=Q[i][j-1]
                               H[i][j]=H[i][j-1]
                               h[i][j]=h[i][j-1]
                           else:
                               Q[i][j]=Q0
                               H[i][j]=Hres-((k+1+(f*(j-1)*dx[pipe]/D[pipe]))*(Q[i][j]**2/(2*g*A[pipe]**2)))
                               h[i][j]=H[i][j]-(Z[0]+alpha[pipe]*(j-1)*dx[pipe])
                else: #calcul les autres conduites
                    for j in range(n[pipe-1]+pipe+one(c1,pipe-1),n[pipe]+pipe+1+one(c1,pipe)):
                        if j<=n_ch:
                            if j==n[pipe-1]+pipe:
                                Q[i][j]=Q[i][j-1]
                                H[i][j]=H[i][j-1]
                                h[i][j]=h[i][j-1]
                            else:
                                Q[i][j]=Q0
                                H[i][j]=H[i][n[pipe-1]+pipe]-(((f*(j-pipe-n[pipe-1])*dx[pipe])/D[pipe])*(Q[i][j]**2/(2*g*A[pipe]**2)))
                                dz=alpha*L
                                h[i][j]=H[i][j]-(Z[0]+(alpha[pipe]*(j-pipe-n[pipe-1])*dx[pipe])+sum(dz[0:pipe]))
                        else:
                            if j==n[pipe-1]+pipe+1:
                                Q[i][j]=Q[i][j-1]
                                H[i][j]=H[i][j-1]
                                h[i][j]=h[i][j-1]
                            elif j==n_ch+1:
                                
                                Q[i][j]=Q[i][j-1]
                                H[i][j]=H[i][j-1]
                                h[i][j]=h[i][j-1]
                                
                            else:
                                 Q[i][j]=Q0
                                 H[i][j]=H[i][n[pipe-1]+pipe]-(((f*(j-1-pipe-n[pipe-1])*dx[pipe])/D[pipe])*(Q[i][j]**2/(2*g*A[pipe]**2)))
                                 dz=alpha*L
                                 h[i][j]=H[i][j]-(Z[0]+(alpha[pipe]*(j-1-pipe-n[pipe-1])*dx[pipe])+sum(dz[0:pipe])) 
            Qorf[i]=0
            horf[i]=0
            if Hooair=='None':
                    Voair=float(Vooair)
                    Hoair=H[i][n_ch]-((Vairch-Voair)/Ac)+Hb             
            if Vooair=='None':
                    Hoair=float(Hooair)
                    Voair=Vairch-(H[i][n_ch]+Hb-Hoair)*Ac
            Hair[i]=Hoair
            Vair[i]=Voair                   
            Z_ch[i]=H[i][n_ch]-Hair[i]+Hb     
            Cst=Hair[i]*Vair[i]**mgas    
            
        elif i==1:                              #le regime a t=0
            for j in range(n[-1]+nc+1):
                    Q[i][j]=Q[0][j]
                    H[i][j]=H[0][j]
                    h[i][j]=h[0][j]            
            if n_ch==n[-1]+nc-1:# si le reservoir d'air se trouve au niveau de la vanne
                    Q[i][n_ch]=Q[i][n[-1]+nc]
                    H[i][n_ch]=H[i][n[-1]+nc]
                    h[i][n_ch]=h[i][n[-1]+nc]            
            Qorf[i]=0
            horf[i]=0
            Hair[i]=Hair[0]
            Vair[i]=Vair[0]
            Z_ch[i]=Z_ch[0]   
    
        else:                                   #regime transitoir
            for pipe in range(nc):
                if pipe==0:#calcul la conduite n°01
                    for j in range(n[pipe]+1+one(c1,pipe)):  
                        if j<=n_ch:
                            if j==0:# resvoir amont
                                k1=(Ca[pipe]*(1+k))/(2*g*A[pipe]**2)
                                if n_ch==0:#si le reservoir d'air se trouve au niveau du reservoir
                                    Cn[i-1][j]=Q[i-1][j+2]-Ca[pipe]*H[i-1][j+2]-R[pipe]*dt*Q[i-1][j+2]*abs(Q[i-1][j+2])
                                else:
                                    Cn[i-1][j]=Q[i-1][j+1]-Ca[pipe]*H[i-1][j+1]-R[pipe]*dt*Q[i-1][j+1]*abs(Q[i-1][j+1])
                                Q[i][j]=(-1+math.sqrt(1+4*k1*(Cn[i-1][j]+Ca[pipe]*Hres)))/(2*k1)
                                if Q[i][j]>=0:
                                    H[i][j]=Hres-(1+k)*((Q[i][j])**2)/(2*g*A[pipe]**2)
                                    h[i][j]=H[i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                                else:
                                    H[i][j]=Hres-(1-k)*((Q[i][j])**2)/(2*g*A[pipe]**2)
                                    h[i][j]=H[i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                              
                            elif (j==n_ch and n_ch!=n[-1]+nc-1) :#reservoir d'air amont
                                if n_ch==n[pipe]+pipe:
                                    Cn[i-1][j+1]=Q[i-1][j+3]-Ca[pipe]*H[i-1][j+3]-R[pipe]*dt*Q[i-1][j+3]*abs(Q[i-1][j+3]) 
                                else:
                                     Cn[i-1][j+1]=Q[i-1][j+2]-Ca[pipe]*H[i-1][j+2]-R[pipe]*dt*Q[i-1][j+2]*abs(Q[i-1][j+2])       
                                Cp[i-1][j]=Q[i-1][j-1]+Ca[pipe]*H[i-1][j-1]-R[pipe]*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                                Qporf=(Zp-Z_ch[i-1])*(Ac/dt)
                                Vpair=Vair[i-1]-Ac*(Zp-Z_ch[i-1])
                                Hp=(Cp[i-1][j]-Cn[i-1][j+1]-Qporf)/(Ca[pipe]+Ca[pipe])
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
                                H[i][j]=(Cp[i-1][j]-Cn[i-1][j+1]-Qorf[i])/(Ca[pipe]+Ca[pipe]) 
                                Hair[i]=Cst/(Vair[i]**mgas) 
                                if Qorf[i]>=0:
                                    horf [i]=Corf_inflow*Qorf[i]*abs(Qorf[i])
                                else:
                                    horf [i]= Corf_outflow*Qorf[i]*abs(Qorf[i])
                                Q[i][j] = Cp[i-1][j]-Ca[pipe]*H[i][j]
                                h[i][j]=H[i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                            elif j==n[pipe]:#le point de jonction amont
                                Cn[i-1][j+1]=Q[i-1][j+2]-Ca[pipe+1]*H[i-1][j+2]-R[pipe+1]*dt*Q[i-1][j+2]*abs(Q[i-1][j+2])
                                Cp[i-1][j]=Q[i-1][j-1]+Ca[pipe]*H[i-1][j-1]-R[pipe]*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                                H[i][j]=(Cp[i-1][j]-Cn[i-1][j+1])/(Ca[pipe]+Ca[pipe+1])
                                Q[i][j]=Cp[i-1][j]-Ca[pipe]*H[i][j]
                                h[i][j]=H[i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                            else:# noeuds intermediaires
                                Cn[i-1][j]=Q[i-1][j+1]-Ca[pipe]*H[i-1][j+1]-R[pipe]*dt*Q[i-1][j+1]*abs(Q[i-1][j+1])
                                Cp[i-1][j]=Q[i-1][j-1]+Ca[pipe]*H[i-1][j-1]-R[pipe]*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                                Q[i][j]=(Cp[i-1][j]+Cn[i-1][j])/2
                                H[i][j]=(Cp[i-1][j]-Cn[i-1][j])/(2*Ca[pipe])
                                h[i][j]=H[i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                        else:
                            
                            if j==n[-1]+nc:# vanne aval
                                if tf==0:#Dead END
                                    tau=0   
                                elif (i-1)*dt<tf:  # Vanne avec temp de fermetue
                                    tau=1-(((i-1)*dt)/tf)
                                else:
                                    tau=0
                                Cp[i-1][j]=Q[i-1][j-1]+Ca[pipe]*H[i-1][j-1]-R[pipe]*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                                Cv=((tau*Q[0][j])**2)/(Ca[pipe]*H[0][j])
                                Q[i][j]=0.5*(-Cv+math.sqrt(Cv**2+4*Cp[i-1][j]*Cv))
                                H[i][j]=(Cp[i-1][j]-Q[i][j])/Ca[pipe]
                                h[i][j]=H[i][j]-(Z[0]+alpha[pipe]*(j-1)*dx[pipe])  
                            elif j==n_ch+1:#le pt de reservoir d'air aval
                                Q[i][j]=Q[i][j-1]-Qorf[i]
                                H[i][j]=H[i][j-1]                 
                                h[i][j]=H[i][j]-(Z[0]+alpha[pipe]*(j-1)*dx[pipe])
                            elif j==n[pipe]+1:#le point de jonction amont
                                Cn[i-1][j+1]=Q[i-1][j+2]-Ca[pipe+1]*H[i-1][j+2]-R[pipe+1]*dt*Q[i-1][j+2]*abs(Q[i-1][j+2])
                                Cp[i-1][j]=Q[i-1][j-1]+Ca[pipe]*H[i-1][j-1]-R[pipe]*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                                H[i][j]=(Cp[i-1][j]-Cn[i-1][j+1])/(Ca[pipe]+Ca[pipe+1])
                                Q[i][j]=Cp[i-1][j]-Ca[pipe]*H[i][j]
                                h[i][j]=H[i][j]-(Z[0]+alpha[pipe]*(j-1)*dx[pipe])
                            else:# noeuds intermediaires
                                Cn[i-1][j]=Q[i-1][j+1]-Ca[pipe]*H[i-1][j+1]-R[pipe]*dt*Q[i-1][j+1]*abs(Q[i-1][j+1])
                                Cp[i-1][j]=Q[i-1][j-1]+Ca[pipe]*H[i-1][j-1]-R[pipe]*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                                Q[i][j]=(Cp[i-1][j]+Cn[i-1][j])/2
                                H [i][j]=(Cp[i-1][j]-Cn[i-1][j])/(2*Ca[pipe])
                                h[i][j]=H[i][j]-(Z[0]+alpha[pipe]*(j-1)*dx[pipe])
                           
                else:#calcul les autres conduites
                    for j in range(n[pipe-1]+pipe+one(c1,pipe-1),n[pipe]+pipe+1+one(c1,pipe)):
                        if j<=n_ch:
                            if (j==n[-1]+nc-1 and n_ch==n[-1]+nc-1):# si le reservoir d'air se trouve au niveau de la vanne
    
                                if tf==0:#Dead END
                                    tau=0   
                                elif (i-1)*dt<tf:  # Vanne avec temp de fermetue
                                    tau=1-(((i-1)*dt)/tf)
                                else:
                                    tau=0
                     
                                Cp[i-1][j]=Q[i-1][j-1]+Ca[pipe]*H[i-1][j-1]-R[pipe]*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                                Cv=((tau*Q[0][j])**2)/(Ca[pipe]*H[0][j])
                                Q[i][j]=0.5*(-Cv+math.sqrt(Cv**2+4*Cp[i-1][j]*Cv))
                                H[i][j]=(Cp[i-1][j]-Q[i][j])/Ca[pipe]
                                dz=alpha*L
                                h[i][j]=H[i][j]-(Z[0]+(alpha[pipe]*(j-1-pipe-n[pipe-1])*dx[pipe])+sum(dz[0:pipe]))
                            elif (j==n_ch and n_ch!=n[-1]+nc-1) :#reservoir d'air amont
                                if n_ch==n[pipe]+pipe:
                                    Cn[i-1][j+1]=Q[i-1][j+3]-Ca[pipe]*H[i-1][j+3]-R[pipe]*dt*Q[i-1][j+3]*abs(Q[i-1][j+3]) 
                                else:
                                     Cn[i-1][j+1]=Q[i-1][j+2]-Ca[pipe]*H[i-1][j+2]-R[pipe]*dt*Q[i-1][j+2]*abs(Q[i-1][j+2])         
                                Cp[i-1][j]=Q[i-1][j-1]+Ca[pipe]*H[i-1][j-1]-R[pipe]*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                                Qporf=(Zp-Z_ch[i-1])*(Ac/dt)
                                Vpair=Vair[i-1]-Ac*(Zp-Z_ch[i-1])
                                Hp=(Cp[i-1][j]-Cn[i-1][j+1]-Qporf)/(Ca[pipe]+Ca[pipe])
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
                                H[i][j]=(Cp[i-1][j]-Cn[i-1][j+1]-Qorf[i])/(Ca[pipe]+Ca[pipe]) 
                                Hair[i]=Cst/(Vair[i]**mgas) 
                                if Qorf[i]>=0:
                                    horf [i]=Corf_inflow*Qorf[i]*abs(Qorf[i])
                                else:
                                    horf [i]= Corf_outflow*Qorf[i]*abs(Qorf[i])
                                Q[i][j] = Cp[i-1][j]-Ca[pipe]*H[i][j]
                                dz=alpha*L
                                h[i][j]=H[i][j]-(Z[0]+(alpha[pipe]*(j-pipe-n[pipe-1])*dx[pipe])+sum(dz[0:pipe]))
                            
                            elif j==n[pipe]+pipe: #le point de jonction amont
                                Cn[i-1][j+1]=Q[i-1][j+2]-Ca[pipe+1]*H[i-1][j+2]-R[pipe+1]*dt*Q[i-1][j+2]*abs(Q[i-1][j+2])
                                Cp[i-1][j]=Q[i-1][j-1]+Ca[pipe]*H[i-1][j-1]-R[pipe]*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                                H[i][j]=(Cp[i-1][j]-Cn[i-1][j+1])/(Ca[pipe]+Ca[pipe+1])
                                Q[i][j]=Cp[i-1][j]-Ca[pipe]*H[i][j]
                                dz=alpha*L
                                h[i][j]=H[i][j]-(Z[0]+(alpha[pipe]*(j-pipe-n[pipe-1])*dx[pipe])+sum(dz[0:pipe]))
                            elif j==n[pipe-1]+pipe: #le point de jonction aval
                                Q[i][j]=Q[i][j-1]
                                H[i][j]=H[i][j-1]
                                h[i][j]=h[i][j-1]
                            else:# noeuds intermediaires
                                Cn[i-1][j]=Q[i-1][j+1]-Ca[pipe]*H[i-1][j+1]-R[pipe]*dt*Q[i-1][j+1]*abs(Q[i-1][j+1])
                                Cp[i-1][j]=Q[i-1][j-1]+Ca[pipe]*H[i-1][j-1]-R[pipe]*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                                Q[i][j]=(Cp[i-1][j]+Cn[i-1][j])/2
                                H [i][j]=(Cp[i-1][j]-Cn[i-1][j])/(2*Ca[pipe])
                                dz=alpha*L
                                h[i][j]=H[i][j]-(Z[0]+(alpha[pipe]*(j-pipe-n[pipe-1])*dx[pipe])+sum(dz[0:pipe]))
                        else:
                            
                            if j==n_ch+1:#reservoir d'air aval
                                Q[i][j]=Q[i][j-1]-Qorf[i]
                                H[i][j]=H[i][j-1]                 
                                dz=alpha*L
                                h[i][j]=H[i][j]-(Z[0]+(alpha[pipe]*(j-1-pipe-n[pipe-1])*dx[pipe])+sum(dz[0:pipe])) 
                            elif j==n[-1]+nc:# vanne aval
                                if tf==0:#Dead END
                                    tau=0   
                                elif (i-1)*dt<tf:  # Vanne avec temp de fermetue
                                    tau=1-(((i-1)*dt)/tf)
                                else:
                                    tau=0
                                Cp[i-1][j]=Q[i-1][j-1]+Ca[pipe]*H[i-1][j-1]-R[pipe]*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                                Cv=((tau*Q[0][j])**2)/(Ca[pipe]*H[0][j])
                                Q[i][j]=0.5*(-Cv+math.sqrt(Cv**2+4*Cp[i-1][j]*Cv))
                                H[i][j]=(Cp[i-1][j]-Q[i][j])/Ca[pipe]
                                dz=alpha*L
                                h[i][j]=H[i][j]-(Z[0]+(alpha[pipe]*(j-1-pipe-n[pipe-1])*dx[pipe])+sum(dz[0:pipe]))
                            elif j==n[pipe]+pipe+1: #le point de jonction amont
                                Cn[i-1][j+1]=Q[i-1][j+2]-Ca[pipe+1]*H[i-1][j+2]-R[pipe+1]*dt*Q[i-1][j+2]*abs(Q[i-1][j+2])
                                Cp[i-1][j]=Q[i-1][j-1]+Ca[pipe]*H[i-1][j-1]-R[pipe]*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                                H[i][j]=(Cp[i-1][j]-Cn[i-1][j+1])/(Ca[pipe]+Ca[pipe+1])
                                Q[i][j]=Cp[i-1][j]-Ca[pipe]*H[i][j]
                                dz=alpha*L
                                h[i][j]=H[i][j]-(Z[0]+(alpha[pipe]*(j-1-pipe-n[pipe-1])*dx[pipe])+sum(dz[0:pipe]))
                            elif j==n[pipe-1]+pipe+1: #le point de jonction aval
                                Q[i][j]=Q[i][j-1]
                                H[i][j]=H[i][j-1]
                                h[i][j]=h[i][j-1]
                            else:# noeuds intermediaires
                                Cn[i-1][j]=Q[i-1][j+1]-Ca[pipe]*H[i-1][j+1]-R[pipe]*dt*Q[i-1][j+1]*abs(Q[i-1][j+1])
                                Cp[i-1][j]=Q[i-1][j-1]+Ca[pipe]*H[i-1][j-1]-R[pipe]*dt*Q[i-1][j-1]*abs(Q[i-1][j-1])
                                Q[i][j]=(Cp[i-1][j]+Cn[i-1][j])/2
                                H [i][j]=(Cp[i-1][j]-Cn[i-1][j])/(2*Ca[pipe])
                                dz=alpha*L
                                h[i][j]=H[i][j]-(Z[0]+(alpha[pipe]*(j-1-pipe-n[pipe-1])*dx[pipe])+sum(dz[0:pipe]))
    #calcule envloppe
    for i in range(n[-1]+nc+1): 
        Hmin[i]=min(H[:,i])  
        Hmax[i]=max(H[:,i]) 
    for i in range(n[-1]+nc+1): 
        hmin[i]=min(h[:,i])  
        hmax[i]=max(h[:,i]) 
    #modification              
    for i in range (m+2):
        if Z_ch[i]<0:
            Z_ch[i]=0     
    return(Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,position,n_ch,Z_ch,Qorf,Hair,Vair)
# %% affiches les graphes [reservoir-conduite en serie-vanne]+reservoir d'air
def display_result(page,canvas,frame,Hres_entry,k_entry,n_entry,f_entry,nc_entry,l1,d1,a1,Z1,Q0_entry,tf_entry,Dc_entry,Vairch_entry,Voair_entry,Hoair_entry,Corf_inflow_entry,Corf_outflow_entry,M_entry,c1_entry,c_entry,T_entry,x_entry):
    Hres=float(Hres_entry.get())
    k=float(k_entry.get())
    f= float(f_entry.get())
    n1 = int(n_entry.get())
    Q0=float(Q0_entry.get())
    tf=float(tf_entry.get())
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
    D=numpy.zeros((nc),dtype=float)
    L=numpy.zeros((nc),dtype=float)
    a=numpy.zeros((nc),dtype=float)
    Z=numpy.zeros((nc+1),dtype=float)
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
    dx=numpy.zeros(nc,dtype=float)           #calcule le dx dans chaque conduite
    for i in range(nc): 
        if i==0:
            dx[i]=L[i]/n1
            dt=dx[i]/a[i]
        else:
            dx[i]=dt*a[i]
    # message d'erreur
    def c_corrector(frame,L,M,c,dx,nc):
            for pipe in range(nc):
                if (sum(L)-M)>sum(L[0:pipe]) and (sum(L)-M)<=sum(L[0:pipe+1]):
                    nb=round(abs((sum(L)-M)-sum(L[0:pipe]))/dx[pipe])
                    length=sum(L[0:pipe])+nb*dx[pipe]
                    break
            if round((sum(L)-M)/dx[0])==0:
                length=0
            if length==sum(L[0:c-1]) and length!=0:
                tk.messagebox.showerror("erreur sur la page 'reservoir d_air'", "remplacer la valeur C1 par %d"%(c1-1))
                for child in frame.winfo_children():
                    child.destroy()
                exit(0)
    if c==0 or c>nc:
        tk.messagebox.showerror("erreur sur la page'exécuter' ", "la valeur C doit être superieur à 0 et inferieur à %d" %nc)
        for child in frame.winfo_children():
            child.destroy()
        exit(0)
    if c1==0 or c1>nc:
        tk.messagebox.showerror("erreur sur la page 'reservoir d_air' ", "la valeur C1 doit être superieur à 0 et inferieur à %d"%nc)
        for child in frame.winfo_children():
            child.destroy()
        exit(0)
    c_corrector(frame,L,M,c1,dx,nc)
    # afficher les graphes     
    Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,position,n_ch,Z_ch,Qorf,Hair,Vair=result(Hres,k,n1,f,nc,L,D,a,Z,Q0,tf,Dc,M,Vairch,Vooair,Hooair,Corf_inflow,Corf_outflow,c1,c,T,x)
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
    aircombobox.bind('<<ComboboxSelected>>',lambda event:zoom(aircombobox,Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,position,n_ch,Z_ch,Qorf,Hair,Vair,x,c))
    canvas.create_window(140, 330,window=aircombobox)
    canvas.create_text(130,310,text="-ZOOM")
    # plots les graphes sur l'interface graphique
    fig = Figure(figsize=(15,9), dpi=80)
    ax = fig.add_subplot(331) 
    fig.subplots_adjust( wspace=0.3, hspace=0.4)
    ax.grid(True)
    ax.plot(Time,(H[1:,position]))
    ax.plot(Time,H[1:,position],'b')
    ax.set_xlabel('Temps [s]')
    ax.set_ylabel('Charge hydraulique H(m)')
    ax.set_title("H(t) de x=%s la Conduite:%s "%(x,c)) 
    
    ax = fig.add_subplot(332)
    ax.grid(True)
    ax.plot(Time,h[1:,position])
    ax.set_xlabel("Temps [s]")
    ax.set_ylabel("pression (m)")
    ax.set_title("Pression (t) de x=%s la Conduite:%s "%(x,c)) 
          
    ax = fig.add_subplot(333)
    ax.grid(True) 
    ax.plot(Time,Q[1:,position])
    ax.plot(Time,Q[1:,position],'r')
    ax.set_xlabel('Temps [s]')
    ax.set_ylabel('Débit volumique Q(m3/s)')        
    ax.set_title("Q(t) de x=%s la Conduite:%s "%(x,c)) 
    
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
    return(graph.get_tk_widget())
# %% enregistrer [reservoir-conduite en serie-vanne]+reservoir d'air
def save(Hres_entry,k_entry,n_entry,f_entry,nc_entry,l1,d1,a1,Z1,Q0_entry,tf_entry,Dc_entry,Vairch_entry,Voair_entry,Hoair_entry,Corf_inflow_entry,Corf_outflow_entry,M_entry,c1_entry,c_entry,T_entry,x_entry):
    Hres=float(Hres_entry.get())
    k=float(k_entry.get())
    f= float(f_entry.get())
    n1 = int(n_entry.get())
    Q0=float(Q0_entry.get())
    tf=float(tf_entry.get())
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
    D=numpy.zeros((nc),dtype=float)
    L=numpy.zeros((nc),dtype=float)
    a=numpy.zeros((nc),dtype=float)
    Z=numpy.zeros((nc+1),dtype=float)
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
    dx=numpy.zeros(nc,dtype=float)           #calcule le dx dans chaque conduite
    for i in range(nc): 
        if i==0:
            dx[i]=L[i]/n1
            dt=dx[i]/a[i]
        else:
            dx[i]=dt*a[i]
    m=int(round(T/dt))                      #time steps 
    n=numpy.zeros(nc,dtype=int)             #nb de segments dans chaque conduite
    for i in range(nc):                     
        if i==0:
            n[i]=n1
        else:
            n[i]=n[i-1]+round(L[i]/dx[i])
    Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,position,n_ch,Z_ch,Qorf,Hair,Vair=result(Hres,k,n1,f,nc,L,D,a,Z,Q0,tf,Dc,M,Vairch,Vooair,Hooair,Corf_inflow,Corf_outflow,c1,c,T,x)   
    #enregistrer "excel"
    workbook = xlsxwriter.Workbook("reservoir-conduite en serie-vanne avec reservoir d'air.xlsx")
    cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})
    cell_format1 = workbook.add_format({'bold': True, 'font_color': 'blue'})
    worksheet = workbook.add_worksheet('H(x,t)')
    for  i in range (m+3):
        pipe=0
        for j in range (n[-1]+nc+2):
            if i==0:
                if j==1:
                    pipe=pipe+1
                    worksheet.write(i,j,'conduite%s'%(pipe),cell_format1)
                elif Distance[j-1]==Distance[j-2] and j!=n_ch+2 and j-2>=0:
                    pipe=pipe+1
                    worksheet.write(i,j,'conduite%s'%(pipe),cell_format1)
            elif i==1:
                if j==0:
                     worksheet.write(i,j,'t[s]')
                else:
                    if j==n_ch+1 or j==n_ch+2:
                        worksheet.write(i,j,' H[%s m]'%int(Distance[j-1]),cell_format)
                    else:
                        worksheet.write(i,j,' H[%s m]'%int(Distance[j-1]))
                        
            else:
                if j==0:
                    worksheet.write(i,j,Time[i-2])
                else:
                    worksheet.write(i,j,H[i-1,j-1])
                    
    worksheet = workbook.add_worksheet('p(x,t)')
    for  i in range (m+3):
        pipe=0
        for j in range (n[-1]+nc+2):
            if i==0:
                if j==1:
                    pipe=pipe+1
                    worksheet.write(i,j,'conduite%s'%(pipe),cell_format1)
                elif Distance[j-1]==Distance[j-2] and j!=n_ch+2 and j-2>=0:
                    pipe=pipe+1
                    worksheet.write(i,j,'conduite%s'%(pipe),cell_format1)
            elif i==1:
                if j==0:
                     worksheet.write(i,j,'t[s]')
                else:
                    if j==n_ch+1 or j==n_ch+2:
                        worksheet.write(i,j,' h[%s m]'%int(Distance[j-1]),cell_format)
                    else:
                        worksheet.write(i,j,' h[%s m]'%int(Distance[j-1]))
            else:
                if j==0:
                    worksheet.write(i,j,Time[i-2])
                else:
                    worksheet.write(i,j,h[i-1,j-1])            
                        
    worksheet = workbook.add_worksheet('Q(x,t)')
    for  i in range (m+3):
        pipe=0
        for j in range (n[-1]+nc+2):
            if i==0:
                if j==1:
                    pipe=pipe+1
                    worksheet.write(i,j,'conduite%s'%(pipe),cell_format1)
                elif Distance[j-1]==Distance[j-2] and j!=n_ch+2 and j-2>=0:
                    pipe=pipe+1
                    worksheet.write(i,j,'conduite%s'%(pipe),cell_format1)
            elif i==1:
                if j==0:
                     worksheet.write(i,j,'t[s]')
                else:
                    if j==n_ch+1 or j==n_ch+2:
                        worksheet.write(i,j,' Q[%s m]'%int(Distance[j-1]),cell_format)
                    else:
                        worksheet.write(i,j,' Q[%s m]'%int(Distance[j-1]))
            else:
                if j==0:
                    worksheet.write(i,j,Time[i-2])
                else:
                    worksheet.write(i,j,Q[i-1,j-1])   
                    
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
        pipe=0
        for j in range (n[-1]+nc+2):
            if i==0:
                if j==1:
                    pipe=pipe+1
                    worksheet.set_column(i, j, 15)
                    worksheet.write(i,j,'conduite%s'%(pipe),cell_format1)
                elif Distance[j-1]==Distance[j-2] and j!=n_ch+2 and j-2>=0:
                    pipe=pipe+1
                    worksheet.set_column(i, j, 15)
                    worksheet.write(i,j,'conduite%s'%(pipe),cell_format1)
            elif i==1:
                if j==0:
                     pass
                else:
                    if j==n_ch+1 or j==n_ch+2:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,' Hmax[%s m]'%int(Distance[j-1]),cell_format)
                    else:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,' Hmax[%s m]'%int(Distance[j-1]))
            elif i==2:
                if j==0:
                    pass
                else:
                    worksheet.set_column(i, j, 15)
                    worksheet.write(i,j,Hmax[j-1])   
            elif i==3:
                if j==0:
                     pass
                else:
                    if j==n_ch+1 or j==n_ch+2:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,' hmax[%s m]'%int(Distance[j-1]),cell_format)
                    else:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,' hmax[%s m]'%int(Distance[j-1]))
            elif i==4:
                if j==0:
                    pass
                else:
                    worksheet.set_column(i, j, 15)
                    worksheet.write(i,j,hmax[j-1])     
    worksheet = workbook.add_worksheet('Hmin(x) et hmin(x)')
    for  i in range (5):
        pipe=0
        for j in range (n[-1]+nc+2):
            if i==0:
                if j==1:
                    pipe=pipe+1
                    worksheet.set_column(i, j, 15)
                    worksheet.write(i,j,'conduite%s'%(pipe),cell_format1)
                elif Distance[j-1]==Distance[j-2] and j!=n_ch+2 and j-2>=0:
                    pipe=pipe+1
                    worksheet.set_column(i, j, 15)
                    worksheet.write(i,j,'conduite%s'%(pipe),cell_format1)
            elif i==1:
                if j==0:
                     pass
                else:
                    if j==n_ch+1 or j==n_ch+2:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,' Hmin[%s m]'%int(Distance[j-1]),cell_format)
                    else:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,' Hmin[%s m]'%int(Distance[j-1]))
            elif i==2:
                if j==0:
                    pass
                else:
                    worksheet.set_column(i, j, 15)
                    worksheet.write(i,j,Hmin[j-1])   
            elif i==3:
                if j==0:
                     pass
                else:
                    if j==n_ch+1 or j==n_ch+2:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,' hmin[%s m]'%int(Distance[j-1]),cell_format)
                    else:
                        worksheet.set_column(i, j, 15)
                        worksheet.write(i,j,' hmin[%s m]'%int(Distance[j-1]))
            elif i==4:
                if j==0:
                    pass
                else:
                    worksheet.set_column(i, j, 15)
                    worksheet.write(i,j,hmin[j-1])        
            
                        
    workbook.close()  
