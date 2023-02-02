import gdown
import random
import os

class Capitulo:
  def __init__(self, nombre, url):
    self.nombre = nombre
    self.url = url

c1 = Capitulo('T1C01.mp4', os.environ['LINK_C1'])
c2 = Capitulo('T1C02.mp4', os.environ['LINK_C2'])
c3 = Capitulo('T1C03.mp4', os.environ['LINK_C3'])
c4 = Capitulo('T1C04.mp4', os.environ['LINK_C4'])
c5 = Capitulo('T1C05.mp4', os.environ['LINK_C5'])
c6 = Capitulo('T1C06.mp4', os.environ['LINK_C6'])
c7 = Capitulo('T1C07.mp4', os.environ['LINK_C7'])
c8 = Capitulo('T1C08.mp4', os.environ['LINK_C8'])
c9 = Capitulo('T1C09.mp4', os.environ['LINK_C9'])
c10 = Capitulo('T1C10.mp4', os.environ['LINK_C10'])
c11 = Capitulo('T1C11.mp4', os.environ['LINK_C11'])
c12 = Capitulo('T1C12.mp4', os.environ['LINK_C12'])
c13 = Capitulo('T1C13.mp4', os.environ['LINK_C13'])
c14 = Capitulo('T2C01.mp4', os.environ['LINK_C14'])
c15 = Capitulo('T2C02.mp4', os.environ['LINK_C15'])
c16 = Capitulo('T2C03.mp4', os.environ['LINK_C16'])
c17 = Capitulo('T2C04.mp4', os.environ['LINK_C17'])
c18 = Capitulo('T2C05.mp4', os.environ['LINK_C18'])
c19 = Capitulo('T2C06.mp4', os.environ['LINK_C19'])
c20 = Capitulo('T2C07.mp4', os.environ['LINK_C20'])
c21 = Capitulo('T2C08.mp4', os.environ['LINK_C21'])
c22 = Capitulo('T2C09.mp4', os.environ['LINK_C22'])
c23 = Capitulo('T2C10.mp4', os.environ['LINK_C23'])
c24 = Capitulo('T2C11.mp4', os.environ['LINK_C24'])

capitulos = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24]

def descargar_capitulo():
    capitulo = random.choice(capitulos)
    url = capitulo.url
    output = 'capitulos/' + capitulo.nombre
    gdown.download(url, output, quiet=False)

descargar_capitulo()
