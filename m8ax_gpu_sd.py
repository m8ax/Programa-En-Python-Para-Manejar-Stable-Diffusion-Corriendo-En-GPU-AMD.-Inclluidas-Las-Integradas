##################################################################################################################################################################################################################################
#
# Programa En Python Creado Por MARCOS OCHOA DIEZ - M8AX - MvIiIaX - http://youtube.com/m8ax - https://oncyber.io/@m8ax
# Programa Para Crear Imágenes Mediante Stable Diffusion, Una Inteligencia Artificial Generadora De Imágenes, Mediante GPU AMD, En El Caso De Este Programa En Python...
# En Mi Caso Lo He Probado En La GPU Integrada Del Propio AMD RYZEN 4800H Y Consigue Multiplicar La Velocidad Por 2.45, Con Respecto A Usar La CPU, Para La Generación De Imágenes Y No Es Cualquier CPU... 🤣 
#
# Ejemplo 1 - py m8ax_gpu_sd.py --help
#
#             Muestra Los Comandos Que Se Pueden Añadir En La Linea De Comandos...
#
# Ejemplo 2 - py m8ax_gpu_sd.py -p "red monster with hat"
#
#             Crea Imágen De 512X512 Con 25 Pasos Por Defecto, Escala Por Defecto También A 7.5, Semilla Aleatoria Y Crea Solo Una Imágen...
#
# Ejemplo 3 - py m8ax_gpu_sd.py -p "red monster with hat" -w 512 -h 512 -st 20 -g 7 -s 5000000 -c 5
#
#             Crea 5 Imágenes De 512X512 Con 20 Pasos, Escala A 7, 5000000 De Semillas... Al Añadir El Comando -c 5, Las Semillas Seran En Cada Imágen Aleatorias Aunque Esté Una Especificada... -c 5 = Crear 5 Imágenes.
#             Al Crear Varias Imágenes Si Los Valores De -st y -g Están Especificados, Solo Las Semillas Serán Aleatorias Y Si No Están Especificados, Serán Los De Por Defecto, Salvo Un Caso Concreto...
#             Si -st Es 0, Steps Seran Aleatorios De 20 A 125. Si -g Es 0, Escala Será Aleatoria De 6.5 A 20.5.
#             Si -c Es 0, Se Crearán Solo 10 Imágenes, Cualquiero Otro Número Generará La Cantidad Indicada De Imágenes, No Especificar El Comando, Solo Creará Una Imágen...
#
# ATENCIÓN... 8 NUEVAS OPCIONES BRUTALES:
#                                           ///// NOTA IMPORTANTE --- -p ".....", Ya No Es Obligatorio, A No Ser Que Queramos, Ya Que Con Otras Opciones De La Línea De Comandos Podemos Generar Prompts, Si No Usamos Ningun Prompt
#                                           Ni Usamos La Opción -wo, Ni La Opción -fp, Entonces Sí Que Deberemos Usar -p ".....", Para Que Nos Genere Lo Que Nosotros Queramos, Si Aún Asi No La Usamos El Programa No Explotará
#                                           Sino Que Usará Un Prompt Ya Definido Por Mí. \\\\\       
#
#
#
#     
#                                          
#                                           1.  Opción -f 5 Por Ejemplo... Creará Al Finalizar, Un Video Con Todas Las Imágenes Generadas, Usando El Codec x264 Formato MP4 Y Un FrameRate De 5 Imágenes Por Segundo...
#
#                                           2.  Opción -wo "Tom Cruise" O -wo "Monster With Black Nose" O -wo "Trees", Buscará En LeXica Art Dicho Parámetro Y Cogerá Un Prompt Aleatorio, Tanto Si Estamos Creando Solo Una
#                                               Imágen Como Varias A La Vez. Si Estamos Creando 500 Cada Una De Ellas Tendra Un Prompt Diferente Pero Con Referencia Al Parametro -wo Que Hemos Puesto. ¿ Mola No ?...                                     
#                                               Si Vamos A Usar Esta Opcion -wo Podemos Usar La Opción -p "hola", Ya Que Es Obligatorio Ponerla... Pero Asi No Tendremos Que Escribir El Prompt Entero, Ya Que Vamos A Usar
#                                               La Opcion -wo En Este Caso... Si Lo Que Queremos Es Un Prompt Específico Indicado Por Nosotros, Entonces No Tendremos Que Usar La Opcion -wo Y La Opción -p Tendrá Que Tener Un
#                                               "Prompt Detallado", Ya Sabeis - p "Detalles De Prompt"... Espero Que Sea Fácil De Entender...
#
#                                           3.  Opción -j Para, Activarla -j 1, Para No Usarla... No Ponerla Y Ya Está... Esta Opción Lo Único Que Hace, Es Usar Unas Semillas "seed", Entre Imágen E Imágen, Que Varian Muy Poco, Con El Fin
#                                               De Que Las Imágenes Que Se Vayan Generando... Cambien Entre Si En Alguna Cosita, Pero No Mucho, Con La Meta De Que Si Ponemos La Opcion -f 25 Y Creamos Las Sufucientes Imagenes, Como Para
#                                               Que El Video Dure Unos 5 Segundos... Estamos Hablando De 125 Imágenes... Pueden Salir Cosas Chulas... Pero Ya Os Digo Que Es Experimental... Pero Lo Mismo Hace Cosas Guapas...
#
#                                           4.  Opción -z Para Activarla -z 1, Para No Usarla... No Ponerla Y Ya Está... Si Está Activada, Al Finalizar Todos Los Procesos De Generación De Imágenes, Se Creará Un Fichero 7Z, Con Todo.
#
#                                           5.  Opción -t Para Activarla -t 1, Para No Usarla... No Ponerla Y Ya Está... Si Está Activado, Se Habilitará El Modo TTA Para Escalar La Imágen x4, Mucho Más Lento, Pero Más Calidad.
#                                               Si No Usamos Esta Opción La Imágen También Se Escalará x4, Pero Con Una Calidad Menor, Pero Aún Así, De Bastante Más Calidad Que Cualquier Escalado Normal...
#                                               Requiere De https://github.com/nihui/realsr-ncnn-vulkan/releases Para Que Funcione Este Programa De Python.
#                                               No TTA - os.system("E:\\M8AX-AmD_Stable_Diffusion_AmD-M8AX\\Real-ESRGAN\\realesrgan-ncnn-vulkan.exe -i Fin.PnG -o Fin-2.png -n realesrgan-x4plus -v -j 2:16:4")
#                                               Si TTA - os.system("E:\\M8AX-AmD_Stable_Diffusion_AmD-M8AX\\Real-ESRGAN\\realesrgan-ncnn-vulkan.exe -i Fin.PnG -o Fin-2.png -n realesrgan-x4plus -v -x -j 2:16:4")
#                                            
#                                           6.  -fp "Archivo.txt", Archivo.txt Puede Ser Cualquier Fichero De Texto, También Una Ruta, Lo Indicaremos En La Línea De Comandos, Como Todos Los Anteriores. En Archivo.txt, Meteremos Un Prompt Por Línea
#                                               Puede Servirnos Para, Crear Videos Con El Comando -f 25, Recordad 25, Son Los FPS Que Queramos Que Tenga El Video Generado. A Lo Que Iba, Puede Servirnos Para Meter En El Fichero De Texto
#                                               Un Prompt Por Linea, Como Si Estuviéramos Describiendo Una Película O Una Historieta Con Ligeros Cambios En Cada Linea De Promts Y A ver Que Sale De Ahí... Esta Opción Intenta Hacer Algo
#                                               Parecido A La Opcion -j Pero Creo Que Con Mejores Resultados, Ni La He Probado Aún... Confío... xD... Al Incluir Esta Opción En La Línea De Comandos, Solo Funcionaran, Aunque Esten Otros
#                                               Comandos... El Comando -w, -h, El Propio -fp, -f, -z, -t ( Si -fx 1 ), -bw Y -fx. Los Demás Comandos Quedarán Anulados... El Propio Programa Generará Semillas, Escala, Pasos, Etc...
#
#                                           7.  -fx 1, Activará La Opción De Multiplicar La Resolución x4 Usando RealEsrgan, Si Esta Opción No Está Puesta A 1, La Opción -t 1, No Tendrá Efecto, Porque Para Ampliar La Imágen, No Usaremos
#                                               RealEsrgan, Sino Que Usaremos Un Metodo Más Rápido Pero De Menor Calidad. Si No Usamos La Opción -fx 1, La Opción Por Defecto Será No Usar RealEsrgan Para El Escalado...
# 
#                                           8.  -bw 1, Activará La Salida De Imágenes En Blanco Y Negro, También El Video. 
#
#
#
#
# EJEMPLOS:
#                                           1.  py m8ax_gpu_sd.py -p "red monster" -w 256 -h 256 -st 0 -g 0 -s 50000 -c 100 -f 5 -wo "amd cpu" -j 1
#
#                                               -p "red monster" Se Anula, Porque Hemos Añadido -wo "amd cpu" Y Esta Opción, Nos Genera Prompts Aleatorios Que Tengan Que Ver Con "amd cpu". ( REQUIERE INTERNET LA OPCIÓN -wo )
#                                               Para La Busqueda De Prompts. Sino Usamos Dicha Opción, Podemos Quitar Internet... xD...
#                                               -w y -h A 256 Creará Cada Imágen Con Una Resolución De 256X256. -st A 0, En Cada Imágen Generada Se Usará Steps Aleatorios De 20 A 125... Es Decir, Una Imágen Puede Crearse Con
#                                               20 Steps Y Otra Con 45. La Opción -g a 0, Más De Lo Mismo Pero En Este Caso Los Valores Aleatorios, Se Tomarán Desde 6.5 A 20.5. -g Es Escala. -S 50000, Semillas Anuladas, Porque En La Opción
#                                               -c Hemos Puesto 100 Y Como Es Más De Una Imágen, Entonces Usaremos Un Seed Diferente, Para Que Las Imágenes No Se Parezcan Mucho... Pero Como Hemos Puesto La Opción -j A 1, Estamos
#                                               A Su Vez Indicando Que No Queremos Mucha Variación En Los Seed, Porque Queremos Hacer Un Video De Las Imágenes Generadas Y Queremos Que Se Parezcan Algo Las Imágenes Para Hacer Un Video
#                                               Porque La Opción -f Está A 5 Y Esto Indica Que Queremos Hacer Un Video A 5 Fps De Las 100 Imágenes -c 100... Espero Que Se Entienda Lo Que He Explicado...
#
#                                           2.  py m8ax_gpu_sd.py -p "red monster" -st 15 -g 7 -s 50000 -f 5
#
#                                               Creará Una Imágen Con El Prompt Red Monster Con 15 Pasos, Escala 7, 50000 Semillas Y Al Final Creará Un Video De La Imágen A 5 Fps.. Lo Cuál Es Una Tonteria... La Opción -f Está
#                                               Pensada Para Cuando Generemos Más Imágenes.
#
#                                           3.  py m8ax_gpu_sd.py -p "red monster" -wo "Julia Roberts" -c 100 -j 1 -f 25
#
#                                               Todos Los Parámetros Por Defecto 512x512, Steps 25, Escala 7.5 Y Semillas Seed, Aleatorias... Crea Una Imágen Con Un Prompt De Lexica Art, Que Tenga Que Ver Con Julia Robets. Red Monster
#                                               Queda Anulado...
#                                           
#                                           4.  py m8ax_gpu_sd.py -p "red monster" -c 200 -f 5
#
#                                               200 Imágenes De 512x512 Con Escala A 7.5, Steps A 25 Y Semillas Aleatorias.
#
#                                           5.  py m8ax_gpu_sd.py -p "red monster" -st 20 -g 0 -s 5000 -bw 1
#
#                                               Crea Una Imágen Calculada Mediante 20 Pasos, Con Escala Aleatoria, 5000 Semillas, En Blanco Y Negro, Con El Tema Red Monster Y De 512x512 De Resolución...
#							  
#                                           6.  py m8ax_gpu_sd.py -w 512 -h 512 -fp "Fichero.txt" -f 25 -t 1 -z 1 -fx 1
#                                               Genera Un Video A 25 Fps De 2048x2048, Ya Que Siempre Multiplicamos La Resolución x4, Con RealEsrgan En Este Caso, -fx 1, Con El Contenido Del Fichero De Texto, Un Prompt Por Línea, Que Tengamos En El Fichero
#                                               Fichero.txt, Recordad... Un Prompt Por Línea Y Además Usará La Opción TTA De Escalado, Más Lento... -t 1 Y Cuando Todo Finalize Lo Comprimirá Todo En Un Fichero 7z, Listo Para Transportar
#                                               Y Enseñar A Los Colegas...	
#
#
#
#
#
#                                           ESPERO QUE CON ESTOS EJEMPLOS, SE ENTIENDA BIEN EL FUNCIONAMIENTO DE ESTE PROGRAMA...
#                    
#
#
# NOTAS IMPORTANTES:      
#
#                                           - El Programa En El Directorio De Trabajo, Donde Crea Las Imágenes Y Demás También Crea Un Fichero TXT Con Los Prompts Usados En Cada Imágen, El Ritmo De Generación De Imágenes Por
#                                             Hora, Minuto Y Segundo, Etc...
#
#                                           - Al Finalizar Todo El Trabajo, Si Hemos Indicado En La Línea De Comandos, Que Queremos Un Video... El Video Se Reproducirá Al Terminar El Proceso De Forma Automática Y En Modo Loop.
#
#                                           - Como Nota, En Mi Portátil, Que Lleva Un Ryzen 4800h Con La GPU Integrada, La GPU Genera Imágenes De 512x512 Con 25 Steps Por Imágen A Un Ritmo De 29.5 Imágenes Por Hora... Y La CPU Con
#                                             Sus 8 Cores Del Ryzen 4800h A Pleno Rendimiento... 12 Imágenes Por Hora, Por Lo Que Estamos Hablando De 2.45X Más Rápido. No Está Mal...
#                                              
#                                           Las Líneas De Código:
#
#                                           - os.mkdir('M8AX-Imágenes_Finales')
#                                           - os.chdir ('E:\\M8AX-AmD_Stable_Diffusion_AmD-M8AX\\M8AX-Imágenes_Finales')
#                                           - fichero='E:\M8AX-AmD_Stable_Diffusion_AmD-M8AX\M8AX-Imágenes_Finales\Sesión --- '+creadire+'\Sesión --- '+creadire +'.TxT'
#                                           - os.chdir ('E:\\M8AX-AmD_Stable_Diffusion_AmD-M8AX\\M8AX-Imágenes_Finales\\Sesión --- '+creadire)
#                                           - os.system("E:\\M8AX-AmD_Stable_Diffusion_AmD-M8AX\\Real-ESRGAN\\realesrgan-ncnn-vulkan.exe -i Fin.PnG -o Fin-2.png -n realesrgan-x4plus -v -j 2:16:4")
#                                           - os.system("E:\\M8AX-AmD_Stable_Diffusion_AmD-M8AX\\Real-ESRGAN\\realesrgan-ncnn-vulkan.exe -i Fin.PnG -o Fin-2.png -n realesrgan-x4plus -v -x -j 2:16:4") 
#                                           - with py7zr.SevenZipFile('E:\M8AX-AmD_Stable_Diffusion_AmD-M8AX\M8AX-Imágenes_Finales\Sesión --- '+creadire+'.7z', 'w') as archive:
#                                           - archive.writeall('E:\M8AX-AmD_Stable_Diffusion_AmD-M8AX\M8AX-Imágenes_Finales\Sesión --- '+creadire, 'Sesión --- '+creadire)
#                                           - sizeff = get_file_size('E:\M8AX-AmD_Stable_Diffusion_AmD-M8AX\M8AX-Imágenes_Finales\Sesión --- '+creadire+'.7z', SIZE_UNIT.MB)
# 
#                                           - Podeis Cambiarlas A Los Directorios Que Useis Vosotros, Pero Mantened La Secuencia Con Vuestros Directorios. Además Os Recomiendo Cambiarlas Porque Sino... No Os Funcionará.
#                                             Creo Que Eso No Necesita Explicación Alguna... ¡¡¡ A Disfrutar !!!
#
##################################################################################################################################################################################################################################
#                                                                                       
#                                                                                           By M8AX On December 11 2022 20:00h
#                                                                                         Programado En Ryzen 4800H Con 32Gb RAM
#
##################################################################################################################################################################################################################################

from os import remove
from PIL import Image, ImageChops, ImageEnhance, ImageOps
from diffusers import StableDiffusionOnnxPipeline
from datetime import datetime, timedelta
from shutil import rmtree
from os import rmdir
import os
import errno
import time
import math
import click
import numpy as np
import cv2
import py7zr
import enum
import glob
import requests
import pandas as pd

@click.command()
@click.option("-p", "--prompt", required=False, type=str)
@click.option("-fp", "--filepro", required=False, type=str)
@click.option("-w", "--width", required=False, type=int, default=512)
@click.option("-h", "--height", required=False, type=int, default=512)
@click.option("-st", "--steps", required=False, type=int, default=25)
@click.option("-g", "--guidance-scale", required=False, type=float, default=7.5)
@click.option("-s", "--seed", required=False, type=int, default=None)
@click.option("-c", "--cuan", required=False, type=int, default=None)
@click.option("-f", "--fps", required=False, type=float, default=None)
@click.option("-wo", "--word", required=False, type=str)
@click.option("-j", "--pseed", required=False, type=int, default=None)
@click.option("-z", "--zip", required=False, type=int, default=None)
@click.option("-fx", "--reales", required=False, type=int, default=None)
@click.option("-t", "--tta", required=False, type=int, default=None)
@click.option("-bw", "--blane", required=False, type=int, default=None)

def run(
    prompt: str, 
    filepro: str,
    word: str,
    width: int, 
    pseed: int,
    blane: int,
    zip: int,
    reales: int,
    tta: int,
    height: int, 
    steps: int, 
    cuan: int,
    fps: int,
    guidance_scale: float, 
    seed: int):

    pipe = StableDiffusionOnnxPipeline.from_pretrained(
        "./stable_diffusion_onnx", 
        provider="DmlExecutionProvider"
    )        

    pipe.safety_checker = lambda images, **kwargs: (images, [False] * len(images))
    fps= 0 if fps is None else fps
    zip= 0 if zip is None else zip
    pseed= 0 if pseed is None else pseed
    reales= 0 if reales is None else reales
    blane= 0 if blane is None else blane
    tta= 0 if tta is None else tta
    word= "" if word is None else word
    prompt= "a gorgeous female, photo of scarlett johansson by helmut newton, realistic, smooth face, perfect eyes, symmetrical, full body shot, wide angle, sharp focus, 8 k high definition, insanely detailed, intricate, elegant, art by greg rutkowski" if prompt is None else prompt
    filepro= "" if filepro is None else filepro
    seed = np.random.randint(np.iinfo(np.int32).max) if seed is None else seed
    latents = get_latents_from_seed(seed, width, height)
    cuan = 1 if cuan is None else cuan
    creadire=time.strftime("%d_%m_%y")+'-'+time.strftime("%H_%M_%S")

    try:
      os.mkdir('M8AX-Imágenes_Finales')
    except OSError as e:
      if e.errno != errno.EEXIST:
        raise

    xsteps=5
    xguidance_scale=5

    if steps==0:
         xsteps=1

    if guidance_scale==0:
         xguidance_scale=1

    if cuan==0:
         cuan=10

    num_images = 0;
    iniciot = time.time()

    wwidth=width*4
    hheight=height*4
    tamano=0
    
    salidav = []

    try:
       with open(filepro) as file:
         lineas = file.readlines()
         for linea in lineas:
           salidav.append (linea.strip('\n'))
         file.close()
         tamalista=len(salidav)
         cuan=tamalista
         steps=steps=np.random.randint(20, 125)
         seed = np.random.randint(np.iinfo(np.int32).max) 
         latents = get_latents_from_seed(seed, width, height)
         guidance_scale=math.floor(np.random.uniform(low=6.5, high=20.5, size=(1,1))*10)/10
         num_images=0
    except:
       salidav= []
       filepro=""
       tamalista=0

    os.chdir ('E:\\M8AX-AmD_Stable_Diffusion_AmD-M8AX\\M8AX-Imágenes_Finales')
    fichero='E:\M8AX-AmD_Stable_Diffusion_AmD-M8AX\M8AX-Imágenes_Finales\Sesión --- '+creadire+'\Sesión --- '+creadire +'.TxT'
    gorko=np.random.randint(999999999, 2147483647 )

    try:
      os.mkdir('Sesión --- '+creadire)
    except OSError as e:
      if e.errno != errno.EEXIST:
        raise
    
    os.chdir ('E:\\M8AX-AmD_Stable_Diffusion_AmD-M8AX\\M8AX-Imágenes_Finales\\Sesión --- '+creadire)

    with open(fichero, 'a') as file:
       file.write("----------------------------\n")
       file.write("Sesión --- "+time.strftime("%d_%m_%y")+"-"+time.strftime("%H_%M_%S")+"\n")
       file.write("----------------------------\n")
       file.close()

    while (num_images < cuan):

      if tamalista==0:
         if word != "":
            s = requests.Session()
            try:
              r = s.get( 'https://lexica.art/api/v1/search?q='+word)
              df = pd.json_normalize(r.json()['images'])
              longi=np.random.randint(len(df))
              prompt=df.prompt[longi]
            except:
              prompt=word
         if cuan>1:
            seed = np.random.randint(np.iinfo(np.int32).max) 
            latents = get_latents_from_seed(seed, width, height)
         if (pseed==1 and cuan>1):
            seed=np.random.randint(gorko,(gorko+(cuan*3)))
         if xsteps==1:
            steps=np.random.randint(20, 125)
         if xguidance_scale==1:
            guidance_scale=math.floor(np.random.uniform(low=6.5, high=20.5, size=(1,1))*10)/10
         inicio = time.time()
         num_images=num_images+1
         print(f"\n--- PROMPT ---> {num_images} ---\n\n{prompt}")
         print(f"\nUsando {seed}, Semillas Para La Generación De La Imágen...\n")

      if tamalista>0:
         inicio = time.time()
         prompt=salidav[num_images]
         num_images=num_images+1
         print(f"\n--- PROMPT ---\n\n{prompt}")
         print(f"\nUsando {seed}, Semillas Para La Generación De La Imágen...\n")

      image = pipe(prompt, height=height, width=width, num_inference_steps=steps, guidance_scale=guidance_scale, latents=latents).images[0]
      print(f"")
      image.save("Salida.PnG",'png')

      if blane==0:
         image = Image.open("Salida.PnG")
         image = ImageEnhance.Sharpness(image).enhance(2)
         image.save("Fin.PnG",'png')
      if blane>0:
          image = Image.open("Salida.PnG")
          image = image.convert('L')
          image.save("FinBN.PnG",'png')
          image = Image.open("FinBN.PnG")
          image = ImageEnhance.Sharpness(image).enhance(3)
          image.save("Fin.PnG",'png')
      nombreimg=time.strftime("%d_%m_%y")+"-"+time.strftime("%H_%M_%S") +"---Res-"+str(width)+" x "+str(height)+"__Steps-"+str(steps)+"__GScale-"+str(guidance_scale)+"__Seed-"+str(seed)+"__Cuan-"+str(cuan)+"__Fps-"+str(fps)+"__Word-"+str(word)+"__FinalResNum-"+str(wwidth)+ ' x '+str(hheight)+'-----'+str(num_images)+'.PnG'
      if reales==1:
        if tta==0:
           print(f"Multiplicando Por 4, La Resolución De La Imágen Final... Resolución Final --- {wwidth} x {hheight}. Metodo - ((( RealESRGAN-X4Plus MODO NO TTA ))).\n")
           os.system("E:\\M8AX-AmD_Stable_Diffusion_AmD-M8AX\\Real-ESRGAN\\realesrgan-ncnn-vulkan.exe -i Fin.PnG -o Fin-2.png -n realesrgan-x4plus -v -j 2:16:4")
        if tta>0:
           print(f"Multiplicando Por 4, La Resolución De La Imágen Final... Resolución Final --- {wwidth} x {hheight}. Metodo - ((( RealESRGAN-X4Plus MODO TTA ))).\n")
           os.system("E:\\M8AX-AmD_Stable_Diffusion_AmD-M8AX\\Real-ESRGAN\\realesrgan-ncnn-vulkan.exe -i Fin.PnG -o Fin-2.png -n realesrgan-x4plus -v -x -j 2:16:4")
      if reales==0:
           print(f"Multiplicando Por 4, La Resolución De La Imágen Final... Resolución Final --- {wwidth} x {hheight}. Metodo - ((( NORMAL - RÁPIDO ))).")
           image = Image.open('Fin.PnG')
           image = image.resize((wwidth,hheight))
           image.save("Fin-2.PnG")
      os.rename("Fin-2.png", nombreimg)
      remove("Salida.PnG")
      remove("Fin.PnG")
      if blane>0:
         remove("FinBN.PnG") 
      sizefile = get_file_size(nombreimg, SIZE_UNIT.MB)
      tamano=tamano+sizefile
      fin = time.time()
      cuantotarda=(fin-inicio)*(cuan-num_images)
      todoloquetarda=segahms(cuantotarda)
      en1hora=(3600*num_images)/(fin-iniciot)
      convertidoo=segahms(fin-iniciot)
      print(f"\nNombre De Fichero Resultante:\n\n{nombreimg}")
      print(f"\nTamaño Del Fichero PNG - ((( {sizefile} MB. )))")
      print(f"\nTotal De MB Ocupados Que Llevamos En {num_images} Imágenes Generadas - ((( {tamano} MB. ))). Aún Quedan Por Generar {cuan-num_images} Imágenes...")
      print(f"\nFin De Generación De Imágen. Tiempo De Cálculo - {fin-inicio} Segundos...")
      print(f"\nRitmo De Generación De Imágenes Por Hora - {en1hora} Imágenes/Hora...")
      print(f"\nRitmo De Generación De Imágenes Por Min - {(60*num_images)/(fin-iniciot)} Imágenes/Min...")
      print(f"\nRitmo De Generación De Imágenes Por Seg - {(num_images)/(fin-iniciot)} Imágenes/Seg...")
      print(f"\n--- Tiempo Total De Cálculo Intensivo De GPU --- {convertidoo}")
      print(f"\n--- Tiempo +/- Que Queda, Para Finalizar Todo El Trabajo --- {todoloquetarda}")
      print(f"\n---------------------------------------------------------------------------------------------------------------------------------------")
      with open(fichero, 'a') as file:
         file.write("\n--- PROMPT ---\n\n"+str(prompt)+"\n\nNombre De Fichero Resultante: "+str(nombreimg)+ "\n\nTamaño Del Fichero PNG - ((( "+str(sizefile)+" MB. )))"+"\n\nFin De Generación De Imágen. Tiempo De Cálculo - "+str(fin-inicio)+" Segundos...\n\nRitmo De Generación De Imágenes Por Hora - "+str(en1hora)+" Imágenes/Hora...\n\nRitmo De Generación De Imágenes Por Min - "+str((60*num_images)/(fin-iniciot))+" Imágenes/Min...\n\n"+"Ritmo De Generación De Imágenes Por Seg - "+str((num_images)/(fin-iniciot))+" Imágenes/Seg...")
         file.write("\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
         file.close()

    if fps>0:
      print(f"\nGenerando Video Con {cuan} Imágenes, A Una Resolución De {wwidth} x {hheight}, Con Un FrameRate De {fps} Fps. ( FORMATO MP4 )...\n")
      frameSize = (wwidth, hheight)
      out = cv2.VideoWriter('Sesion De Video - '+str (cuan)+' Imagenes - '+str(fps)+' Fps - '+str(cuan/fps)+' Frames --- '+creadire +'.Mp4',cv2.VideoWriter_fourcc(*'h265'), fps, frameSize)
      for filename in glob.glob("*.png"):
        img = cv2.imread(filename)
        out.write(img)
        print(f"\n{filename}")
      out.release()
      print(f"\nTamaño De Todas Las Imágenes Generadas - ((( {tamano} MB. )))")
      print(f"\nVideo Realizado Con {cuan} Imágenes, A Una Resolución De {wwidth} x {hheight}, Con Un FrameRate De {fps} Fps. ( FORMATO MP4 )...")
      print(f"\nNombre Del Fichero De Video - "+"Sesion De Video - "+str(cuan)+" Imagenes - "+str(fps)+" Fps - "+str(cuan/fps)+" Frames --- "+creadire +".Mp4")
      fint = time.time()
      tiempot=fint-iniciot
      convertido=segahms(tiempot)
      sizefile = get_file_size('Sesion De Video - '+str (cuan)+' Imagenes - '+str(fps)+' Fps - '+str(cuan/fps)+' Frames --- '+creadire +'.Mp4', SIZE_UNIT.MB)
      tamano=tamano+sizefile
      print(f"\nTamaño Del Video MP4 - ((( {sizefile} MB. )))")
      print(f"\nTamaño De Todas Las Imágenes Generadas + El Video MP4 - ((( {tamano} MB. )))")
      with open(fichero, 'a') as file:
         file.write("\nVideo Realizado Con "+str(cuan)+" Imágenes Con Un FrameRate De "+str(fps)+" Fps. ( FORMATO MP4 )...\n")
         file.write("\nNombre Del Fichero De Video - "+"Sesion De Video - "+str(cuan)+" Imagenes - "+str(fps)+" Fps - "+str(cuan/fps)+" Frames --- "+creadire +".Mp4\n")
         file.write("\nTamaño Del Video MP4 - ((( "+str(sizefile)+" MB. )))\n")
         file.close()

    if fps==0:
       fint = time.time()
       tiempot=fint-iniciot
       convertido=segahms(tiempot)
       print(f"\nTamaño De Todas Las Imágenes Generadas - ((( {tamano} MB. )))")
       with open(fichero, 'a') as file:
           file.write("\nFin De Generación De "+str(cuan)+" Imágenes. Tiempo Total De Cálculo Intensivo De GPU - "+str(tiempot)+" Segundos...\n\n"+"Tamaño Total De Imágenes Creadas "+str(tamano)+" MB.\n\n"+"Tiempo Total De Cálculo Intensivo De GPU --- "+str(convertido)+"\n\nBy M8AX - http://youtube.com/m8ax - https://oncyber.io/m8ax\n\nPodeis Suscribiros, No Me Enfadaré... xD")
           file.write("\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
           file.close()

    if fps>0:
       with open(fichero, 'a') as file:
           file.write("\nFin De Generación De "+str(cuan)+" Imágenes. Tiempo Total De Cálculo Intensivo De GPU - "+str(tiempot)+" Segundos...\n\n"+"Tamaño Total De Imágenes Creadas + Video MP4 "+str(tamano)+" MB.\n\n"+"Tiempo Total De Cálculo Intensivo De GPU --- "+str(convertido)+"\n\nBy M8AX - http://youtube.com/m8ax - https://oncyber.io/m8ax\n\nPodeis Suscribiros, No Me Enfadaré... xD")
           file.write("\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
           file.close()

    if zip>0:
       with open(fichero, 'a') as file:
          file.write("\n\nFichero - ((( Sesión --- "+str(creadire)+".7z ))) Creado.")
          file.write("\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
          file.close()
       with py7zr.SevenZipFile('E:\M8AX-AmD_Stable_Diffusion_AmD-M8AX\M8AX-Imágenes_Finales\Sesión --- '+creadire+'.7z', 'w') as archive:
          archive.writeall('E:\M8AX-AmD_Stable_Diffusion_AmD-M8AX\M8AX-Imágenes_Finales\Sesión --- '+creadire, 'Sesión --- '+creadire)
       sizeff = get_file_size('E:\M8AX-AmD_Stable_Diffusion_AmD-M8AX\M8AX-Imágenes_Finales\Sesión --- '+creadire+'.7z', SIZE_UNIT.MB)
       print(f"\nFichero - Sesión --- {creadire}.7z Creado. Tamaño Del Fichero 7z - ((( {sizeff} MB. )))")
       with open(fichero, 'a') as file:
          file.write("\n\nTamaño Del Fichero 7z - ((( "+str(sizeff)+" MB. )))")
          file.write("\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
          file.close()

    print(f"\nFin De Generación De {cuan} Imágenes. Tiempo Total De Cálculo Intensivo De GPU - {tiempot} Segundos...\n\nTiempo Total De Cálculo Intensivo De GPU --- {convertido}\n\nBy M8AX - http://youtube.com/m8ax - https://oncyber.io/m8ax\n\nPodeis Suscribiros, No Me Enfadaré... xD") 
    
    if fps>0:   
      while True:
         isclosed=0
         cap = cv2.VideoCapture("Sesion De Video - "+str(cuan)+" Imagenes - "+str(fps)+" Fps - "+str(cuan/fps)+" Frames --- "+creadire +".Mp4")
         while (True):
            ret, frame = cap.read()
            if ret == True:
               cv2.imshow('frame',frame)
               if cv2.waitKey(1) == 27:
                  isclosed=1
                  break
            else:
               break
         if isclosed:
           break
      cap.release()
      cv2.destroyAllWindows()

class SIZE_UNIT(enum.Enum):
   BYTES = 1
   KB = 2
   MB = 3
   GB = 4

def get_latents_from_seed(seed: int, width: int, height:int) -> np.ndarray:
    latents_shape = (1, 4, height // 8, width // 8)
    rng = np.random.default_rng(seed)
    image_latents = rng.standard_normal(latents_shape).astype(np.float32)
    return image_latents

def segahms(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60
    return f"{horas}h:{minutos}m:{int(segundos)}s"

def convert_unit(size_in_bytes, unit):
    if unit == SIZE_UNIT.KB:
        return size_in_bytes/1024
    elif unit == SIZE_UNIT.MB:
        return size_in_bytes/(1024*1024)
    elif unit == SIZE_UNIT.GB:
        return size_in_bytes/(1024*1024*1024)
    else:
        return size_in_bytes

def get_file_size(file_name, size_type = SIZE_UNIT.BYTES ):
    size = os.path.getsize(file_name)
    return convert_unit(size, size_type)

if __name__ == '__main__':
    run()