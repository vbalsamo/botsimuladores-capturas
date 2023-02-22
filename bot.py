import tweepy
from tweepy import OAuthHandler
import os
import random
import subprocess

consumerKey = os.environ['API_KEY']
consumerSecret = os.environ['API_KEY_SECRET']
accessKey = os.environ['ACCESS_TOKEN']
accessSecret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth)

def generate_thumbnail(in_filename, out_filename, duracion):
    timess = random.uniform(1, duracion)
    os.system(f"ffmpeg -ss {timess} -copyts -i {in_filename} -vf subtitles={nombreSubtitulos(in_filename)} -vframes 1 {out_filename}")

def generate_gif(in_filename, out_filename, duracion):
    timess = random.uniform(1, duracion) #select random timestamp from video
    os.system(f'ffmpeg -ss {timess} -t 3 -i {in_filename} -vf "subtitles={nombreSubtitulos(in_filename)},fps=10,scale=600:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 {out_filename}')

def get_length(input_video):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_video], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return float(result.stdout)

def nombreSubtitulos(filename):
    nombreSinFormato = (filename.split('.')[0]).split('/')[-1]
    subtitleFolder = 'subtitulos/'
    subtitlePath = subtitleFolder + nombreSinFormato + '.srt'
    return subtitlePath

def post_frame():
    path = 'capitulos/'

    files = os.listdir(path)
    path_new = path +str(files[0])

    duracion = get_length(path_new)

    captura = ''

    #if(random.randint(1,2) ==1):
    #    captura = 'captura.png'
    #    generate_thumbnail(path_new, captura, duracion)
    #else:
    #    captura = 'captura.gif'
    #    generate_gif(path_new, captura, duracion)
    captura = 'captura.gif'
    generate_gif(path_new, captura, duracion)

    media = api.media_upload(captura)

    api.update_status(status = '', media_ids=[media.media_id]) #tweet screenshot

    os.remove(captura) #remove screenshot

print("Twitteando captura...")
post_frame()
print("Captura twitteada")
