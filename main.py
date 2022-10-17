import tkinter as tk
from tkinter import ttk, END
from tkinter.messagebox import showinfo
import threading
import math
import threading

class App(tk.Tk):

  def __init__(self):
    super().__init__()
    # configure the root window
    self.title('Mon morpion')
    self.geometry('400x460')
    self.resizable(False, False)

    self.value = None
    self.joueur = 0

    self.cercle = tk.PhotoImage(file="cerle.png")
    self.croix = tk.PhotoImage(file="croix.png")
    self.vide = tk.PhotoImage(file="vide.png")

    self.button1 = tk.Button(text="", width=120, height=120, image=self.vide, command=self.set1)
    self.button1.grid(row=0, column=0)

    self.button2 = tk.Button(text="", width=120, height=120, image=self.vide, command=self.set2)
    self.button2.grid(row=1, column=0)

    self.button3 = tk.Button(text="", width=120, height=120, image=self.vide, command=self.set3)
    self.button3.grid(row=2, column=0)

    self.button4 = tk.Button(text="", width=120, height=120, image=self.vide, command=self.set4)
    self.button4.grid(row=0, column=1)

    self.button5 = tk.Button(text="", width=120, height=120, image=self.vide, command=self.set5)
    self.button5.grid(row=1, column=1)

    self.button6 = tk.Button(text="", width=120, height=120, image=self.vide, command=self.set6)
    self.button6.grid(row=2, column=1)

    self.button7 = tk.Button(text="", width=120, height=120, image=self.vide, command=self.set7)
    self.button7.grid(row=0, column=2)

    self.button8 = tk.Button(text="", width=120, height=120, image=self.vide, command=self.set8)
    self.button8.grid(row=1, column=2)

    self.button9 = tk.Button(text="", width=120, height=120, image=self.vide, command=self.set9)
    self.button9.grid(row=2, column=2)

    self.buttonstop = tk.Button(text="Reset", width=5, height=1, command=self.stop)
    self.buttonstop.place(relx=0.45, rely=0.90)

  def stop(self):
    self.button1.configure(text="", width=120, height=120, image=self.vide)
    self.button2.configure(text="", width=120, height=120, image=self.vide)
    self.button3.configure(text="", width=120, height=120, image=self.vide)
    self.button4.configure(text="", width=120, height=120, image=self.vide)
    self.button5.configure(text="", width=120, height=120, image=self.vide)
    self.button6.configure(text="", width=120, height=120, image=self.vide)
    self.button7.configure(text="", width=120, height=120, image=self.vide)
    self.button8.configure(text="", width=120, height=120, image=self.vide)
    self.button9.configure(text="", width=120, height=120, image=self.vide)


  def set1(self):
    print(self.joueur)

    if self.button1["image"] == "pyimage3" and self.joueur == 1:
      self.button1["image"] = self.croix
      if self.button2["image"] == "pyimage2" and self.button3["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button4["image"] == "pyimage2" and self.button7["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button5["image"] == "pyimage2" and self.button8["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 0
    else:
      self.button1["image"] = self.cercle
      if self.button2["image"] == "pyimage1" and self.button3["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button4["image"] == "pyimage1" and self.button7["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button5["image"] == "pyimage1" and self.button9["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 1

  def set2(self):
    if self.button2["image"] == "pyimage3" and self.joueur == 1:
      self.button2["image"] = self.croix
      if self.button1["image"] == "pyimage2" and self.button3["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button5["image"] == "pyimage2" and self.button8["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 0
    else:
      self.button2["image"] = self.cercle
      if self.button1["image"] == "pyimage1" and self.button3["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button5["image"] == "pyimage1" and self.button8["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 1

  def set3(self):
    if self.button3["image"] == "pyimage3" and self.joueur == 1:
      self.button3["image"] = self.croix
      if self.button1["image"] == "pyimage2" and self.button2["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button6["image"] == "pyimage2" and self.button9["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button5["image"] == "pyimage2" and self.button7["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 0
    else:
      self.button3["image"] = self.cercle
      if self.button1["image"] == "pyimage1" and self.button2["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button6["image"] == "pyimage1" and self.button9["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button5["image"] == "pyimage1" and self.button7["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 1

  def set4(self):
    if self.button4["image"] == "pyimage3" and self.joueur == 1:
      self.button4["image"] = self.croix
      if self.button1["image"] == "pyimage2" and self.button7["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button5["image"] == "pyimage2" and self.button6["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 0
    else:
      self.button4["image"] = self.cercle
      if self.button1["image"] == "pyimage1" and self.button7["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button5["image"] == "pyimage1" and self.button6["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 1
  def set5(self):
    if self.button5["image"] == "pyimage3" and self.joueur == 1:
      self.button5["image"] = self.croix
      if self.button2["image"] == "pyimage2" and self.button8["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button4["image"] == "pyimage2" and self.button6["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button1["image"] == "pyimage2" and self.button9["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button3["image"] == "pyimage2" and self.button7["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 0
    else:
      self.button5["image"] = self.cercle
      if self.button2["image"] == "pyimage1" and self.button8["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button4["image"] == "pyimage1" and self.button6["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button1["image"] == "pyimage1" and self.button9["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button3["image"] == "pyimage1" and self.button7["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 1

  def set6(self):
    if self.button6["image"] == "pyimage3" and self.joueur == 1:
      self.button6["image"] = self.croix
      if self.button3["image"] == "pyimage2" and self.button9["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button4["image"] == "pyimage2" and self.button5["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 0
    else:
      self.button6["image"] = self.cercle
      if self.button3["image"] == "pyimage1" and self.button9["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button4["image"] == "pyimage1" and self.button5["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 1

  def set7(self):
    if self.button7["image"] == "pyimage3" and self.joueur == 1:
      self.button7["image"] = self.croix
      if self.button1["image"] == "pyimage2" and self.button4["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button8["image"] == "pyimage2" and self.button9["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button3["image"] == "pyimage2" and self.button5["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 0
    else:
      self.button7["image"] = self.cercle
      if self.button1["image"] == "pyimage1" and self.button4["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button8["image"] == "pyimage1" and self.button9["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button3["image"] == "pyimage1" and self.button5["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 1

  def set8(self):
    if self.button8["image"] == "pyimage3" and self.joueur == 1:
      self.button8["image"] = self.croix
      if self.button7["image"] == "pyimage2" and self.button9["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button1["image"] == "pyimage2" and self.button4["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 0
    else:
      self.button8["image"] = self.cercle
      if self.button7["image"] == "pyimage1" and self.button9["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button1["image"] == "pyimage1" and self.button4["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 1

  def set9(self):
    if self.button9["image"] == "pyimage3" and self.joueur == 1:
      self.button9["image"] = self.croix
      if self.button3["image"] == "pyimage2" and self.button6["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button7["image"] == "pyimage2" and self.button8["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button1["image"] == "pyimage2" and self.button5["image"] == "pyimage2":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 0
    else:
      self.button9["image"] = self.cercle
      if self.button3["image"] == "pyimage1" and self.button6["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button7["image"] == "pyimage1" and self.button8["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      if self.button1["image"] == "pyimage1" and self.button5["image"] == "pyimage1":
        tk.messagebox.showinfo("Info", "Victoire")
        self.stop()
      self.joueur = 1








if __name__ == "__main__":
  app = App()
  app.mainloop()