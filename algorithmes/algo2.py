# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:42:06 2020

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
def zoom(combobox,t,x1,H,h,Q,Hmax,Hmin,hmax,hmin,Zp,Qps,x,L,dx,n):    
    choice=combobox.get()
    if choice== "- Charge hydraulique H(m)":
            window=tk.Tk()
            window.state('zoomed')
            window.title(choice)
            window.iconbitmap(r'photos\images.ico')
            fig =Figure (figsize=(16,11), dpi=140)
            ax = fig.add_subplot(111) 
            if x<=L and x>=0 :
                fig.subplots_adjust( wspace=1.4, hspace=1)
                ax.grid(True)
                ax.plot(t,H[round(x/dx)][:])
                ax.plot(t,H[round(x/dx)][:],'b')
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
            if x<=L and x>=0 :
                fig.subplots_adjust( wspace=1.4, hspace=1)
                ax.grid(True)
                ax.plot(t,h[round(x/dx)][:])
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
            if x<=L and x>=0 :
                fig.subplots_adjust( wspace=1.4, hspace=1)
                ax.grid(True)
                ax.plot(x1,Hmax[:],'r',label='H max')
                ax.plot(x1,Hmin[:],'b',label='H min')
                for i in range (0,n+1) :
                    if Hmax[i]==max(Hmax):
                        ax.plot(x1[i],Hmax[i],'bo')
                        p=x1[i]
                ax.plot(p,max(Hmax),'bo',label='max(H max)')
                for i in range (0,n+1) :
                    if Hmin[i]==min(Hmin):
                        ax.plot(x1[i],Hmin[i],'ro')
                        p=x1[i]
                ax.plot(p,min(Hmin),'ro',label='min(H min)')
                ax.set_xlabel("Distance x[m]")
                ax.set_ylabel("Charge hydraulique H(m)")
                ax.set_title("Enveloppe H(x)")
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
            if x<=L and x>=0 :
                fig.subplots_adjust( wspace=1.4, hspace=1)
                ax.grid(True)
                ax.plot(x1,hmax[:],'r',label='h max')
                ax.plot(x1,hmin[:],'b',label='h min')
                for i in range (0,n+1) :
                    if hmax[i]==max(hmax):
                        ax.plot(x1[i],hmax[i],'bo')
                        p=x1[i]
                ax.plot(p,max(hmax),'bo',label='max(h max)')
                for i in range (0,n+1) :
                    if hmin[i]==min(hmin):
                        ax.plot(x1[i],hmin[i],'ro')
                        p=x1[i]
                ax.plot(p,min(hmin),'ro',label='min(h min)')
                ax.set_xlabel("Distance x[m]")
                ax.set_ylabel("Pression (m)")
                ax.set_title("Enveloppe Pression(x) ")
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
            if x<=L and x>=0 :
                fig.subplots_adjust( wspace=1.4, hspace=1)
                ax.grid(True) 
                ax.plot(t,Q[round(x/dx)][:])
                ax.plot(t,Q[round(x/dx)][:],'r')
                ax.set_xlabel('Temps [s]')
                ax.set_ylabel('Débit volumique Q(m3/s)')        
                ax.set_title("Q(t) de x=%s"%x)
                graph = FigureCanvasTkAgg(fig,master=window)
                graph.get_tk_widget().pack()
    if choice=="- Qps(t) de cheminée d'équilibre ":
            window=tk.Tk()
            window.state('zoomed')
            window.title(choice)
            window.iconbitmap(r'photos\images.ico')
            fig =Figure (figsize=(16,11), dpi=140)
            ax = fig.add_subplot(111) 
            if x<=L and x>=0 :
                fig.subplots_adjust( wspace=1.4, hspace=1)
                ax.grid(True)
                ax.plot(t,Qps[:])
                ax.set_xlabel("Temps [s]")
                ax.plot(t,Qps[:],'r')
                ax.set_ylabel("Qps [m^3/s]")
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
            if x<=L and x>=0 :
                fig.subplots_adjust( wspace=1.4, hspace=1)
                ax.grid(True)
                ax.plot(t,Zp[:])
                ax.set_xlabel("Temps [s]")
                ax.plot(t,Zp[:],'b')
                ax.set_ylabel("Zp [m]")
                ax.set_title("Zp(t) de cheminée d'équilibre ")
                graph = FigureCanvasTkAgg(fig,master=window)
                graph.get_tk_widget().pack()
# %% calcul [reservoir-conduite-vanne]+cheminee d'equilbre
def result(Hres,k,L,D,a,f,n,Z0,Z1,Ds,M,Q0,tf,T):
        A=(math.pi*D**2)/4
        As=(math.pi*Ds**2)/4 
        R=f/(2*D*A)
        dx=L/float(n)  #dx:Le pas spatiale 
        dt=dx/a #dt:Le pas temporel
        ca=9.81*A/a
        n1=round(M/dx) # noeud au niveau de la cheminée d'équilibre 
        
        thau=numpy.zeros((round(T/dt)+1),dtype=float)
        Q=numpy.zeros((n+1,round(T/dt)+2),dtype=float)
        H=numpy.zeros((n+1,round(T/dt)+2),dtype=float)
        h=numpy.zeros((n+1,round(T/dt)+2),dtype=float)
        cn=numpy.zeros((n+1,round(T/dt)+3),dtype=float)
        cp=numpy.zeros((n+1,round(T/dt)+3),dtype=float)
        cv=numpy.zeros((round(T/dt)+1),dtype=float)
        Hmax=numpy.zeros((n+1),dtype=float)
        Hmin=numpy.zeros((n+1),dtype=float)
        hmax=numpy.zeros((n+1),dtype=float)
        hmin=numpy.zeros((n+1),dtype=float)
        x1=numpy.zeros((n+1),dtype=float)
        Qps=numpy.zeros((round(T/dt)+2),dtype=float)
        Zp=numpy.zeros((round(T/dt)+2),dtype=float)
        # calcul de Q(x,t),H(x,t),h(x,t),Hmax(x)etHmin(x) aprés fermeture de la vanne
        # étape1:calcul en régime permanant(i.e avant la fermeture de la vanne)
        for i in range(0,n+1):
            Q[i][0]=Q0
            H[i][0]= Hres-(k+1+f*dx*i/D)*((Q0/A)**2)/(2*9.81)
            h[i][0]=H[i][0]-Z0-((Z0-Z1)*dx*i)/L
          
        Qps[0]=0
        Zp[0]=H[n1][0] 
        
        for i in range(0,n+1):
            if i!=n:
                Q[i][1]=Q0
                H[i][1]=H[i][0]
                h[i][1]=h[i][0]
            else :
                if tf==0:
                    Q[n][1]=0
                    H[n][1]=H[n][0]
                else:
                    Q[n][1]=Q0    
                    H[n][1]=H[n][0]
                h[i][1]=h[i][0]
        Qps[1]=0
        Zp[1]=H[n1][1]
        
        for i in range (0,n):
                    cn[i][2]=Q[i+1][1]-ca*H[i+1][1] -R*Q[i+1][1]*abs(Q[i+1][1])*dt
                    cp[i+1][2]=Q[i][1]+ca*H[i][1] -R*Q[i][1]*abs(Q[i][1])*dt
        # étape2:calcul en régime transitoire(i.e aprés la fermeture de la vanne)
        for j in range (2,round(T/dt)+2):
            if dt*(j-2)<tf:
                 thau[j-2]=1-(j-1)*dt/tf     
            else:
                thau[j-2]=0
            
            for i in range (0,n+1):
                if i==0: # calcul au niveau de réservoir
                    Q[i][j]=(-1+(1+4*(ca*(1+k)/(2*9.81*(A**2)))*(cn[i][j]+ca*Hres))**0.5)/(2*(ca*(1+k)/(2*9.81*(A**2))))
                    if Q[i][j]>=0:
                        Q[i][j]=(-1+(1+4*(ca*(1+k)/(2*9.81*(A**2)))*(cn[i][j]+ca*Hres))**0.5)/(2*(ca*(1+k)/(2*9.81*(A**2))))
                        H[i][j]=Hres-(1+k)*((Q[i][j])**2)/(2*9.81*A**2)
                        h[i][j]=H[i][j]-Z0-((Z0-Z1)*dx*i)/L
                    else :
                        Q[i][j]=(-1+(1+4*(ca*(1+k)/(2*9.81*(A**2)))*(cn[i][j]+ca*Hres))**0.5)/(2*(ca*(1+k)/(2*9.81*(A**2))))
                        if  Q[i][j]>=0:
                                 print("***********ya un probleme ***********")
                        else:
                            H[i][j]=Hres-(1-k)*((Q[i][j])**2)/(2*9.81*A**2)
                            h[i][j]=H[i][j]-Z0-((Z0-Z1)*dx*i)/L
                else :
                    # calcul pour les noeuds intermédiaires
                    if i<n1:
                        Q[i][j]=(cp[i][j]+cn[i][j])/2
                        H[i][j]=(Q[i][j]-cn[i][j])/(ca)
                        h[i][j]=H[i][j]-Z0-((Z0-Z1)*dx*i)/L
                    else :
                        #n1:le noeud au niveau de la cheminée d'équilibre 
                        if i==n1:
                            H[i][j]=(cp[i][j]-cn[i][j]+Qps[j-1]+2*(As*Zp[j-1]/dt))/(ca+ca+2*(As/dt))
                            Q[i][j] = cp[i][j]-ca*H[i][j]
                            h[i][j]=H[i][j]-Z0-((Z0-Z1)*dx*i)/L
                        else :
                            #n:le noeud au niveau de la vanne
                            if i!=n:
                                Q[i][j]=(cp[i][j]+cn[i][j])/2
                                H[i][j]=(Q[i][j]-cn[i][j])/(ca)
                                h[i][j]=H[i][j]-Z0-((Z0-Z1)*dx*i)/L
                            else:
                                cv[j-2]=((Q[n][1]*thau[j-2])**2)/(ca*H[n][1])
                                Q[i][j]=0.5*(-cv[j-2]+(cv[j-2]**2+4*cp[i][j]*cv[j-2])**0.5)
                                H[i][j]=(cp[i][j]-Q[i][j])/ca
                                h[i][j]=H[i][j]-Z0-((Z0-Z1)*dx*i)/L
            for i in range (1,n+1):
                cp[i][j+1]=Q[i-1][j]+ca*H[i-1][j] -R*Q[i-1][j]*abs(Q[i-1][j])*dt
            for i in range (0,n):
                cn[i][j+1]=Q[i+1][j]-ca*H[i+1][j] -R*Q[i+1][j]*abs(Q[i+1][j])*dt
            Qps[j]=Q[n1][j]-Q[n1+1][j]
            Zp[j]=Zp[j-1]+0.5*(dt/As)*(Qps[j]+Qps[j-1])
        
        t=numpy.zeros((round(T/dt)+2),dtype=float)
        for i in range(1,round(T/dt)+2):
            t[i]=dt+t[i-1]
         # calcul les Hmax(x),Hmin(x),hmax(x) et hmin(x)
        for i in range(0,n+1):
            Hmax[i]=max(H[i][:])
            Hmin[i]=min(H[i][:])
            hmax[i]=max(h[i][:])
            hmin[i]=min(h[i][:])
            if i==0:
                x1[i]=0
            else:
                x1[i]=dx+x1[i-1]
        return(t,x1,H,h,Q,Hmax,Hmin,hmax,hmin,Zp,Qps)
# %% affiches les graphes [reservoir-conduite-vanne]        
def display_result(page,canvas,frame,Hres_entry,k_entry,L_entry,D_entry,a_entry,f_entry,n_entry,Z0_entry,Z1_entry,Ds_entry,M_entry,Q0_entry,tf_entry,T_entry,x_entry):
        Hres=float(Hres_entry.get())
        K=float(k_entry.get())
        L=float(L_entry.get())
        D= float(D_entry.get())
        a=float(a_entry.get())
        f= float(f_entry.get())
        n = int(n_entry.get())
        Z0=float(Z0_entry.get())
        Z1=float(Z1_entry.get())
        Ds=float(Ds_entry.get())
        M=float(M_entry.get())
        Q0=float(Q0_entry.get())
        tf=float(tf_entry.get())
        T=float(T_entry.get())
        x=float(x_entry.get())        
        dx=L/float(n)   
        t,x1,H,h,Q,Hmax,Hmin,hmax,hmin,Zp,Qps=result(Hres,K,L,D,a,f,n,Z0,Z1,Ds,M,Q0,tf,T)
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
        aircombobox.bind('<<ComboboxSelected>>',lambda event:zoom(aircombobox,t,x1,H,h,Q,Hmax,Hmin,hmax,hmin,Zp,Qps,x,L,dx,n))
        canvas.create_window(140, 260,window=aircombobox)
        canvas.create_text(130,240,text="-ZOOM")
        # plots les graphes sur l'interface graphique 
        fig = Figure(figsize=(15,9), dpi=80)
        if x<=L and x>=0 :
            ax = fig.add_subplot(331) 
            fig.subplots_adjust( wspace=0.3, hspace=0.4)
            ax.grid(True)
            ax.plot(t,H[round(x/dx)][:])
            ax.plot(t,H[round(x/dx)][:],'b')
            ax.set_xlabel('Temps [s]')
            ax.set_ylabel('Charge hydraulique H(m)')
            ax.set_title("H(t) x=%s"%x)
                
            ax = fig.add_subplot(332)
            ax.grid(True)
            ax.plot(t,h[round(x/dx)][:])
            ax.set_xlabel("Temps [s]")
            ax.set_ylabel("pression (m)")
            ax.set_title("Pression (t) de x=%s"%x)
            
            ax = fig.add_subplot(333)
            ax.grid(True) 
            ax.plot(t,Q[round(x/dx)][:])
            ax.plot(t,Q[round(x/dx)][:],'r')
            ax.set_xlabel('Temps [s]')
            ax.set_ylabel('Débit volumique Q(m3/s)')        
            ax.set_title("Q(t) de x=%s"%x)
            
            ax = fig.add_subplot(334)
            ax.grid(True)
            ax.plot(x1,Hmax[:],'r',label='H max')
            ax.plot(x1,Hmin[:],'b',label='H min')
            for i in range (0,n+1) :
                if Hmax[i]==max(Hmax):
                    ax.plot(x1[i],Hmax[i],'bo')
                    p=x1[i]
            ax.plot(p,max(Hmax),'bo',label='max(H max)')
            for i in range (0,n+1) :
                if Hmin[i]==min(Hmin):
                    ax.plot(x1[i],Hmin[i],'ro')
                    p=x1[i]
            ax.plot(p,min(Hmin),'ro',label='min(H min)')
            ax.set_xlabel("Distance x[m]")
            ax.set_ylabel("Charge hydraulique H(m)")
            ax.set_title("Enveloppe H(x)")
            ax.legend()

            ax = fig.add_subplot(335)
            ax.grid(True)
            ax.plot(x1,hmax[:],'r',label='h max')
            ax.plot(x1,hmin[:],'b',label='h min')
            for i in range (0,n+1) :
                if hmax[i]==max(hmax):
                    ax.plot(x1[i],hmax[i],'bo')
                    p=x1[i]
            ax.plot(p,max(hmax),'bo',label='max(h max)')
            for i in range (0,n+1) :
                if hmin[i]==min(hmin):
                    ax.plot(x1[i],hmin[i],'ro')
                    p=x1[i]
            ax.plot(p,min(hmin),'ro',label='min(h min)')
            ax.set_xlabel("Distance x[m]")
            ax.set_ylabel("Pression (m)")
            ax.set_title("Enveloppe Pression(x) ")
            ax.legend()
                       
            ax = fig.add_subplot(337)
            ax.grid(True)
            ax.plot(t,Qps[:])
            ax.set_xlabel("Temps [s]")
            ax.plot(t,Qps[:],'r')
            ax.set_ylabel("Qps [m^3/s]")
            ax.set_title("Qps(t) de cheminée d'équilibre ") 
            
            ax = fig.add_subplot(338)
            ax.grid(True)
            ax.plot(t,Zp[:])
            ax.set_xlabel("Temps [s]")
            ax.plot(t,Zp[:],'b')
            ax.set_ylabel("Zp [m]")
            ax.set_title("Zp(t) de cheminée d'équilibre ")
            
                      
            graph = FigureCanvasTkAgg(fig,master=frame)
            return(graph)
# %% enregistre les resultas [reservoir-conduite-vanne] +cheminee d'equilbre
def save(Hres_entry,k_entry,L_entry,D_entry,a_entry,f_entry,n_entry,Z0_entry,Z1_entry,Ds_entry,M_entry,Q0_entry,tf_entry,T_entry,x_entry):
            Hres=float(Hres_entry.get())
            K=float(k_entry.get())
            L=float(L_entry.get())
            D= float(D_entry.get())
            a=float(a_entry.get())
            f= float(f_entry.get())
            n = int(n_entry.get())
            Z0=float(Z0_entry.get())
            Z1=float(Z1_entry.get()) 
            Ds=float(Ds_entry.get())
            M=float(M_entry.get())
            Q0=float(Q0_entry.get())
            tf=float(tf_entry.get())
            T=float(T_entry.get())
            dx=L/float(n)  
            dt=dx/a 
            t,x1,H,h,Q,Hmax,Hmin,hmax,hmin,Zp,Qps=result(Hres,K,L,D,a,f,n,Z0,Z1,Ds,M,Q0,tf,T)
            workbook = xlsxwriter.Workbook('Réservoir-conduite-vanne avec cheminee.xlsx')
            worksheet = workbook.add_worksheet('H(x,t)')
            for j in range (1,round(T/dt)+3):
                for i in range (1,n+2):
                    worksheet.write(0,0,'t[s]')
                    worksheet.write(i,0,'H[%s m]'%int(x1[i-1]))
                    worksheet.write(0,j,t[j-1])
                    worksheet.write(i,j,H[i-1][j-1])
                    
            worksheet = workbook.add_worksheet('p(x,t)')
            for j in range (1,round(T/dt)+3):
                for i in range (1,n+2):
                    worksheet.write(0,0,'t[s]')
                    worksheet.write(i,0,'h[%s m]'%int(x1[i-1]))
                    worksheet.write(0,j,t[j-1])
                    worksheet.write(i,j,h[i-1][j-1])
            worksheet = workbook.add_worksheet('Q(x,t)')
            for j in range (1,round(T/dt)+3):
                for i in range (1,n+2):
                    worksheet.write(0,0,'t[s]')
                    worksheet.write(i,0,'Q[%s m]'%int(x1[i-1]))
                    worksheet.write(0,j,t[j-1])
                    worksheet.write(i,j,Q[i-1][j-1])
                    
            worksheet = workbook.add_worksheet('Hmax et hmax')
            for i in range (1,n+2):
                    worksheet.write(i,0,'Hmax[%s m]'%int(x1[i-1]))
                    worksheet.write(i,1,Hmax[i-1])
                    worksheet.write(i,2,'hmax[%s m]'%int(x1[i-1]))
                    worksheet.write(i,3,hmax[i-1])
            worksheet = workbook.add_worksheet('Hmin et hmin')
            for i in range (1,n+2):
                    worksheet.write(i,0,'Hmin[%s m]'%int(x1[i-1]))
                    worksheet.write(i,1,Hmin[i-1])
                    worksheet.write(i,2,'hmin[%s m]'%int(x1[i-1]))
                    worksheet.write(i,3,hmin[i-1])
            worksheet = workbook.add_worksheet('Zp et Qps')
            for j in range (1,round(T/dt)+3):
                worksheet.write(0,0,'t[s]')
                worksheet.write(0,j,t[j-1])
                worksheet.write(1,0,'Zp[m]')
                worksheet.write(1,j,Zp[j-1])
                worksheet.write(2,0,'Qps[m^3/s]')
                worksheet.write(2,j,Qps[j-1])           
            workbook.close() 
