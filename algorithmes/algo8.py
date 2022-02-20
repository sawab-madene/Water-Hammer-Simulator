# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 17:11:22 2020

@author: hp
"""
# %% bibliotheques
import tkinter as tk
from tkinter import ttk
import math
import numpy
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import xlsxwriter
# %% zoom function
def zoom(combobox,t,x1,H,h1,Q,Hmax,Hmin,h1max,h1min,Zp,Qps,x,c,L,n,nc,dx):    
    choice=combobox.get()
    if choice== "- Charge hydraulique H(m)":
            window=tk.Tk()
            window.state('zoomed')
            window.title(choice)
            window.iconbitmap(r'photos\images.ico')
            fig =Figure (figsize=(16,11), dpi=140)
            ax = fig.add_subplot(111) 
            if x<=L[c-1] and x>=0 :
                fig.subplots_adjust( wspace=1.4, hspace=1)
                ax.grid(True)
                ax.plot(t,H[c-1][int(round(x/dx[c-1]))][:])
                ax.plot(t,H[c-1][int(round(x/dx[c-1]))][:],'b')
                ax.set_xlabel("Temps [s]")
                ax.set_ylabel("Charge hydraulique H(m)")
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
            if x<=L[c-1] and x>=0 :
                fig.subplots_adjust( wspace=1.4, hspace=1)
                ax.grid(True)
                ax.plot(t,h1[c-1][int(round(x/dx[c-1]))][:])
                ax.plot(t,h1[c-1][int(round(x/dx[c-1]))][:],'b')
                ax.set_xlabel("Temps [s]")
                ax.set_ylabel("Pression (m)")
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
            if x<=L[c-1] and x>=0 :
                    fig.subplots_adjust( wspace=1.4, hspace=1)
                    ax.grid(True)
                    ax.plot(x1[c-1],Hmax[c-1][:],'r',label='H max')
                    ax.plot(x1[c-1],Hmin[c-1][:],'b',label='H min')
                    for i in range (0,n[c-1]+1) :
                        if Hmax[c-1][i]==max(Hmax[c-1]):
                            ax.plot(x1[c-1][i],Hmax[c-1][i],'bo')
                            p=x1[c-1][i]
                    ax.plot(p,max(Hmax[c-1]),'bo',label='max(Hmax)')
                    for i in range (0,n[c-1]+1) :
                        if Hmin[c-1][i]==min(Hmin[c-1]):
                            ax.plot(x1[c-1][i],Hmin[c-1][i],'ro')
                            p=x1[c-1][i]
                    ax.plot(p,min(Hmin[c-1]),'ro',label='max(Hmax)')
                    ax.set_xlabel("Distance x[m]")
                    ax.set_ylabel("Charge hydraulique H(m)")
                    ax.set_title("Enveloppe H(x) de   Conduite:%s "%(c))
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
            if x<=L[c-1] and x>=0 :
                    fig.subplots_adjust( wspace=1.4, hspace=1)
                    ax.grid(True)
                    ax.plot(x1[c-1],h1max[c-1][:],'r',label='h max')
                    ax.plot(x1[c-1],h1min[c-1][:],'b',label='h min')
                    for i in range (0,n[c-1]+1) :
                        if h1max[c-1][i]==max(h1max[c-1]):
                            ax.plot(x1[c-1][i],h1max[c-1][i],'bo')
                            p=x1[c-1][i]
                    ax.plot(x1[c-1][i],h1max[c-1][i],'bo',label='max(h max)')
                    for i in range (0,n[c-1]+1) :
                        if h1min[c-1][i]==min(h1min[c-1]):
                            ax.plot(x1[c-1][i],h1min[c-1][i],'ro')
                            p=x1[c-1][i]
                    ax.plot(x1[c-1][i],h1min[c-1][i],'ro',label='min(h min)')
                    ax.set_xlabel("Distance x[m]")
                    ax.set_ylabel("Pression (m)")
                    ax.set_title("Pression (x)dans Conduite:%s "%(c))
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
            if x<=L[c-1] and x>=0 :
                fig.subplots_adjust( wspace=1.4, hspace=1)
                ax.grid(True)  
                ax.plot(t,Q[c-1][int(round(x/dx[c-1]))][:])
                ax.plot(t,Q[c-1][int(round(x/dx[c-1]))][:],'r')
                ax.set_xlabel("Temps [s]")
                ax.set_ylabel("Débit volumique Q(m3/s)")
                ax.set_title("Q(t) x=%s la Conduite:%s "%(x,c))
                graph = FigureCanvasTkAgg(fig,master=window)
                graph.get_tk_widget().pack()
    if choice=="- Qps(t) de cheminée d'équilibre ":
            window=tk.Tk()
            window.state('zoomed')
            window.title(choice)
            window.iconbitmap(r'photos\images.ico')
            fig =Figure (figsize=(16,11), dpi=140)
            ax = fig.add_subplot(111) 
            if x<=L[c-1] and x>=0 :
                fig.subplots_adjust( wspace=1.4, hspace=1)
                ax.grid(True)
                ax.plot(t,Qps[:],'b')
                ax.set_xlabel("Temps [s]")
                ax.set_ylabel("Qps")
                ax.set_title("Qps(t) de cheminée d'équilibre ") 
                graph = FigureCanvasTkAgg(fig,master=window)
                graph.get_tk_widget().pack()
    if choice== "- Zp(t) de cheminée d'équilibre ":
            window=tk.Tk()
            window.state('zoomed')
            window.title(choice)
            window.iconbitmap(r'photos\images.ico')
            fig =Figure (figsize=(16,11), dpi=140)
            ax = fig.add_subplot(111) 
            if x<=L[c-1] and x>=0 :
                fig.subplots_adjust( wspace=1.4, hspace=1)
                ax.grid(True)
                ax.plot(t,Zp[:],'b')
                ax.set_xlabel("Temps [s]")
                ax.set_ylabel("Zp[m]")
                ax.set_title("Zp(t) de cheminée d'équilibre ")
                graph = FigureCanvasTkAgg(fig,master=window)
                graph.get_tk_widget().pack()
# %% calcul [reservoir-conduite en parallèle-vanne]+cheminee d'equilibre
def result(Hres,k,Q00,n1,f,nc,L,D,a,Z,tf,Ds,M,c1,c,T,x):
            n=numpy.zeros((nc+1),dtype=int)
            for h in range (0,nc+1):
                if h==0:
                    n[0]=n1
                else:
                    n[h]= int(round((L[h]*a[0]*n[0])/(L[0]*a[h])))
                
            g=9.81
            A=numpy.zeros((nc+1),dtype=float)
            R=numpy.zeros((nc+1),dtype=float)
            dx=numpy.zeros((nc+1),dtype=float)
            dt=numpy.zeros((nc+1),dtype=float)
            ca=numpy.zeros((nc+1),dtype=float)
            Q0=numpy.zeros((nc+1),dtype=float)
            
            for h in range (0,nc+1):
                A[h]=(math.pi*D[h]**2)/4
                R[h]=f/(2*D[h]*A[h])
                dx[h]=L[h]/round(n[h])
                dt[h]=dx[h]/a[h]
                ca[h]=g*A[h]/a[h]
            for h in range (0,nc+1):
                if h==0:
                    Q0[h]=Q00
                else:
                    if h==nc:
                        Q0[h]=Q00-(sum(Q0[1:nc]))
                    else:
                        Q0[h]=(Q00*A[h])/(sum(A[1:nc+1]))
            As=(math.pi*Ds**2)/4
            n11=int(M/dx[c1-1])
            
            Q=list(numpy.zeros((nc+1),dtype=list))
            H=list(numpy.zeros((nc+1),dtype=list))
            h1=list(numpy.zeros((nc+1),dtype=list))
            cp=list(numpy.zeros((nc+1),dtype=list))
            cn=list(numpy.zeros((nc+1),dtype=list))
            Qps=numpy.zeros((int(round(T/dt[0])+2)),dtype=float)
            Zp=numpy.zeros((int(round(T/dt[0])+2)),dtype=float)
            Hmax=list(numpy.zeros((nc+1),dtype=list))
            Hmin=list(numpy.zeros((nc+1),dtype=list))
            h1max=list(numpy.zeros((nc+1),dtype=list))
            h1min=list(numpy.zeros((nc+1),dtype=list))
            x1=list(numpy.zeros((nc+1),dtype=list))  
            for h in range(0,nc+1):
                Q[h]=numpy.zeros((n[h]+1,int(round(T/dt[0])+2)),dtype=float)
                H[h]=numpy.zeros((n[h]+1,int(round(T/dt[0])+2)),dtype=float)
                Hmax[h]=numpy.zeros((n[h]+1),dtype=float)
                Hmin[h]=numpy.zeros((n[h]+1),dtype=float)
                h1max[h]=numpy.zeros((n[h]+1),dtype=float)
                h1min[h]=numpy.zeros((n[h]+1),dtype=float)
                x1[h]=numpy.zeros((n[h]+1),dtype=float)
                h1[h]=numpy.zeros((n[h]+1,int(round(T/dt[0])+2)),dtype=float)
                cp[h]=numpy.zeros((n[h]+1,int(round(T/dt[0])+3)),dtype=float)
                cn[h]=numpy.zeros((n[h]+1,int(round(T/dt[0])+3)),dtype=float)
                cv=numpy.zeros((nc+1,int(round(T/dt[0])+1)),dtype=float)
                thau=numpy.zeros((nc+1,int(round(T/dt[0])+1)),dtype=float)
            # calcul de Q(x,t),H(x,t),h(x,t),Hmax(x)et Hmin(x) aprés fermeture de la vanne
            # étape1:calcul en régime permanant(i.e avant la fermeture de la vanne
            for h in range(0,nc+1):
                if h==0:
                    for i in range(0,n[0]+1):
                        Q[h][i][0]=Q0[h]
                        H[h][i][0]=Hres-(k+1+f*i*dx[h]/D[h])*(Q00/A[h])**2/(2*g)
                        h1[h][i][0]=H[h][i][0]-Z[h]-(((Z[h]-Z[h+1])*dx[h]*i)/L[h])
                else:
                    for i in range(0,n[h]+1):
                        Q[h][i][0]=Q0[h]
                        H[h][i][0]=Hres-(k+1+(f*L[0]/D[0]))*(Q0[0]/A[0])**2/(2*g)-(f*i*dx[h]/D[h])*(Q0[h]/A[h])**2/(2*g)
                        h1[h][i][0]=H[h][i][0]-Z[1]-(((Z[1]-Z[h+1])*dx[h]*i)/L[h])
            Zp[0]=H[c1-1][n11][0]
            Qps[0]=0
            
            for h in range(0,nc+1):
                if h==0:
                    for i in range(0,n[0]+1):
                        Q[h][i][1]=Q0[h]
                        H[h][i][1]=Hres-(k+1+f*i*dx[h]/D[h])*(Q00/A[h])**2/(2*g)
                        h1[h][i][1]=H[h][i][1]-Z[h]-(((Z[h]-Z[h+1])*dx[h]*i)/L[h])
                else:
                    for i in range(0,n[h]+1):
                        if i<n[h]:
                            Q[h][i][1]=Q0[h]
                            H[h][i][1]=Hres-(k+1+(f*L[0]/D[0]))*(Q0[0]/A[0])**2/(2*g)-(f*i*dx[h]/D[h])*(Q0[h]/A[h])**2/(2*g)
                            h1[h][i][1]=H[h][i][1]-Z[1]-(((Z[1]-Z[h+1])*dx[h]*i)/L[h])
                        else:
                            if tf[h-1]==0:
                                Q[h][i][1]=0
                                H[h][i][1]=Hres-(k+1+(f*L[0]/D[0]))*(Q0[0]/A[0])**2/(2*g)-(f*i*dx[h]/D[h])*(Q0[h]/A[h])**2/(2*g) 
                            else:
                                Q[h][i][1]=Q0[h]
                                H[h][i][1]=Hres-(k+1+(f*L[0]/D[0]))*(Q0[0]/A[0])**2/(2*g)-(f*i*dx[h]/D[h])*(Q0[h]/A[h])**2/(2*g) 
                            h1[h][i][1]=H[h][i][1]-Z[1]-(((Z[1]-Z[h+1])*dx[h]*i)/L[h])
            Zp[1]=H[c1-1][n11][1]
            Qps[1]=0
            
            for h in range(0,nc+1):
                for i in range(0,n[h]):
                    cp[h][i+1][2]=Q[h][i][1]+g*A[h]/a[h]*H[h][i][1]-R[h]*dt[0]*Q[h][i][1]*abs(Q[h][i][1])
                    cn[h][i][2]=Q[h][i+1][1]-g*A[h]/a[h]*H[h][i+1][1]-R[h]*dt[0]*Q[h][i+1][1]*abs(Q[h][i+1][1])
                     
               # étape2:calcul en régime transitoire(i.e aprés la fermeture de les vannes)
            for j in range(2,int(round(T/dt[0])+2)):
                for h in range(0,nc+1):
                    if dt[0]*(j-1)<tf[h-1]:
                        thau[h][j-2]=1-(j-1)*dt[0]/tf[h-1]
                    else:
                        thau[h][j-2]=0
                    for i in range(0,n[h]+1):
                        if i==0:
                            if h==0:#calcul au niveau de réservoir
                                Q[h][i][j]=(-1+(1+4*(ca[h]*(1+k)/(2*g*A[h]**2))*(cn[h][i][j]+ca[h]*Hres))**0.5)/(2*(ca[h]*(1+k)/(2*g*A[h]**2)))
                                if Q[h][i][j]>=0:
                                    Q[h][i][j]=(-1+(1+4*(ca[h]*(1+k)/(2*g*A[h]**2))*(cn[h][i][j]+ca[h]*Hres))**0.5)/(2*(ca[h]*(1+k)/(2*g*A[h]**2)))
                                    H[h][i][j]=Hres-(1+k)*Q[h][i][j]**2/(2*g*A[h]**2)
                                else:
                                    Q[h][i][j]=(-1+(1+4*(ca[h]*(1-k)/(2*g*A[h]**2))*(cn[h][i][j]+ca[h]*Hres))**0.5)/(2*(ca[h]*(1-k)/(2*g*A[h]**2)))
                                    if  Q[h][i][j]>=0:
                                        print("***********ya un probleme ***********")
                                    else:
                                        H[h][i][j]=Hres-(1-k)*Q[h][i][j]**2/(2*g*A[h]**2)
                                h1[h][i][j]=H[h][i][j]-Z[h]-(((Z[h]-Z[h+1])*dx[h]*i)/L[h])
                            else: #calcul au premier  noeud de chaque conduite sauf premiere conduite
                                H[h][i][j]=H[0][n[0]][j]
                                Q[h][i][j]=cn[h][i][j]+ca[h]*H[h][i][j]
                                h1[h][i][j]=h1[0][n[0]][j]              
                        elif i==n[h]:#calcul au dernier noeud de chaque conduite 
                            if h==0: # premiere conduite'conduite principale 
                                cnt=0
                                for p in range(1,nc+1):
                                    cnt=cnt+cn[p][0][j]
                                    H[h][i][j]=(cp[h][i][j]-cnt)/(sum(ca))
                                    Q[h][i][j]=cp[h][i][j]-ca[h]*H[h][i][j]
                                    h1[h][i][j]=H[h][i][j]-Z[h]-(((Z[h]-Z[h+1])*dx[h]*i)/L[h])
                            else: # les aures conduites 
                                cv[h][j-2]=((thau[h][j-2]*Q[h][round(n[h])][1])**2)/(ca[h]*H[h][round(n[h])][1])
                                Q[h][i][j]=0.5*(-cv[h][j-2]+(cv[h][j-2]**2+4*cp[h][i][j]*cv[h][j-2])**0.5)
                                H[h][i][j]=(cp[h][i][j]-Q[h][i][j])/ca[h]
                                h1[h][i][j]=H[h][i][j]-Z[1]-(((Z[1]-Z[h+1])*dx[h]*i)/L[h])
                        elif i==n11 and h==c1-1: #calcul au niveau de la cheminée d'équilibre 
                            H[h][i][j]=(cp[h][i][j]-cn[h][i][j]+Qps[j-1]+2*(As*Zp[j-1]/dt[0]))/(ca[h]+ca[h]+2*(As/dt[0]))
                            Q[h][i][j] = cp[h][i][j]-ca[h]*H[h][i][j]
                            if c1==1:
                                h1[h][i][j]=H[h][i][j]-Z[h]-(((Z[h]-Z[h+1])*dx[h]*i)/L[h])
                            else:
                                h1[h][i][j]=H[h][i][j]-Z[1]-(((Z[1]-Z[h+1])*dx[h]*i)/L[h])
                        elif i<n[h]: # calcul pour les noeuds intermédiaires
                            Q[h][i][j]=(cp[h][i][j]+cn[h][i][j])/2
                            H[h][i][j]=(Q[h][i][j]-cn[h][i][j])/ca[h]
                            if h==0:
                                h1[h][i][j]=H[h][i][j]-Z[h]-(((Z[h]-Z[h+1])*dx[h]*i)/L[h])
                            else:
                                h1[h][i][j]=H[h][i][j]-Z[1]-(((Z[1]-Z[h+1])*dx[h]*i)/L[h])
                                
                for h in range(0,nc+1):
                    for i in range (1,n[h]+1):
                              cp[h][i][j+1]=Q[h][i-1][j]+ca[h]*H[h][i-1][j]-R[h]*dt[0]*Q[h][i-1][j]*abs(Q[h][i-1][j])
                    for i in range (0,n[h]):
                              cn[h][i][j+1]=Q[h][i+1][j]-ca[h]*H[h][i+1][j]-R[h]*dt[0]*Q[h][i+1][j]*abs(Q[h][i+1][j])
                Qps[j]=Q[c1-1][n11][j]-Q[c1-1][n11+1][j]
                Zp[j]=Zp[j-1]+0.5*(dt[0]/As)*(Qps[j]+Qps[j-1])
            
            t=numpy.zeros((int(round(T/dt[0])+2)),dtype=float)
            for i in range(1,int(round(T/dt[0])+2)):
                t[i]=dt[0]+t[i-1]
             # calcul les Hmax(x),Hmin(x),hmax(x) et hmin(x)   
            for h in range(0,nc+1):
                for i in range(0,n[h]+1):
                    Hmax[h][i]=max(H[h][i][:])
                    Hmin[h][i]=min(H[h][i][:])
                    h1max[h][i]=max(h1[h][i][:])
                    h1min[h][i]=min(h1[h][i][:])
                    if i==0:
                        x1[h][i]=0
                    else:
                        x1[h][i]=dx[h]+x1[h][i-1]
            return(t,x1,H,h1,Q,Hmax,Hmin,h1max,h1min,Zp,Qps)
# %% affiches les graphes [reservoir-conduite en parallèle-vanne]+reservoir d'air
def display_result(page,canvas,frame,Hres_entry,k_entry,Q0_entry,n_entry,f_entry,nc_entry,l1,d1,a1,Z1,tf1,Ds_entry,M_entry,c1_entry,c_entry,T_entry,x_entry):                   
            nc=int(nc_entry.get()) 
            f= float(f_entry.get())  
            n1 = int(n_entry.get()) 
            Hres=float( Hres_entry.get())
            Q00=float(Q0_entry.get()) 
            k=float(k_entry.get()) 
            x=float(x_entry.get())
            T=float(T_entry.get())
            c=int(c_entry.get()) 
            c1=int(c1_entry.get())
            Ds=int(Ds_entry.get())
            M=int(M_entry.get())
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
            n=numpy.zeros((nc+1),dtype=int)
            for h in range (0,nc+1):
                if h==0:
                    n[0]=n1
                else:
                    n[h]= int(round((L[h]*a[0]*n[0])/(L[0]*a[h])))
            dx=numpy.zeros((nc+1),dtype=float)
            for h in range (0,nc+1):
                dx[h]=L[h]/round(n[h])
            # message d'erreur
            if c==0 or c>nc+1:
                tk.messagebox.showerror("erreur sur la page'exécuter' ", "la valeur C doit être superieur à 0 et inferieur à %d" %nc)
                for child in frame.winfo_children():
                    child.destroy()
                exit(0)    
            if c1==0 or c1>nc+1:
                tk.messagebox.showerror("erreur sur la page'cheminee d'equilibre'", "la valeur C doit être superieur à 0 et inferieur à %d" %nc)
                for child in frame.winfo_children():
                    child.destroy()
                exit(0) 
            t,x1,H,h1,Q,Hmax,Hmin,h1max,h1min,Zp,Qps=result(Hres,k,Q00,n1,f,nc,L,D,a,Z,tf,Ds,M,c1,c,T,x)
            # zoom les graphe
            aircombobox = ttk.Combobox(page, values=[
                                        "- Charge hydraulique H(m)", 
                                        "- Pression(m)",
                                        "- Enveloppe H(x)",
                                        "- Enveloppe de pression (m)",
                                        "- Débit volumique Q(m3/s)",
                                        "- Qps(t) de cheminée d'équilibre ",
                                        "- Zp(t) de cheminée d'équilibre "],width=35)
            aircombobox.insert(0,'sélectionnez une réponse')
            aircombobox.bind('<<ComboboxSelected>>',lambda event:zoom(aircombobox,t,x1,H,h1,Q,Hmax,Hmin,h1max,h1min,Zp,Qps,x,c,L,n,nc,dx))
            canvas.create_window(140, 310,window=aircombobox)
            canvas.create_text(130,290,text="-ZOOM")
            
            # plots les graphes sur l'interface graphique 
            fig = Figure(figsize=(15,9), dpi=80)
            if x<=L[c-1] and x>=0 :
                ax = fig.add_subplot(331)
                fig.subplots_adjust( wspace=0.3, hspace=0.4)
                ax.grid(True)
                ax.plot(t,H[c-1][int(round(x/dx[c-1]))][:])
                ax.plot(t,H[c-1][int(round(x/dx[c-1]))][:],'b')
                ax.set_xlabel("Temps [s]")
                ax.set_ylabel("Charge hydraulique H(m)")
                ax.set_title("H(t) x=%s la Conduite:%s "%(x,c))
                
                ax = fig.add_subplot(332)
                ax.grid(True)
                ax.plot(t,h1[c-1][int(round(x/dx[c-1]))][:])
                ax.plot(t,h1[c-1][int(round(x/dx[c-1]))][:],'b')
                ax.set_xlabel("Temps [s]")
                ax.set_ylabel("Pression (m)")
                ax.set_title("Pression(t) x=%s la Conduite:%s "%(x,c))
                
                ax = fig.add_subplot(333)
                ax.grid(True)  
                ax.plot(t,Q[c-1][int(round(x/dx[c-1]))][:])
                ax.plot(t,Q[c-1][int(round(x/dx[c-1]))][:],'r')
                ax.set_xlabel("Temps [s]")
                ax.set_ylabel("Débit volumique Q(m3/s)")
                ax.set_title("Q(t) x=%s la Conduite:%s "%(x,c))
                
                ax = fig.add_subplot(334)
                ax.grid(True)
                ax.plot(x1[c-1],Hmax[c-1][:],'r',label='H max')
                ax.plot(x1[c-1],Hmin[c-1][:],'b',label='H min')
                for i in range (0,n[c-1]+1) :
                    if Hmax[c-1][i]==max(Hmax[c-1]):
                        ax.plot(x1[c-1][i],Hmax[c-1][i],'bo')
                        p=x1[c-1][i]
                ax.plot(p,max(Hmax[c-1]),'bo',label='max(Hmax)')
                for i in range (0,n[c-1]+1) :
                    if Hmin[c-1][i]==min(Hmin[c-1]):
                        ax.plot(x1[c-1][i],Hmin[c-1][i],'ro')
                        p=x1[c-1][i]
                ax.plot(p,min(Hmin[c-1]),'ro',label='max(Hmax)')
                ax.set_xlabel("Distance x[m]")
                ax.set_ylabel("Charge hydraulique H(m)")
                ax.set_title("Enveloppe H(x) de   Conduite:%s "%(c))
                ax.legend()
                
                ax = fig.add_subplot(335)
                ax.grid(True)
                ax.plot(x1[c-1],h1max[c-1][:],'r',label='h max')
                ax.plot(x1[c-1],h1min[c-1][:],'b',label='h min')
                for i in range (0,n[c-1]+1) :
                    if h1max[c-1][i]==max(h1max[c-1]):
                        ax.plot(x1[c-1][i],h1max[c-1][i],'bo')
                        p=x1[c-1][i]
                ax.plot(x1[c-1][i],h1max[c-1][i],'bo',label='max(h max)')
                for i in range (0,n[c-1]+1) :
                    if h1min[c-1][i]==min(h1min[c-1]):
                        ax.plot(x1[c-1][i],h1min[c-1][i],'ro')
                        p=x1[c-1][i]
                ax.plot(x1[c-1][i],h1min[c-1][i],'ro',label='min(h min)')
                ax.set_xlabel("Distance x[m]")
                ax.set_ylabel("Pression (m)")
                ax.set_title("Enveloppe Pression (x)dans Conduite:%s "%(c))
                ax.legend()
                
                if c==c1:
                    ax = fig.add_subplot(337)
                    ax.grid(True)
                    ax.plot(t,Zp[:],'b')
                    ax.set_xlabel("Temps [s]")
                    ax.set_ylabel("Zp[m]")
                    ax.set_title("Zp(t) de cheminée d'équilibre ")
                    
                    ax = fig.add_subplot(338)
                    ax.grid(True)
                    ax.plot(t,Qps[:],'b')
                    ax.set_xlabel("Temps [s]")
                    ax.set_ylabel("Qps")
                    ax.set_title("Qps(t) de cheminée d'équilibre ")                 
                graph = FigureCanvasTkAgg(fig,master=frame)                    
                return(graph.get_tk_widget())
# %% enregistrer [reservoir-conduite en parallèle-vanne]+reservoir d'air
def save(Hres_entry,k_entry,Q0_entry,n_entry,f_entry,nc_entry,l1,d1,a1,Z1,tf1,Ds_entry,M_entry,c1_entry,c_entry,T_entry,x_entry):
    nc=int(nc_entry.get()) # nombre de conduite
    f= float(f_entry.get())  # coefficient de frottement de Darcy_weisbach    
    n1 = int(n_entry.get()) # discrétisation de la premier  conduite : nombre de ségements
    Hres=float( Hres_entry.get())# niveau d'eau dans le réservoir 
    Q00=float(Q0_entry.get()) # débit initial d'ecoulement
    k=float(k_entry.get()) # débit initial d'ecoulement
    x=float(x_entry.get())# coefficient de perte de charge sigulière 
    T=float(T_entry.get())# the coordinate for which H(t),Q(t)and h(t) will be ploted
    c=int(c_entry.get()) # temps de simulation 
    c1=int(c1_entry.get())# temps de fermeture de la vanne
    Ds=int(Ds_entry.get())# tracer les paramètres de la conduite c 
    M=int(M_entry.get())
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
    n=numpy.zeros((nc+1),dtype=int)
    for h in range (0,nc+1):
        if h==0:
            n[0]=n1
        else:
            n[h]= int(round((L[h]*a[0]*n[0])/(L[0]*a[h])))
    dx=numpy.zeros((nc+1),dtype=float)
    dt=numpy.zeros((nc+1),dtype=float)
    for h in range (0,nc+1):
        dx[h]=L[h]/round(n[h])
        dt[h]=dx[h]/a[h]
    
    t,x1,H,h1,Q,Hmax,Hmin,h1max,h1min,Zp,Qps=result(Hres,k,Q00,n1,f,nc,L,D,a,Z,tf,Ds,M,c1,c,T,x)
    workbook = xlsxwriter.Workbook("reservoir-conduite_en_parallèle-vanne+reservoir d'air.xlsx")
    worksheet = workbook.add_worksheet('H(x,t)')
    for h in range(0,nc+1):
        if h==0: 
            for j in range (1,int(round(T/dt[0])+2)):
                for i in range (1,n[h]+2):
                    worksheet.write(0,0,'t[s]')
                    worksheet.write(i,0,'H[%s m]'%int(x1[h][i-1]))
                    worksheet.write(0,j,t[j-1])
                    worksheet.write(i,j,H[h][i-1][j-1])
        else:
            for j in range (1,int(round(T/dt[0])+2)):
                for i in range (1,n[h]+2):
                    worksheet.write(i+sum(n[0:h]+1)+h,0,'H[%s m]'%int(x1[h][i-1]))
                    worksheet.write(i+sum(n[0:h]+1)+h,j,H[h][i-1][j-1])
            
    worksheet = workbook.add_worksheet('p(x,t)')
    for h in range(0,nc+1):
        if h==0: 
            for j in range (1,int(round(T/dt[0])+2)):
                for i in range (1,n[h]+2):
                    worksheet.write(0,0,'t[s]')
                    worksheet.write(i,0,'h[%s m]'%int(x1[h][i-1]))
                    worksheet.write(0,j,t[j-1])
                    worksheet.write(i,j,h1[h][i-1][j-1])
        else:
            for j in range (1,int(round(T/dt[0])+2)):
                for i in range (1,n[h]+2):
                    worksheet.write(i+sum(n[0:h]+1)+h,0,'h[%s m]'%int(x1[h][i-1]))
                    worksheet.write(i+sum(n[0:h]+1)+h,j,h1[h][i-1][j-1])
            
    worksheet = workbook.add_worksheet('Q(x,t)')
    for h in range(0,nc+1):
        if h==0: 
            for j in range (1,int(round(T/dt[0])+2)):
                for i in range (1,n[h]+2):
                    worksheet.write(0,0,'t[s]')
                    worksheet.write(i,0,'Q[%s m^3/s]'%int(x1[h][i-1]))
                    worksheet.write(0,j,t[j-1])
                    worksheet.write(i,j,Q[h][i-1][j-1])
        else:
            for j in range (1,int(round(T/dt[0])+2)):
                for i in range (1,n[h]+2):
                    worksheet.write(i+sum(n[0:h]+1)+h,0,'Q[%s m^3/s]'%int(x1[h][i-1]))
                    worksheet.write(i+sum(n[0:h]+1)+h,j,Q[h][i-1][j-1])
     
    worksheet = workbook.add_worksheet('Zp et Qps')
    for j in range (1,int(round(T/dt[0])+2)):
        worksheet.write(0,0,'t[s]')
        worksheet.write(0,j,t[j-1])
        worksheet.write(1,0,'Zp[m]')
        worksheet.write(1,j,Zp[j-1])
        worksheet.write(2,0,'Qps[m^3/s]')
        worksheet.write(2,j,Qps[j-1])
                           
    worksheet = workbook.add_worksheet('Hmax et hmax')
    for h in range(0,nc+1):
        if h==0: 
            for i in range (1,n[h]+2):
                worksheet.write(i,0,'Hmax[%s m]'%int(x1[h][i-1]))
                worksheet.write(i,1,Hmax[h][i-1])
                worksheet.write(i,2,'hmax[%s m]'%int(x1[h][i-1]))
                worksheet.write(i,3,h1max[h][i-1])
        else:
            for i in range (1,n[h]+2):
                worksheet.write(i+sum(n[0:h]+1)+h,0,'Hmax[%s m]'%int(x1[h][i-1]))
                worksheet.write(i+sum(n[0:h]+1)+h,1,Hmax[h][i-1])
                worksheet.write(i+sum(n[0:h]+1)+h,2,'hmax[%s m]'%int(x1[h][i-1]))
                worksheet.write(i+sum(n[0:h]+1)+h,3,h1max[h][i-1])
                    
    worksheet = workbook.add_worksheet('Hminet hmin')
    for h in range(0,nc+1):
        if h==0: 
            for i in range (1,n[h]+2):
                worksheet.write(i,0,'Hmin[%s m]'%int(x1[h][i-1]))
                worksheet.write(i,1,Hmin[h][i-1])
                worksheet.write(i,2,'hmin[%s m]'%int(x1[h][i-1]))
                worksheet.write(i,3,h1min[h][i-1])
        else:
            for i in range (1,n[h]+2):
                worksheet.write(i+sum(n[0:h]+1)+h,0,'Hmin[%s m]'%int(x1[h][i-1]))
                worksheet.write(i+sum(n[0:h]+1)+h,1,Hmin[h][i-1])
                worksheet.write(i+sum(n[0:h]+1)+h,2,'hmin[%s m]'%int(x1[h][i-1]))
                worksheet.write(i+sum(n[0:h]+1)+h,3,h1min[h][i-1])                            
    workbook.close() 