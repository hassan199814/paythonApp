from tkinter import *
import sqlite3

root = Tk()
root.config(bg="LightBlue")
root.title("Python Form")
root.geometry("1000x700")
vid = StringVar()
vnote = StringVar()
vtext = StringVar()

def insNote():
    NoteTitle = vname.get()
    NoteText = vadrs.get()

    conn = sqlite3.connect("DB.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE If NOT EXISTS Notes_Info( ID INT, NoteTitle TEXT, NoteText TEXT)')
        cursor.execute("INSERT INTO Notes_Info( NoteTitle, NoteText) values ( ?,?)",(NoteTitle, NoteText))
    conn.commit()

def updNote():
    NoteTitle = vname.get()
    NoteText = vadrs.get()

    conn = sqlite3.connect("DB.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Notes_Info set( NoteTitle, NoteText) = ( ?,?)",(NoteTitle, NoteText))
    conn.commit()

def delNote():
    NoteTitle = vname.get()
    NoteText = vadrs.get()

    conn = sqlite3.connect("DB.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Notes_Info WHERE NoteTitle like ? and NoteText like ? ",(NoteTitle, NoteText))
    conn.commit()


Label(root, text="Main Form", width=20, fg="Blue", bg="#9397C7", font=("bold", 30 ), borderwidth=2, relief="solid").place(x=290, y=33)
Label(root , width=136 , height=35 , borderwidth=2 , relief="solid" ).place(x=20 , y=130)
Label(root , text="Contacts Entry" , width=25 , fg="Blue" , bg="LightBlue" , font=("bold" , 15) , borderwidth=1 , relief="solid").place(x=130 , y=140)
Label(root , text="Notes Entry" , width=25 , fg="Blue" , bg="LightBlue" , font=("bold" , 15) , borderwidth=1 , relief="solid").place(x=600 , y=140)
Label(root , width=65 , height=31 , borderwidth=2 , relief="solid").place(x=25 , y= 185)
Label(root , text="ID" , width=10 , font=("bold" , 12) , anchor="w").place(x= 40 , y= 200)
Entry(root , width=45 , font=("bold" , 10) , fg="blue" , bg="LightGray" ,justify="center").place(x=150 , y=200)
Label(root , text="Name" , width=10 , font=("bold" , 12) , anchor="w" , name="ename").place(x= 40 , y= 230)
Entry(root , width=45 , font=("bold" , 10) , fg="blue"  ,justify="center" , textvariable=vname).place(x=150 , y=230)
Label(root , text="Address" , width=10 , font=("bold" , 12) , anchor="w").place(x= 40 , y= 260)
Entry(root , width=45 , font=("bold" , 10) , fg="blue"  ,justify="center" , textvariable=vadrs).place(x=150 , y=260)
Label(root , text="Phone No1" , width=10 , font=("bold" , 12) , anchor="w").place(x= 40 , y= 290)
Entry(root , width=45 , font=("bold" , 10) , fg="blue"  ,justify="center" , textvariable=vphnno1).place(x=150 , y=290)
Label(root , text="Phone No2" , width=10 , font=("bold" , 12) , anchor="w").place(x= 40 , y= 320)
Entry(root , width=45 , font=("bold" , 10) , fg="blue"  ,justify="center" , textvariable=vphnno2).place(x=150 , y=320)
Label(root , text="Phone No3" , width=10 , font=("bold" , 12) , anchor="w").place(x= 40 , y= 350)
Entry(root , width=45 , font=("bold" , 10) , fg="blue"  ,justify="center" , textvariable=vphnno3).place(x=150 , y=350)
Label(root , text="Phone No4" , width=10 , font=("bold" , 12) , anchor="w").place(x= 40 , y= 380)
Entry(root , width=45 , font=("bold" , 10) , fg="blue"  ,justify="center" , textvariable=vphnno4).place(x=150 , y=380)
Label(root , text="Email" , width=10 , font=("bold" , 12) , anchor="w" ).place(x= 40 , y= 410)
Entry(root , width=45 , font=("bold" , 10) , fg="blue"  ,justify="center" , textvariable=vemail).place(x=150 , y=410)
Button(root , text="Add" , bg="Green" , fg="White" , width=13 ).place(x=370 , y=620)
Button(root , text="Edit" , bg="Orange" , fg="White" , width=13).place(x=260 , y=620)
Button(root , text="Delete" , bg="Red" , fg="White" , width=13).place(x=150 , y=620)
Button(root , text="Find" , bg="Purple" , fg="White" , width=13).place(x=40 , y=620)
Label(root , width=65 , height=31 , borderwidth=2 , relief="solid").place(x=512 , y= 185)
Label(root , text="ID" , width=10 , font=("bold" , 12) , anchor="w").place(x= 530 , y= 200)
Entry(root , width=45 , font=("bold" , 10) , fg="blue" , bg="LightGray" ,justify="center").place(x=640 , y=200)
Label(root , text="Title" , width=10 , font=("bold" , 12) , anchor="w").place(x= 530 , y= 230)
Entry(root , width=45 , font=("bold" , 10) , fg="blue"  ,justify="center").place(x=640 , y=230)
Label(root , text="Note Text" , width=10 , font=("bold" , 12) , anchor="w").place(x= 530 , y= 260)
Text(root , width=45 , height=20 ,font=("bold" , 10) , fg="blue").place(x=640 , y=260)
Button(root , text="Add" , bg="Green" , fg="White" , width=13 ,command=insNote).place(x=857 , y=620)
Button(root , text="Edit" , bg="Orange" , fg="White" , width=13 , command=updNote).place(x=747 , y=620)
Button(root , text="Delete" , bg="Red" , fg="White" , width=13 , command=delNote).place(x=637 , y=620)
Button(root , text="Find" , bg="Purple" , fg="White" , width=13).place(x=527 , y=620)

root.mainloop()


