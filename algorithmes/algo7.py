# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:29:21 2020

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
def zoom(combobox,Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,position,c,x):
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
# %% calcul [reservoir-conduite en parallele-vanne]
def result(Hres,k,Q00,n1,f,nc,L,D,a,Z,tf,c,T,x): 
    g=9.81
    A=numpy.zeros(nc+1,dtype=float)
    R=numpy.zeros(nc+1,dtype=float)
    Ca=numpy.zeros(nc+1,dtype=float)
    alpha=numpy.zeros(nc+1,dtype=float)
    dx=numpy.zeros(nc+1,dtype=float)
    n=numpy.zeros(nc+1,dtype=int)
    # calcule des paramtres
    A=(math.pi*D**2)/4
    R=f/(2*D*A)
    Ca=(g*A)/a
    
    for i in range(nc+1):
        if i==0:
            dx[i]=L[i]/n1
            dt=dx[i]/a[i]
        else:
            dx[i]=dt*a[i]
    
    for i in range(nc+1): #les pentes des conduite
        if i==0:
            alpha[i]=(Z[i]-Z[i+1])/L[i]
        else:
            alpha[i]=(Z[1]-Z[i+1])/L[i]
            
    m=int(round(T/dt))
    for i in range(nc+1):
        if i==0:
            n[i]=n1
        else:
            n[i]=round(L[i]/dx[i])
    def find_position(x,c,dx):
        p=round(x/dx[c-1])
        return int(p)
    # initialisation
    Q0=numpy.zeros((nc+1),dtype=float)
    Q=list(numpy.zeros((nc+1),dtype=list))
    H=list(numpy.zeros((nc+1),dtype=list))
    Hmax=list(numpy.zeros((nc+1),dtype=list))
    Hmin=list(numpy.zeros((nc+1),dtype=list))
    h=list(numpy.zeros((nc+1),dtype=list))
    hmax=list(numpy.zeros((nc+1),dtype=list))
    hmin=list(numpy.zeros((nc+1),dtype=list))
    Cp=list(numpy.zeros((nc+1),dtype=list))
    Cn=list(numpy.zeros((nc+1),dtype=list))
    Distance=list(numpy.zeros((nc+1),dtype=list))
    Time=numpy.zeros(m+1)
    for pipe in range(nc+1):
        H[pipe]=numpy.zeros((m+2,n[pipe]+1),dtype=float)
        Hmax[pipe]=numpy.zeros(n[pipe]+1,dtype=float)
        Hmin[pipe]=numpy.zeros(n[pipe]+1,dtype=float)
        Q[pipe]=numpy.zeros((m+2,n[pipe]+1),dtype=float)
        h[pipe]=numpy.zeros((m+2,n[pipe]+1),dtype=float)
        hmax[pipe]=numpy.zeros(n[pipe]+1,dtype=float)
        hmin[pipe]=numpy.zeros(n[pipe]+1,dtype=float)
        Cp[pipe]=numpy.zeros((m+1,n[pipe]+1),dtype=float)
        Cn[pipe]=numpy.zeros((m+1,n[pipe]+1),dtype=float)
        Distance[pipe]=numpy.zeros(n[pipe]+1)
    for pipe in range(nc+1):
        if pipe==0:
            Q0[pipe]=Q00
        else:
            Q0[pipe]=Q00*(A[pipe]/(sum(A[1:nc+1])))
    for j in range(m):
        Time[j+1]=Time[j]+dt
        
    for pipe in range(nc+1):
        for j in range(n[pipe]):
                Distance[pipe][j+1]=Distance[pipe][j]+dx[pipe]
    
    position=find_position(x,c,dx)  
    #calcul   
    for i in range (m+2):
        if i==0:#regime permanent
            for pipe in range(nc+1):
                if pipe==0:#calcul la conduite n°01
                    for j in range(n[pipe]+1):
                        Q[pipe][i][j]=Q0[pipe]
                        H[pipe][i][j]=Hres-((k+1+(f*j*dx[pipe]/D[pipe]))*(Q[pipe][i][j]**2/(2*g*A[pipe]**2)))
                        h[pipe][i][j]=H[pipe][i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                else:
                    for j in range(n[pipe]+1):
                        Q[pipe][i][j]=Q0[pipe]
                        H[pipe][i][j]=H[0][i][n[0]]-((f*j*dx[pipe]/D[pipe])*(Q[pipe][i][j]**2/(2*g*A[pipe]**2)))
                        h[pipe][i][j]=H[pipe][i][j]-(Z[0]+(alpha[pipe]*j*dx[pipe])+(alpha[0]*L[0]))
        elif i==1: #le regime a t=0
            for pipe in range(nc+1):
                if pipe==0:#calcul la conduite n°01
                    for j in range(n[pipe]+1):
                        Q[pipe][i][j]=Q[pipe][0][j]
                        H[pipe][i][j]=H[pipe][0][j]
                        h[pipe][i][j]=h[pipe][0][j]
                else:      
                    for j in range(n[pipe]+1):
                        if j!=n[pipe]:
                            Q[pipe][i][j]=Q[pipe][0][j]
                            H [pipe][i][j]=H[pipe][0][j]
                            h[pipe][i][j]=h[pipe][0][j]
                        else:
                            if tf[pipe-1]==0:
                                Q[pipe][i][j]=0
                                H[pipe][i][j]=H[pipe][0][j]
                                h[pipe][i][j]=h[pipe][0][j]
                            else:
                                Q[pipe][i][j]=Q0[pipe]
                                H[pipe][i][j]=H[pipe][0][j]
                                h[pipe][i][j]=h[pipe][0][j]
        else:#regime transitoir
            for pipe in range(nc+1):
                if pipe==0:#calcul la conduite n°01
                    for j in range(n[pipe]+1):
                        if j==0:# resvoir amont
                            k1=(Ca[pipe]*(1+k))/(2*g*A[pipe]**2)
                            Cn[pipe][i-1][j]=Q[pipe][i-1][j+1]-Ca[pipe]*H[pipe][i-1][j+1]-R[pipe]*dt*Q[pipe][i-1][j+1]*abs(Q[pipe][i-1][j+1])
                            Q[pipe][i][j]=(-1+math.sqrt(1+4*k1*(Cn[pipe][i-1][j]+Ca[pipe]*Hres)))/(2*k1)
                            if Q[pipe][i][j]>=0:
                                H[pipe][i][j]=Hres-(1+k)*((Q[pipe][i][j])**2)/(2*g*A[pipe]**2)
                                h[pipe][i][j]=H[pipe][i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                            else:
                                H[pipe][i][j]=Hres-(1-k)*((Q[pipe][i][j])**2)/(2*g*A[pipe]**2)
                                h[pipe][i][j]=H[pipe][i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                        elif j==n[pipe]:
                            Cn_sum=0
                            for w in range (1,nc+1):
                                Cn[w][i-1][0]=Q[w][i-1][1]-Ca[w]*H[w][i-1][1]-R[w]*dt*Q[w][i-1][1]*abs(Q[w][i-1][1])
                                Cn_sum=Cn_sum+Cn[w][i-1][0]
                            Cp[pipe][i-1][j]=Q[pipe][i-1][j-1]+Ca[pipe]*H[pipe][i-1][j-1]-R[pipe]*dt*Q[pipe][i-1][j-1]*abs(Q[pipe][i-1][j-1])
                            H[pipe][i][j]=(Cp[pipe][i-1][j]-Cn_sum)/sum(Ca)
                            Q[pipe][i][j]=Cp[pipe][i-1][j]-Ca[pipe]*H[pipe][i][j]
                            h[pipe][i][j]=H[pipe][i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                            
                        else:# noeuds intermediaires
                            Cn[pipe][i-1][j]=Q[pipe][i-1][j+1]-Ca[pipe]*H[pipe][i-1][j+1]-R[pipe]*dt*Q[pipe][i-1][j+1]*abs(Q[pipe][i-1][j+1])
                            Cp[pipe][i-1][j]=Q[pipe][i-1][j-1]+Ca[pipe]*H[pipe][i-1][j-1]-R[pipe]*dt*Q[pipe][i-1][j-1]*abs(Q[pipe][i-1][j-1])
                            Q[pipe][i][j]=(Cp[pipe][i-1][j]+Cn[pipe][i-1][j])/2
                            H[pipe][i][j]=(Cp[pipe][i-1][j]-Cn[pipe][i-1][j])/(2*Ca[pipe])
                            h[pipe][i][j]=H[pipe][i][j]-(Z[0]+alpha[pipe]*j*dx[pipe])
                else:
                    for j in range(n[pipe]+1):
                        if j==n[pipe]:# vanne aval
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
                        
                        elif j==0:
                            Cn[pipe][i-1][j]=Q[pipe][i-1][j+1]-Ca[pipe]*H[pipe][i-1][j+1]-R[pipe]*dt*Q[pipe][i-1][j+1]*abs(Q[pipe][i-1][j+1])
                            H[pipe][i][j]=H[0][i][n[0]]
                            Q[pipe][i][j]=Cn[pipe][i-1][j]+Ca[pipe]*H[pipe][i][j]
                            h[pipe][i][j]=H[pipe][i][j]-(Z[0]+(alpha[pipe]*j*dx[pipe])+(alpha[0]*L[0]))    
                            
                        else:# noeuds intermediaires
                            Cn[pipe][i-1][j]=Q[pipe][i-1][j+1]-Ca[pipe]*H[pipe][i-1][j+1]-R[pipe]*dt*Q[pipe][i-1][j+1]*abs(Q[pipe][i-1][j+1])
                            Cp[pipe][i-1][j]=Q[pipe][i-1][j-1]+Ca[pipe]*H[pipe][i-1][j-1]-R[pipe]*dt*Q[pipe][i-1][j-1]*abs(Q[pipe][i-1][j-1])
                            Q[pipe][i][j]=(Cp[pipe][i-1][j]+Cn[pipe][i-1][j])/2
                            H[pipe][i][j]=(Cp[pipe][i-1][j]-Cn[pipe][i-1][j])/(2*Ca[pipe])
                            h[pipe][i][j]=H[pipe][i][j]-(Z[0]+(alpha[pipe]*j*dx[pipe])+(alpha[0]*L[0]))   
    #calcule envloppe
    for pipe in range(nc+1):
        for i in range(n[pipe]+1): 
            Hmin[pipe][i]=min(H[pipe][:,i])  
            Hmax[pipe][i]=max(H[pipe][:,i])  
    for pipe in range(nc+1):
        for i in range(n[pipe]+1): 
            hmin[pipe][i]=min(h[pipe][:,i])  
            hmax[pipe][i]=max(h[pipe][:,i])     


           
    return(Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,position)
# %% affiches les graphes [reservoir-conduite en parallele-vanne]        
def display_result(page,canvas,frame,Hres_entry,k_entry,Q0_entry,n_entry,f_entry,nc_entry,l1,d1,a1,Z1,tf1,c_entry,T_entry,x_entry):
            nc=int(nc_entry.get())
            f= float(f_entry.get())   
            n1 = int(n_entry.get())
            Hres=float( Hres_entry.get())
            Q00=float(Q0_entry.get())
            k=float(k_entry.get())
            x=float(x_entry.get())
            T=float(T_entry.get())
            c=int(c_entry.get())
            D=numpy.zeros((nc+1),dtype=float)
            L=numpy.zeros((nc+1),dtype=float)
            a=numpy.zeros((nc+1),dtype=float)
            tf=numpy.zeros(nc,dtype=float)
            Z=numpy.zeros((nc+2),dtype=float)
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
            Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,position=result(Hres,k,Q00,n1,f,nc,L,D,a,Z,tf,c,T,x)
            # zoom les graphe
            aircombobox = ttk.Combobox(page, values=[
                                        "- Charge hydraulique H(m)", 
                                        "- Pression(m)",
                                        "- Enveloppe H(x)",
                                        "- Enveloppe de pression (m)",
                                        "- Débit volumique Q(m3/s)"],width=35)
            aircombobox.insert(0,'sélectionnez une réponse')
            aircombobox.bind('<<ComboboxSelected>>',lambda event:zoom(aircombobox,Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,position,c,x))
            canvas.create_window(140, 310,window=aircombobox)
            canvas.create_text(130,290,text="-ZOOM")
            # plots les graphes sur l'interface graphique
            fig =Figure (figsize=(16,11), dpi=60)
            ax = fig.add_subplot(321) 
            fig.subplots_adjust( wspace=0.3, hspace=0.4)
            ax.grid(True)
            ax.plot(Time,(H[c-1][1:,position]))
            ax.plot(Time,H[c-1][1:,position],'b')
            ax.set_xlabel('Temps [s]')
            ax.set_ylabel('Charge hydraulique H(m)')
            ax.set_title("H(t) x=%s la Conduite:%s "%(x,c))
            
            ax = fig.add_subplot(322)
            ax.grid(True)
            ax.plot(Time,h[c-1][1:,position])
            ax.set_xlabel("Temps [s]")
            ax.set_ylabel("pression (m)")
            ax.set_title("Pression(t) x=%s la Conduite:%s "%(x,c))
            
            ax = fig.add_subplot(323)
            ax.grid(True)
            ax.plot(Distance[c-1], Hmax[c-1], 'r',label='(Hmax)')
            ax.plot(Distance[c-1], Hmin[c-1], 'b',label='(Hmin)')
            ax.set_xlabel("Distance x[m]")
            ax.set_ylabel("Charge hydraulique H(m)")
            ax.set_title("Enveloppede H(x) la Conduite:%s "%(c))
            ax.legend()
            
            ax = fig.add_subplot(324)
            ax.grid(True)
            ax.plot(Distance[c-1], hmax[c-1], 'r',label='(hmax)')
            ax.plot(Distance[c-1], hmin[c-1], 'b',label='(hmin)')
            ax.set_xlabel("Distance x[m]")
            ax.set_ylabel("pression h(m)")
            ax.set_title("Enveloppe de Pression(x) la Conduite:%s "%(c)) 
            ax.legend()
                  
            ax = fig.add_subplot(325)
            ax.grid(True) 
            ax.plot(Time,Q[c-1][1:,position])
            ax.plot(Time,Q[c-1][1:,position],'r')
            ax.set_xlabel('Temps [s]')
            ax.set_ylabel('Débit volumique Q(m3/s)')        
            ax.set_title("Q(t)  x=%s la Conduite:%s "%(x,c))  
            
            
            graph = FigureCanvasTkAgg(fig,master=frame)
            return(graph.get_tk_widget())
# %% enregistrer les graphes [reservoir-conduite en serie-vanne]+reservoir d'air
def save(Hres_entry,k_entry,Q0_entry,n_entry,f_entry,nc_entry,l1,d1,a1,Z1,tf1,c_entry,T_entry,x_entry):
    nc=int(nc_entry.get())
    f= float(f_entry.get())   
    n1 = int(n_entry.get())
    Hres=float( Hres_entry.get())
    Q00=float(Q0_entry.get())
    k=float(k_entry.get())
    x=float(x_entry.get())
    T=float(T_entry.get())
    c=int(c_entry.get())
    D=numpy.zeros((nc+1),dtype=float)
    L=numpy.zeros((nc+1),dtype=float)
    a=numpy.zeros((nc+1),dtype=float)
    tf=numpy.zeros(nc,dtype=float)
    Z=numpy.zeros((nc+2),dtype=float)
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
    m=int(round(T/dt))
    n=numpy.zeros(nc+1,dtype=int)
    for i in range(nc+1):
        if i==0:
            n[i]=n1
        else:
            n[i]=round(L[i]/dx[i])

    Time,Distance,H,h,Q,Hmax,Hmin,hmax,hmin,position=result(Hres,k,Q00,n1,f,nc,L,D,a,Z,tf,c,T,x)
    #  enregistrer "excel"
    workbook = xlsxwriter.Workbook('reservoir-conduite_en_parallèle-vanne.xlsx')
    cell_format1 = workbook.add_format({'bold': True, 'font_color': 'blue'})
    worksheet = workbook.add_worksheet('H(x,t)')
    for  i in range (m+3):
        for pipe in range(nc+1):
            if pipe==0:
                for j in range (n[pipe]+2):
                    if i==0 :
                            if j==1:
                                worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                    elif i==1:
                        if j==0:
                            worksheet.write(i,j,'t[s]')
                        else:
                            worksheet.write(i,j,'H[%s m]'%int(Distance[pipe][j-1]))
                    else:
                        if j==0:
                            worksheet.write(i,j,Time[i-2])
                        else:
                            worksheet.write(i,j,H[pipe][i-1,j-1])
            else:
                for j in range (sum(n[0:pipe])+2+pipe,sum(n[0:pipe])+2+pipe+n[pipe]+1):
                    if i==0 :
                            if j==sum(n[0:pipe])+2+pipe:
                                worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                    elif i==1:
                        worksheet.write(i,j,'H[%s m]'%int(Distance[pipe][j-sum(n[0:pipe])-2-pipe]))
                    else:
                        worksheet.write(i,j,(H[pipe][i-1,j-1-sum(n[0:pipe])-1-pipe]))
    
    worksheet = workbook.add_worksheet('Q(x,t)')
    for  i in range (m+3):
        for pipe in range(nc+1):
            if pipe==0:
                for j in range (n[pipe]+2):
                    if i==0:
                        if j==1:
                                worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)                    
                    elif i==1:
                        if j==0:
                            worksheet.write(i,j,'t[s]')
                        else:
                            worksheet.write(i,j,'H[%s m]'%int(Distance[pipe][j-1]))
                    else:
                        if j==0:
                            worksheet.write(i,j,Time[i-2])
                        else:
                            worksheet.write(i,j,Q[pipe][i-1,j-1])
            else:
                for j in range (sum(n[0:pipe])+2+pipe,sum(n[0:pipe])+2+pipe+n[pipe]+1):
                    if i==0 :
                        if j==sum(n[0:pipe])+2+pipe:
                            worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                    elif i==1:
                        worksheet.write(i,j,'H[%s m]'%int(Distance[pipe][j-sum(n[0:pipe])-2-pipe]))
                    else:
                        worksheet.write(i,j,(Q[pipe][i-1,j-1-sum(n[0:pipe])-1-pipe]))
                        
    worksheet = workbook.add_worksheet('p(x,t)')
    for  i in range (m+3):
        for pipe in range(nc+1):
            if pipe==0:
                for j in range (n[pipe]+2):
                    if i==0 :
                            if j==1:
                                worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                    elif i==1:
                        if j==0:
                            worksheet.write(i,j,'t[s]')
                        else:
                            worksheet.write(i,j,'H[%s m]'%int(Distance[pipe][j-1]))
                    else:
                        if j==0:
                            worksheet.write(i,j,Time[i-2])
                        else:
                            worksheet.write(i,j,h[pipe][i-1,j-1])
            else:
                for j in range (sum(n[0:pipe])+2+pipe,sum(n[0:pipe])+2+pipe+n[pipe]+1):
                    if i==0 :
                        if j==sum(n[0:pipe])+2+pipe:
                            worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                    elif i==1:
                        worksheet.write(i,j,'H[%s m]'%int(Distance[pipe][j-sum(n[0:pipe])-2-pipe]))
                    else:
                        worksheet.write(i,j,(h[pipe][i-1,j-1-sum(n[0:pipe])-1-pipe]))
    worksheet = workbook.add_worksheet('Hmax(x) et hmax(x)')
    for i in range(5):
        for pipe in range(nc+1):
            if pipe==0:
                for j in range (n[pipe]+2):
                        if i==0 :
                                if j==1:
                                    worksheet.set_column(i, j, 13)
                                    worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                        elif i==1:
                            if j==0:
                                pass
                            else:
                                worksheet.set_column(i, j, 13)
                                worksheet.write(i,j,'Hmax[%s m]'%int(Distance[pipe][j-1]))
                        elif i==2:
                            if j==0:
                                pass
                            else:
                                worksheet.set_column(i, j, 13)
                                worksheet.write(i,j,Hmax[pipe][j-1])
                        elif i==3:
                            if j==0:
                                pass
                            else:
                                worksheet.set_column(i, j, 13)
                                worksheet.write(i,j,'hmax[%s m]'%int(Distance[pipe][j-1]))
                        else :
                            if j==0:
                                pass
                            else:
                                worksheet.set_column(i, j, 13)
                                worksheet.write(i,j,hmax[pipe][j-1])                                         
            else:
                for j in range (sum(n[0:pipe])+2+pipe,sum(n[0:pipe])+2+pipe+n[pipe]+1):
                        if i==0 :
                            if j==sum(n[0:pipe])+2+pipe:
                                worksheet.set_column(i, j, 13)
                                worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                        elif i==1:
                            worksheet.set_column(i, j, 13)
                            worksheet.write(i,j,'Hmax[%s m]'%int(Distance[pipe][j-sum(n[0:pipe])-2-pipe]))
                        elif i==2:
                            worksheet.set_column(i, j, 13)
                            worksheet.write(i,j,(Hmax[pipe][j-sum(n[0:pipe])-2-pipe]))
                        elif i==3:
                            worksheet.set_column(i, j, 13)
                            worksheet.write(i,j,'hmax[%s m]'%int(Distance[pipe][j-sum(n[0:pipe])-2-pipe]))
                        else :
                            worksheet.set_column(i, j, 13)
                            worksheet.write(i,j,(hmax[pipe][j-sum(n[0:pipe])-2-pipe]))
    worksheet = workbook.add_worksheet('Hmin(x) hmin(x)')
    for i in range(5):
        for pipe in range(nc+1):
            if pipe==0:
                for j in range (n[pipe]+2):
                        if i==0 :
                                if j==1:
                                    worksheet.set_column(i, j, 13)
                                    worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                        elif i==1:
                            if j==0:
                                pass
                            else:
                                worksheet.set_column(i, j, 13)
                                worksheet.write(i,j,'Hmin[%s m]'%int(Distance[pipe][j-1]))
                        elif i==2:
                            if j==0:
                                pass
                            else:
                                worksheet.set_column(i, j, 13)
                                worksheet.write(i,j,Hmin[pipe][j-1])
                        elif i==3:
                            if j==0:
                                pass
                            else:
                                worksheet.set_column(i, j, 13)
                                worksheet.write(i,j,'hmin[%s m]'%int(Distance[pipe][j-1]))
                        else :
                            if j==0:
                                pass
                            else:
                                worksheet.set_column(i, j, 13)
                                worksheet.write(i,j,hmin[pipe][j-1])                                         
            else:
                for j in range (sum(n[0:pipe])+2+pipe,sum(n[0:pipe])+2+pipe+n[pipe]+1):
                        if i==0 :
                            if j==sum(n[0:pipe])+2+pipe:
                                worksheet.set_column(i, j, 13)
                                worksheet.write(i,j,'conduite%s'%(pipe+1),cell_format1)
                        elif i==1:
                            worksheet.set_column(i, j, 13)
                            worksheet.write(i,j,'Hmin[%s m]'%int(Distance[pipe][j-sum(n[0:pipe])-2-pipe]))
                        elif i==2:
                            worksheet.set_column(i, j, 13)
                            worksheet.write(i,j,(Hmin[pipe][j-sum(n[0:pipe])-2-pipe]))
                        elif i==3:
                            worksheet.set_column(i, j, 13)
                            worksheet.write(i,j,'hmin[%s m]'%int(Distance[pipe][j-sum(n[0:pipe])-2-pipe]))
                        else :
                            worksheet.set_column(i, j, 13)
                            worksheet.write(i,j,(hmin[pipe][j-sum(n[0:pipe])-2-pipe]))
    workbook.close()             
                   
            
