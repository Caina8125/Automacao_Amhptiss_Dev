import customtkinter
from Presentation.Desktop.Login import Login
from Presentation.Desktop.TesteAwait import chamada_assincrona
import tkinter as tk

class Aplication(tk.Tk):
    def __init__(self):
        self.corAtual = "light"
        customtkinter.set_appearance_mode(self.corAtual)
        self.janela = customtkinter.CTk()
        self.janela.geometry("640x480")
        
        self.janela.title("AMHP - Automações")
        self.janela.iconbitmap(r"Infra\Arquivos\Robo.ico")
        self.janela.resizable(width=False, height=False)
        self.janela.eval('tk::PlaceWindow . center')
        Login(self.janela, self.corAtual)
        # chamada_assincrona(self)

    def modoEscuro(self):
        if (self.corAtual == "light"):
            self.corAtual = "dark"
            customtkinter.set_appearance_mode(self.corAtual)
            customtkinter.set_default_color_theme("dark-blue")
        else:
            self.corAtual = "light"
            customtkinter.set_appearance_mode(self.corAtual)