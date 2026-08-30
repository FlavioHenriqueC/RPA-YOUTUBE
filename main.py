import os
import imageio_ffmpeg
import yt_dlp

def baixar_audio_youtube(url_do_video, pasta_destino=r'C:\Users\flavi\OneDrive\Área de Trabalho\music'):
    os.makedirs(pasta_destino, exist_ok=True)

    opcoes = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
        'ffmpeg_location': imageio_ffmpeg.get_ffmpeg_exe(),  # Pega o caminho do FFmpeg automaticamente
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,
        'quiet': False,
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        print(f"Baixando áudio: {url_do_video}")
        ydl.download([url_do_video])
        print("Download e conversão concluídos!")

if __name__ == '__main__':
    url = "--"
    baixar_audio_youtube(url)