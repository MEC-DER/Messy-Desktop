# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:10:27 2020

@author: MEC DER
"""
"""
_______mess types______
Folders
PDF's
txt
CSV
JPG
PNG
xlsx excell file 
HTML 

________mess names__________
photo (number)
stuff (number)
thing (number)
IMG (number)
untitled (number)
name (number)
part (number)

"""
# This section is where the external libraries are imported these need to be installed
#before the programm will full run use python pip install. 
from reportlab.pdfgen import canvas
import random #for randomly generated numbers
import os #for working with folders and file paths.
from PIL import Image, ImageDraw #for image creation and manipulation.
import openpyxl as xl # this is usefull for working with excell files. for more advanced excell work, pandas, is realy good.
# as xl changes the call term from openpyxl to xl this makes it easier to type.

user_name=os.getlogin() #getting the user name this is used to alow acsess to write to the desktop.
desktop_path=file_path="C:\\Users\\"+user_name+"\\Desktop\\" # use double back slashes for the file path as a back slash is an escape character.

record_of_created_paths=[] #will record the file path to undo the programm, must only be recorded to be if created.

messy_name_bases=["photo","stuff","thing",
                  "IMG","untitled","name","part","date"]
number_of_files_created=100
for j in range(number_of_files_created):
    #randomly selecting the messy file name base
    messy_name_select=random.randint(0,len(messy_name_bases)-1)
    messy_name=messy_name_bases[messy_name_select]
    
    # randomly generating a messy number
    messy_number=random.randint(0,1000)
    messy_number_formated=str(messy_number).rjust(4,"0")
    messy_file_name=messy_name+messy_number_formated
    
    path_created=True# this is a flag so the programm knows if a file was successfully created
    
    file_type=random.randint(1,8)# randomly selecting the file type
    
    path=""#the file path is cleared each itteration to prevent any strange errors
    
    try:  #exception catching if the program fails with n error it will move to the except part and execute that instead.
        if file_type==1:
            #____________folder 1_______________#creating a folder
            folder_name=messy_file_name
            
            folder_path=desktop_path+folder_name
            path=folder_path
            os.mkdir(folder_path)
        
        elif file_type==2:
            #_________________txt 2____________
            
            
            
            text_file_path=desktop_path+messy_file_name+".txt"
            path=text_file_path
            
            text_file=open(text_file_path,"w+")
            text_file_content="Hello this is a text file."
            text_file.write(text_file_content)
            
            text_file.close()
        
        elif file_type==3:
            #_________________csv 3______________
            
            csv_file_path=desktop_path+messy_file_name+".csv"
            path=csv_file_path
            
            csv_file=open(csv_file_path,"w+")
            csv_file.write("Hello, this, is, a, comma, seperated, values, file")
            
            csv_file.close()
        
        elif file_type==4:
        
            #____________jpg 4______________
            image_file_path=desktop_path+messy_file_name+".jpg"
            path=image_file_path
            image_jpg=Image.new('RGB',(161,161),color=(0,0,0))
            image_add_text=ImageDraw.Draw(image_jpg)
            image_add_text.text((10,10),"Hello Im A JPG",fill=(255,255,255))
            image_jpg.save(image_file_path)
        
        elif file_type==5:
        
            #____________png 5_____________
            image_file_path=desktop_path+messy_file_name+".png"
            path=image_file_path
            image_png=Image.new('RGB',(161,161),color=(255,255,255))
            image_add_text=ImageDraw.Draw(image_png)
            image_add_text.text((10,10),"Hello Im A PNG",fill=(0,0,0))
            image_png.save(image_file_path)
        
        elif file_type==6:
            #_____________html 6____________________
            
            html_file_path=desktop_path+messy_file_name+".html"
            path=html_file_path
            html_file=open(html_file_path,"w+")
            html_file.write("<h1> Hello this is a html file.</h1>")
            
            html_file.close()
        
        elif file_type==7:
            #________________xlsx 7______________
            excel_file_path=desktop_path+messy_file_name+".xlsx"
            path= excel_file_path
            excel_file=xl.Workbook()
            
            work_sheet=excel_file.active
            work_sheet.title="Hello excel"
            
            excel_write=["Hello","This", "IS", "An", "Excel","File"]
            for i in range(len(excel_write)):
                work_sheet.cell(row = i+1,column=i+1).value=excel_write[i] # writes the words diagonally
                
            excel_file.save(excel_file_path)
            
        
        elif file_type==8:
            #_________________PDF 8________________
            
            pdf_file_path=desktop_path+messy_file_name+".pdf"
            path=pdf_file_path
            page_to_be_drawn=canvas.Canvas(pdf_file_path)
            page_to_be_drawn.drawString(100,100,"Hello this is a PDF")
            page_to_be_drawn.save()
        
        else:
            path_created=False
            
        
        path_created=True
        print("created ",path)
   
    except:
        path_created=False
        print("already there", path)
    
    if path_created==True:
        record_of_created_paths.append(path)#only records the path for deletion if it was successfully created
        
input("press enter to delete what you have created")

#removing all created files

for paths in record_of_created_paths:
    try:
        try:
            os.remove(paths)
            print("deleted ",paths)
        except:
            os.rmdir(paths)
        
    except:
        print("could not find ", paths)

         
    
    
    
