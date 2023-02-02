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

def generate_thumbnail(in_filename, out_filename, timess):
    os.system(f"ffmpeg -ss {timess} -copyts -i {in_filename} -vf subtitles={nombreSubtitulos(in_filename)} -vframes 1 {out_filename}")

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

    frame_seq = random.uniform(2, duracion) #select random timestamp from video

    generate_thumbnail(path_new, 'captura.png', frame_seq) #generate screenshot

    media = api.media_upload('captura.png')

    #api.update_status(status = '', media_ids=[media.media_id]) #tweet screenshot

    os.remove('captura.png') #remove screenshot

print("Twitteando captura...")
post_frame()
print("Captura twitteada")
