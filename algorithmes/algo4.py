# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 07:45:43 2020

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
def zoom(combobox,t,x1,H,h1,Q,Hmax,Hmin,h1max,h1min,MaxHmax,MinHmin,Maxhmax,Minhmin,L,x,c,nc,n,dx):
    
    choice=combobox.get()
    if choice== "- Charge hydraulique H(m)":
            window=tk.Tk()
            window.state('zoomed')
            window.title(choice)
            window.iconbitmap(r'photos\images.ico')
            fig =Figure (figsize=(16,11), dpi=140)
            ax = fig.add_subplot(111) 
            if x<=sum(L[0:c]) and x>=0 :
                fig.subplots_adjust( wspace=1.4, hspace=1)
                ax.grid(True)
                ax.plot(t,H[int(sum(n[0:c])+(round(((x-sum(L[0:c]))/dx[c-1])+c-1)))][:])
                ax.plot(t,H[int(sum(n[0:c])+(round(((x-sum(L[0:c]))/dx[c-1])+c-1)))][:],'b')
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
            if x<=sum(L[0:c]) and x>=0 :
                fig.subplots_adjust( wspace=1.4, hspace=1)
                ax.grid(True)
                ax.plot(t,h1[int(sum(n[0:c])+(round(((x-sum(L[0:c]))/dx[c-1])+c-1)))][:])
                ax.plot(t,h1[int(sum(n[0:c])+(round(((x-sum(L[0:c]))/dx[c-1])+c-1)))][:],'g')
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
            if x<=sum(L[0:c]) and x>=0:
                 fig.subplots_adjust( wspace=1.4, hspace=1)
                 ax.grid(True)
                 ax.plot(x1,Hmax[:],'r',label='H max')
                 ax.plot(x1,Hmin[:],'b',label='H min')
                 for h in range(0,nc):
                     if h==0:
                         for i in range (0,int(n[h]+1)):
                             if Hmax[i]==MaxHmax[h]:
                                 ax.plot(x1[i],MaxHmax[h],'bo')
                     else:
                         for i in range(int(sum(n[0:h]+1)),int(sum(n[0:h+1]+1))):
                            if Hmax[i]==MaxHmax[h]:
                                ax.plot(x1[i],MaxHmax[h],'bo')
                                p=x1[i]
                 ax.plot(p,MaxHmax[h],'bo',label='max(H max)')
                 for h in range(0,nc):
                     if h==0:
                         for i in range (0,int(n[h]+1)):
                             if Hmin[i]==MinHmin[h]:
                                 ax.plot(x1[i],MinHmin[h],'ro')
                     else:
                         for i in range(int(sum(n[0:h]+1)),int(sum(n[0:h+1]+1))):
                             if Hmin[i]==MinHmin[h]:
                                 ax.plot(x1[i],MinHmin[h],'ro')
                                 p=x1[i]
                 ax.plot(p,MinHmin[h],'ro',label='min(H min)')
                 ax.set_xlabel("Distance x[m]")
                 ax.set_ylabel("Charge hydraulique H(m)")
                 ax.set_title("Enveloppe H(x) de x=%s "%x)
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
            if x<=sum(L[0:c]) and x>=0:
                 fig.subplots_adjust( wspace=1.4, hspace=1)
                 ax.grid(True)
                 ax.plot(x1,h1max[:],'r',label='h max')
                 ax.plot(x1,h1min[:],'b',label='h min')
                 for h in range(0,nc):
                    if h==0:
                         for i in range (0,int(n[h]+1)):
                             if h1max[i]==Maxhmax[h]:
                                 ax.plot(x1[i],Maxhmax[h],'bo')
                                 
                    else:
                        for i in range(int(sum(n[0:h]+1)),int(sum(n[0:h+1]+1))):
                            if h1max[i]==Maxhmax[h]:
                                ax.plot(x1[i],Maxhmax[h],'bo')
                                p=x1[i]    
                 ax.plot(p,Maxhmax[h],'bo',label='max(h max)')
                 
                 for h in range(0,nc):
                    if h==0:
                        for i in range (0,int(n[h]+1)):
                            if h1min[i]==Minhmin[h]:
                                ax.plot(x1[i],Minhmin[h],'ro')
                    else:
                        for i in range(int(sum(n[0:h]+1)),int(sum(n[0:h+1]+1))):
                            if h1min[i]==Minhmin[h]:
                                ax.plot(x1[i],Minhmin[h],'ro')
                                p=x1[i]
                 ax.plot(p,Minhmin[h],'ro',label='min(h min)')
                 ax.set_xlabel("Distance x[m]")
                 ax.set_ylabel("Pression(m)")
                 ax.set_title("Enveloppe de Pression(x) de x=%s "%x)
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
            if x<=sum(L[0:c]) and x>=0 :
                fig.subplots_adjust( wspace=1.4, hspace=1)
                ax.grid(True)  
                ax.plot(t,Q[int(sum(n[0:c])+(round(((x-sum(L[0:c]))/dx[c-1])+c-1)))][:])
                ax.plot(t,Q[int(sum(n[0:c])+(round(((x-sum(L[0:c]))/dx[c-1])+c-1)))][:],'r')
                ax.set_xlabel("Temps [s]")
                ax.set_ylabel("Débit volumique Q(m3/s)")
                ax.set_title("Q(t) x=%s la Conduite:%s "%(x,c))
                graph = FigureCanvasTkAgg(fig,master=window)
                graph.get_tk_widget().pack()
# %% calcul [reservoir-conduite en serie-vanne]
def result(Hres,k,n,nc,f,L,D,a,Z,Q0,tf,T):
            g=9.81
            A=numpy.zeros((nc),dtype=float)
            R=numpy.zeros((nc),dtype=float)
            dx=numpy.zeros((nc),dtype=float)
            dt=numpy.zeros((nc),dtype=float)
            ca=numpy.zeros((nc),dtype=float)
            for h in range (0,nc):
                A[h]=(math.pi*D[h]**2)/4
                R[h]=f/(2*D[h]*A[h])
                dx[h]=L[h]/round(n[h])
                dt[h]=dx[h]/a[h]
                ca[h]=g*A[h]/a[h]
            Q=numpy.zeros((int(sum(n)+nc),int(round(T/min(dt))+2)),dtype=float)
            H=numpy.zeros((int(sum(n)+nc),int(round(T/min(dt))+2)),dtype=float)
            h1=numpy.zeros((int(sum(n)+nc),int(round(T/min(dt))+2)),dtype=float)
            cn=numpy.zeros((int(sum(n)+nc),int(round(T/min(dt))+3)),dtype=float)
            cp=numpy.zeros((int(sum(n)+nc),int(round(T/min(dt))+3)),dtype=float)
            thau=numpy.zeros((int(round(T/min(dt))+3)),dtype=float)
            cv=numpy.zeros((int(round(T/min(dt))+3)),dtype=float)
            Hmax=numpy.zeros((int(sum(n)+nc)),dtype=float)
            Hmin=numpy.zeros((int(sum(n)+nc)),dtype=float)
            h1max=numpy.zeros((int(sum(n)+nc)),dtype=float)
            h1min=numpy.zeros((int(sum(n)+nc)),dtype=float)
            MaxHmax=numpy.zeros((nc),dtype=float)
            MinHmin=numpy.zeros((nc),dtype=float)
            Maxhmax=numpy.zeros((nc),dtype=float)
            Minhmin=numpy.zeros((nc),dtype=float)
            x1=numpy.zeros((int(sum(n)+nc)),dtype=float)
            
            # calcul de Q(x,t),H(x,t),h(x,t),Hmax(x)et Hmin(x) aprés fermeture de la vanne
            # étape1:calcul en régime permanant(i.e avant la fermeture de la vanne)
            for h in range(0,nc):
                p=0
                for y in range (0,h):
                    if y==0:
                        p=p+(k+1+(f*L[y]/D[y]))*(Q0/A[y])**2/(2*g)
                    else:
                        p=p+(f*L[y]/D[y])*(Q0/A[y])**2/(2*g)
                   
                if h==0:
                    for i in range (0,int(n[h]+1)):
                        Q[i][0]=Q0
                        H[i][0]=Hres-(k+1+f*i*dx[0]/D[0])*(Q0/A[0])**2/(2*g)
                        h1[i][0]=H[i][0]-Z[h]-(((Z[h]-Z[h+1])*dx[h]*i)/sum(L))
                        
                else:
                    for i in range(int(sum(n[0:h]+1)),int(sum(n[0:h+1]+1))):
                        if i==sum(n[0:h]+1):
                            Q[i][0]=Q0
                            H[i][0]=H[sum(n[0:h])+h-1][0]
                            h1[i][0]=h1[sum(n[0:h])+h-1][0]
                        else :
                            Q[i][0]=Q0
                            H[i][0]=Hres-(p)-(f*(i-(sum(n[0:h])+h))*dx[h]/D[h])*(Q0/A[h])**2/(2*g) 
                            h1[i][0]=H[i][0]-Z[h]-(((Z[h]-Z[h+1])*dx[h]*(i-(sum(n[0:h])+h)))/sum(L))
            for h in range(0,nc):
                p=0
                for y in range (0,h):
                    if y==0:
                        p=p+(k+1+(f*L[y]/D[y]))*(Q0/A[y])**2/(2*g)
                    else:
                        p=p+(f*L[y]/D[y])*(Q0/A[y])**2/(2*g)
                if h==0:
                    for i in range (0,int(n[h]+1)):
                        Q[i][1]=Q0
                        H[i][1]=Hres-(k+1+f*i*dx[0]/D[0])*(Q0/A[0])**2/(2*g)
                        h1[i][1]=H[i][1]-Z[h]-(((Z[h]-Z[h+1])*dx[h]*i)/sum(L))
                else:
                    for i in range(int(sum(n[0:h]+1)),int(sum(n[0:h+1]+1))):
                        if i!=sum(n)+nc-1:
                                if i==sum(n[0:h]+1):
                                    Q[i][1]=Q0
                                    H[i][1]=H[sum(n[0:h])+h-1][1]
                                    h1[i][1]=h1[sum(n[0:h])+h-1][1]
                                else :
                                    Q[i][1]=Q0
                                    H[i][1]=Hres-(p)-(f*(i-(sum(n[0:h])+h))*dx[h]/D[h])*(Q0/A[h])**2/(2*g) 
                                    h1[i][1]=H[i][1]-Z[h]-(((Z[h]-Z[h+1])*dx[h]*(i-(sum(n[0:h])+h)))/sum(L))                         
                        else:
                            H[i][1]=H[i][0]
                            h1[i][1]=h1[i][0]
                            if tf==0:
                                Q[i][1]=0
                            else:
                                Q[i][1]=Q0
                          
            for h in range(0,nc):
                if h ==0:
                    for i in range (0,int(n[h]+1)):            
                        cp[i+1][2]=Q[i][1]+g*A[h]/a[h]*H[i][1]-R[h]*min(dt)*Q[i][1]*abs(Q[i][1])
                        cn[i][2]=Q[i+1][1]-g*A[h]/a[h]*H[i+1][1]-R[h]*min(dt)*Q[i+1][1]*abs(Q[i+1][1])
                else:
                    for i in range (int(sum(n[0:h]+1)),int(sum(n[0:h+1])+h)):
                        cp[i+1][2]=Q[i][1]+g*A[h]/a[h]*H[i][1]-R[h]*min(dt)*Q[i][1]*abs(Q[i][1])
                        cn[i][2]=Q[i+1][1]-g*A[h]/a[h]*H[i+1][1]-R[h]*min(dt)*Q[i+1][1]*abs(Q[i+1][1])
            # étape2:calcul en régime transitoire(i.e aprés la fermeture de la vanne)            
            for j in range(2,int(round(T/min(dt))+2)):
                if min(dt)*(j-1)<tf:
                       thau[j-2]=1-(j-1)*min(dt)/tf
                else:
                    thau[j-2]=0
                for h in range(0,nc):
                    for i in range(int(sum(n[0:h]+1)),int(sum(n[0:h+1]+1))):
                        if i==0: #calcul au niveau de réservoir
                            Q[i][j]=(-1+(1+4*(ca[0]*(1+k)/(2*g*A[0]**2))*(cn[i][j]+ca[0]*Hres))**0.5)/(2*(ca[0]*(1+k)/(2*g*A[0]**2)))
                            if Q[i][j]>=0:
                                Q[i][j]=(-1+(1+4*(ca[0]*(1+k)/(2*g*A[0]**2))*(cn[i][j]+ca[0]*Hres))**0.5)/(2*(ca[0]*(1+k)/(2*g*A[0]**2)))
                                H[i][j]=Hres-(1+k)*Q[i][j]**2/(2*g*A[0]**2)
                            else:
                                Q[i][j]=(-1+(1+4*(ca[0]*(1-k)/(2*g*A[0]**2))*(cn[i][j]+ca[0]*Hres))**0.5)/(2*(ca[0]*(1-k)/(2*g*A[0]**2)))
                                if Q[i][j]>=0:
                                    print("***********ya un probleme ***********")
                                else:
                                    H[i][j]=Hres-(1-k)*Q[i][j]**2/(2*g*A[0]**2)
                            h1[i][j]=H[i][j]-Z[h]
                        else:
                            if i==sum(n)+nc-1: # calcul au niveau de la vanne 
                                cv[j-2]=(thau[j-2]*Q[sum(n)+nc-1][1])**2/(ca[nc-1]*H[sum(n)+nc-1][1])
                                Q[i][j]=0.5*(-cv[j-2]+(cv[j-2]**2+4*cp[i][j]*cv[j-2])**0.5)
                                H[i][j]=(cp[i][j]-Q[i][j])/ca[nc-1]
                                h1[i][j]=H[i][j]-(Z[0]-((Z[0]-Z[nc])/sum(L)))
                            else :
                                if i==sum(n[0:h]+1): #calcul au dernier noeud de chaque conduite  
                                    H[i][j]= H[sum(n[0:h])+h-1][j]
                                    Q[i][j]=cn[i][j]+ca[h]*H[i][j]
                                    h1[i][j]=h1[sum(n[0:h])+h-1][j]
                                elif i==(sum(n[0:h+1]+1))-1 :#calcul au premier  noeud de chaque conduite
                                    H[i][j]=(cp[i][j]-cn[i+1][j])/(ca[h]+ca[h+1])
                                    Q[i][j]=cp[i][j]-ca[h]*H[i][j]
                                    h1[i][j]=H[i][j]-Z[h+1]
                                else: # calcul pour les noeuds intermédiaires
                                    Q[i][j]=(cp[i][j]+cn[i][j])/2
                                    H[i][j]=(Q[i][j]-cn[i][j])/ca[h]
                                    h1[i][j]=H[i][j]-Z[h]-(((Z[h]-Z[h+1])*dx[h]*(i-(sum(n[0:h])+h)))/sum(L))
                       
                for h in range(0,nc):
                    if h ==0:
                        for i in range (0,int(n[h]+1)):
                            cn[i][j+1]=Q[i+1][j]-g*A[0]/a[0]*H[i+1][j]-R[0]*min(dt)*Q[i+1][j]*abs(Q[i+1][j])
                        for i in range (1,n[h]+1):
                            cp[i][j+1]=Q[i-1][j]+g*A[0]/a[0]*H[i-1][j]-R[0]*min(dt)*Q[i-1][j]*abs(Q[i-1][j])
                    else:
                        for i in range (int(sum(n[0:h]+1)),int(sum(n[0:h+1])+h)):
                            cn[i][j+1]=Q[i+1][j]-g*A[h]/a[h]*H[i+1][j]-R[h]*min(dt)*Q[i+1][j]*abs(Q[i+1][j])
                        for i in range (sum(n[0:h]+1),sum(n[0:h+1]+1)):
                            cp[i][j+1]=Q[i-1][j]+g*A[h]/a[h]*H[i-1][j]-R[h]*min(dt)*Q[i-1][j]*abs(Q[i-1][j])
                            
            t=numpy.zeros((int(round(T/min(dt))+2)),dtype=float)
            for i in range(1,int(round(T/min(dt))+2)):
                t[i]=min(dt)+t[i-1]
            # calcul les Hmax(x),Hmin(x),hmax(x) et hmin(x)

            for h in range(0,nc):
                if h==0:
                    for i in range (0,int(n[h]+1)):
                        Hmax[i]=max(H[i][:])
                        Hmin[i]=min(H[i][:])
                        h1max[i]=max(h1[i][:])
                        h1min[i]=min(h1[i][:])
                        if i==0:
                            x1[i]=0
                        else:
                            x1[i]=dx[h]+x1[i-1]
                else:
                    for i in range(int(sum(n[0:h]+1)),int(sum(n[0:h+1]+1))):
                        Hmax[i]=max(H[i][:])
                        Hmin[i]=min(H[i][:])
                        h1max[i]=max(h1[i][:])
                        h1min[i]=min(h1[i][:])
                        if i==int(sum(n[0:h]+1)):
                            x1[i]=x1[i-1]
                        else:
                            x1[i]=dx[h]+x1[i-1]
                MaxHmax[h]=max(Hmax)
                MinHmin[h]=min(Hmin[0:sum(n[0:h+1]+1)])
                Maxhmax[h]=max(h1max)
                Minhmin[h]=min(h1min[0:sum(n[0:h+1]+1)])
            return (t,x1,H,h1,Q,Hmax,Hmin,h1max,h1min,MaxHmax,MinHmin,Maxhmax,Minhmin)

# %% affiches les graphes [reservoir-conduite en serie-vanne]        
def display_result(page,canvas,frame,Hres_entry,k_entry,n_entry,nc_entry,f_entry,l1,d1,a1,Z1,Q0_entry,tf_entry,T_entry,x_entry,c_entry):
        Hres=float(Hres_entry.get())
        k=float(k_entry.get())
        f= float(f_entry.get())
        n1 = int(n_entry.get())
        Q0=float(Q0_entry.get())
        tf=float(tf_entry.get())
        T=float(T_entry.get())
        x=float(x_entry.get())
        nc=int(nc_entry.get())
        c=int(c_entry.get())
        D=numpy.zeros((nc),dtype=float)
        L=numpy.zeros((nc),dtype=float)
        n=numpy.zeros((nc),dtype=int)
        a=numpy.zeros((nc),dtype=float)
        Z=numpy.zeros((nc+1),dtype=float)
        dx=numpy.zeros((nc),dtype=float)
        dt=numpy.zeros((nc),dtype=float)
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
        
        for h in range (0,nc):
            if h==0:
                n[0]=n1
            else:
                n[h] = round((L[h]*a[h-1]*n[h-1])/(L[h-1]*a[h])) 
        for h in range (0,nc):
                dx[h]=L[h]/round(n[h])
                dt[h]=dx[h]/a[h]
        # message d'erreur
        if c==0 or c>nc:
            tk.messagebox.showerror("erreur sur la page'exécuter' ", "la valeur C doit être superieur à 0 et inferieur à %d" %nc)
            for child in frame.winfo_children():
                child.destroy()
            exit(0)
        t,x1,H,h1,Q,Hmax,Hmin,h1max,h1min,MaxHmax,MinHmin,Maxhmax,Minhmin=result(Hres,k,n,nc,f,L,D,a,Z,Q0,tf,T)
        # zoom les graphe
        aircombobox = ttk.Combobox(page, values=[
                                    "- Charge hydraulique H(m)", 
                                    "- Pression(m)",
                                    "- Enveloppe H(x)",
                                    "- Enveloppe de pression (m)",
                                    "- Débit volumique Q(m3/s)"],width=35)
        aircombobox.insert(0,'sélectionnez une réponse')
        aircombobox.bind('<<ComboboxSelected>>',lambda event:zoom(aircombobox,t,x1,H,h1,Q,Hmax,Hmin,h1max,h1min,MaxHmax,MinHmin,Maxhmax,Minhmin,L,x,c,nc,n,dx))
        canvas.create_window(140, 310,window=aircombobox)
        canvas.create_text(130,290,text="-ZOOM")
        # plots les graphes sur l'interface graphique
        fig = Figure(figsize=(16,10.5), dpi=60)
        if x<=sum(L[0:c]) and x>=0 :
                     ax = fig.add_subplot(321)
                     fig.subplots_adjust( wspace=0.3, hspace=0.4)                    
                     ax.grid(True)
                     ax.plot(t,H[int(sum(n[0:c])+(round(((x-sum(L[0:c]))/dx[c-1])+c-1)))][:])
                     ax.plot(t,H[int(sum(n[0:c])+(round(((x-sum(L[0:c]))/dx[c-1])+c-1)))][:],'b')
                     ax.set_xlabel("Temps [s]")
                     ax.set_ylabel("Charge hydraulique H(m)")
                     ax.set_title("H(t) x=%s la Conduite:%s "%(x,c))
                    
                     ax = fig.add_subplot(322)                 
                     ax.grid(True)
                     ax.plot(t,h1[int(sum(n[0:c])+(round(((x-sum(L[0:c]))/dx[c-1])+c-1)))][:])
                     ax.plot(t,h1[int(sum(n[0:c])+(round(((x-sum(L[0:c]))/dx[c-1])+c-1)))][:],'g')
                     ax.set_xlabel("Temps [s]")
                     ax.set_ylabel("Pression (m)")
                     ax.set_title("Pression(t) x=%s la Conduite:%s "%(x,c))
                                       
                     ax = fig.add_subplot(323)                       
                     ax.grid(True)
                     ax.plot(x1,Hmax[:],'r',label='H max')
                     ax.plot(x1,Hmin[:],'b',label='H min')
                     for h in range(0,nc):
                         if h==0:
                             for i in range (0,int(n[h]+1)):
                                 if Hmax[i]==MaxHmax[h]:
                                     ax.plot(x1[i],MaxHmax[h],'bo')
                         else:
                             for i in range(int(sum(n[0:h]+1)),int(sum(n[0:h+1]+1))):
                                if Hmax[i]==MaxHmax[h]:
                                    ax.plot(x1[i],MaxHmax[h],'bo')
                                    p=x1[i]
                     ax.plot(p,MaxHmax[h],'bo',label='max(H max)')
                     for h in range(0,nc):
                         if h==0:
                             for i in range (0,int(n[h]+1)):
                                 if Hmin[i]==MinHmin[h]:
                                     ax.plot(x1[i],MinHmin[h],'ro')
                         else:
                             for i in range(int(sum(n[0:h]+1)),int(sum(n[0:h+1]+1))):
                                 if Hmin[i]==MinHmin[h]:
                                     ax.plot(x1[i],MinHmin[h],'ro')
                                     p=x1[i]
                     ax.plot(p,MinHmin[h],'ro',label='min(H min)')
                     ax.set_xlabel("Distance x[m]")
                     ax.set_ylabel("Charge hydraulique H(m)")
                     ax.set_title("Enveloppe H(x) de x=%s "%x)
                     ax.legend()
                                       
                     ax = fig.add_subplot(324)                    
                     ax.grid(True)
                     ax.plot(x1,h1max[:],'r',label='h max')
                     ax.plot(x1,h1min[:],'b',label='h min')
                     for h in range(0,nc):
                        if h==0:
                             for i in range (0,int(n[h]+1)):
                                 if h1max[i]==Maxhmax[h]:
                                     ax.plot(x1[i],Maxhmax[h],'bo')
                                     
                        else:
                            for i in range(int(sum(n[0:h]+1)),int(sum(n[0:h+1]+1))):
                                if h1max[i]==Maxhmax[h]:
                                    ax.plot(x1[i],Maxhmax[h],'bo')
                                    p=x1[i]    
                     ax.plot(p,Maxhmax[h],'bo',label='max(h max)')
                     
                     for h in range(0,nc):
                        if h==0:
                            for i in range (0,int(n[h]+1)):
                                if h1min[i]==Minhmin[h]:
                                    ax.plot(x1[i],Minhmin[h],'ro')
                        else:
                            for i in range(int(sum(n[0:h]+1)),int(sum(n[0:h+1]+1))):
                                if h1min[i]==Minhmin[h]:
                                    ax.plot(x1[i],Minhmin[h],'ro')
                                    p=x1[i]
                     ax.plot(p,Minhmin[h],'ro',label='min(h min)')
                     ax.set_xlabel("Distance x[m]")
                     ax.set_ylabel("Pression(m)")
                     ax.set_title("Enveloppe de Pression(x) de x=%s "%x)
                     ax.legend()
                     
                     ax = fig.add_subplot(325)
                     ax.grid(True)  
                     ax.plot(t,Q[int(sum(n[0:c])+(round(((x-sum(L[0:c]))/dx[c-1])+c-1)))][:])
                     ax.plot(t,Q[int(sum(n[0:c])+(round(((x-sum(L[0:c]))/dx[c-1])+c-1)))][:],'r')
                     ax.set_xlabel("Temps [s]")
                     ax.set_ylabel("Débit volumique Q(m3/s)")
                     ax.set_title("Q(t) x=%s la Conduite:%s "%(x,c))
                                               
        graph =FigureCanvasTkAgg(fig,master=frame)   
        return(graph)
# %% enregistre les resultas [reservoir-conduite en serie-vanne] 
def save (Hres_entry,k_entry,n_entry,nc_entry,f_entry,l1,d1,a1,Z1,Q0_entry,tf_entry,T_entry,x_entry,c_entry):
                Hres=float(Hres_entry.get())
                k=float(k_entry.get())
                f= float(f_entry.get())
                n1 = int(n_entry.get())
                Q0=float(Q0_entry.get())
                tf=float(tf_entry.get())
                T=float(T_entry.get())
                nc=int(nc_entry.get())
                D=numpy.zeros((nc),dtype=float)
                L=numpy.zeros((nc),dtype=float)
                n=numpy.zeros((nc),dtype=int)
                a=numpy.zeros((nc),dtype=float)
                Z=numpy.zeros((nc+1),dtype=float)
                dx=numpy.zeros((nc),dtype=float)
                dt=numpy.zeros((nc),dtype=float)
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
        
                for h in range (0,nc):
                    if h==0:
                        n[0]=n1
                    else:
                        n[h] = round((L[h]*a[h-1]*n[h-1])/(L[h-1]*a[h]))      
                t,x1,H,h1,Q,Hmax,Hmin,h1max,h1min,MaxHmax,MinHmin,Maxhmax,Minhmin=result(Hres,k,n,nc,f,L,D,a,Z,Q0,tf,T)
                for h in range (0,nc):
                    dx[h]=L[h]/round(n[h])
                    dt[h]=dx[h]/a[h]

                workbook = xlsxwriter.Workbook('reservoir-conduite_en_serie-vanne sans protection.xlsx')
                worksheet = workbook.add_worksheet('H(x,t)')
                for j in range (1,int(round(T/min(dt))+2)):
                    for i in range (1,sum(n)+nc+1):
                        worksheet.write(0,0,'t[s]')
                        worksheet.write(i,0,'H[%s m]'%int(x1[i-1]))
                        worksheet.write(0,j,t[j-1])
                        worksheet.write(i,j,H[i-1][j-1])
                worksheet = workbook.add_worksheet('p(x,t)')
                for j in range (1,int(round(T/min(dt))+2)):
                    for i in range (1,sum(n)+nc+1):
                        worksheet.write(0,0,'t[s]')
                        worksheet.write(i,0,'h[%s m]'%int(x1[i-1]))
                        worksheet.write(0,j,t[j-1])
                        worksheet.write(i,j,h1[i-1][j-1])
                        
                worksheet = workbook.add_worksheet('Q(x,t)')
                for j in range (1,int(round(T/min(dt))+2)):
                    for i in range (1,sum(n)+nc+1):
                        worksheet.write(0,0,'t[s]')
                        worksheet.write(i,0,'Q[%s m]'%int(x1[i-1]))
                        worksheet.write(0,j,t[j-1])
                        worksheet.write(i,j,Q[i-1][j-1])
                worksheet = workbook.add_worksheet('Hmax et hmax')
                for i in range (1,sum(n)+nc+1):
                        worksheet.write(i,0,'Hmax[%s m]'%int(x1[i-1]))
                        worksheet.write(i,1,Hmax[i-1])
                        worksheet.write(i,2,'hmax[%s m]'%int(x1[i-1]))
                        worksheet.write(i,3,h1max[i-1])
                worksheet = workbook.add_worksheet('Hmin et hmin')
                for i in range (1,sum(n)+nc+1):
                        worksheet.write(i,0,'Hmin[%s m]'%int(x1[i-1]))
                        worksheet.write(i,1,Hmin[i-1])
                        worksheet.write(i,2,'hmin[%s m]'%int(x1[i-1]))
                        worksheet.write(i,3,h1min[i-1])
                workbook.close() 


