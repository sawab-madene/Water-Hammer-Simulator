# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 03:20:08 2020

@author: hp

"" bibliotheques"""   
import tkinter as tk
from PIL import ImageTk,Image   
from fenetres import system_type,about_us 

                                                                             
""" create widgets """
##window                                            
main_window=tk.Tk()
main_window.state('zoomed')
main_window.title("Water Hammer Simulator  v.2019")
main_window.iconbitmap(r'photos\images.ico')
w, h = main_window.winfo_screenwidth(), main_window.winfo_screenheight()
##canvas
canvas = tk.Canvas(main_window,width=w, height=h)
##images
#background image
background_im=Image.open(r'photos\background.png')
background_im = ImageTk.PhotoImage(background_im.resize((w,h), Image.ANTIALIAS))
canvas.create_image(0, 0, image=background_im, anchor='nw')
##text
canvas.create_text(730,100, text="Bienvenue a",fill='white',font=('Arial',40,'bold'))
canvas.create_text(730,170, text="Water Hammer Simulator",fill='white',font=('Arial',40))
##buttons
project_B=tk.Button(main_window,text='Créer Un Nouveau Projet ',command=system_type ,bg='white',
                    fg='#0077DD',bd=2,font=('Arial',15,'bold'),height=1, width =25)
propos_B=tk.Button(main_window,text='À propos',command=about_us,bg='white',fg='#0077DD',bd=2,font=('Arial',15,'bold'),height=1, 
         width =25)
project_B_W=canvas.create_window(730 ,300,window=project_B)
propos_B_W=canvas.create_window(730 ,360,window=propos_B)
""" activate widgets"""
canvas.place(x=-1.5,y=-1.5)                                                                                                                    
main_window.mainloop()