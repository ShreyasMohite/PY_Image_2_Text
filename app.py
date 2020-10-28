from tkinter import *
from PIL import ImageTk
from PIL import *
from tkinter import filedialog
import pytesseract
from PIL import Image
import tkinter.messagebox



class ImagetoText:
    def __init__(self,root):
        self.root=root
        self.root.title("Image-2-Text")
        self.root.geometry("600x600")
        self.root.iconbitmap("logo540.ico")
        self.root.resizable(0,0)

#=========================================================================#

        def on_enter1(e):
            but_browse['background']="black"
            but_browse['foreground']="cyan"
            
            

        def on_leave1(e):
            but_browse['background']="SystemButtonFace"
            but_browse['foreground']="SystemButtonText"


        def on_enter2(e):
            but_convert['background']="black"
            but_convert['foreground']="cyan"
            
            

        def on_leave2(e):
            but_convert['background']="SystemButtonFace"
            but_convert['foreground']="SystemButtonText"


        def on_enter3(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
            
            

        def on_leave3(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"
#==========================================================================#

        def clear():
            text.delete('1.0',"end")

        def browse():           
            global filename
            file_path = filedialog.askopenfilename(title = "Select file",filetypes = (("all files","*.*"),("Jpeg files","*.jpg"),("png files","*.png"))) 
            filename =file_path
            self.original = Image.open(file_path)
            resized = self.original.resize((355,160),Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(resized)
            #bglab=Label(F1,image=self.image,bd=2).place(x=0,y=0)
            photo_image=Label(siframe,image=self.image,bd=2)
            photo_image.place(x=100,y=15)

        
        def Convert_text():
            try:

                pytesseract.pytesseract.tesseract_cmd='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
                img=Image.open(filename)
                result = pytesseract.image_to_string(img) 
                with open("C:/TEMP/abc.txt","w") as f:
                    f.write(result)
                with open("C:/TEMP/abc.txt","r") as f:
                    text.insert("end",f.read())
            except:
                tkinter.messagebox.showerror("Error","Please select image first")
                

#==================================================================================================================#




        


#===============================frame========================================#
        mainframe=Frame(self.root,width=600,height=600,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=594,height=350,relief="ridge",bd=3)
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=594,height=243,relief="ridge",bd=3)
        secondframe.place(x=0,y=350)


        fiframe=Frame(firstframe,width=588,height=150,relief="ridge",bd=3,bg="grey77")
        fiframe.place(x=0,y=0)

        siframe=Frame(firstframe,width=588,height=193,relief="ridge",bd=3,bg="black")
        siframe.place(x=0,y=150)
#===============================firstframe button================================================#
        but_browse=Button(fiframe,text="Browse Image",width=17,font=('times new roman',12,'bold'),cursor="hand2",command=browse)
        but_browse.place(x=210,y=10)
        but_browse.bind("<Enter>",on_enter1)
        but_browse.bind("<Leave>",on_leave1)


        but_convert=Button(fiframe,text="Convert To text",width=17,font=('times new roman',12,'bold'),cursor="hand2",command=Convert_text)
        but_convert.place(x=50,y=80)
        but_convert.bind("<Enter>",on_enter2)
        but_convert.bind("<Leave>",on_leave2)


        but_clear=Button(fiframe,text="Clear",width=17,font=('times new roman',12,'bold'),cursor="hand2",command=clear)
        but_clear.place(x=370,y=80)
        but_clear.bind("<Enter>",on_enter3)
        but_clear.bind("<Leave>",on_leave3)

#====================================================================================================#
       
        self.original = Image.open("C:\\Users\\SHREYAS\\Desktop\\shreyas python\\img_to_text\\imgs\\black.png")
        resized = self.original.resize((355,160),Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        #bglab=Label(F1,image=self.image,bd=2).place(x=0,y=0)
        photo_image=Label(siframe,image=self.image,bd=2)
        photo_image.place(x=100,y=15)
        
    

#====================================secondframe===============================================#
        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=12,width=70,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)

#==============================================================================================#




if __name__ == "__main__":
    root=Tk()
    app=ImagetoText(root)
    root.mainloop()