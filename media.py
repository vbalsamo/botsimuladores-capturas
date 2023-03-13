import os
import random
import subprocess

def generate_thumbnail(in_filename, out_filename, duracion):
    timess = random.uniform(1, duracion)
    os.system(f"ffmpeg -ss {timess} -copyts -i {in_filename} -vf subtitles={nombreSubtitulos(in_filename)} -vframes 1 {out_filename}")
    return out_filename

def generate_gif(in_filename, out_filename, duracion):
    timess = random.uniform(1, duracion) #select random timestamp from video
    os.system(f'ffmpeg -ss {timess} -t 3 -copyts -i {in_filename} -vf "subtitles={nombreSubtitulos(in_filename)},fps=10,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -c:a copy -ss {timess} -loop 0 {out_filename}')
    return out_filename

def get_length(input_video):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_video], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return float(result.stdout)

def nombreSubtitulos(filename):
    nombreSinFormato = (filename.split('.')[0]).split('/')[-1]
    subtitleFolder = 'subtitulos/'
    subtitlePath = subtitleFolder + nombreSinFormato + '.srt'
    return subtitlePath

def generar_aleatorio(path_new, duracion):
    if(random.randint(1,2) ==1):
        generate_thumbnail(path_new, 'captura.png', duracion)
        return 'captura.png'
    else:
        generate_gif(path_new, 'captura.gif', duracion)
        return 'captura.gif'