from toga import App, Box, Button, Label, TextInput, Window
from toga.style import Pack
from toga.style.pack import COLUMN
from yt_dlp import YoutubeDL
import os
import tkinter as tk
from tkinter import filedialog

def escolher_arquivo():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    caminho = filedialog.askopenfilename(title="Selecione o arquivo de links", filetypes=[("Text files", "*.txt")])
    root.destroy()
    return caminho


def baixar_audio(url, nome_arquivo=None):
    pasta_download = os.path.join(os.path.expanduser("~"), "Downloads", "MYTUBE")
    os.makedirs(pasta_download, exist_ok=True)

    if nome_arquivo:
        outtmpl = os.path.join(pasta_download, f"{nome_arquivo}.%(ext)s")
    else:
        outtmpl = os.path.join(pasta_download, "%(title)s.%(ext)s")

    ydl_opts = {
        'outtmpl': outtmpl,
        'ignoreerrors': True,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

class YouTubeDownloader(App):
    def startup(self):
        self.main_window = Window(title=self.formal_name)
        main_box = Box(style=Pack(direction=COLUMN, padding=10))

        # Campo de texto para link
        self.url_input = TextInput(placeholder="Cole o link do vídeo", style=Pack(flex=1, margin_bottom=5))
        # Campo para nome do arquivo
        self.nome_input = TextInput(placeholder="Digite o nome do arquivo (opcional)", style=Pack(flex=1, margin_bottom=5))
        # Botão para baixar link único
        btn_link = Button("Baixar Áudio", on_press=self.baixar, style=Pack(margin_bottom=5))
        # Botão para baixar de arquivo .txt
        btn_arquivo = Button("Baixar de Arquivo", on_press=self.baixar_arquivo, style=Pack(margin_bottom=5))
        # Label de status
        self.status = Label("", style=Pack(margin_top=5))

        main_box.add(self.url_input)
        main_box.add(self.nome_input)
        main_box.add(btn_link)
        main_box.add(btn_arquivo)
        main_box.add(self.status)

        self.main_window.content = main_box
        self.main_window.show()

    def baixar(self, widget):
        url = self.url_input.value.strip()
        nome_arquivo = self.nome_input.value.strip() or None

        if url:
            try:
                self.status.text = "⏳ Baixando..."
                baixar_audio(url, nome_arquivo)
                self.status.text = "✅ Download concluído!"
            except Exception as e:
                self.status.text = f"❌ Erro: {e}"
        else:
            self.status.text = "⚠️ Insira um link válido."

    def baixar_arquivo(self, widget):
        arquivo = escolher_arquivo()
        if not arquivo:
            return

        with open(arquivo, "r") as f:
            links = f.read().splitlines()

        for i, link in enumerate(links, start=1):
            try:
                nome_arquivo = f"musica_{i}"
                self.status.text = f"⏳ Baixando {nome_arquivo}..."
                baixar_audio(link)
                self.status.text = f"✅ Baixado: {nome_arquivo}"
            except Exception as e:
                self.status.text = f"❌ Erro: {e}"

def main():
    return YouTubeDownloader("MyTube", "com.mytube")

if __name__ == "__main__":
    main().main_loop()
