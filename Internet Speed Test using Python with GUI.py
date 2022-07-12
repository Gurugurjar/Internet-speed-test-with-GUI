#!/usr/bin/env python
# coding: utf-8

# In[31]:


pip install speedtest-cli


# In[3]:


from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    download = str(round(sp.download()/(10**6),3))+"Mbps"
    upload = str(round(sp.upload()/(10**6),3))+"Mbps"
    label_download.config(text=download)
    label_up.config(text=upload)
    

sp = Tk()
sp.title("Internet Speed")
sp.geometry("500x700")
sp.config(bg="pink")

label = Label(sp,text = "Internet Speed Test",font=("Time New Roman",30,"bold"),bg="pink", fg="white")
label.place(x=60,y=40,height=50,width=380)

label = Label(sp,text = "Download Speed",font=("Time New Roman",30,"bold"),)
label.place(x=60,y=130,height=50,width=380)

label_download = Label(sp,text = "00",font=("Time New Roman",30,"bold"),)
label_download.place(x=60,y=200,height=50,width=380)

label = Label(sp,text = "Upload Speed",font=("Time New Roman",30,"bold"),)
label.place(x=60,y=290,height=50,width=380)

label_up = Label(sp,text = "00",font=("Time New Roman",30,"bold"),)
label_up.place(x=60,y=360,height=50,width=380)

# create a button 
button = Button(sp,text="CHECK Speed",font=("Time New Roman",30,"bold"),relief=RAISED,bg="red",command=speedcheck)
button.place(x=60,y=460,height=50,width=380)




sp.mainloop()


# In[ ]:




