import serial  
import time
import tkinter
def quit():
 global tkTop
 ser.write(b'L')
 tkTop.destroy()

def set_button1_state():
 global b
 b += 1
 varLabel.set("LED ON ")
 ser.write(b'H')
 varLabel2.set(b)
 print(b)

def set_button2_state():
 varLabel.set("LED OFF")
 ser.write(b'L')

ser = serial.Serial('COM13', 9600)
print("Reset Arduino")
time.sleep(3)
ser.write(b'L')

tkTop = tkinter.Tk()
tkTop.geometry('700x600')
tkTop.title("Controlling LED")
label3 = tkinter.Label(text = 'Control LED by pressing Button',font=("Courier", 12,'bold')).pack()
tkTop.counter = 0
b = tkTop.counter
varLabel = tkinter.IntVar()
tkLabel = tkinter.Label(textvariable=varLabel, )
tkLabel.pack()
varLabel2 = tkinter.IntVar()
tkLabel2 = tkinter.Label(textvariable=varLabel2, )
tkLabel2.pack()
button1 = tkinter.IntVar()

button1state = tkinter.Button(tkTop,
text="ON",
command=set_button1_state,
height = 4,
fg = "black",
width = 8,
bd = 5,
activebackground='green'
)
button1state.pack(side='top', ipadx=10, padx=10, pady=15)
button2 = tkinter.IntVar()
button2state = tkinter.Button(tkTop,
text="OFF",
command=set_button2_state,
height = 4,
fg = "black",
width = 8,
bd = 5
)
button2state.pack(side='top', ipadx=10, padx=10, pady=15)

tkButtonQuit = tkinter.Button(
tkTop,
text="Quit",
command=quit,
height = 4,
fg = "black",
width = 8,
bg = 'yellow',
bd = 5
)
tkButtonQuit.pack(side='top', ipadx=10, padx=10,
pady=15)
tkinter.mainloop()