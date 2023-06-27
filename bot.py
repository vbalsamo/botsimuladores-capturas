from tweepy import OAuthHandler
import os
from descargar_capitulo import descargar_capitulo
from auth import client_v1
from auth import client_v2
from media import get_length, generar_aleatorio

def post_frame():
    descargar_capitulo()

    path = 'capitulos/'
    files = os.listdir(path)
    path_new = path +str(files[0])

    duracion = get_length(path_new)
    captura = generar_aleatorio(path_new, duracion)

    media_path = captura
    media = client_v1.media_upload(filename=media_path)
    media_id = media.media_id

    client_v2.create_tweet(text="", media_ids=[media_id])
    
    #media = api.media_upload(captura)
    #api.update_status(status = '', media_ids=[media.media_id])
    os.remove(captura)

print("Twitteando captura...")
post_frame()
print("Captura twitteada")
