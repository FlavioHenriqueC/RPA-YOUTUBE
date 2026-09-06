import os
import imageio_ffmpeg
import yt_dlp
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permite que o React (que roda em outra porta) converse com o Python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/baixar")
def baixar_musica(url: str):
    pasta_temporaria = "downloads_temp"
    os.makedirs(pasta_temporaria, exist_ok=True)

    opcoes = {
        'format': 'bestaudio/best',
        'outtmpl': f'{pasta_temporaria}/%(title)s.%(ext)s',
        'ffmpeg_location': imageio_ffmpeg.get_ffmpeg_exe(),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            info = ydl.extract_info(url, download=True)
            titulo = info.get('title', 'audio')
            caminho_arquivo = os.path.join(pasta_temporaria, f"{titulo}.mp3")
            
        # Devolve o arquivo para o navegador baixar
        return FileResponse(path=caminho_arquivo, filename=f"{titulo}.mp3", media_type='audio/mpeg')
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Para rodar: uvicorn api:app --reload