import turtle as trl, tkinter as tk, time as t, os

#if u want Version Exe or the offline version,
#go to this link: https://drive.google.com/drive/folders/1DNdIB9ABMoHD1qvEMpm_rmNhmM1Y3MPA?usp=drive_link

keyboard_mode_active = False

def refresh():
  trl.bye()
  trl.Screen()
  keyboard_mode_1
  trl.mainloop()

def hentikan():
  trl.Terminator('t')
  trl.Screen()
  trl.mainloop()


def ditekan():
  turtle_maju50()


def turtle_maju50():
  trl.forward(50)


def turtle_maju25():
  trl.forward(25)


def tengah():
  trl.goto(0, 0)


def turtle_mundur50():
  trl.backward(50)


def turtle_mundur25():
  trl.backward(25)


def turtle_kiri90():
  trl.left(90)

 
def turtle_kiri45():
  trl.left(45)


def turtle_kanan90():
  trl.right(90)


def turtle_kanan45():
  trl.right(45)


def turtle_bulat50():
  trl.circle(50)


def keyboard_mode_1():
  root.destroy()
  t.sleep(1)
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Mode Keyboard dipilih")
  print('Tanda Panah = arah Turtle \nWASD = Gerak Setengah\nC = Lingkaran \nSpasi = Kalibrasi/Tengah \nT = Menghentikan Turtle ketika setengah jalan')
  trl.onkeypress(turtle_maju50, "Up")
  trl.onkeypress(turtle_mundur50, "Down")
  trl.onkeypress(turtle_kiri90, "Left")
  trl.onkeypress(turtle_kanan90, "Right")

  trl.onkeypress(turtle_maju25, 'w')
  trl.onkeypress(turtle_mundur25, 's')
  trl.onkeypress(turtle_kiri45, 'a')
  trl.onkeypress(turtle_kanan45, 'd')

  trl.onkeypress(turtle_bulat50, "c")
  trl.onkeypress(refresh, "r")
  trl.onkeypress(tengah, ' ')
  trl.onkeypress(hentikan, 't')
  trl.listen()
  trl.mainloop()
  

def keyboard_mode_2():
  t.sleep(1)
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Keyboard mode Choosen")
  print('Arrow Keys = Move Turtle \nWASD Keys = Move Half Ways\nC = Make A circle \nSpace = Callibrate/Go to Center \nT = Stop turtle when the turtle go'
  )
  trl.onkeypress(turtle_maju50, "Up")
  trl.onkeypress(turtle_mundur50, "Down")
  trl.onkeypress(turtle_kiri90, "Left")
  trl.onkeypress(turtle_kanan90, "Right")

  trl.onkeypress(turtle_maju25, 'w')
  trl.onkeypress(turtle_mundur25, 's')
  trl.onkeypress(turtle_kiri45, 'a')
  trl.onkeypress(turtle_kanan45, 'd')

  trl.onkeypress(turtle_bulat50, "c")
  trl.onkeypress(refresh, "r")
  trl.onkeypress(tengah, ' ')
  trl.onkeypress(hentikan, 't')
  trl.listen()
  trl.mainloop()
 
def tombol_mode_1():
  root = tk.Tk()
  root.title('Kontroller turtle (Mode Tombol)')
  print('klik 2x kalibrasi untuk memunculkan Tanda Panah \nJika Mengeklik Refresh')
  t.sleep(1)
  #Lebar dan panjang jendela
  root.geometry('350x150')
  #Command tombol
  tombol_maju = tk.Button(root, text="Maju", command=turtle_maju50)
  tombol_tengah = tk.Button(root, text='kalibrasi', command=tengah)
  tombol_mundur = tk.Button(root, text='mundur', command=turtle_mundur50)
  tombol_kiri = tk.Button(root, text='Kiri', command=turtle_kiri90)
  tombol_kanan = tk.Button(root, text='kanan', command=turtle_kanan90)
  tombol_refresh = tk.Button(root, text='Refresh', command=refresh)
  tombol_circle = tk.Button(root, text='circle', command=turtle_bulat50)

  #Penempatan tombol
  tombol_tengah.place(relx=0.5, rely=0.5, anchor='center')
  tombol_maju.pack(side='top', pady=5)
  tombol_mundur.pack(side='bottom', pady=5)
  tombol_kiri.place(relx=0.3, rely=0.5, anchor='center')
  tombol_kanan.place(relx=0.7, rely=0.5, anchor='center')
  tombol_refresh.place(x=0, y=0)
  tombol_circle.place(relx=1, rely=1, anchor='se')
  
  root.mainloop()
  


def tombol_mode_2():
  root = tk.Tk()
  root.title('Controller turtle (Button Mode)')
  print('Press Callibrate 2 Times To Display Turtle Arrow \nIf You Press The Refresh Button')
  t.sleep(1)
  #Lebar dan panjang jendela
  root.geometry('350x150')
  #Command tombol
  tombol_maju = tk.Button(root, text="Forward", command=turtle_maju50)
  tombol_tengah = tk.Button(root, text='Calibrate', command=tengah)
  tombol_mundur = tk.Button(root, text='Backward', command=turtle_mundur50)
  tombol_kiri = tk.Button(root, text='Left', command=turtle_kiri90)
  tombol_kanan = tk.Button(root, text='Right', command=turtle_kanan90)
  tombol_refresh = tk.Button(root, text='Refresh', command=refresh)
  tombol_circle = tk.Button(root, text='Circle', command=turtle_bulat50)

  #Penempatan tombol
  tombol_tengah.place(relx=0.5, rely=0.5, anchor='center')
  tombol_maju.pack(side='top', pady=5)
  tombol_mundur.pack(side='bottom', pady=5)
  tombol_kiri.place(relx=0.3, rely=0.5, anchor='center')
  tombol_kanan.place(relx=0.7, rely=0.5, anchor='center')
  tombol_refresh.place(x=0, y=0)
  tombol_circle.place(relx=1, rely=1, anchor='se')

  root.mainloop()


# Pertanyaan Apakah memakai keyboard atau tombol (IN)
def indo():
  root.title('Mode Kontrol')
  indolabel = tk.Label(root, text='↓ Pilih mode Kontrol ↓')
  indo1 = tk.Button(root, text='Tombol', command=tombol_mode_1)
  indo2 = tk.Button(root, text='Keyboard', command=keyboard_mode_1)

  indolabel.place(relx=0.5, rely=0.1, anchor='center')
  indo1.place(relx=0.3, rely=0.5, anchor='center')
  indo2.place(relx=0.7, rely=0.5, anchor='center')

def english():
  root.destroy()
  t.sleep(1)
  os.system('cls' if os.name == 'nt' else 'clear')
  print('Turtle Controller')
  print('Choose Keyboard mode or Button Mode')
  inp_english = input('Keyboard -> K (For Advance Users) \nButton -> B (For General Users)\n>>>').lower()
  if inp_english == 'k':
    os.system('cls' if os.name == 'nt' else 'clear')
    keyboard_mode_2()
  elif inp_english == 'b':
    os.system('cls' if os.name == 'nt' else 'clear')
    tombol_mode_2()
    print('Button Mode Activated')
  else:
    print('Invalid Input. Closing..')
    t.sleep(2)


root = tk.Tk()
root.geometry('350x150')
root.title('Language Option')
label1 = tk.Label(root, text='Language')
lang1 = tk.Button(root, text='English', command=english)
lang2 = tk.Button(root, text='Indonesia', command=indo)

label1.place(relx=0.5, rely=0.1, anchor='center')
lang1.place(relx=0.3, rely=0.5, anchor='center')
lang2.place(relx=0.7, rely=0.5, anchor='center')

root.mainloop()