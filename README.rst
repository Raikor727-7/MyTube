# 🎵 MyTube Downloader

**MyTube** é um aplicativo simples para baixar áudios do YouTube diretamente em **.mp3**.  
Ele possui uma interface gráfica minimalista feita com [Toga](https://beeware.org/project/projects/libraries/toga/), e no futuro contará com versão mobile para Android.

---

## 📌 Funcionalidades atuais
- Baixa **áudio em MP3** a partir de um **link único** ou de uma **playlist inteira**.
- Playlist deve estar **pública** ou **não listada** (não funciona com vídeos privados).
- Mini versão gráfica simples para copiar e colar links.
- Arquivos são salvos automaticamente em:

- Os arquivos recebem o **nome original do vídeo**.



---

## 📖 Como usar
1. Clone este repositório:
 ```bash
 git clone https://github.com/SEU-USUARIO/mytube.git
 cd mytube

pip install -r requirements.txt

briefcase dev

```
## 📂 Estrutura
```
mytube/
│
├── src/mytube/       # Código principal do app
├── pyproject.toml    # Configuração do Briefcase/Toga
└── README.md         # Documentação
```

## 🛠️ Funcionalidades futuras

- 📜 Baixar letras da música e embedar no arquivo.

- 🖼️ Baixar thumbnail do vídeo e usar como capa.

- 👤 Salvar nome do canal/postador como autor no arquivo.

- 💾 Escolher onde salvar os arquivos.

- 🎚️ Escolher o formato de saída (.mp3 ou .mp4) e a qualidade.

- 📱 Versão mobile para Android.

## ⚠️ Observações

- O projeto está em desenvolvimento inicial (versão 0.0.1).

- Alguns recursos podem não funcionar em todas as plataformas.

- Para playlists privadas, o download não é suportado.

### 👨‍💻 Autor

Jonathan Matthias
> ✉️ jjmmss.173@gmail.com
