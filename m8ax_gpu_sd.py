##################################################################################################################################################################################################################################
#
# Programa En Python Creado Por MARCOS OCHOA DIEZ - M8AX - MvIiIaX - https://youtube.com/m8ax - https://oncyber.io/@m8ax
# Programa Para Crear Imágenes Mediante Stable Diffusion, Una Inteligencia Artificial Generadora De Imágenes. Las Imágenes Pueden Generarse Mediante GPU AMD, En El Caso De Este Programa En Python O Mediante CPU. -gp 1 = GPU, -gp 0 = CPU. Por Defecto, Se Usará GPU.
# En Mi Caso Lo He Probado En La GPU Integrada Del Propio AMD RYZEN 4800H Y Consigue Multiplicar La Velocidad Por 2.45, Con Respecto A Usar La CPU, Para La Generación De Imágenes Y No Es Cualquier CPU... 🤣
#
# 										     	  --------------------------------------------------------------------------
# 											  ------ Bienvenid@ A Stable Diffusion Para GPU'S AMD, O CPU'S x86-64 ------
# 											  ------ Se Recomiendan 16GB De VRAM O 16GB De RAM Si Sólo Usamos CPU ------
# 											  ------ Resoluciones - 256, 320, 384, 448, 512 576 640 704 768 832   ------
# 											  ------                896, 960, 1024, 1088, 1152, 1216, 1280, Etc.  ------
# 											  ------ Ejemplos: 512x256, 512x512, 512x768, 256x512, 960x1024...    ------
# 											  ------ A Resoluciones Más Altas Más RAM O VRAM Se Necesitará        ------
# 											  ------ Si El Programa Crashea, Posiblemente Sea La Falta De Memoria ------
# 											  --------------------------------------------------------------------------
#                                                                   ------------------YouTube    - https://youtube.com/m8ax-------------------
#                                                                   ------------------My Art NFT - https://oncyber.io/@m8ax-------------------
#                                                                   --------------------------------------------------------------------------
#
# Ejemplo 1 - py m8ax_gpu_sd.py --help
#
#             Muestra Los Comandos Que Se Pueden Añadir En La Linea De Comandos...
#
# Ejemplo 2 - py m8ax_gpu_sd.py -p "red monster with hat" -np "low quality"
#
#             Crea Imágen De 512X512 Con 25 Pasos Por Defecto, Escala Por Defecto También A 7.5, Semilla Aleatoria Y Crea Solo Una Imágen... Imágen Que Concuerde Con -p Y -np. Buscar Negative Prompt Y Prompt En Google, Para Más Información.
#
# Ejemplo 3 - py m8ax_gpu_sd.py -p "red monster with hat" -w 512 -h 512 -st 20 -g 7 -s 5000000 -c 5
#
#             Crea 5 Imágenes De 512X512 Con 20 Pasos, Escala A 7, 5000000 De Semillas... Al Añadir El Comando -c 5, Las Semillas Seran En Cada Imágen Aleatorias Aunque Esté Una Especificada... -c 5 = Crear 5 Imágenes.
#             Al Crear Varias Imágenes Si Los Valores De -st y -g Están Especificados, Solo Las Semillas Serán Aleatorias Y Si No Están Especificados, Serán Los De Por Defecto, Salvo Un Caso Concreto...
#             Si -st Es 0, Steps Seran Aleatorios De 20 A 125. Si -g Es 0, Escala Será Aleatoria De 6.5 A 20.5.
#             Si -c Es 0, Se Crearán Solo 10 Imágenes, Cualquiero Otro Número Generará La Cantidad Indicada De Imágenes, No Especificar El Comando, Solo Creará Una Imágen...
#
# ATENCIÓN... 17 NUEVAS OPCIONES BRUTALES:
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
#                                               "Prompt Detallado", Ya Sabeis -p "Detalles De Prompt"... Espero Que Sea Fácil De Entender...
#
#                                           3.  Opción -j Para, Activarla -j 1, Para No Usarla... No Ponerla Y Ya Está... Esta Opción Lo Único Que Hace, Es Usar Unas Semillas "seed", Entre Imágen E Imágen, Que Varian Muy Poco, Con El Fin
#                                               De Que Las Imágenes Que Se Vayan Generando... Cambien Entre Si En Alguna Cosita, Pero No Mucho, Con La Meta De Que Si Ponemos La Opcion -f 25 Y Creamos Las Sufucientes Imagenes, Como Para
#                                               Que El Video Dure Unos 5 Segundos... Estamos Hablando De 125 Imágenes... Pueden Salir Cosas Chulas... Pero Ya Os Digo Que Es Experimental... Pero Lo Mismo Hace Cosas Guapas...
#
#                                           4.  Opción -z Para Activarla -z 1, Para No Usarla... No Ponerla Y Ya Está... Si Está Activada, Al Finalizar Todos Los Procesos De Generación De Imágenes, Se Creará Un Fichero 7Z, Con Todo.
#
#                                           5.  Opción -t Para Activarla -t 1, Para No Usarla... No Ponerla Y Ya Está... Si Está Activado, Se Habilitará El Modo TTA Para Escalar La Imágen x4, Mucho Más Lento, Pero Más Calidad.
#                                               Si No Usamos Esta Opción La Imágen También Se Escalará x4, Pero Con Una Calidad Menor, Pero Aún Así, De Bastante Más Calidad Que Cualquier Escalado Normal... -fx Debe Estar A 1 Para
#                                               Que -t 1, Tenga Efecto. De Lo Contrario, Se Hará El Escalado x4 Rápido Y De Menos Calidad.
#                                               Requiere De https://github.com/nihui/realsr-ncnn-vulkan/releases Para Que Funcione Este Programa De Python. Más Abajo, En Notas Importantes, Teneis Instrucciones Sobre En Que Directorio Grabarlo
#                                               Para Que Todo Fluya Correctamente. Versión Probada En Este Programa, La Release 20220728.
#
#                                               . if os.path.isfile("..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe"): - Comprueba Si Existe realsr-ncnn-vulkan.exe
#                                               . os.system(f"..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i BenchCPU.PnG -o 4X-BenchCPU.png -v -m models-DF2K -g -1 -j 8:16:8") - Escala Imágen x4 Usando CPU
#                                               . os.system("..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i BenchGPU.PnG -o 4X-BenchGPU.png -v -m models-DF2K -j 8:16:8") - Escala Imágen x4 Usando GPU
#                                               . if os.path.isfile("..\\..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe"): - Comprueba Si Existe realsr-ncnn-vulkan.exe
#                                               . os.system("..\\..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i Fin.PnG -o Fin-2.png -m models-DF2K -v -j 8:16:8") - Escala Imágen x4, Usando GPU
#                                               . os.system("..\\..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i Fin.PnG -o Fin-2.png -m models-DF2K -g -1 -v -j 8:16:8") - Escala Imágen x4, Usando CPU
#                                               . os.system("..\\..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i Fin.PnG -o Fin-2.png -m models-DF2K -v -x -j 8:16:8") - Escala Imágen x4, Modo TTA, Usando GPU
#                                               . os.system("..\\..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i Fin.PnG -o Fin-2.png -m models-DF2K -g -1 -v -x -j 8:16:8") - Escala Imágen x4, Modo TTA, Usando CPU
#
#                                           6.  -fp "Archivo.txt", Archivo.txt Puede Ser Cualquier Fichero De Texto, También Una Ruta, Lo Indicaremos En La Línea De Comandos, Como Todos Los Anteriores. En Archivo.txt, Meteremos Un Prompt Por Línea
#                                               Puede Servirnos Para, Crear Videos Con El Comando -f 25, Recordad 25, Son Los FPS Que Queramos Que Tenga El Video Generado. A Lo Que Iba, Puede Servirnos Para Meter En El Fichero De Texto
#                                               Un Prompt Por Linea, Como Si Estuviéramos Describiendo Una Película O Una Historieta Con Ligeros Cambios En Cada Linea De Promts Y A ver Que Sale De Ahí... Esta Opción Intenta Hacer Algo
#                                               Parecido A La Opcion -j Pero Creo Que Con Mejores Resultados, Ni La He Probado Aún... Confío... xD... Al Incluir Esta Opción En La Línea De Comandos, Solo Funcionaran, Aunque Esten Otros
#                                               Comandos... El Comando -w, -h, El Propio -fp, -f, -z, -t ( Si -fx 1 ), -bw, -fx, -ei, -mt, -tl, -ts, -co Y -gp. Los Demás Comandos Quedarán Anulados... El Propio Programa Generará Semillas, Escala, Pasos, Etc...
#
#                                           7.  -fx 1, Activará La Opción De Multiplicar La Resolución x4 Usando RealEsrgan, Si Esta Opción No Está Puesta A 1, La Opción -t 1, No Tendrá Efecto, Porque Para Ampliar La Imágen, No Usaremos
#                                               RealEsrgan, Sino Que Usaremos Un Metodo Más Rápido Pero De Menor Calidad. Si No Usamos La Opción -fx 1, La Opción Por Defecto Será No Usar RealEsrgan Para El Escalado...
#
#                                           8.  -bw 1, Activará La Salida De Imágenes En Blanco Y Negro, También El Video.
#
#                                           9.  -ei 1, Al Terminar De Generar Una Imágen, La Mostrará En Pantalla, Además También Nos Mostrará Los 10 Colores Predominantes En La Imágen Y El HistoGrama. Así Con Todas. Si Esta Opción
#                                               Está Habilitada, Al Finalizar Todo, Nos Preguntará Si Queremos Hacer Un Video Con La Propia Imágen + Predominancia De Color + HistoGrama, De Todas Las Imágenes Que Hemos Generado En La Sesión.
#
#                                           10. -mt "Texto No Muy Largo +/- 10 Caracteres", En Cada Imágen, Incluiremos El Texto Indicado, En La Parte Inferior Izquierda, Con El Color Del Texto Aleatorio En Cada Imágen.
#
#                                           11. -gp 1, La Generación De La Imágen Estará A Cargo De La GPU. -gp 0, La Generación De La Imágen Estará A Cargo De La CPU, Más Lento. Por Defecto, Si No Usamos Este Comando, Se Usará La GPU.
#
#                                           12. -bm 1, Hace Un BenchMark. Primero Genera Una Imágen Con La CPU Y Luego Con La GPU, Con Los Mismos Pasos, Semillas, Prompt, Etc... Y Nos Dice El Tiempo De Cálculo Tanto De La CPU, Como De La GPU
#                                               Así Como Alguna Que Otra Estadística Más. -bm 1, No Necesita Ningún Parámetro Más, Ya Que Está Preconfgurado Ya, Con Un Prompt, Semillas, Pasos, Etc...
#
#                                           13. -sc 0, -sc 1, -sc 2, -sc 3, -sc 4, -sc 5, -sc 6. Selecciona El Algoritmo De Cálculo De La Imágen. 0=ddpm, 1=ddim, 2=pndm, 3=lms, 4=euler_anc, 5=euler, 6=dpm.
#                                               Información - https://huggingface.co/docs/diffusers/index
#
#                                           14. -tl 1, Activará La Creación De Un TimeLapse, Con Esta Opción Activada, El Programa Creará Una Captura De Pantalla Cada 5 Segundos Y Cuando Todo El Proceso De Creación De Imágenes Termine
#                                               Creará Un Video A 20 Fps Con Todas Las Capturas... Más O Menos Unas 720 Capturas Por Hora, +/- 36 Segundos De Video Por Hora A 20 Fps.
#                                               Los Fps Del Video Se Pueden Cambiar Modificando La Variable fpstimlap, Y Los Segundos Entre Capturas, Modificando La Variable esperatimel.
#                                               No Se Creará Ningun TimeLapse Si -bm 1, Si BenchMark Está Activado... No Hay TimeLapse.
#
#                                           15. -co 1, Activará La Salida De Consola A Fichero De Texto M8AX-Log-Fecha-Hora.LoG, El Cuál Se Grabará En El Directorio Raíz De Nuestro Virtual Environment. Por Defecto Está Desactivado.
#
#                                           16. -ts 1, Activara TTS, El Ordenador Nos Dirá A Viva Voz - ( Text To Speech ), Algunos De Los Datos, Que El Programa Vaya Generando, Tiempo Restante Para Acabar, Número De Imágenes Generadas
#                                                Y Cosas Por El Estilo. Por Defecto, Está Desactivado, Para Activarlo, -ts 1. Ralentiza Algo La Generación De Imágenes, Porque Para El Programa, Para Hablar.
#
#                                           17. -ip "1977-50,60,80-0". Formato -ip "Num_ComiEnzo-RGB_Color-Num". Ejemplo: -ip "1-15,120,75-3". Sirve Para Pintar Píxeles Primos En Imágenes, Los Píxeles De La Imágen Comenzarán Por El Número Que Pases
#                                               Con La Opción -ip. Es Decir, Si Le Damos El Número 997, Que Sabemos Que Es Un Número Primo, El Pixel Número 1 De La Imágen Estara Pintado, El Siguiente No, Porque Sería El 998 Y 998 No Es Primo...
#                                               El Color RGB, Cada Color Separado Por Una , Y El Último Número... Si Es 0, Número De Comienzo, El Especificado Y El Color También. Si Ponemos 1, El Número Será El Especificado Y El Color Aleatorio, Pero Todos Iguales En Color.
#                                               Si 2, Número Aleatorio Y Colores Aleatorios, Cada Pixel Primo De Un Color. Si 3, Número Aleatorio Y Colores También. Si 4, Número Aleatorio, Pero Respeta El Color Que Hemos Puesto Nosotros.
#                                               Si 5, Número Aleatorio Y Color Aleatorio, Pero Todos El Mismo Color En Cada Imágen. Si 6, Número Especificado Y Color También, Pero Nos Añadirá También, En Color Amarillo, Los Píxeles Que Correspondan A Números Primos Gemelos...
#                                               Obviamente... Empezando Desde El Número Que Nosotros Le Hemos Indicado... Así Que Habrá Que Elegir Un Color Diferente Al Amarillo, Para Poder Distinguirlos Correctamente.
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
#                                               20 Steps Y Otra Con 45. La Opción -g a 0, Más De Lo Mismo Pero En Este Caso Los Valores Aleatorios, Se Tomarán Desde 6.5 A 20.5. -g Es Escala. -s 50000, Semillas Anuladas, Porque En La Opción
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
#                                               Queda Anulado... También Hara Un Video A 25 Fps, Con Las Imágenes Generadas.
#
#                                           4.  py m8ax_gpu_sd.py -p "red monster" -c 200 -f 5 -tl 1
#
#                                               200 Imágenes De 512x512 Con Escala A 7.5, Steps A 25 Y Semillas Aleatorias. Hará Un Video A 5 Fps, Con Las Imágenes Generadas Y También Hará Un TimeLapse Con Todo El Proceso De Cálculo. Una Captura Cada 5s Y Al Terminar Hará El Video
#                                               A 20 Fps, El Cuál Se Grabará En M8AX-Imágenes_Finales\Sesion --- Fecha-Hora.
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
#                                           7.  py m8ax_gpu_sd.py -wo "portrait" -ei 1 -mt "m8ax" -gp 0 -sc 1 -co 1
#                                               Generará Una Imágen Con Un Prompt Sacado De Lexica Art, Que Contenga La Palabra Portrait, De 512 x 512, Con 25 Pasos, 7.5 De Escala Y Semillas Aleatorias Y Además En La Parte Inferior Izquierda
#                                               Incrustará En La Imágen El Texto m8ax Con Un Color Aleatorio. Usará La CPU Y No La GPU, Para La Generación De La Imágen Y El Algoritmo De Generación DDIM Y Como -co 1, Toda La Salida De La Consola
#                                               Se Grabará En Un Fichero De Texto.
#
#                                           8.  py m8ax_gpu_sd.py -bm 1 -ts 1
#                                               Hará Un BenchMark Tanto En CPU, Como En GPU Y Presentará Resultados... La Opción -bm 1 Si La Ponemos Anulará Todas Las Que Esten Puestas... Se Ejecutará Solo El BenchMark. Bueno, -ts 1 Se Puede
#                                               Poner Y Nos Dirá Por Voz Alguna Cosilla.
#
#                                           9.  py m8ax_gpu_sd.py -w 512 -h 768 -gp 0 -p "a detailed portrait" -c 5 -ip "1977-25,175,90-0"
#                                               Generará 5 Imágenes A Una Resolución De 512 X 768, Usando La CPU Con El Prompt "a detailed portrait". Como La Opción -ip, Esta Puesta, A Cada Imágen Generada, Se Le Pintarán Los Píxeles Primos.
#                                               Teniendo En Cuenta Que Le Hemos Pasado El Número 1977 Como Inicio, El Pixel Número 1 En La Imágen, Comenzará Desde 1977 Hasta Que Se Acaben Los Píxeles De La Imágen Y Como Hemos Puesto Un 0
#                                               Al Final Pues Nos Respetará El Número De Inicio Y El Color Para Pintar Los Píxeles Primos Indicado. Teneis Más Ayuda Sobre Este Comando, En Las Opciones Brutales, Punto 17.
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
#                                           - En El Directorio Raíz De Nuestro Virtual Environment Se Creará El Fichero M8AX-PromptS.TxT, En El Cuál Se Irán Grabando Todos Los Prompts, Que Usemos, Tanto Aleatorios Como Nuestros Propios.
#
#                                           - El Directorio De Trabajo Es M8AX-Imágenes_Finales, Se Creará Automáticamente Y Es Ahí, Donde Todo El Trabajo Quedará Grabado, Datos De BenchMark, Imágenes, Videos, Ficheros 7Z, Etc...
#
#                                           - Al Finalizar Todo El Trabajo, Si Hemos Indicado En La Línea De Comandos, Que Queremos Un Video... El Video Se Reproducirá Al Terminar El Proceso De Forma Automática Y En Modo Loop.
#
#                                           - Como Nota, En Mi Portátil, Que Lleva Un Ryzen 4800h Con La GPU Integrada, La GPU Genera Imágenes De 512x512 Con 25 Steps Por Imágen A Un Ritmo De 29.5 Imágenes Por Hora... Y La CPU Con
#                                             Sus 8 Cores Del Ryzen 4800h A Pleno Rendimiento... 12 Imágenes Por Hora, Por Lo Que Estamos Hablando De 2.45X Más Rápido. No Está Mal...
#
#                                           Las Líneas De Código:
#
#                                           - elecciongpu = ('DmlExecutionProvider', {'device_id': 0,})
#
#                                                 . Si Tienes 2 GPUS AMD, Por Ejemplo, La Integrada En La CPU Y Otra Externa Más Potente 0 = GPU Interna 1 = GPU Externa.
#                                                 . Si Tienes Una GPU Interna En La CPU Intel Y Otra Externa AMD, Poner 1.
#                                                 . Si Solo Tienes Una GPU AMD, Dejarlo En 0.
#
#                                           - if os.path.isfile("..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe"): - Comprueba Si Existe realsr-ncnn-vulkan.exe
#                                           - os.system(f"..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i BenchCPU.PnG -o 4X-BenchCPU.png -v -m models-DF2K -g -1 -j 8:16:8") - Escala Imágen x4 Usando CPU
#                                           - os.system("..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i BenchGPU.PnG -o 4X-BenchGPU.png -v -m models-DF2K -j 8:16:8") - Escala Imágen x4 Usando GPU
#                                           - if os.path.isfile("..\\..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe"): - Comprueba Si Existe realsr-ncnn-vulkan.exe
#                                           - os.system("..\\..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i Fin.PnG -o Fin-2.png -m models-DF2K -v -j 8:16:8") - Escala Imágen x4, Usando GPU
#                                           - os.system("..\\..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i Fin.PnG -o Fin-2.png -m models-DF2K -g -1 -v -j 8:16:8") - Escala Imágen x4, Usando CPU
#                                           - os.system("..\\..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i Fin.PnG -o Fin-2.png -m models-DF2K -v -x -j 8:16:8") - Escala Imágen x4, Modo TTA, Usando GPU
#                                           - os.system("..\\..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i Fin.PnG -o Fin-2.png -m models-DF2K -g -1 -v -x -j 8:16:8") - Escala Imágen x4, Modo TTA, Usando CPU
#
#                                                 . Para Poder Activar La Opción De Aumentar El Tamaño De La Imágen Por Cuatro Mediante RealEsrgan, Debereis Descargar
#                                                   Desde Aquí El Programa, https://github.com/nihui/realsr-ncnn-vulkan/releases Y Descomprimirlo En
#                                                   Vuestro Virtual Environment, En El Directorio Principal, En La Carpeta Real-ESRGAN. Versión Probada En Este Programa, La Release 20220728.
#                                                 . Por Defecto Si La Opción -fx No La Usais, No Os Dara Error Y Si La Usais Y No Teneis Descargado RealEsrgan, Tampoco Os Dará Error Y Utilizará
#                                                   Un Escalado x4 Normal De La Imágen, Pero Os Lo Recomiendo, Ya Que La Calidad Del Escalado Es Mucho Mejor Y El BenchMark -bm 1, También Lo Utiliza
#                                                   Para Hacer Un BenchMarkY Más Detallado. De Todas Formas, El Programa Se Puede Usar Perfectamente Sin RealEsrgan, Pero Os Lo Recomiendo...
#
##################################################################################################################################################################################################################################
#
#                                                                                           By M8AX On December 28 2022 00:00h
#
#                                                                                         Programado En Ryzen 4800H Con 32Gb RAM
#
#                                                                                                   KUU G3 PRO Laitnin
#
#                                                                                                   27H De Programación
#
#                                                                                             M A R C O S  O C H O A  D I E Z
#
##################################################################################################################################################################################################################################

from os import remove
from win32api import GetSystemMetrics
from PIL import Image, ImageChops, ImageEnhance, ImageOps
from PIL.PngImagePlugin import PngInfo
from diffusers import OnnxStableDiffusionPipeline
from datetime import datetime, timedelta
from os import rmdir
from shutil import rmtree
from sklearn.cluster import KMeans
from diffusers import (
    DDPMScheduler,
    DDIMScheduler,
    PNDMScheduler,
    LMSDiscreteScheduler,
    EulerDiscreteScheduler,
    EulerAncestralDiscreteScheduler,
    DPMSolverMultistepScheduler,
)

import os
import errno
import time
import qrcode
import curses, random
import climage
import math
import sympy
import click
import multiprocessing
import shutil
import numpy as np
import matplotlib.pyplot as plt
import sys
import cv2
import pyttsx3
import pathlib
import py7zr
import sys
import enum
import glob
import requests
import pandas as pd
import msvcrt
import pyautogui

@click.command()
@click.option(
    "-gp",
    "--gpu",
    required=False,
    type=int,
    default=1,
    help=(
        "Activa O Desactiva El Uso De GPU, Para La Generación De La Imágen. Si 1, Solo"
        " GPU, Si 0, Solo CPU, Más Lento. Valores 1 Ó 0. Ejemplo: -gp 1"
    ),
)
@click.option(
    "-p",
    "--prompt",
    required=False,
    type=str,
    help=(
        "Lo Que Queremos Que Stable Diffusion Nos 'Dibuje'. Ejemplo: Las ' Son Comillas"
        " Shift+2. -p 'Red Car'"
    ),
)
@click.option(
    "-np",
    "--negp",
    required=False,
    type=str,
    help=(
        "Lo Que No Queremos Que Nos 'Dibuje'. Ejemplo: Las ' Son Comillas Shift+2. -np"
        " 'car'"
    ),
)
@click.option(
    "-w",
    "--width",
    required=False,
    type=int,
    default=512,
    help="Ancho De La Imágen En Pixels. Ejemplo: -w 512",
)
@click.option(
    "-h",
    "--height",
    required=False,
    type=int,
    default=512,
    help="Alto De La Imágen En Pixels. Ejemplo: -h 512",
)
@click.option(
    "-sc",
    "--sched",
    required=False,
    type=int,
    default=None,
    help=(
        "Algoritmo A Usar. -sc 0 = ddpm, -sc 1 = ddim, -sc 2 = pndm, -sc 3 = lms, -sc 4"
        " = euler_anc, -sc 5 = euler, -sc 6 = dpm. Ejemplo: -sc 4. Si No Se Pone Este"
        " Parámetro, Por Defecto Se Usará Euler Ancestral, Osea -sc 4"
    ),
)
@click.option(
    "-wo",
    "--word",
    required=False,
    type=str,
    help=(
        "Genera Imágenes Con Prompts Aleatorios De Lexica Art, Le Pasamos Un Texto Y"
        " Busca Prompts En Lexica Art, Que Tengan Que Ver Con El Texto Pasado. Ejemplo:"
        " Las ' Son Comillas Shift+2. -wo 'Kate Mara'"
    ),
)
@click.option(
    "-fp",
    "--filepro",
    required=False,
    type=str,
    help=(
        "Cogerá Los Prompts Desde Un Fichero De Texto. Un Prompt Por Línea. Ejemplo:"
        " Las ' Son Comillas Shift+2. -fp 'Archivo_TXT_Prompts.txt'"
    ),
)
@click.option(
    "-mt",
    "--mtext",
    required=False,
    type=str,
    help=(
        "Incrustaremos En Cada Imágen, En La Parte Inferior Izquierda, Nuestra Marca De"
        " Agua. Ejemplo: Las ' Son Comillas Shift+2. -mt 'M8AX'"
    ),
)
@click.option(
    "-bw",
    "--blane",
    required=False,
    type=int,
    default=None,
    help=(
        "Todas Las Imágenes Generadas Y El Video, Serán En Blanco Y Negro. Valores 1 Ó"
        " 0. Ejemplo: -bw 0"
    ),
)
@click.option(
    "-ip",
    "--impr",
    required=False,
    type=str,
    default="",
    help=(
        "Formato -ip 'Num_ComiEnzo-RGB_Color-Num'. Ejemplo: -ip '1-15,120,75-3'. Sirve"
        " Para Pintar Píxeles Primos En Imágenes, Los Píxeles De La Imágen Comenzarán"
        " Por El Número Que Pases Con La Opción -ip. Es Decir, Si Le Damos El Número"
        " 997, Que Sabemos Que Es Un Número Primo, El Pixel Número 1 De La Imágen"
        " Estara Pintado, El Siguiente No, Porque Sería El 998 Y 998 No Es Primo... El"
        " Color RGB, Cada Color Separado Por Una , Y El Último Número... Si Es 0,"
        " Número De Comienzo, El Especificado Y El Color También. Si Ponemos 1, El"
        " Número Será El Especificado Y El Color Aleatorio, Pero Todos Iguales En"
        " Color. Si 2, Número Aleatorio Y Colores Aleatorios, Cada Pixel Primo De Un"
        " Color. Si 3, Número Aleatorio Y Colores También. Si 4, Número Aleatorio, Pero"
        " Respeta El Color Que Hemos Puesto Nosotros. Si 5, Número Aleatorio Y Color"
        " Aleatorio, Pero Todos El Mismo Color En Cada Imágen. Si 6, Número"
        " Especificado Y Color También, Pero Nos Añadirá También, En Color Amarillo,"
        " Los Píxeles Que Correspondan A Números Primos Gemelos, Obviamente..."
        " Empezando Desde El Número Que Nosotros Le Hemos Indicado... Así Que Habrá Que"
        " Elegir Un Color Diferente Al Amarillo, Para Poder Distinguirlos"
        " Correctamente."
    ),
)
@click.option(
    "-fx",
    "--reales",
    required=False,
    type=int,
    default=None,
    help=(
        "Habilita El Escalado De Imágen X4, Utilizando RealEsrgan. Valores 1 Ó 0."
        " Ejemplo: -fx 0"
    ),
)
@click.option(
    "-t",
    "--tta",
    required=False,
    type=int,
    default=None,
    help=(
        "Habilita El Modo De Escalado De Imágen TTA, Muy Lento, Solo Si -fx 1. Valores"
        " 1 Ó 0. Ejemplo: -t 0"
    ),
)
@click.option(
    "-ei",
    "--mimag",
    required=False,
    type=int,
    default=None,
    help=(
        "Por Cada Imágen Generada, Nos La Muestra JuntO Con La Predominancia De Color Y"
        " Su HistoGrama, Si Valor 1, Si Valor 0, No. Valores 1 Ó 0. Ejemplo: -ei 0"
    ),
)
@click.option(
    "-st",
    "--steps",
    required=False,
    type=int,
    default=25,
    help=(
        "Pasos Para Realizar La Imágen, Cuantos Más, Más Lento, Pero Más Calidad."
        " Ejemplo: -st 25"
    ),
)
@click.option(
    "-g",
    "--guidance-scale",
    required=False,
    type=float,
    default=7.5,
    help=(
        "Cuanto Más Alto, Más Dibujará Lo Que Queremos, Pero Tendrá Menor Calidad."
        " Ejemplo: -g 7.5"
    ),
)
@click.option(
    "-s",
    "--seed",
    required=False,
    type=int,
    default=None,
    help="Semillas Para La Generación De La Imágen. Ejemplo: -s 10031977",
)
@click.option(
    "-j",
    "--pseed",
    required=False,
    type=int,
    default=None,
    help=(
        "Semillas Aleatorias Entre Imágen E Imágen Que Varían Muy Poco. Valores 1 Ó 0."
        " Ejemplo: -j 1"
    ),
)
@click.option(
    "-c",
    "--cuan",
    required=False,
    type=int,
    default=None,
    help="Número De Imágenes Que Queremos. Ejemplo: -c 100",
)
@click.option(
    "-f",
    "--fps",
    required=False,
    type=float,
    default=None,
    help=(
        "Fps Del Video A Generar, Habilita La Creación De Video, Con Las Imágenes."
        " Ejemplo: -f 30"
    ),
)
@click.option(
    "-tl",
    "--tlapse",
    required=False,
    type=int,
    default=None,
    help=(
        "Crea Un TimeLapse, Mediante Capturas De Pantalla, Realizadas Durante La"
        " Generación De Imágenes. Ejemplo: -tl 1"
    ),
)
@click.option(
    "-z",
    "--zip",
    required=False,
    type=int,
    default=None,
    help=(
        "Al Finalizar, Genera Un Fichero 7z, Con Todas Las Imágenes Generadas. Valores"
        " 1 Ó 0. Ejemplo: -z 1"
    ),
)
@click.option(
    "-bm",
    "--bench",
    required=False,
    type=int,
    default=None,
    help=(
        "Hará Un BenchMark, Usando Primero La GPU Y Luego La CPU Y Presentará"
        " Resultados. Ejemplo: -bm 1"
    ),
)
@click.option(
    "-co",
    "--conso",
    required=False,
    type=int,
    default=None,
    help=(
        "Toda La Salida De Consola, Se Grabará En Un Fichero De Texto, En El Directorio"
        " Raiz De Nuestro Virtual Environment. Ejemplo: -co 1"
    ),
)
@click.option(
    "-ts",
    "--hablo",
    required=False,
    type=int,
    default=None,
    help=(
        "El Programa Nos Hablará, ( Text To Speech ), De Algunas Circunstancias Del"
        " Programa, Finalización, Tiempo, Etc... Ralentiza Un Poco, Porque Para El"
        " Programa Para Hablar. Ejemplo: -ts 1"
    ),
)
def run(
    prompt: str,
    filepro: str,
    mtext: str,
    negp: str,
    word: str,
    width: int,
    mimag: int,
    conso: int,
    bench: int,
    pseed: int,
    impr: str,
    blane: int,
    hablo: int,
    tlapse: int,
    gpu: int,
    sched: int,
    zip: int,
    reales: int,
    tta: int,
    height: int,
    steps: int,
    cuan: int,
    fps: int,
    guidance_scale: float,
    seed: int,
):
    os.system("cls")
    if impr != "":
        try:
            impri, colorcete, colaleynum = impr.split(sep="-")
            impri = int(impri)
            colorc1, colorc2, colorc3 = colorcete.split(sep=",")
            colorc1 = int(colorc1)
            colorc2 = int(colorc2)
            colorc3 = int(colorc3)
            colorcete = [colorc3, colorc2, colorc1]
            colaleynum = int(colaleynum)
        except:
            print(
                "\nPor Lo Visto... Has Seleccionado Que En La Imágen, Se Pinten Píxeles"
                " Primos, Pero Lo Has Especificado Mal, Debes Especificar"
                " Así...\nEjemplo: -ip 5-24,56,100-2 Estamos Indicando Que Empiece El"
                " Pixel 1 De La Imágen Como Si Fuera El Número 5 Y Se Pintarán Todos"
                " Los Píxeles Primos\nA Partir Del Número 5, Con El Color RGB 24,56,100"
                " Y El Último 2 Indica Que Obviemos Lo Anterior Y Que Tanto Los"
                " Colores\nDe Los Píxeles Como El Número De Comienzo Del Pixel 1 En"
                " Cada Imágen, Sea Aleatorio. Así Que... Si Queremos Que Se Cumpla Lo"
                " Que Nosotros Queremos, El 2 Del Final, Debe Ser 0.\nOtro Ejemplo: -ip"
                " 1000000000-255,0,0-0 El Pixel 1 De La Imágen Sera El Número"
                " 1000000000, El Segundo... 1000000001 Y Se Pintarán Los\nQue Sean"
                " Primos Y Como Hemos Puesto Al Final Un 0, Pues Se Cumplirá Lo Que"
                " Hemos Dicho, Si Fuera Un 2, El Número De Comienzo\nSerá Aleatorio En"
                " Cada Imágen Generada Y Los Colores De Los Pixeles También.\n\n- NOTA"
                " IMPORTANTE -"
            )
            print(
                "\nEl Número Del Final, Solo Puede Tener Siete Valores, O 0, O 1, O 2,"
                " O 3, O 4, O 5, O 6... Los Voy A Explicar Ahora Con Más Detalle, Para"
                " Que Se Entiendan..."
            )
            print(
                "\nSi Al Final Ponemos Un 0 - El Número De Comienzo, Será El"
                " Especificado Y El Color De Los Píxeles Primos Pintados Será El"
                " Especificado Por Tí."
            )
            print(
                "\nSi Al Final Ponemos Un 1 - El Número De Comienzo, Será El"
                " Especificado, Pero El Color De Los Píxeles, En Cada Imágen Generada"
                " Cambiará, Pero Serán Todos Iguales, Del Mismo Color."
            )
            print(
                "\nSi Al Final Ponemos Un 2 - El Número De Comienzo, Será Aleatorio Y"
                " El Color De Cada Pixel Pintado, También, Así En Todas Las Imágenes"
                " Generadas."
            )
            print(
                "\nSi Al Final Ponemos Un 3 - El Número De Comienzo, Será El"
                " Especificado, Pero El Color De Cada Pixel Pintado Será Aleatorio, Así"
                " En Cada Imágen Generada."
            )
            print(
                "\nSi Al Final Ponemos Un 4 - El Número De Comienzo, Será Aleatorio,"
                " Pero Se Respeta El Color Que Hemos Elegido, Así... Para Todas Las"
                " Imágenes Generadas."
            )
            print(
                "\nSi Al Final Ponemos Un 5 - El Número De Comienzo, Será Aleatorio Y"
                " El Color De Cada Pixel En Cada Imágen Generada Cambiará, Pero En Cada"
                " Imágen Generada, Todos Serán Del Mismo Color."
            )
            print(
                "\nSi Al Final Ponemos Un 6 - El Número De Comienzo, Será El"
                " Especificado Y El Color También, Pero Además... Se Pintarán De Color"
                " Amarillo, Los Píxeles Que Coincidan Con Números Primos Gemelos.\n\nSe"
                " Pintarán De Amarillo, Así Que Procura Elegir Otro Color, Para Pintar"
                " Los Píxeles Primos Y Se Vea La Diferencia..."
            )
            print("\n\n... Espero Que Todo Este Aclarado Y Comprendido ...\n")
            sys.exit(1)
    consolacomentada = ""
    frase1 = ""
    frase2 = ""
    frase2a = ""
    frase3 = ""
    frase4 = ""
    frase5 = ""
    frase6 = ""
    frase7 = ""
    frase8 = ""
    frase9 = ""
    frase10 = ""
    frase11 = ""
    frase12 = ""
    frase13 = ""
    frase14 = ""
    frase15 = ""
    frase16 = ""
    frase17 = ""
    frase18 = ""
    grabo = 0
    despertot = 0
    contandopri = 0
    creadire = time.strftime("%d_%m_%y") + "-" + time.strftime("%H_%M_%S")
    elecciongpu = (
        "DmlExecutionProvider",
        {
            "device_id": 0,
        },
    )
    fps = 0 if fps is None else fps
    zip = 0 if zip is None else zip
    pseed = 0 if pseed is None else pseed
    reales = 0 if reales is None else reales
    blane = 0 if blane is None else blane
    tlapse = 0 if tlapse is None else tlapse
    conso = 0 if conso is None else conso
    sched = 4 if sched is None else sched
    hablo = 0 if hablo is None else hablo
    bench = 0 if bench is None else bench
    mimag = 0 if mimag is None else mimag
    impr = "" if impr is None else impr
    tta = 0 if tta is None else tta
    word = "" if word is None else word
    mtext = "" if mtext is None else mtext
    negp = "" if negp is None else negp
    prompt = (
        "a gorgeous female, photo of scarlett johansson by helmut newton, realistic,"
        " smooth face, perfect eyes, symmetrical, full body shot, wide angle, sharp"
        " focus, 8 k high definition, insanely detailed, intricate, elegant, art by"
        " greg rutkowski"
        if prompt is None
        else prompt
    )
    filepro = "" if filepro is None else filepro
    seed = np.random.randint(np.iinfo(np.int32).max) if seed is None else seed
    latents = get_latents_from_seed(seed, width, height)
    cuan = 1 if cuan is None else cuan
    nn = 1
    sizetm = 0
    tamano2 = 0
    tamano3 = 0
    esperatimel = 5000
    fpstimlap = 20
    proc = multiprocessing.Process(target=capturas, args=(nn, esperatimel, creadire))
    model = "./stable_diffusion_onnx/scheduler"
    ddpm = DDPMScheduler.from_pretrained(model, subfolder="scheduler")
    ddim = DDIMScheduler.from_pretrained(model, subfolder="scheduler")
    pndm = PNDMScheduler.from_pretrained(model, subfolder="scheduler")
    lms = LMSDiscreteScheduler.from_pretrained(model, subfolder="scheduler")
    euler_anc = EulerAncestralDiscreteScheduler.from_pretrained(
        model, subfolder="scheduler"
    )
    euler = EulerDiscreteScheduler.from_pretrained(model, subfolder="scheduler")
    dpm = DPMSolverMultistepScheduler.from_pretrained(model, subfolder="scheduler")
    modocall = [ddpm, ddim, pndm, lms, euler_anc, euler, dpm]
    modocale = [
        "Denoising Diffusion Probabilistic Models",
        "Denoising Diffusion Implicit Models",
        "Pseudo Numerical Methods For Diffusion Models On Manifolds",
        "Least Mean Square Algorithm",
        "Euler Ancestral",
        "Euler",
        "DPM Solver",
    ]
    if sched > 6 or sched < 0:
        sched = 4
    modocal = modocall[sched]
    try:
        rmtree("M8AX-Imágenes_Finales\\M8AX-TimeLapse")
    except:
        cuan = cuan
    try:
        os.mkdir("M8AX-Imágenes_Finales")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir("M8AX-Imágenes_Finales\\M8AX-TimeLapse")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    screen = curses.initscr()
    lwidth = screen.getmaxyx()[1]
    lheight = screen.getmaxyx()[0]
    size = lwidth * lheight
    char = [" ", ".", ":", "^", "*", "x", "s", "S", "#", "$"]
    b = []
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, 0, 0)
    curses.init_pair(2, 1, 0)
    curses.init_pair(3, 3, 0)
    curses.init_pair(4, 4, 0)
    print(
        f"--------------------------------------------------------------------------\n"
    )
    print(
        f"------ Bienvenid@ A Stable Diffusion Para GPU'S AMD, O CPU'S x86-64 ------\n"
    )
    print(
        f"------ Se Recomiendan 16GB De VRAM O 16GB De RAM Si Sólo Usamos CPU ------\n"
    )
    print(
        f"------ Resoluciones - 256, 320, 384, 448, 512 576 640 704 768 832   ------\n"
    )
    print(
        f"------                896, 960, 1024, 1088, 1152, 1216, 1280, Etc.  ------\n"
    )
    print(
        f"------ Ejemplos: 512x256, 512x512, 512x768, 256x512, 960x1024...    ------\n"
    )
    print(
        f"------ A Resoluciones Más Altas Más RAM O VRAM Se Necesitará        ------\n"
    )
    print(
        f"------ Si El Programa Crashea, Posiblemente Sea La Falta De Memoria ------\n"
    )
    print(
        f"--------------------------------------------------------------------------\n"
    )
    print(
        f"------------------YouTube    - https://youtube.com/m8ax-------------------\n"
    )
    print(
        f"------------------My Art NFT - https://oncyber.io/@m8ax-------------------\n"
    )
    print(
        f"--------------------------------------------------------------------------\n"
    )
    print("\x1b[31m... Espera, HAL 9000, Está Pensando ...\n\x1b[0m")
    for i in range(size + lwidth + 1):
        b.append(0)
    colore1 = np.random.randint(1, 10)
    colore2 = np.random.randint(1, 10)
    colore3 = np.random.randint(1, 10)
    while 1:
        for i in range(int(lwidth / 9)):
            b[int((random.random() * lwidth) + lwidth * (lheight - 1))] = 75
        for i in range(size):
            b[i] = int((b[i] + b[i + 1] + b[i + lwidth] + b[i + lwidth + 1]) / 4)
            color = (
                colore1
                if b[i] > 15
                else (colore2 if b[i] > 9 else (colore3 if b[i] > 4 else 1))
            )
            if i < size - 1:
                screen.addstr(
                    int(i / lwidth),
                    i % lwidth,
                    char[(9 if b[i] > 9 else b[i])],
                    curses.color_pair(color) | curses.A_BOLD,
                )
        screen.refresh()
        screen.timeout(3)
        if screen.getch() != -1:
            break
    curses.endwin()
    if hablo == 1:
        dime(
            "Bienvenido Al Generador De Imágenes Mediante Inteligencia Artificial,"
            " Programado Por M 8 A X..."
        )
    color = ("b", "g", "r")
    if conso == 1:
        sys.stdout = open("M8AX-Log-" + creadire + ".LoG", "w", encoding="utf-8")
    if bench == 1:
        prompt = "a gorgeous photo of an astronaut driving a motorcycle on venus"
        negp = "bad hands, blurry, low quality, nude, black and white"
        if hablo == 1:
            dime("Preparando El BenchMark... No Toques Nada Hasta Que Todo Finalice...")
            print("")
        sched = np.random.randint(0, 7)
        modocal = modocall[sched]
        s = requests.Session()
        tiempo1 = time.time()
        try:
            promeleg = np.random.randint(1, 6)
            if promeleg == 1:
                r = s.get(
                    "https://lexica.art/api/v1/search?q="
                    + "hyperrealistic gorgeous detailed face portrait"
                )
            if promeleg == 2:
                r = s.get(
                    "https://lexica.art/api/v1/search?q="
                    + "hyperrealistic gorgeous detailed face portrait goya"
                )
            if promeleg == 3:
                r = s.get(
                    "https://lexica.art/api/v1/search?q="
                    + "hyperrealistic gorgeous detailed face portrait picasso"
                )
            if promeleg == 4:
                r = s.get(
                    "https://lexica.art/api/v1/search?q="
                    + "a hyperrealistic gorgeous nude female photo, professionally"
                    " retouched, insanely detailed, perfect eyes, 8k render"
                )
            if promeleg == 5:
                r = s.get(
                    "https://lexica.art/api/v1/search?q="
                    + "a landscape by simon stalenhag of a very large realistic highly"
                    " detailed imposing robotic mechanical cat"
                )
            df = pd.json_normalize(r.json()["images"])
            longi = np.random.randint(len(df))
            prompt = df.prompt[longi]
        except:
            prompt = prompt
        try:
            with open("M8AX-PromptS.TxT", "r", encoding="utf-8") as file:
                lineas = file.readlines()
                grabo = 0
                for linea in lineas:
                    if prompt == linea.strip("\n"):
                        grabo = grabo + 1
                file.close()
        except:
            grabo = 0
        if grabo == 0:
            with open("M8AX-PromptS.TxT", "a", encoding="utf-8") as filet:
                filet.write(str(prompt) + "\n")
                filet.close()
        todocorrecto = 1
        if conso == 0:
            consolacomentada = (
                "... Comentario De Consola ...\n\nSe Ejecutará Un BenchMark..."
            )
        else:
            consolacomentada = (
                "... Comentario De Consola ...\n\nSe Ejecutará Un BenchMark Y La Salida"
                " De Consola Se Grabará En Un Fichero De Texto, En El Directorio Raíz"
                " De Vuestro Virtual Environment..."
            )
        if hablo == 1:
            consolacomentada = (
                consolacomentada
                + " Además Nos Dirá Por Voz, Como Va El Desarrollo Del BenchMark."
            )
        consolacomandos = (
            "py m8ax_gpu_sd.py"
            + " -gp "
            + str(gpu)
            + " -p "
            + '"'
            + str(prompt)
            + '"'
            + " -np "
            + '"'
            + str(negp)
            + '"'
            + " -w "
            + str(width)
            + " -h "
            + str(height)
            + " -sc "
            + str(sched)
            + " -wo "
            + '"'
            + str(word)
            + '"'
            + " -fp "
            + '"'
            + str(filepro)
            + '"'
            + " -mt "
            + '"'
            + str(mtext)
            + '"'
            + " -bw "
            + str(blane)
            + " -ip "
            + '"'
            + str(impr)
            + '"'
            + " -fx "
            + str(reales)
            + " -t "
            + str(tta)
            + " -ei "
            + str(mimag)
            + " -st "
            + str(steps)
            + " -g "
            + str(guidance_scale)
            + " -s "
            + str(seed)
            + " -j "
            + str(pseed)
            + " -c "
            + str(cuan)
            + " -f "
            + str(fps)
            + " -tl "
            + str(tlapse)
            + " -z "
            + str(zip)
            + " -bm "
            + str(bench)
            + " -co "
            + str(conso)
            + " -ts "
            + str(hablo)
        )
        print(f"{consolacomandos}\n\n{consolacomentada}\n")
        steps = np.random.randint(200, 301)
        width = 512
        height = 512
        seed = np.random.randint(1003197710) + 1003197719770310
        latents = get_latents_from_seed(seed, width, height)
        guidance_scale = (
            math.floor(np.random.uniform(low=4.5, high=20.5, size=(1, 1)) * 10) / 10
        )
        pipe = OnnxStableDiffusionPipeline.from_pretrained(
            "./stable_diffusion_onnx",
            provider="CPUExecutionProvider",
            revision="onnx",
            safety_checker=None,
            scheduler=modocal,
        )
        os.chdir("M8AX-Imágenes_Finales")
        print(f"\nLatents: {latents}\n")
        print(f"Scheduler: {modocal}")
        print(f"Prompt: {prompt}\n")
        print(f"Negative Prompt: {negp}\n")
        print(f"Resolución: 512 x 512\n")
        print(f"Seed: {seed}\n")
        print(f"Steps: {steps}\n")
        print(f"Guidande Scale: {guidance_scale}\n")
        print(
            f"-------------------------------------------NO TOCAR NADA PARA QUE EL"
            f" BENCHMARK SEA MÁS EXACTO------------------------------------------\n"
        )
        print(f"------ BenchMark CPU - ESPERA UN MOMENTO... ------\n")
        if hablo == 1:
            dime("Comienza El BenchMark De Generación De Imágenes En, C, P, U...")
        inicpu = time.time()
        image = pipe(
            prompt, height, width, steps, guidance_scale, negp, latents=latents
        ).images[0]
        fincpu = time.time()
        print(f"")
        if hablo == 1:
            dime(
                "BenchMark De Generación De Imágenes En C, P, U. Terminado. Ahora"
                " Comienza El De G, P, U. Espera..."
            )
        image.save("BenchCPU1.PnG", "png")
        image = cv2.imread("BenchCPU1.PnG")
        ubicacion = (1, height - 2)
        font = cv2.FONT_HERSHEY_PLAIN
        if height < 512:
            tamañoLetra = 0.6
            grosorLetra = 0
        else:
            tamañoLetra = 1.2
            grosorLetra = 2
        colorLetra = (
            np.random.randint(0, 256),
            np.random.randint(0, 256),
            np.random.randint(0, 256),
        )
        cv2.putText(
            image, "- CPU -", ubicacion, font, tamañoLetra, colorLetra, grosorLetra
        )
        cv2.imwrite("BenchCPU.PnG", image)
        remove("BenchCPU1.PnG")
        convcpu = segahms(fincpu - inicpu, hablo)
        print(
            f"Tiempo De Cálculo De CPU - {round(fincpu-inicpu,2)} Segundos -"
            f" {convcpu}\n"
        )
        print(
            f"---------------------------------------------------------------------------------------------------------------------------------------\n"
        )
        cv2.namedWindow("Benchmark CPU 512x512 - " + str(convcpu), cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Benchmark CPU 512x512 - " + str(convcpu), width, height)
        imagencita = cv2.imread("BenchCPU.PnG")
        cv2.imshow("Benchmark CPU 512x512 - " + str(convcpu), imagencita)
        cv2.waitKey(1)
        os.chdir("..")
        pipe = OnnxStableDiffusionPipeline.from_pretrained(
            "./stable_diffusion_onnx",
            provider=elecciongpu,
            revision="onnx",
            safety_checker=None,
            scheduler=modocal,
        )
        os.chdir("M8AX-Imágenes_Finales")
        print(f"\nLatents: {latents}\n")
        print(f"Scheduler: {modocal}")
        print(f"Prompt: {prompt}\n")
        print(f"Negative Prompt: {negp}\n")
        print(f"Resolución: 512 x 512\n")
        print(f"Seed: {seed}\n")
        print(f"Steps: {steps}\n")
        print(f"Guidande Scale: {guidance_scale}\n")
        print(
            f"-------------------------------------------NO TOCAR NADA PARA QUE EL"
            f" BENCHMARK SEA MÁS EXACTO------------------------------------------\n"
        )
        print(f"------ BenchMark GPU - ESPERA UN MOMENTO... ------\n")
        inigpu = time.time()
        image = pipe(
            prompt, height, width, steps, guidance_scale, negp, latents=latents
        ).images[0]
        fingpu = time.time()
        if hablo == 1:
            dime("BenchMark De Generación De Imágenes En G, P, U. Terminado...")
        print(f"")
        image.save("BenchGPU1.PnG", "png")
        image = cv2.imread("BenchGPU1.PnG")
        ubicacion = (1, height - 2)
        font = cv2.FONT_HERSHEY_PLAIN
        if height < 512:
            tamañoLetra = 0.6
            grosorLetra = 0
        else:
            tamañoLetra = 1.2
            grosorLetra = 2
        colorLetra = (
            np.random.randint(0, 256),
            np.random.randint(0, 256),
            np.random.randint(0, 256),
        )
        cv2.putText(
            image, "- GPU -", ubicacion, font, tamañoLetra, colorLetra, grosorLetra
        )
        cv2.imwrite("BenchGPU.PnG", image)
        remove("BenchGPU1.PnG")
        convgpu = segahms(fingpu - inigpu, hablo)
        print(
            f"Tiempo De Cálculo De GPU - {round(fingpu-inigpu,2)} Segundos - {convgpu}"
        )
        print(
            f"\n---------------------------------------------------------------------------------------------------------------------------------------\n"
        )
        print(
            f"Tiempo De Cálculo De CPU - {round(fincpu-inicpu,2)} Segundos -"
            f" {convcpu} - ( +/- {round((fincpu-inicpu)/steps,3)} Seg/Iteración )\n"
        )
        print(
            f"Tiempo De Cálculo De GPU - {round(fingpu-inigpu,2)} Segundos -"
            f" {convgpu} - ( +/- {round((fingpu-inigpu)/steps,3)} Seg/Iteración )"
        )
        print(
            f"\n---------------------------------------------------------------------------------------------------------------------------------------"
        )
        tmpgpu = fingpu - inigpu
        tmpcpu = fincpu - inicpu
        if tmpgpu > tmpcpu:
            resu = tmpgpu / tmpcpu
            pcen = (tmpgpu * 100) / tmpcpu
            print(
                f"\nLa CPU Es {round(resu,2)}x Veces Superior A La GPU, Para La"
                " Generación De Imágenes Mediante Inteligencia Artificial. Por"
                f" Consiguiente La CPU Es Un {round(pcen,2)}% Más Rápida."
            )
            resficpu = (
                "\nLa CPU Es {round(resu,2)}x Veces Superior A La GPU, Para La"
                " Generación De Imágenes Mediante Inteligencia Artificial. Por"
                " Consiguiente La CPU Es Un {round(pcen,2)}% Más Rápida."
            )
        else:
            resu = tmpcpu / tmpgpu
            pcen = (tmpcpu * 100) / tmpgpu
            print(
                f"\nLa GPU Es {round(resu,2)}x Veces Superior A La CPU, Para La"
                " Generación De Imágenes Mediante Inteligencia Artificial. Por"
                f" Consiguiente La GPU Es Un {round(pcen,2)}% Más Rápida."
            )
            resfigpu = (
                "\nLa GPU Es {round(resu,2)}x Veces Superior A La CPU, Para La"
                " Generación De Imágenes Mediante Inteligencia Artificial. Por"
                " Consiguiente La GPU Es Un {round(pcen,2)}% Más Rápida."
            )
        print(
            f"\n---------------------------------------------------------------------------------------------------------------------------------------"
        )
        cv2.namedWindow("Benchmark GPU 512x512 - " + str(convgpu), cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Benchmark GPU 512x512 - " + str(convgpu), width, height)
        imagencita = cv2.imread("BenchGPU.PnG")
        cv2.imshow("Benchmark GPU 512x512 - " + str(convgpu), imagencita)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        img1 = cv2.imread("BenchCPU.png")
        img2 = cv2.imread("BenchGPU.png")
        Hori = np.concatenate((img1, img2), axis=1)
        if tmpgpu > tmpcpu:
            cv2.imshow(
                "La CPU Es "
                + str(round(resu, 2))
                + "x Veces Superior A La GPU, Para La Generacion De Imagenes. La CPU"
                " Es Un "
                + str(round(pcen, 2))
                + "% Mas Rapida",
                Hori,
            )
        else:
            cv2.imshow(
                "La GPU Es "
                + str(round(resu, 2))
                + "x Veces Superior A La CPU, Para La Generacion De Imagenes. La GPU"
                " Es Un "
                + str(round(pcen, 2))
                + "% Mas Rapida",
                Hori,
            )
        cv2.waitKey(1000)
        if os.path.isfile("..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe"):
            todocorrecto = 1
        else:
            todocorrecto = 0
        if todocorrecto == 1:
            if hablo == 1:
                dime(
                    "El BenchMark De Escalado Por 4, Con Real Esrgan, En C, P, U."
                    " Comienza Ahora..."
                )
            print(
                f"\nBenchMark Real-ESRGAN En CPU, Paciencia... Puede Tardar Un Rato. No"
                f" Tocar Nada... ( TÓMATE UN CAFÉ )\n"
            )
            realicpu = time.time()
            os.system(
                f"..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i BenchCPU.PnG -o"
                f" 4X-BenchCPU.png -v -m models-DF2K -g -1 -j 8:16:8"
            )
            realfcpu = time.time()
            realtotalcpu = realfcpu - realicpu
            if hablo == 1:
                dime(
                    "BenchMark De Escalado Por 4, Con Real Esrgan, En C, P, U."
                    " Terminado. Comienza Ahora En G, P, U..."
                )
            print(
                "\nTiempo De Cálculo De CPU Para Escalar Imágenes x4 -"
                f" {round(realtotalcpu,2)} Segundos - {segahms(realtotalcpu,hablo)}"
            )
            print(
                f"\nBenchMark Real-ESRGAN En GPU, Paciencia... Puede Tardar Un Rato. No"
                f" Tocar Nada... ( SERÁ MÁS RÁPIDO QUE CON CPU, TRANQUILOS )\n"
            )
            realigpu = time.time()
            os.system(
                "..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i BenchGPU.PnG -o"
                " 4X-BenchGPU.png -v -m models-DF2K -j 8:16:8"
            )
            realfgpu = time.time()
            realtotalgpu = realfgpu - realigpu
            if hablo == 1:
                dime(
                    "BenchMark De Escalado Por 4, Con Real Esrgan, En G, P, U."
                    " Terminado. Espera..."
                )
            print(
                "\nTiempo De Cálculo De GPU Para Escalar Imágenes x4 -"
                f" {round(realtotalgpu,2)} Segundos - {segahms(realtotalgpu,hablo)}"
            )
            print(
                f"\n***************************************************************************************************************************************"
            )
            if realtotalgpu > realtotalcpu:
                resuu = realtotalgpu / realtotalcpu
                pcenn = (realtotalgpu * 100) / realtotalcpu
                print(
                    f"\nLa CPU Es {round(resuu,2)}x Veces Superior A La GPU, Para El"
                    " Escalado De Imágenes x4, Mediante Real-ESRGAN. Por Consiguiente"
                    f" La CPU Es Un {round(pcenn,2)}% Más Rápida."
                )
                resficpuu = (
                    "\nLa CPU Es {round(resuu,2)}x Veces Superior A La GPU, Para El"
                    " Escalado De Imágenes x4, Mediante Real-ESRGAN. Por Consiguiente"
                    " La CPU Es Un {round(pcenn,2)}% Más Rápida."
                )
                if hablo == 1:
                    dime(
                        "La C P U, Es "
                        + str(round(resuu, 2))
                        + " Veces Superior A La G P U, Para El Escalado De Imágenes Por"
                        " 4, Mediante Real EsrGan. Por Consiguiente La C P U, Es Un "
                        + str(round(pcenn, 2))
                        + "% Más Rápida..."
                    )
            else:
                resuu = realtotalcpu / realtotalgpu
                pcenn = (realtotalcpu * 100) / realtotalgpu
                print(
                    f"\nLa GPU Es {round(resuu,2)}x Veces Superior A La CPU, Para El"
                    " Escalado De Imágenes x4, Mediante Real-ESRGAN. Por Consiguiente"
                    f" La GPU Es Un {round(pcenn,2)}% Más Rápida."
                )
                resfigpuu = (
                    "\nLa GPU Es {round(resuu,2)}x Veces Superior A La CPU, Para El"
                    " Escalado De Imágenes x4, Mediante Real-ESRGAN. Por Consiguiente"
                    " La GPU Es Un {round(pcenn,2)}% Más Rápida."
                )
                if hablo == 1:
                    dime(
                        "La G P U, Es "
                        + str(round(resuu, 2))
                        + " Veces Superior A La C P U, Para El Escalado De Imágenes Por"
                        " 4, Mediante Real EsrGan. Por Consiguiente La G P U, Es Un "
                        + str(round(pcenn, 2))
                        + "% Más Rápida..."
                    )
            print(
                f"\n---------------------------------------------------------------------------------------------------------------------------------------"
            )
            remove("4X-BenchGPU.PnG")
            remove("4X-BenchCPU.PnG")
        if todocorrecto == 1:
            if tmpgpu > tmpcpu:
                resu = tmpgpu / tmpcpu
                pcen = (tmpgpu * 100) / tmpcpu
                print(
                    f"\nLa CPU Es {round(resu,2)}x Veces Superior A La GPU, Para La"
                    " Generación De Imágenes Mediante Inteligencia Artificial. Por"
                    f" Consiguiente La CPU Es Un {round(pcen,2)}% Más Rápida."
                )
                resficpu = (
                    "\nLa CPU Es {round(resu,2)}x Veces Superior A La GPU, Para La"
                    " Generación De Imágenes Mediante Inteligencia Artificial. Por"
                    " Consiguiente La CPU Es Un {round(pcen,2)}% Más Rápida."
                )
                if hablo == 1:
                    dime(
                        "La C P U, Es "
                        + str(round(resu, 2))
                        + " Veces Superior A La G P U, Para La Generación De Imágenes"
                        " Mediante Inteligencia Artificial. Por Consiguiente La C P"
                        " U, Es Un "
                        + str(round(pcen, 2))
                        + "% Más Rápida..."
                    )
            else:
                resu = tmpcpu / tmpgpu
                pcen = (tmpcpu * 100) / tmpgpu
                print(
                    f"\nLa GPU Es {round(resu,2)}x Veces Superior A La CPU, Para La"
                    " Generación De Imágenes Mediante Inteligencia Artificial. Por"
                    f" Consiguiente La GPU Es Un {round(pcen,2)}% Más Rápida."
                )
                resfigpu = (
                    "\nLa GPU Es {round(resu,2)}x Veces Superior A La CPU, Para La"
                    " Generación De Imágenes Mediante Inteligencia Artificial. Por"
                    " Consiguiente La GPU Es Un {round(pcen,2)}% Más Rápida."
                )
                if hablo == 1:
                    dime(
                        "La G P U, Es "
                        + str(round(resu, 2))
                        + " Veces Superior A La C P U, Para La Generación De Imágenes"
                        " Mediante Inteligencia Artificial. Por Consiguiente La G P"
                        " U, Es Un "
                        + str(round(pcen, 2))
                        + "% Más Rápida..."
                    )
        else:
            if tmpgpu > tmpcpu:
                if hablo == 1:
                    dime(
                        "La C P U, Es "
                        + str(round(resu, 2))
                        + " Veces Superior A La G P U, Para La Generación De Imágenes"
                        " Mediante Inteligencia Artificial. Por Consiguiente La C P"
                        " U, Es Un "
                        + str(round(pcen, 2))
                        + "% Más Rápida..."
                    )
            else:
                if hablo == 1:
                    dime(
                        "La G P U, Es "
                        + str(round(resu, 2))
                        + " Veces Superior A La C P U, Para La Generación De Imágenes"
                        " Mediante Inteligencia Artificial. Por Consiguiente La G P"
                        " U, Es Un "
                        + str(round(pcen, 2))
                        + "% Más Rápida..."
                    )
        if todocorrecto == 1:
            print(
                f"\n---------------------------------------------------------------------------------------------------------------------------------------"
            )
        remove("BenchGPU.PnG")
        remove("BenchCPU.PnG")
        creadire = time.strftime("%d_%m_%y") + "-" + time.strftime("%H_%M_%S")
        with open("BenchMark - " + creadire + ".TxT", "w", encoding="utf-8") as file:
            file.write(
                "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n"
            )
            file.write("M8AX - Sesión De BenchMark - " + creadire + " - M8AX")
            file.write("\n\nComandos De Consola - " + str(consolacomandos))
            file.write("\n\n" + consolacomentada)
            file.write(
                "\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n"
            )
            file.write("Latents: " + str(latents) + "\n")
            file.write("\nScheduler: " + str(modocal))
            file.write("\nPrompt: " + str(prompt) + "\n\n")
            file.write("Negative Prompt: " + str(negp) + "\n\n")
            file.write("Resolución: 512 x 512\n\n")
            file.write("Seed: " + str(seed) + "\n\n")
            file.write("Steps: " + str(steps) + "\n\n")
            file.write("Guidande Scale: " + str(guidance_scale) + "\n\n")
            file.write(
                "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n"
            )
            file.write(
                "Tiempo De Cálculo De CPU Para Generación De Imágen - "
                + str(round(fincpu - inicpu, 2))
                + " Segundos - "
                + str(convcpu)
                + " - ( +/- "
                + str(round((fincpu - inicpu) / steps, 3))
                + " Seg/Iteración )\n\n"
            )
            file.write(
                "Tiempo De Cálculo De GPU Para Generación De Imágen - "
                + str(round(fingpu - inigpu, 2))
                + " Segundos - "
                + str(convgpu)
                + " - ( +/- "
                + str(round((fingpu - inigpu) / steps, 3))
                + " Seg/Iteración )\n"
            )
            file.write(
                "\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
            )
            if tmpgpu > tmpcpu:
                resu = tmpgpu / tmpcpu
                pcen = (tmpgpu * 100) / tmpcpu
                resficpu = (
                    "\nLa CPU Es "
                    + str(round(resu, 2))
                    + "x Veces Superior A La GPU, Para La Generación De Imágenes"
                    " Mediante Inteligencia Artificial. Por Consiguiente La CPU"
                    " Es Un "
                    + str(round(pcen, 2))
                    + "% Más Rápida."
                )
                file.write(resficpu)
            else:
                resu = tmpcpu / tmpgpu
                pcen = (tmpcpu * 100) / tmpgpu
                resfigpu = (
                    "\nLa GPU Es "
                    + str(round(resu, 2))
                    + "x Veces Superior A La CPU, Para La Generación De Imágenes"
                    " Mediante Inteligencia Artificial. Por Consiguiente La GPU"
                    " Es Un "
                    + str(round(pcen, 2))
                    + "% Más Rápida."
                )
                file.write(resfigpu)
            file.write(
                "\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
            )
            if todocorrecto == 1:
                file.write(
                    "\n\nTiempo De Cálculo De CPU Para Escalar Imágenes x4 - "
                    + str(round(realtotalcpu, 2))
                    + " Segundos - "
                    + str(segahms(realtotalcpu, hablo))
                )
                file.write(
                    "\n\nTiempo De Cálculo De GPU Para Escalar Imágenes x4 - "
                    + str(round(realtotalgpu, 2))
                    + " Segundos - "
                    + str(segahms(realtotalgpu, hablo))
                )
                file.write(
                    "\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
                )
                if realtotalgpu > realtotalcpu:
                    resuu = realtotalgpu / realtotalcpu
                    pcenn = (realtotalgpu * 100) / realtotalcpu
                    resficpuu = (
                        "\n\nLa CPU Es "
                        + str(round(resuu, 2))
                        + "x Veces Superior A La GPU, Para El Escalado De Imágenes x4,"
                        " Mediante Real-ESRGAN. Por Consiguiente La CPU Es Un "
                        + str(round(pcenn, 2))
                        + "% Más Rápida."
                    )
                    file.write(resficpuu)
                else:
                    resuu = realtotalcpu / realtotalgpu
                    pcenn = (realtotalcpu * 100) / realtotalgpu
                    resfigpuu = (
                        "\n\nLa GPU Es "
                        + str(round(resuu, 2))
                        + "x Veces Superior A La CPU, Para El Escalado De Imágenes x4,"
                        " Mediante Real-ESRGAN. Por Consiguiente La GPU Es Un "
                        + str(round(pcenn, 2))
                        + "% Más Rápida."
                    )
                    file.write(resfigpuu)
                file.write(
                    "\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
                )
            else:
                file.write(
                    "\n\nNo Se Ha Podido Llevar A Cabo La Prueba De Escalado De Imágen"
                    " x4 Mediante Real-ESRGAN, Lee El Principio Del Código Del"
                    " Programa, Para Descargarlo Y Ubicarlo En Su Directorio Correcto."
                    " Por Consiguiente, Los Resultados Del BenchMark De Escalado x4 De"
                    " Imágen, No Se Realizarán, Puedes Descargar El Programa Aquí:"
                    " https://github.com/nihui/realsr-ncnn-vulkan/releases, Versión"
                    " Probada En Este Programa, La Release 20220728. El Ejecutable Y"
                    " Sus Ficheros, Deben Estar Alojados En La Carpeta Real-ESRGAN, En"
                    " El Directorio Raiz, De Tu Virtual Environment..."
                )
                file.write(
                    "\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
                )
            file.close()
        if todocorrecto == 1:
            print(
                "\nTiempo De Cálculo De CPU Para Escalar Imágenes x4 -"
                f" {round(realtotalcpu,2)} Segundos - {segahms(realtotalcpu,hablo)}"
            )
            print(
                "\nTiempo De Cálculo De GPU Para Escalar Imágenes x4 -"
                f" {round(realtotalgpu,2)} Segundos - {segahms(realtotalgpu,hablo)}"
            )
        else:
            if hablo == 1:
                dime(
                    "No Se Ha Podido Llevar A Cabo La Prueba De Escalado De Imágen x4"
                    " Mediante Real-ESRGAN, Lee El Principio Del Código Del Programa,"
                    " Para Descargarlo Y Ubicarlo En Su Directorio Correcto. Por"
                    " Consiguiente, Los Resultados Del BenchMark De Escalado x4 De"
                    " Imágen, No Se Realizarán, Puedes Descargar El Programa Aquí:"
                    " https://github.com/nihui/realsr-ncnn-vulkan/releases, Versión"
                    " Probada En Este Programa, La Release 20220728. El Ejecutable Y"
                    " Sus Ficheros, Deben Estar Alojados En La Carpeta Real-ESRGAN, En"
                    " El Directorio Raiz, De Tu Virtual Environment..."
                )
            print(
                f"\nNo Se Ha Podido Llevar A Cabo La Prueba De Escalado De Imágen x4"
                f" Mediante Real-ESRGAN, Lee El Principio Del Código Del Programa, Para"
                f" Descargarlo Y Ubicarlo En Su Directorio Correcto. Por Consiguiente,"
                f" Los Resultados Del BenchMark De Escalado x4 De Imágen, No Se"
                f" Realizarán, Puedes Descargar El Programa Aquí:"
                f" https://github.com/nihui/realsr-ncnn-vulkan/releases, Versión"
                f" Probada En Este Programa, La Release 20220728. El Ejecutable Y Sus"
                f" Ficheros, Deben Estar Alojados En La Carpeta Real-ESRGAN, En El"
                f" Directorio Raiz, De Tu Virtual Environment..."
            )
            print(
                f"\n---------------------------------------------------------------------------------------------------------------------------------------"
            )
        print(
            "\nTiempo De Cálculo De CPU Para La Generación De Imágen -"
            f" {round(fincpu-inicpu,2)} Segundos - {convcpu} - ( +/-"
            f" {round((fincpu-inicpu)/steps,3)} Seg/Iteración )"
        )
        print(
            "\nTiempo De Cálculo De GPU Para La Generación De Imágen -"
            f" {round(fingpu-inigpu,2)} Segundos - {convgpu} - ( +/-"
            f" {round((fingpu-inigpu)/steps,3)} Seg/Iteración )"
        )
        if todocorrecto == 1:
            print(
                f"\n***************************************************************************************************************************************"
            )
        else:
            print(
                f"\n---------------------------------------------------------------------------------------------------------------------------------------"
            )
        cv2.waitKey(1000)
        screenshot = pyautogui.screenshot()
        screenshot.save("BenchMark.PnG")
        image = cv2.imread("BenchMark.PnG")
        remove("BenchMark.PnG")
        ubicacion = (1, GetSystemMetrics(1) - 2)
        font = cv2.FONT_HERSHEY_PLAIN
        tamañoLetra = 1.2
        grosorLetra = 2
        colorLetra = (
            np.random.randint(0, 256),
            np.random.randint(0, 256),
            np.random.randint(0, 256),
        )
        tiempo2 = time.time()
        fintiempot = tiempo2 - tiempo1
        cv2.putText(
            image,
            "BenchMark - "
            + creadire
            + " - Tiempo Total - "
            + str(segahms(fintiempot, hablo)),
            ubicacion,
            font,
            tamañoLetra,
            colorLetra,
            grosorLetra,
        )
        cv2.imwrite("BenchMark - " + creadire + ".PnG", image)
        im = Image.open("BenchMark - " + creadire + ".PnG")
        im.show()
        if hablo == 1:
            dime(
                "BenchMarks Terminados. Espero Que Estes Conforme, Con La Velocidad De"
                " Tu P C..."
            )
        print(f"\n... Suscríbete A Mi Canal De Youtube - https://youtube.com/m8ax ...")
        if todocorrecto == 1:
            print(
                f"\n***************************************************************************************************************************************"
            )
        else:
            print(
                f"\n---------------------------------------------------------------------------------------------------------------------------------------"
            )
        if conso == 1:
            sys.stdout.close()
        sys.exit(1)
    if tlapse == 1:
        proc.start()
    if gpu == 1:
        pipe = OnnxStableDiffusionPipeline.from_pretrained(
            "./stable_diffusion_onnx",
            provider=elecciongpu,
            revision="onnx",
            safety_checker=None,
            scheduler=modocal,
        )
    else:
        pipe = OnnxStableDiffusionPipeline.from_pretrained(
            "./stable_diffusion_onnx",
            provider="CPUExecutionProvider",
            revision="onnx",
            safety_checker=None,
            scheduler=modocal,
        )
    xsteps = 5
    xguidance_scale = 5
    if steps == 0:
        xsteps = 1
    if guidance_scale == 0:
        xguidance_scale = 1
    if cuan == 0:
        cuan = 10
    num_images = 0
    iniciot = time.time()
    wwidth = width * 4
    hheight = height * 4
    tamano = 0
    tamalista = 0
    creadire2 = (
        "M8AX - Sesion ---> "
        + creadire
        + " - Imagen Generada Grabada A "
        + str(wwidth)
        + " x "
        + str(hheight)
        + ". Esta Ventana - "
        + str(width * 3)
        + " x "
        + str(height)
        + ". - M8AX"
    )
    salidav = []
    try:
        with open(filepro, "r", encoding="utf-8") as file:
            lineas = file.readlines()
            for linea in lineas:
                salidav.append(linea.strip("\n"))
            file.close()
            tamalista = len(salidav)
            cuan = tamalista
            steps = np.random.randint(20, 126)
            seed = np.random.randint(np.iinfo(np.int32).max)
            latents = get_latents_from_seed(seed, width, height)
            guidance_scale = (
                math.floor(np.random.uniform(low=6.5, high=20.5, size=(1, 1)) * 10) / 10
            )
            num_images = 0
    except:
        salidav = []
        filepro = ""
        tamalista = 0
    os.chdir("M8AX-Imágenes_Finales")
    fichero = "Sesión --- " + creadire + ".TxT"
    gorko = np.random.randint(999999999, 2147483647)
    try:
        os.mkdir("Sesión --- " + creadire)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    os.chdir("Sesión --- " + creadire)
    if negp == "":
        pronega = "----- PROMPT NEGATIVO NO UTILIZADO -----"
    else:
        pronega = negp
    while num_images < cuan:
        if tamalista == 0:
            if word != "":
                try:
                    s = requests.Session()
                    r = s.get("https://lexica.art/api/v1/search?q=" + word)
                    df = pd.json_normalize(r.json()["images"])
                    longi = np.random.randint(len(df))
                    prompt = df.prompt[longi]
                except:
                    prompt = word
            if num_images == 0:
                if reales == 1 and tta == 1:
                    frase1 = (
                        "Se Aplicará El Escalado x4 RealEsrgan, Aplicando El Modo"
                        " TTA.\n"
                    )
                if reales == 1 and tta == 0:
                    frase1 = (
                        "Se Aplicará El Escalado x4 RealEsrgan, No Se Aplicará El Modo"
                        " TTA.\n"
                    )
                if reales == 0:
                    frase1 = "Se Aplicará Un Escalado x4 Normal.\n"
                if gpu == 0:
                    frase2 = (
                        "Para Todos Los Cálculos, Se Utilizará La CPU De Tu Ordenador."
                        " Resolución De Imágen "
                        + str(width)
                        + " x "
                        + str(height)
                        + ".\n"
                    )
                else:
                    frase2 = (
                        "Para Todos Los Cálculos, Se Utilizará La GPU De Tu Ordenador."
                        " Resolución De Imágen "
                        + str(width)
                        + " x "
                        + str(height)
                        + ".\n"
                    )
                if negp != "":
                    frase3 = "Se Utilizará Un Negative Prompt: " + str(negp) + ".\n"
                else:
                    frase3 = "No Se Utilizará Ningún Negative Prompt.\n"
                if word != "":
                    frase4 = (
                        "Como Hemos Habilitado La Opción -wo, El Prompt Normal, Si Lo"
                        " Hemos Puesto, No Tendra Efecto Y Creará Un Prompt"
                        " Automáticamente Con La Frase Introducida En -wo, Utilizando"
                        " Lexica Art, Que En Este Caso Es "
                        + str(word)
                        + ".\n"
                    )
                if filepro != "":
                    frase4 = ""
                    frase5 = (
                        "Como Prompt, -fp "
                        + str(filepro)
                        + " Está Fijado, Solo Se Utilizarán Los Prompts Que Tengamos En"
                        " El Fichero De Texto "
                        + str(filepro)
                        + " Que Hemos Indicado. Además... Tanto Los Steps, Semillas,"
                        " Escala, Etc...\nLos Elegirá El Ordenador Aleatoriamente,"
                        " Pero Una Vez Elegidos, Serán Iguales, Para Todas Las Lineas"
                        " Del Fichero TxT, Es Decir, Para Cada Prompt, Del Fichero De"
                        " Texto, Que Por Cierto Tiene "
                        + str(len(salidav))
                        + " Líneas, Con Lo Cuál, Esas Serán Las Imágenes A Generar.\n"
                    )
                if mtext != "":
                    frase6 = (
                        "En Cada Imágen Generada Añadiremos En La Parte Inferior"
                        " Izquierda, El Texto - "
                        + str(mtext)
                        + ".\n"
                    )
                if blane == 1:
                    frase7 = "Las Imágenes Generadas, Serán En Blanco Y Negro.\n"
                if mimag == 1:
                    frase8 = (
                        "Cada Imágen Generada Por La Inteligencia Artificial, La"
                        " Mostrará En Pantalla, Junto Con Los 10 Colores Predominantes"
                        " En La Imágen Y Su HistoGrama.\n"
                    )
                else:
                    frase8 = (
                        "No Se Mostrará La Imágen Generada Por Pantalla, Cuando Acabe"
                        " De Generarla La Intelgencia Artificial.\n"
                    )
                if cuan == 1:
                    if xsteps == 1 and filepro == "":
                        frase9 = (
                            "Se Utilizarán Pasos Aleatorios. De 20 A 125 Y "
                            + str(seed)
                            + " Semillas.\n"
                        )
                    else:
                        if filepro == "":
                            frase9 = (
                                "Para La Generación De Imágen Se Utilizarán Los Pasos"
                                " Indicados, "
                                + str(steps)
                                + " Y "
                                + str(seed)
                                + " Semillas.\n"
                            )
                else:
                    if xsteps == 1 and filepro == "":
                        frase9 = (
                            "Se Utilizarán Pasos Aleatorios. Para La Generación De Cada"
                            " Imágen. De 20 A 125 Y Semillas Aleatorias.\n"
                        )
                    else:
                        if filepro == "":
                            frase9 = (
                                "Para La Generación De Las Imágenes, Se Utilizarán Los"
                                " Pasos Indicados Puestos Por Tí O Por Defecto, "
                                + str(steps)
                                + " Y Semillas Aleatorias...\n"
                            )
                if pseed == 1 and filepro == "":
                    if cuan != 0:
                        frase10 = (
                            "En Cada Imágen Generada Se Usaran Semillas Que Varian Muy"
                            " Poco.\n"
                        )
                if filepro == "":
                    if cuan != 0:
                        frase10 = "Se Crearán " + str(cuan) + " Imágenes.\n"
                    if cuan == 0:
                        frase10 = "Se Crearán 10 Imágenes.\n"
                    if cuan == 1:
                        frase10 = "Se Creará Solo, Una Imágen.\n"
                if fps == 1:
                    frase11 = (
                        "Se Creará Un Video Con Las Imágenes Generadas A "
                        + str(fps)
                        + " Fps.\n"
                    )
                if tlapse == 1:
                    frase12 = (
                        "Se Creará Un Timelapse En Video, Con Las Capturas De Pantalla"
                        " Creadas Automáticamente, Durante El Proceso De Generación De"
                        " Imágenes, A 20 Fps.\n"
                    )
                if zip == 1:
                    frase13 = (
                        "Se Creará Un Fichero 7z, Con Todo El Trabajo Generado En Esta"
                        " Sesión.\n"
                    )
                if impr != "":
                    frase18 = (
                        "Una Vez Escalada La Imágen A x4, Se Pintarán Sobre Ella, Los"
                        " Píxeles Primos Que Hemos Indicado Con El Comando -ip "
                        + str(impr)
                        + "\n"
                    )
                if xguidance_scale == 1 and filepro == "":
                    frase14 = (
                        "Cada Imágen Se Creará Con Una Guidance Scale Aleatoria, De 6.5"
                        " A 20.5.\n"
                    )
                else:
                    if filepro == "":
                        frase14 = (
                            "Cada Imágen Se Creará Con Una Guidance Scale De "
                            + str(guidance_scale)
                            + ".\n"
                        )
                frase16 = "Se Usará El Prompt: " + str(prompt) + ".\n"
                if hablo == 1:
                    frase17 = (
                        "El Programa Usará ( Text To Speech ), Para Decirnos Por Voz,"
                        " Como Va La Generación De Imágenes Y Algunos Otros Datos,"
                        " Usando El Habla.\n"
                    )
                if conso == 1:
                    frase15 = (
                        "Toda La Salida De Consola, Se Grabará En Un Fichero De Texto,"
                        " M8AX-Log-Fecha-Hora.LoG, En El Directorio Raiz De Vuestro"
                        " Virtual Environment.\n"
                    )
                frase2a = (
                    "Se Utilizará El Algoritmo De Cálculo Para La Generación De"
                    " Imágenes, "
                    + str(modocale[sched])
                    + ".\n"
                )
                consolacomentada = (
                    "\n... Comentario De Consola ...\n\n"
                    + frase2
                    + frase2a
                    + frase16
                    + frase3
                    + frase4
                    + frase5
                    + frase6
                    + frase1
                    + frase18
                    + frase7
                    + frase8
                    + frase9
                    + frase14
                    + frase10
                    + frase11
                    + frase12
                    + frase13
                    + frase15
                    + frase17
                )
                consolacomandos = (
                    "py m8ax_gpu_sd.py"
                    + " -gp "
                    + str(gpu)
                    + " -p "
                    + '"'
                    + str(prompt)
                    + '"'
                    + " -np "
                    + '"'
                    + str(negp)
                    + '"'
                    + " -w "
                    + str(width)
                    + " -h "
                    + str(height)
                    + " -sc "
                    + str(sched)
                    + " -wo "
                    + '"'
                    + str(word)
                    + '"'
                    + " -fp "
                    + '"'
                    + str(filepro)
                    + '"'
                    + " -mt "
                    + '"'
                    + str(mtext)
                    + '"'
                    + " -bw "
                    + str(blane)
                    + " -ip "
                    + '"'
                    + str(impr)
                    + '"'
                    + " -fx "
                    + str(reales)
                    + " -t "
                    + str(tta)
                    + " -ei "
                    + str(mimag)
                    + " -st "
                    + str(steps)
                    + " -g "
                    + str(guidance_scale)
                    + " -s "
                    + str(seed)
                    + " -j "
                    + str(pseed)
                    + " -c "
                    + str(cuan)
                    + " -f "
                    + str(fps)
                    + " -tl "
                    + str(tlapse)
                    + " -z "
                    + str(zip)
                    + " -bm "
                    + str(bench)
                    + " -co "
                    + str(conso)
                    + " -ts "
                    + str(hablo)
                )
                print(f"\n{consolacomandos}\n{consolacomentada}")
                with open(fichero, "a", encoding="utf-8") as file:
                    file.write("----------------------------\n")
                    file.write(
                        "Sesión --- "
                        + time.strftime("%d_%m_%y")
                        + "-"
                        + time.strftime("%H_%M_%S")
                        + "\n"
                    )
                    file.write("----------------------------\n")
                    file.write(
                        "\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
                    )
                    file.write(
                        "... Comandos De Consola ...\n\n" + str(consolacomandos) + "\n"
                    )
                    file.write(consolacomentada)
                    file.write(
                        "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
                    )
                    file.close()
            if cuan > 1:
                seed = np.random.randint(np.iinfo(np.int32).max)
                latents = get_latents_from_seed(seed, width, height)
            if pseed == 1 and cuan > 1:
                seed = np.random.randint(gorko, (gorko + (cuan * 3)))
                latents = get_latents_from_seed(seed, width, height)
            if xsteps == 1:
                steps = np.random.randint(20, 126)
            if xguidance_scale == 1:
                guidance_scale = (
                    math.floor(np.random.uniform(low=6.5, high=20.5, size=(1, 1)) * 10)
                    / 10
                )
            num_images = num_images + 1
            print(f"--- Latents ---\n")
            print(f"Se Encuentran En El Fichero TxT De Logs De Sesión.")
            print(f"\n--- Algoritmo De Cálculo - Scheduler ---\n")
            print(f"{modocale[sched]}\n")
            print(f"--- PROMPT ---> {num_images} De {cuan} ---\n\n{prompt}")
            if negp != "":
                print(
                    f"\n--- NEGATIVE PROMPT ---> {num_images} De {cuan} ---\n\n{negp}"
                )
            else:
                print(
                    f"\n--- NEGATIVE PROMPT ---> {num_images} De"
                    f" {cuan} ---\n\n{pronega}"
                )
            print(f"\nUsando {seed}, Semillas Para La Generación De La Imágen...\n")
            if hablo == 1 and num_images == 1:
                dime(consolacomentada)
            inicio = time.time()
        if tamalista > 0:
            prompt = salidav[num_images]
            if num_images == 0:
                if reales == 1 and tta == 1:
                    frase1 = (
                        "Se Aplicará El Escalado x4 RealEsrgan, Aplicando El Modo"
                        " TTA.\n"
                    )
                if reales == 1 and tta == 0:
                    frase1 = (
                        "Se Aplicará El Escalado x4 RealEsrgan, No Se Aplicará El Modo"
                        " TTA.\n"
                    )
                if reales == 0:
                    frase1 = "Se Aplicará Un Escalado x4 Normal.\n"
                if gpu == 0:
                    frase2 = (
                        "Para Todos Los Cálculos, Se Utilizará La CPU De Tu Ordenador."
                        " Resolución De Imágen "
                        + str(width)
                        + " x "
                        + str(height)
                        + ".\n"
                    )
                else:
                    frase2 = (
                        "Para Todos Los Cálculos, Se Utilizará La GPU De Tu Ordenador."
                        " Resolución De Imágen "
                        + str(width)
                        + " x "
                        + str(height)
                        + ".\n"
                    )
                if negp != "":
                    frase3 = "Se Utilizará Un Negative Prompt: " + str(negp) + ".\n"
                else:
                    frase3 = "No Se Utilizará Ningún Negative Prompt.\n"
                if word != "":
                    frase4 = (
                        "Como Hemos Habilitado La Opción -wo, El Prompt Normal, Si Lo"
                        " Hemos Puesto, No Tendra Efecto Y Creará Un Prompt"
                        " Automáticamente Con La Frase Introducida En -wo, Utilizando"
                        " Lexica Art, Que En Este Caso Es "
                        + str(word)
                        + ".\n"
                    )
                if filepro != "":
                    frase4 = ""
                    frase5 = (
                        "Como Prompt, -fp "
                        + str(filepro)
                        + " Está Fijado, Solo Se Utilizarán Los Prompts Que Tengamos En"
                        " El Fichero De Texto "
                        + str(filepro)
                        + " Que Hemos Indicado. Además... Tanto Los Steps, Semillas,"
                        " Escala, Etc...\nLos Elegirá El Ordenador Aleatoriamente,"
                        " Pero Una Vez Elegidos, Serán Iguales, Para Todas Las Lineas"
                        " Del Fichero TxT, Es Decir, Para Cada Prompt, Del Fichero De"
                        " Texto, Que Por Cierto Tiene "
                        + str(len(salidav))
                        + " Líneas, Con Lo Cuál, Esas Serán Las Imágenes A Generar.\n"
                    )
                if mtext != "":
                    frase6 = (
                        "En Cada Imágen Generada Añadiremos En La Parte Inferior"
                        " Izquierda, El Texto - "
                        + str(mtext)
                        + ".\n"
                    )
                if blane == 1:
                    frase7 = "Las Imágenes Generadas, Serán En Blanco Y Negro.\n"
                if mimag == 1:
                    frase8 = (
                        "Cada Imágen Generada Por La Inteligencia Artificial, La"
                        " Mostrará En Pantalla, Junto Con Los 10 Colores Predominantes"
                        " En La Imágen Y Su HistoGrama.\n"
                    )
                else:
                    frase8 = (
                        "No Se Mostrará La Imágen Generada Por Pantalla, Cuando Acabe"
                        " De Generarla La Intelgencia Artificial.\n"
                    )
                if cuan == 1:
                    if xsteps == 1 and filepro == "":
                        frase9 = (
                            "Se Utilizarán Pasos Aleatorios. De 20 A 125 Y "
                            + str(seed)
                            + " Semillas.\n"
                        )
                    else:
                        if filepro == "":
                            frase9 = (
                                "Para La Generación De Imágen Se Utilizarán Los Pasos"
                                " Indicados, "
                                + str(steps)
                                + " Y "
                                + str(seed)
                                + " Semillas.\n"
                            )
                else:
                    if xsteps == 1 and filepro == "":
                        frase9 = (
                            "Se Utilizarán Pasos Aleatorios. Para La Generación De Cada"
                            " Imágen. De 20 A 125 Y Semillas Aleatorias.\n"
                        )
                    else:
                        if filepro == "":
                            frase9 = (
                                "Para La Generación De Las Imágenes, Se Utilizarán Los"
                                " Pasos Indicados Puestos Por Tí O Por Defecto, "
                                + str(steps)
                                + " Y Semillas Aleatorias...\n"
                            )
                if pseed == 1 and filepro == "":
                    if cuan != 0:
                        frase10 = (
                            "En Cada Imágen Generada Se Usaran Semillas Que Varian Muy"
                            " Poco.\n"
                        )
                if filepro == "":
                    if cuan != 0:
                        frase10 = "Se Crearán " + str(cuan) + " Imágenes.\n"
                    if cuan == 0:
                        frase10 = "Se Crearán 10 Imágenes.\n"
                    if cuan == 1:
                        frase10 = "Se Creará Solo, Una Imágen.\n"
                if fps == 1:
                    frase11 = (
                        "Se Creará Un Video Con Las Imágenes Generadas A "
                        + str(fps)
                        + " Fps.\n"
                    )
                if tlapse == 1:
                    frase12 = (
                        "Se Creará Un Timelapse En Video, Con Las Capturas De Pantalla"
                        " Creadas Automáticamente, Durante El Proceso De Generación De"
                        " Imágenes, A 20 Fps.\n"
                    )
                if zip == 1:
                    frase13 = (
                        "Se Creará Un Fichero 7z, Con Todo El Trabajo Generado En Esta"
                        " Sesión.\n"
                    )
                if impr != "":
                    frase18 = (
                        "Una Vez Escalada La Imágen A x4, Se Pintarán Sobre Ella, Los"
                        " Píxeles Primos Que Hemos Indicado Con El Comando -ip "
                        + str(impr)
                        + "\n"
                    )
                if xguidance_scale == 1 and filepro == "":
                    frase14 = (
                        "Cada Imágen Se Creará Con Una Guidance Scale Aleatoria, De 6.5"
                        " A 20.5.\n"
                    )
                else:
                    if filepro == "":
                        frase14 = (
                            "Cada Imágen Se Creará Con Una Guidance Scale De "
                            + str(guidance_scale)
                            + ".\n"
                        )
                frase16 = "Se Usará El Prompt: " + str(prompt) + ".\n"
                if hablo == 1:
                    frase17 = (
                        "El Programa Usará ( Text To Speech ), Para Decirnos Por Voz,"
                        " Como Va La Generación De Imágenes Y Algunos Otros Datos,"
                        " Usando El Habla.\n"
                    )
                if conso == 1:
                    frase15 = (
                        "Toda La Salida De Consola, Se Grabará En Un Fichero De Texto,"
                        " M8AX-Log-Fecha-Hora.LoG, En El Directorio Raiz De Vuestro"
                        " Virtual Environment.\n"
                    )
                frase2a = (
                    "Se Utilizará El Algoritmo De Cálculo Para La Generación De"
                    " Imágenes, "
                    + str(modocale[sched])
                    + ".\n"
                )
                consolacomentada = (
                    "\n... Comentario De Consola ...\n\n"
                    + frase2
                    + frase2a
                    + frase16
                    + frase3
                    + frase4
                    + frase5
                    + frase6
                    + frase1
                    + frase18
                    + frase7
                    + frase8
                    + frase9
                    + frase14
                    + frase10
                    + frase11
                    + frase12
                    + frase13
                    + frase15
                    + frase17
                )
                consolacomandos = (
                    "py m8ax_gpu_sd.py"
                    + " -gp "
                    + str(gpu)
                    + " -p "
                    + '"'
                    + str(prompt)
                    + '"'
                    + " -np "
                    + '"'
                    + str(negp)
                    + '"'
                    + " -w "
                    + str(width)
                    + " -h "
                    + str(height)
                    + " -sc "
                    + str(sched)
                    + " -wo "
                    + '"'
                    + str(word)
                    + '"'
                    + " -fp "
                    + '"'
                    + str(filepro)
                    + '"'
                    + " -mt "
                    + '"'
                    + str(mtext)
                    + '"'
                    + " -bw "
                    + str(blane)
                    + " -ip "
                    + '"'
                    + str(impr)
                    + '"'
                    + " -fx "
                    + str(reales)
                    + " -t "
                    + str(tta)
                    + " -ei "
                    + str(mimag)
                    + " -st "
                    + str(steps)
                    + " -g "
                    + str(guidance_scale)
                    + " -s "
                    + str(seed)
                    + " -j "
                    + str(pseed)
                    + " -c "
                    + str(cuan)
                    + " -f "
                    + str(fps)
                    + " -tl "
                    + str(tlapse)
                    + " -z "
                    + str(zip)
                    + " -bm "
                    + str(bench)
                    + " -co "
                    + str(conso)
                    + " -ts "
                    + str(hablo)
                )
                print(f"\n{consolacomandos}\n{consolacomentada}")
                with open(fichero, "a", encoding="utf-8") as file:
                    file.write("----------------------------\n")
                    file.write(
                        "Sesión --- "
                        + time.strftime("%d_%m_%y")
                        + "-"
                        + time.strftime("%H_%M_%S")
                        + "\n"
                    )
                    file.write("----------------------------\n")
                    file.write(
                        "\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
                    )
                    file.write(
                        "... Comandos De Consola ...\n\n" + str(consolacomandos) + "\n"
                    )
                    file.write(consolacomentada)
                    file.write(
                        "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
                    )
                    file.close()
            num_images = num_images + 1
            print(f"--- Latents ---\n")
            print(f"Se Encuentran En El Fichero TxT De Logs De Sesión.")
            print(f"\n--- Algoritmo De Cálculo - Scheduler ---\n")
            print(f"{modocale[sched]}\n")
            print(f"--- PROMPT ---> {num_images} De {cuan} ---\n\n{prompt}")
            if negp != "":
                print(
                    f"\n--- NEGATIVE PROMPT ---> {num_images} De {cuan} ---\n\n{negp}"
                )
            else:
                print(
                    f"\n--- NEGATIVE PROMPT ---> {num_images} De"
                    f" {cuan} ---\n\n{pronega}"
                )
            print(f"\nUsando {seed}, Semillas Para La Generación De La Imágen...\n")
            if hablo == 1 and num_images == 1:
                dime(consolacomentada)
            inicio = time.time()
        image = pipe(
            prompt, height, width, steps, guidance_scale, negp, latents=latents
        ).images[0]
        print(f"")
        image.save("Salida.PnG", "png")
        if mtext != "":
            os.rename("Salida.PnG", "MeteTexto.PnG")
            image = cv2.imread("MeteTexto.PnG")
            ubicacion = (1, height - 2)
            font = cv2.FONT_HERSHEY_PLAIN
            if height < 512:
                tamañoLetra = 0.6
                grosorLetra = 0
            else:
                tamañoLetra = 1.2
                grosorLetra = 2
            colorLetra = (
                np.random.randint(0, 256),
                np.random.randint(0, 256),
                np.random.randint(0, 256),
            )
            cv2.putText(
                image, mtext, ubicacion, font, tamañoLetra, colorLetra, grosorLetra
            )
            cv2.imwrite("Salida.PnG", image)
            remove("MeteTexto.PnG")
        if blane == 0:
            image = Image.open("Salida.PnG")
            image = ImageEnhance.Sharpness(image).enhance(2)
            image.save("Fin.PnG", "png")
        if blane > 0:
            image = Image.open("Salida.PnG")
            image = image.convert("L")
            image.save("FinBN.PnG", "png")
            image = Image.open("FinBN.PnG")
            image = ImageEnhance.Sharpness(image).enhance(3)
            image.save("Fin.PnG", "png")
        nombreimg = (
            time.strftime("%d_%m_%y")
            + "-"
            + time.strftime("%H_%M_%S")
            + "---Res-"
            + str(width)
            + " x "
            + str(height)
            + "__Steps-"
            + str(steps)
            + "__GScale-"
            + str(guidance_scale)
            + "__Seed-"
            + str(seed)
            + "__Cuan-"
            + str(cuan)
            + "__Fps-"
            + str(fps)
            + "__Word-"
            + str(word)
            + "__FinalResNum-"
            + str(wwidth)
            + " x "
            + str(hheight)
            + "-----"
            + str(num_images)
            + ".PnG"
        )
        nombreimg2 = (
            "Código QR - Sesión - "
            + time.strftime("%d_%m_%y")
            + "-"
            + time.strftime("%H_%M_%S")
            + ".JpG"
        )
        todocorrecto = 1
        if os.path.isfile("..\\..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe"):
            todocorrecto = 1
        else:
            todocorrecto = 0
        if todocorrecto == 1:
            if reales == 0:
                print(
                    "Multiplicando Por 4, La Resolución De La Imágen Final..."
                    f" Resolución Final --- {wwidth} x {hheight}. Metodo - ((( NORMAL -"
                    " RÁPIDO - CPU )))."
                )
                image = Image.open("Fin.PnG")
                image = image.resize((wwidth, hheight))
                if impr == "":
                    image.save("Fin-2.PnG")
                else:
                    image.save("Fin-P.PnG")
            if reales == 1:
                if tta == 0:
                    if gpu == 1:
                        print(
                            "Multiplicando Por 4, La Resolución De La Imágen Final..."
                            f" Resolución Final --- {wwidth} x {hheight}. Metodo - ((("
                            " RealESRGAN-X4Plus MODO NO TTA - GPU ))).\n"
                        )
                        os.system(
                            "..\\..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i Fin.PnG -o"
                            " Fin-2.png -m models-DF2K -v -j 8:16:8"
                        )
                    else:
                        print(
                            "Multiplicando Por 4, La Resolución De La Imágen Final..."
                            f" Resolución Final --- {wwidth} x {hheight}. Metodo - ((("
                            " RealESRGAN-X4Plus MODO NO TTA - CPU ))).\n"
                        )
                        os.system(
                            "..\\..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i Fin.PnG -o"
                            " Fin-2.png -m models-DF2K -g -1 -v -j 8:16:8"
                        )
                if tta > 0:
                    if gpu == 1:
                        print(
                            "Multiplicando Por 4, La Resolución De La Imágen Final..."
                            f" Resolución Final --- {wwidth} x {hheight}. Metodo - ((("
                            " RealESRGAN-X4Plus MODO TTA - GPU ))).\n"
                        )
                        os.system(
                            "..\\..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i Fin.PnG -o"
                            " Fin-2.png -m models-DF2K -v -x -j 8:16:8"
                        )
                    else:
                        print(
                            "Multiplicando Por 4, La Resolución De La Imágen Final..."
                            f" Resolución Final --- {wwidth} x {hheight}. Metodo - ((("
                            " RealESRGAN-X4Plus MODO TTA - CPU ))).\n"
                        )
                        os.system(
                            "..\\..\\Real-ESRGAN\\realsr-ncnn-vulkan.exe -i Fin.PnG -o"
                            " Fin-2.png -m models-DF2K -g -1 -v -x -j 8:16:8"
                        )
                if impr != "":
                    os.rename("Fin-2.png", "Fin-P.PnG")
        else:
            if reales == 1 or tta == 1:
                print(
                    "No Se Ha Podido Llevar A Cabo El Escalado De Imágen x4 Mediante"
                    " Real-ESRGAN, Se Usará Un Metodo De Menos Calidad. Lee El"
                    " Principio Del Código Del Programa, Para Descargarlo Y Ubicarlo"
                    " En Su Directorio Correcto. Puedes Descargar El Programa Aquí:"
                    " https://github.com/nihui/realsr-ncnn-vulkan/releases, Versión"
                    " Probada En Este Programa, La Release 20220728. El Ejecutable Y"
                    " Sus Ficheros, Deben Estar Alojados En La Carpeta Real-ESRGAN, En"
                    " El Directorio Raiz, De Tu Virtual"
                    " Environment...\n\nMultiplicando Por 4, La Resolución De La"
                    f" Imágen Final... Resolución Final --- {wwidth} x {hheight}."
                    " Metodo - ((( NORMAL - RÁPIDO - CPU )))."
                )
                image = Image.open("Fin.PnG")
                image = image.resize((wwidth, hheight))
                if impr == "":
                    image.save("Fin-2.PnG")
                else:
                    image.save("Fin-P.PnG")
            else:
                print(
                    "Multiplicando Por 4, La Resolución De La Imágen Final..."
                    f" Resolución Final --- {wwidth} x {hheight}. Metodo - ((( NORMAL -"
                    " RÁPIDO - CPU )))."
                )
                image = Image.open("Fin.PnG")
                image = image.resize((wwidth, hheight))
                if impr == "":
                    image.save("Fin-2.PnG")
                else:
                    image.save("Fin-P.PnG")
        if impr != "":
            comienzodesden = 0
            elultimop = 0
            auxcomienzo = 0
            cuantosprimos = 0
            antfil = 0
            antcol = 0
            primgeme = 0
            antprim = 0
            imagenprima = cv2.imread("Fin-P.PnG")
            wip = imagenprima.shape[1]
            hep = imagenprima.shape[0]
            if hep > wip:
                cambiando = wip
                wip = hep
                hep = cambiando
            else:
                cambiando = hep
                hep = wip
                wip = cambiando
            if colaleynum == 1 or colaleynum == 5:
                colorcete = [
                    np.random.randint(0, 256),
                    np.random.randint(0, 256),
                    np.random.randint(0, 256),
                ]
            if colaleynum == 2 or colaleynum == 4 or colaleynum == 5:
                impri = np.random.randint(
                    2147483647, 9223372036854775807, dtype=np.int64
                )
            comienzodesden = impri
            auxcomienzo = comienzodesden
            cuantosprimos = 0
            comipri = time.time()
            tiembarra = time.time()
            if hablo == 1:
                dime("Pintando Píxeles Primos...")
            print(f"\n... Pintando Píxeles Primos, En La Imágen Ya Escalada A x4 ...\n")
            for fila in range(wip):
                for columna in range(hep):
                    if sympy.isprime(comienzodesden):
                        if colaleynum == 2 or colaleynum == 3:
                            colorcete = [
                                np.random.randint(0, 256),
                                np.random.randint(0, 256),
                                np.random.randint(0, 256),
                            ]
                        cuantosprimos = cuantosprimos + 1
                        elultimop = comienzodesden
                        imagenprima[fila, columna] = colorcete
                        if colaleynum == 6 and antprim > 2:
                            if comienzodesden - antprim == 2:
                                primgeme = primgeme + 1
                                imagenprima[antfil, antcol] = [0, 255, 255]
                                imagenprima[fila, columna] = [0, 255, 255]
                        antfil = fila
                        antcol = columna
                        antprim = comienzodesden
                    comienzodesden = comienzodesden + 1
                barra_progreso_vibrante(
                    (fila * columna * 100) / (wip * hep), 100, tiembarra
                )
            barra_progreso_vibrante((wip * hep * 100) / (wip * hep), 100, tiembarra)
            print(
                "\n\n... Trabajo De Pintado De Píxeles Primos, Terminado"
                " Correctamente ..."
            )
            finpri = time.time()
            cv2.imwrite("Fin-2.PnG", imagenprima)
            pcentajep = (cuantosprimos * 100) / (comienzodesden - auxcomienzo)
            pcentajeg = ((2 * primgeme) * 100) / (comienzodesden - auxcomienzo)
            if colaleynum == 0:
                print(
                    f"\nImágen Con {comienzodesden-auxcomienzo} De Píxeles, De Los"
                    f" Cuáles, Hemos Coloreado, {cuantosprimos} Píxeles Primos, Con El"
                    f" Color RGB - R-{colorc1} G-{colorc2} B-{colorc3} - "
                    + coloreando(colorc1, colorc2, colorc3, "█████")
                    + f", Un {round(pcentajep,3)}% De La Imágen.\n\nEmpezando Desde El"
                    " Pixel Número 1 De La Imágen, Como Si Fuera El Número"
                    f" {auxcomienzo}.\n\nEl Último Número Primo Pintado, Es El"
                    f" {elultimop}.\n\nVelocidad De Píxeles Primos Pintados -"
                    f" {round(cuantosprimos/(finpri-comipri),2)} PPP/Seg."
                )
                primosafi = (
                    "\n\nImágen Con "
                    + str(comienzodesden - auxcomienzo)
                    + " De Píxeles, De Los Cuáles, Hemos Coloreado, "
                    + str(cuantosprimos)
                    + " Píxeles Primos, Con El Color RGB - R-"
                    + str(colorc1)
                    + " G-"
                    + str(colorc2)
                    + " B-"
                    + str(colorc3)
                    + ", Un "
                    + str(round(pcentajep, 3))
                    + "% De La Imágen.\n\nEmpezando Desde El Pixel Número 1 De La"
                    " Imágen, Como Si Fuera El Número "
                    + str(auxcomienzo)
                    + ".\n\nEl Último Número Primo Pintado, Es El "
                    + str(elultimop)
                    + ".\n\nVelocidad De Píxeles Primos Pintados - "
                    + str(round(cuantosprimos / (finpri - comipri), 2))
                    + " PPP/Seg."
                )
            if colaleynum == 1:
                print(
                    f"\nImágen Con {comienzodesden-auxcomienzo} De Píxeles, De Los"
                    f" Cuáles, Hemos Coloreado, {cuantosprimos} Píxeles Primos, Con El"
                    " Color RGB -"
                    f" R-{colorcete[2]} G-{colorcete[1]} B-{colorcete[0]} - "
                    + coloreando(colorcete[2], colorcete[1], colorcete[0], "█████")
                    + f", Un {round(pcentajep,3)}% De La Imágen.\n\nEmpezando Desde El"
                    " Pixel Número 1 De La Imágen, Como Si Fuera El Número"
                    f" {auxcomienzo}.\n\nEl Último Número Primo Pintado, Es El"
                    f" {elultimop}.\n\nVelocidad De Píxeles Primos Pintados -"
                    f" {round(cuantosprimos/(finpri-comipri),2)} PPP/Seg."
                )
                primosafi = (
                    "\n\nImágen Con "
                    + str(comienzodesden - auxcomienzo)
                    + " De Píxeles, De Los Cuáles, Hemos Coloreado, "
                    + str(cuantosprimos)
                    + " Píxeles Primos, Con El Color RGB - R-"
                    + str(colorcete[2])
                    + " G-"
                    + str(colorcete[1])
                    + " B-"
                    + str(colorcete[0])
                    + ", Un "
                    + str(round(pcentajep, 3))
                    + "% De La Imágen.\n\nEmpezando Desde El Pixel Número 1 De La"
                    " Imágen, Como Si Fuera El Número "
                    + str(auxcomienzo)
                    + ".\n\nEl Último Número Primo Pintado, Es El "
                    + str(elultimop)
                    + ".\n\nVelocidad De Píxeles Primos Pintados - "
                    + str(round(cuantosprimos / (finpri - comipri), 2))
                    + " PPP/Seg."
                )
            if colaleynum == 2:
                print(
                    f"\nImágen Con {comienzodesden-auxcomienzo} De Píxeles, De Los"
                    f" Cuáles, Hemos Coloreado, {cuantosprimos} Píxeles Primos, Con"
                    f" Colores Aleatorios, Un {round(pcentajep,3)}% De La"
                    " Imágen.\n\nEmpezando Desde El Pixel Número 1 De La Imágen, Como"
                    f" Si Fuera El Número {auxcomienzo}.\n\nEl Último Número Primo"
                    f" Pintado, Es El {elultimop}.\n\nVelocidad De Píxeles Primos"
                    f" Pintados - {round(cuantosprimos/(finpri-comipri),2)} PPP/Seg."
                )
                primosafi = (
                    "\n\nImágen Con "
                    + str(comienzodesden - auxcomienzo)
                    + " De Píxeles, De Los Cuáles, Hemos Coloreado, "
                    + str(cuantosprimos)
                    + " Píxeles Primos, Con Colores Aleatorios"
                    + ", Un "
                    + str(round(pcentajep, 3))
                    + "% De La Imágen.\n\nEmpezando Desde El Pixel Número 1 De La"
                    " Imágen, Como Si Fuera El Número "
                    + str(auxcomienzo)
                    + ".\n\nEl Último Número Primo Pintado, Es El "
                    + str(elultimop)
                    + ".\n\nVelocidad De Píxeles Primos Pintados - "
                    + str(round(cuantosprimos / (finpri - comipri), 2))
                    + " PPP/Seg."
                )
            if colaleynum == 3:
                print(
                    f"\nImágen Con {comienzodesden-auxcomienzo} De Píxeles, De Los"
                    f" Cuáles, Hemos Coloreado, {cuantosprimos} Píxeles Primos, Con"
                    f" Colores Aleatorios, Un {round(pcentajep,3)}% De La"
                    " Imágen.\n\nEmpezando Desde El Pixel Número 1 De La Imágen, Como"
                    f" Si Fuera El Número {auxcomienzo}.\n\nEl Último Número Primo"
                    f" Pintado, Es El {elultimop}.\n\nVelocidad De Píxeles Primos"
                    f" Pintados - {round(cuantosprimos/(finpri-comipri),2)} PPP/Seg."
                )
                primosafi = (
                    "\n\nImágen Con "
                    + str(comienzodesden - auxcomienzo)
                    + " De Píxeles, De Los Cuáles, Hemos Coloreado, "
                    + str(cuantosprimos)
                    + " Píxeles Primos, Con Colores Aleatorios"
                    + ", Un "
                    + str(round(pcentajep, 3))
                    + "% De La Imágen.\n\nEmpezando Desde El Pixel Número 1 De La"
                    " Imágen, Como Si Fuera El Número "
                    + str(auxcomienzo)
                    + ".\n\nEl Último Número Primo Pintado, Es El "
                    + str(elultimop)
                    + ".\n\nVelocidad De Píxeles Primos Pintados - "
                    + str(round(cuantosprimos / (finpri - comipri), 2))
                    + " PPP/Seg."
                )
            if colaleynum == 4:
                print(
                    f"\nImágen Con {comienzodesden-auxcomienzo} De Píxeles, De Los"
                    f" Cuáles, Hemos Coloreado, {cuantosprimos} Píxeles Primos, Con El"
                    f" Color RGB - R-{colorc1} G-{colorc2} B-{colorc3} - "
                    + coloreando(colorc1, colorc2, colorc3, "█████")
                    + f", Un {round(pcentajep,3)}% De La Imágen.\n\nEmpezando Desde El"
                    " Pixel Número 1 De La Imágen, Como Si Fuera El Número"
                    f" {auxcomienzo}.\n\nEl Último Número Primo Pintado, Es El"
                    f" {elultimop}.\n\nVelocidad De Píxeles Primos Pintados -"
                    f" {round(cuantosprimos/(finpri-comipri),2)} PPP/Seg."
                )
                primosafi = (
                    "\n\nImágen Con "
                    + str(comienzodesden - auxcomienzo)
                    + " De Píxeles, De Los Cuáles, Hemos Coloreado, "
                    + str(cuantosprimos)
                    + " Píxeles Primos, Con El Color RGB - R-"
                    + str(colorc1)
                    + " G-"
                    + str(colorc2)
                    + " B-"
                    + str(colorc3)
                    + ", Un "
                    + str(round(pcentajep, 3))
                    + "% De La Imágen.\n\nEmpezando Desde El Pixel Número 1 De La"
                    " Imágen, Como Si Fuera El Número "
                    + str(auxcomienzo)
                    + ".\n\nEl Último Número Primo Pintado, Es El "
                    + str(elultimop)
                    + ".\n\nVelocidad De Píxeles Primos Pintados - "
                    + str(round(cuantosprimos / (finpri - comipri), 2))
                    + " PPP/Seg."
                )
            if colaleynum == 5:
                print(
                    f"\nImágen Con {comienzodesden-auxcomienzo} De Píxeles, De Los"
                    f" Cuáles, Hemos Coloreado, {cuantosprimos} Píxeles Primos, Con El"
                    " Color RGB -"
                    f" R-{colorcete[2]} G-{colorcete[1]} B-{colorcete[0]} - "
                    + coloreando(colorcete[2], colorcete[1], colorcete[0], "█████")
                    + f", Un {round(pcentajep,3)}% De La Imágen.\n\nEmpezando Desde El"
                    " Pixel Número 1 De La Imágen, Como Si Fuera El Número"
                    f" {auxcomienzo}.\n\nEl Último Número Primo Pintado, Es El"
                    f" {elultimop}.\n\nVelocidad De Píxeles Primos Pintados -"
                    f" {round(cuantosprimos/(finpri-comipri),2)} PPP/Seg."
                )
                primosafi = (
                    "\n\nImágen Con "
                    + str(comienzodesden - auxcomienzo)
                    + " De Píxeles, De Los Cuáles, Hemos Coloreado, "
                    + str(cuantosprimos)
                    + " Píxeles Primos, Con El Color RGB - R-"
                    + str(colorcete[2])
                    + " G-"
                    + str(colorcete[1])
                    + " B-"
                    + str(colorcete[0])
                    + ", Un "
                    + str(round(pcentajep, 3))
                    + "% De La Imágen.\n\nEmpezando Desde El Pixel Número 1 De La"
                    " Imágen, Como Si Fuera El Número "
                    + str(auxcomienzo)
                    + ".\n\nEl Último Número Primo Pintado, Es El "
                    + str(elultimop)
                    + ".\n\nVelocidad De Píxeles Primos Pintados - "
                    + str(round(cuantosprimos / (finpri - comipri), 2))
                    + " PPP/Seg."
                )
            if colaleynum == 6:
                print(
                    f"\nImágen Con {comienzodesden-auxcomienzo} De Píxeles, De Los"
                    f" Cuáles, Hemos Coloreado, {cuantosprimos} Píxeles Primos, Con El"
                    f" Color RGB - R-{colorc1} G-{colorc2} B-{colorc3} - "
                    + coloreando(colorc1, colorc2, colorc3, "█████")
                    + f", Un {round(pcentajep,3)}% De La Imágen.\n\nEmpezando Desde El"
                    " Pixel Número 1 De La Imágen, Como Si Fuera El Número"
                    f" {auxcomienzo}.\n\nEl Último Número Primo Pintado, Es El"
                    f" {elultimop}. Además, Hemos Pintado {primgeme*2} Números Primos"
                    f" Gemelos De Color Amarillo, {primgeme} Parejas, Un"
                    f" {round(pcentajeg,3)}% De La Imágen.\n\nVelocidad De Píxeles"
                    " Primos Pintados -"
                    f" {round(cuantosprimos/(finpri-comipri),2)} PPP/Seg.\n\nVelocidad"
                    " De Píxeles Primos Gemelos Pintados -"
                    f" {round((primgeme*2)/(finpri-comipri),2)} PPGP/Seg."
                )
                primosafi = (
                    "\n\nImágen Con "
                    + str(comienzodesden - auxcomienzo)
                    + " De Píxeles, De Los Cuáles, Hemos Coloreado, "
                    + str(cuantosprimos)
                    + " Píxeles Primos, Con El Color RGB - R-"
                    + str(colorc1)
                    + " G-"
                    + str(colorc2)
                    + " B-"
                    + str(colorc3)
                    + ", Un "
                    + str(round(pcentajep, 3))
                    + "% De La Imágen.\n\nEmpezando Desde El Pixel Número 1 De La"
                    " Imágen, Como Si Fuera El Número "
                    + str(auxcomienzo)
                    + ".\n\nEl Último Número Primo Pintado, Es El "
                    + str(elultimop)
                    + ". Además, Hemos Pintado "
                    + str(primgeme * 2)
                    + " Números Primos Gemelos De Color Amarillo, "
                    + str(primgeme)
                    + " Parejas, Un "
                    + str(round(pcentajeg, 3))
                    + "% De La Imágen.\n\nVelocidad De Píxeles Primos Pintados - "
                    + str(round(cuantosprimos / (finpri - comipri), 2))
                    + " PPP/Seg.\n\nVelocidad De Píxeles Primos Gemelos Pintados - "
                    + str(round((primgeme * 2) / (finpri - comipri), 2))
                    + " PPGP/Seg."
                )
        print("\nIntroduciendo MetaDatos A Imágen Final...\n")
        targetImage = Image.open("Fin-2.PnG")
        if hablo == 1:
            dime("Saco La Imágen Por Colsola, A Baja Calidad...")
        output = climage.convert("Fin-2.PnG")
        print(output)
        metadata = PngInfo()
        metadata.add_text(
            "MvIiIaX.M8AX - Comentario - ",
            consolacomandos
            + "\n\n"
            + consolacomentada
            + " MvIiIaX Corp.\n\nhttps://youtube.com/m8ax\n\nhttps://oncyber.io/@m8ax",
        )
        metadata.add_text("M8AX-ID", str(10031977))
        targetImage.save("Fin-2.PnG", pnginfo=metadata)
        print("Metadatos Introducidos...")
        if num_images == 1:
            print("\nGenerando QRCODE Con Los Comandos De Consola Para Esta Sesión...")
            data = (
                consolacomandos
                + "\n\nhttps://youtube.com/m8ax\n\nhttps://oncyber.io/@m8ax"
            )
            qr = qrcode.QRCode(version=5, box_size=15, border=1)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(
                fill_color="#"
                + rgb_a_hex(
                    (
                        np.random.randint(150, 256),
                        np.random.randint(150, 256),
                        np.random.randint(150, 256),
                    )
                ),
                back_color="#"
                + rgb_a_hex(
                    (
                        np.random.randint(0, 70),
                        np.random.randint(0, 70),
                        np.random.randint(0, 70),
                    )
                ),
            )
            img.save(nombreimg2)
            print("\nCódigo QRCODE Generado - " + nombreimg2)
        os.rename("Fin-2.png", nombreimg)
        print("")
        imagenc = cv2.imread("Fin.PnG")
        imhist = imagenc
        imagenc = cv2.cvtColor(imagenc, cv2.COLOR_BGR2RGB)
        imagenc = imagenc.reshape((imagenc.shape[0] * imagenc.shape[1], 3))
        clt = KMeans(n_clusters=10)
        clt.fit(imagenc)
        hist = centroid_histogram(clt)
        bar = plot_colors(hist, clt.cluster_centers_)
        kolplt = "#" + rgb_a_hex(
            (
                int(clt.cluster_centers_[0][0]),
                int(clt.cluster_centers_[0][1]),
                int(clt.cluster_centers_[0][2]),
            )
        )
        if hablo == 1:
            dime(
                "Uno De Los Colores Que Más Sale, En Formato R. G. B, Es... R"
                + str(int(clt.cluster_centers_[0][0]))
                + ". G"
                + str(int(clt.cluster_centers_[0][1]))
                + ". B"
                + str(int(clt.cluster_centers_[0][2]))
                + "."
            )
        if (
            int(clt.cluster_centers_[0][0]) < 20
            and int(clt.cluster_centers_[0][1]) < 20
            and int(clt.cluster_centers_[0][2]) < 20
        ):
            laeleccion = np.random.randint(1, 10)
            kolplt = "#" + rgb_a_hex(
                (
                    int(clt.cluster_centers_[laeleccion][0]),
                    int(clt.cluster_centers_[laeleccion][1]),
                    int(clt.cluster_centers_[laeleccion][2]),
                )
            )
        if mimag > 0:
            plt.figure(facecolor=kolplt)
            plt.axis("on")
            plt.imshow(bar)
            plt.title(
                "M8AX - Predominancia De Los 10 Colores Más Frecuentes -"
                " M8AX\nAlgoritmo De Generación De Imágen\n"
                + modocale[sched]
            )
            plt.savefig("M8AX-Predominancia-Color.PnG")
            plt.close(1)
        try:
            print(
                "\nCalculando La Predominancia De Color En Imágen Generada, Para"
                " Mostrarla En Pantalla. ( Los Colores, Que Más Salen En La Imágen."
                " ).\n"
            )
            kol1 = (
                "Color RGB - ( R-"
                + str(int(clt.cluster_centers_[0][0]))
                + " G-"
                + str(int(clt.cluster_centers_[0][1]))
                + " B-"
                + str(int(clt.cluster_centers_[0][2]))
                + " ) - Color HEX - ( #"
                + rgb_a_hex(
                    (
                        int(clt.cluster_centers_[0][0]),
                        int(clt.cluster_centers_[0][1]),
                        int(clt.cluster_centers_[0][2]),
                    )
                )
                + " )"
            )
            kol2 = (
                "Color RGB - ( R-"
                + str(int(clt.cluster_centers_[1][0]))
                + " G-"
                + str(int(clt.cluster_centers_[1][1]))
                + " B-"
                + str(int(clt.cluster_centers_[1][2]))
                + " ) - Color HEX - ( #"
                + rgb_a_hex(
                    (
                        int(clt.cluster_centers_[1][0]),
                        int(clt.cluster_centers_[1][1]),
                        int(clt.cluster_centers_[1][2]),
                    )
                )
                + " )"
            )
            kol3 = (
                "Color RGB - ( R-"
                + str(int(clt.cluster_centers_[2][0]))
                + " G-"
                + str(int(clt.cluster_centers_[2][1]))
                + " B-"
                + str(int(clt.cluster_centers_[2][2]))
                + " ) - Color HEX - ( #"
                + rgb_a_hex(
                    (
                        int(clt.cluster_centers_[2][0]),
                        int(clt.cluster_centers_[2][1]),
                        int(clt.cluster_centers_[2][2]),
                    )
                )
                + " )"
            )
            kol4 = (
                "Color RGB - ( R-"
                + str(int(clt.cluster_centers_[3][0]))
                + " G-"
                + str(int(clt.cluster_centers_[3][1]))
                + " B-"
                + str(int(clt.cluster_centers_[3][2]))
                + " ) - Color HEX - ( #"
                + rgb_a_hex(
                    (
                        int(clt.cluster_centers_[3][0]),
                        int(clt.cluster_centers_[3][1]),
                        int(clt.cluster_centers_[3][2]),
                    )
                )
                + " )"
            )
            kol5 = (
                "Color RGB - ( R-"
                + str(int(clt.cluster_centers_[4][0]))
                + " G-"
                + str(int(clt.cluster_centers_[4][1]))
                + " B-"
                + str(int(clt.cluster_centers_[4][2]))
                + " ) - Color HEX - ( #"
                + rgb_a_hex(
                    (
                        int(clt.cluster_centers_[4][0]),
                        int(clt.cluster_centers_[4][1]),
                        int(clt.cluster_centers_[4][2]),
                    )
                )
                + " )"
            )
            kol6 = (
                "Color RGB - ( R-"
                + str(int(clt.cluster_centers_[5][0]))
                + " G-"
                + str(int(clt.cluster_centers_[5][1]))
                + " B-"
                + str(int(clt.cluster_centers_[5][2]))
                + " ) - Color HEX - ( #"
                + rgb_a_hex(
                    (
                        int(clt.cluster_centers_[5][0]),
                        int(clt.cluster_centers_[5][1]),
                        int(clt.cluster_centers_[5][2]),
                    )
                )
                + " )"
            )
            kol7 = (
                "Color RGB - ( R-"
                + str(int(clt.cluster_centers_[6][0]))
                + " G-"
                + str(int(clt.cluster_centers_[6][1]))
                + " B-"
                + str(int(clt.cluster_centers_[6][2]))
                + " ) - Color HEX - ( #"
                + rgb_a_hex(
                    (
                        int(clt.cluster_centers_[6][0]),
                        int(clt.cluster_centers_[6][1]),
                        int(clt.cluster_centers_[6][2]),
                    )
                )
                + " )"
            )
            kol8 = (
                "Color RGB - ( R-"
                + str(int(clt.cluster_centers_[7][0]))
                + " G-"
                + str(int(clt.cluster_centers_[7][1]))
                + " B-"
                + str(int(clt.cluster_centers_[7][2]))
                + " ) - Color HEX - ( #"
                + rgb_a_hex(
                    (
                        int(clt.cluster_centers_[7][0]),
                        int(clt.cluster_centers_[7][1]),
                        int(clt.cluster_centers_[7][2]),
                    )
                )
                + " )"
            )
            kol9 = (
                "Color RGB - ( R-"
                + str(int(clt.cluster_centers_[8][0]))
                + " G-"
                + str(int(clt.cluster_centers_[8][1]))
                + " B-"
                + str(int(clt.cluster_centers_[8][2]))
                + " ) - Color HEX - ( #"
                + rgb_a_hex(
                    (
                        int(clt.cluster_centers_[8][0]),
                        int(clt.cluster_centers_[8][1]),
                        int(clt.cluster_centers_[8][2]),
                    )
                )
                + " )"
            )
            kol10 = (
                "Color RGB - ( R-"
                + str(int(clt.cluster_centers_[9][0]))
                + " G-"
                + str(int(clt.cluster_centers_[9][1]))
                + " B-"
                + str(int(clt.cluster_centers_[9][2]))
                + " ) - Color HEX - ( #"
                + rgb_a_hex(
                    (
                        int(clt.cluster_centers_[9][0]),
                        int(clt.cluster_centers_[9][1]),
                        int(clt.cluster_centers_[9][2]),
                    )
                )
                + " )"
            )
            aa1 = (
                int(clt.cluster_centers_[0][0]),
                int(clt.cluster_centers_[0][1]),
                int(clt.cluster_centers_[0][2]),
            )
            aa2 = (
                int(clt.cluster_centers_[1][0]),
                int(clt.cluster_centers_[1][1]),
                int(clt.cluster_centers_[1][2]),
            )
            aa3 = (
                int(clt.cluster_centers_[2][0]),
                int(clt.cluster_centers_[2][1]),
                int(clt.cluster_centers_[2][2]),
            )
            aa4 = (
                int(clt.cluster_centers_[3][0]),
                int(clt.cluster_centers_[3][1]),
                int(clt.cluster_centers_[3][2]),
            )
            aa5 = (
                int(clt.cluster_centers_[4][0]),
                int(clt.cluster_centers_[4][1]),
                int(clt.cluster_centers_[4][2]),
            )
            aa6 = (
                int(clt.cluster_centers_[5][0]),
                int(clt.cluster_centers_[5][1]),
                int(clt.cluster_centers_[5][2]),
            )
            aa7 = (
                int(clt.cluster_centers_[6][0]),
                int(clt.cluster_centers_[6][1]),
                int(clt.cluster_centers_[6][2]),
            )
            aa8 = (
                int(clt.cluster_centers_[7][0]),
                int(clt.cluster_centers_[7][1]),
                int(clt.cluster_centers_[7][2]),
            )
            aa9 = (
                int(clt.cluster_centers_[8][0]),
                int(clt.cluster_centers_[8][1]),
                int(clt.cluster_centers_[8][2]),
            )
            aa10 = (
                int(clt.cluster_centers_[9][0]),
                int(clt.cluster_centers_[9][1]),
                int(clt.cluster_centers_[9][2]),
            )
            print("1.  ", end="")
            print(kol1, end="")
            print(" -----> ", end="")
            print(
                coloreando(
                    int(aa1[0]), int(aa1[1]), int(aa1[2]), "█████████████████████████\n"
                )
            )
            print("2.  ", end="")
            print(kol2, end="")
            print(" -----> ", end="")
            print(
                coloreando(
                    int(aa2[0]), int(aa2[1]), int(aa2[2]), "█████████████████████████\n"
                )
            )
            print("3.  ", end="")
            print(kol3, end="")
            print(" -----> ", end="")
            print(
                coloreando(
                    int(aa3[0]), int(aa3[1]), int(aa3[2]), "█████████████████████████\n"
                )
            )
            print("4.  ", end="")
            print(kol4, end="")
            print(" -----> ", end="")
            print(
                coloreando(
                    int(aa4[0]), int(aa4[1]), int(aa4[2]), "█████████████████████████\n"
                )
            )
            print("5.  ", end="")
            print(kol5, end="")
            print(" -----> ", end="")
            print(
                coloreando(
                    int(aa5[0]), int(aa5[1]), int(aa5[2]), "█████████████████████████\n"
                )
            )
            print("6.  ", end="")
            print(kol6, end="")
            print(" -----> ", end="")
            print(
                coloreando(
                    int(aa6[0]), int(aa6[1]), int(aa6[2]), "█████████████████████████\n"
                )
            )
            print("7.  ", end="")
            print(kol7, end="")
            print(" -----> ", end="")
            print(
                coloreando(
                    int(aa7[0]), int(aa7[1]), int(aa7[2]), "█████████████████████████\n"
                )
            )
            print("8.  ", end="")
            print(kol8, end="")
            print(" -----> ", end="")
            print(
                coloreando(
                    int(aa8[0]), int(aa8[1]), int(aa8[2]), "█████████████████████████\n"
                )
            )
            print("9.  ", end="")
            print(kol9, end="")
            print(" -----> ", end="")
            print(
                coloreando(
                    int(aa9[0]), int(aa9[1]), int(aa9[2]), "█████████████████████████\n"
                )
            )
            print("10. ", end="")
            print(kol10, end="")
            print(" -----> ", end="")
            print(
                coloreando(
                    int(aa10[0]),
                    int(aa10[1]),
                    int(aa10[2]),
                    "█████████████████████████",
                )
            )
        except:
            print(
                "\nSe Ha Producido Un Error, No Podré Mostrar Los Colores"
                " Predominantes, De La Imágen Generada."
            )
        if mimag > 0:
            plt.figure(facecolor=kolplt)
            for iii, ccc in enumerate(color):
                hist = cv2.calcHist([imhist], [iii], None, [256], [0, 256])
                plt.plot(hist, color=ccc)
                plt.xlim([0, 256])
            plt.title("M8AX - HistoGrama - M8AX\nImágen Número - " + str(num_images))
            plt.savefig("M8AX-HistoGrama.PnG")
            plt.close(1)
            image = Image.open("M8AX-Predominancia-Color.PnG")
            image = image.resize((width, height))
            image.save("1.PnG")
            image = Image.open("M8AX-HistoGrama.PnG")
            image = image.resize((width, height))
            image.save("2.PnG")
            im1 = cv2.imread("Fin.PnG")
            im2 = cv2.imread("1.PnG")
            im3 = cv2.imread("2.PnG")
            hori = np.concatenate((im1, im2, im3), axis=1)
            cv2.imshow(creadire2, hori)
            cv2.waitKey(1)
            remove("M8AX-Predominancia-Color.PnG")
            remove("1.PnG")
            remove("2.PnG")
            remove("M8AX-HistoGrama.PnG")
            if num_images == 1:
                try:
                    os.mkdir("M8AX-Imagenes-Im_Pc_Hs")
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise
            cv2.imwrite(
                "M8AX-Imagenes-Im_Pc_Hs/M8AX-Imagen-Im_Pc_Hs-"
                + str(num_images)
                + ".PnG",
                hori,
            )
            output = climage.convert(
                "M8AX-Imagenes-Im_Pc_Hs/M8AX-Imagen-Im_Pc_Hs-"
                + str(num_images)
                + ".PnG"
            )
            print("\n" + output)
            sizet3 = get_file_size(
                "M8AX-Imagenes-Im_Pc_Hs/M8AX-Imagen-Im_Pc_Hs-"
                + str(num_images)
                + ".PnG",
                SIZE_UNIT.MB,
            )
            tamano3 = tamano3 + sizet3
        remove("Salida.PnG")
        remove("Fin.PnG")
        if blane > 0:
            remove("FinBN.PnG")
        if impr != "":
            remove("Fin-P.PnG")
        sizefile = get_file_size(nombreimg, SIZE_UNIT.MB)
        tamano = tamano + sizefile
        tamano2 = tamano2 + sizefile
        fin = time.time() + despertot
        cuantotarda = (fin - inicio) * (cuan - num_images)
        todoloquetarda = segahms(cuantotarda, hablo)
        en1hora = (3600 * num_images) / (fin - iniciot)
        convertidoo = segahms(fin - iniciot, hablo)
        if mimag > 0:
            print(f"Nombre De Fichero Resultante:\n\n{nombreimg}")
        else:
            print(f"\nNombre De Fichero Resultante:\n\n{nombreimg}")
        print(f"\nTamaño Del Fichero PNG - ((( {round(sizefile,3)} MB. )))")
        print(
            f"\nTotal De MB Ocupados Que Llevamos En {num_images} Imágenes Generadas -"
            f" ((( {round((tamano+tamano3),3)} MB. ))). Aún Quedan Por Generar"
            f" {cuan-num_images} Imágenes..."
        )
        print(
            "\nFin De Generación De Imágen. Tiempo De Cálculo -"
            f" {round(fin-inicio,3)} Segundos..."
        )
        print(
            "\nRitmo De Generación De Imágenes Por Hora -"
            f" {round(en1hora,3)} Imágenes/Hora..."
        )
        print(
            "\nRitmo De Generación De Imágenes Por Min -"
            f" {round((60*num_images)/(fin-iniciot),3)} Imágenes/Min..."
        )
        print(
            "\nRitmo De Generación De Imágenes Por Seg -"
            f" {round((num_images)/(fin-iniciot),3)} Imágenes/Seg..."
        )
        if hablo == 1:
            desperhabla = time.time()
            dime(
                "Llevamos "
                + str(num_images)
                + ", Imágenes Generadas. La Última Imágen Generada, Ocupa  "
                + str(round(sizefile, 2))
                + " Megas. Total De Megas Ocupados, Contando Todas Las Imágenes, "
                + str(round((tamano + tamano3), 2))
                + " Megas..."
            )
            dime(
                "Ritmo De Generación De Imágenes Por Hora, "
                + str(round(en1hora, 2))
                + " Imágenes Por Hora... La Última Imágen, Ha Tardado En Generarse, "
                + str(round((fin - inicio), 2))
                + " Segundos..."
            )
            dime("Tiempo Total De Cálculo Que Llevamos, " + str(convertidoo) + "...")
            dime(
                "Quedan, "
                + str(cuan - num_images)
                + " Imágenes, Por Generar. Tiempo Restante Más O Menos Que Queda, Para"
                " Terminar... "
                + str(todoloquetarda)
                + "..."
            )
            despertot = time.time() - desperhabla
        if gpu == 1:
            print(f"\n--- Tiempo Total De Cálculo Intensivo De GPU --- {convertidoo}")
        else:
            print(f"\n--- Tiempo Total De Cálculo Intensivo De CPU --- {convertidoo}")
        print(
            "\n--- Tiempo +/- Que Queda, Para Finalizar Todo El Trabajo ---"
            f" {todoloquetarda}"
        )
        print(
            f"\n---------------------------------------------------------------------------------------------------------------------------------------\n"
        )
        with open(fichero, "a", encoding="utf-8") as file:
            file.write(
                "\n--- Latents ---\n\n"
                + str(latents)
                + "\n\n--- Algoritmo De Cálculo - Scheduler ---\n\n"
                + str(modocal)
            )
            file.write(
                "\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
            )
            file.write(
                "\n\n--- PROMPT ---> "
                + str(num_images)
                + " De "
                + str(cuan)
                + " ---\n\n"
                + str(prompt)
                + "\n\n--- NEGATIVE PROMPT ---> "
                + str(num_images)
                + " De "
                + str(cuan)
                + " ---\n\n"
                + str(pronega)
            )
            file.write(
                "\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
            )
            file.write("\n\nSteps - " + str(steps) + ".")
            file.write("\n\nEscala De Orientación - " + str(guidance_scale) + ".")
            file.write("\n\nSemillas - " + str(seed) + ".")
            file.write(
                "\n\nTamaño De Imágen Creada - "
                + str(width)
                + " x "
                + str(height)
                + ", Escalada A "
                + str(wwidth)
                + " x "
                + str(hheight)
                + "."
            )
            if todocorrecto == 1:
                if reales == 1:
                    if tta == 0:
                        file.write("\n\nMétodo De Escalado De Imágen - RealEsrgan.")
                    else:
                        file.write("\n\nMétodo De Escalado De Imágen - RealEsrgan TTA.")
                else:
                    file.write("\n\nMétodo De Escalado De Imágen - Normal")
            else:
                file.write(
                    "\n\nMétodo De Escalado Normal. No Se Encuentra El Ejecutable De"
                    " RealEsrgan, Lee La Parte De Arriba Del Código Fuente, Para"
                    " Instalarlo Y Ubicarlo En Su Sitio. Puedes Descargarlo Aquí -"
                    " https://github.com/nihui/realsr-ncnn-vulkan/releases"
                )
            if mtext != "":
                file.write(
                    "\n\nTexto - "
                    + str(mtext)
                    + ", Añadido A La Parte Inferior Izquierda De La Imágen."
                )
            if blane == 1:
                file.write("\n\nImágen En Blanco Y Negro.")
            else:
                file.write("\n\nImágen En Color.")
            file.write("\n\n--- Predominancia De Colores En La Imágen ---")
            file.write("\n\n1. " + kol1)
            file.write("\n\n2. " + kol2)
            file.write("\n\n3. " + kol3)
            file.write("\n\n4. " + kol4)
            file.write("\n\n5. " + kol5)
            file.write("\n\n6. " + kol6)
            file.write("\n\n7. " + kol7)
            file.write("\n\n8. " + kol8)
            file.write("\n\n9. " + kol9)
            file.write("\n\n10. " + kol10)
            file.write(
                "\n\nNombre De Fichero Resultante: "
                + str(nombreimg)
                + "\n\nTamaño Del Fichero PNG - ((( "
                + str(round(sizefile, 3))
                + " MB. )))"
            )
            if impr != "":
                file.write(primosafi)
            file.write(
                "\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
            )
            file.write(
                "\n\nFin De Generación De Imágen. Tiempo De Cálculo - "
                + str(round(fin - inicio, 3))
                + " Segundos...\n\nRitmo De Generación De Imágenes Por Hora - "
                + str(round(en1hora, 3))
                + " Imágenes/Hora...\n\nRitmo De Generación De Imágenes Por Min - "
                + str(round((60 * num_images) / (fin - iniciot), 3))
                + " Imágenes/Min...\n\n"
                + "Ritmo De Generación De Imágenes Por Seg - "
                + str(round((num_images) / (fin - iniciot), 3))
                + " Imágenes/Seg..."
            )
            file.write(
                "\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
            )
            file.close()
        try:
            with open("../../M8AX-PromptS.TxT", "r", encoding="utf-8") as file:
                lineas = file.readlines()
                grabo = 0
                for linea in lineas:
                    if prompt == linea.strip("\n"):
                        grabo = grabo + 1
                file.close()
        except:
            grabo = 0
        if grabo == 0:
            with open("../../M8AX-PromptS.TxT", "a", encoding="utf-8") as file:
                file.write(str(prompt) + "\n")
                file.close()
    if tlapse == 1:
        print(f"Creando TimeLapse. Espera... ( FORMATO MP4 )...\n")
        proc.terminate()
        tcomi = time.time()
        frameSizee = (GetSystemMetrics(0), GetSystemMetrics(1))
        os.chdir("..")
        os.chdir("M8AX-TimeLapse")
        outv = cv2.VideoWriter(
            "M8AX-TimeLapse.Mp4", cv2.VideoWriter_fourcc(*"h265"), fpstimlap, frameSizee
        )
        nn = 0
        cuantospng = len(glob.glob("*.png"))
        print("")
        tiembarra = time.time()
        for filename in sorted(glob.glob("*.png"), key=os.path.getmtime):
            imgv = cv2.imread(filename)
            outv.write(imgv)
            nn = nn + 1
            barra_progreso_roja((nn * 100) / cuantospng, 100, tiembarra)
        barra_progreso_roja((cuantospng * 100) / cuantospng, 100, tiembarra)
        print(""), print("")
        print(*sorted(glob.glob("*.png"), key=os.path.getmtime), sep="\n")
        outv.release()
        tfine = time.time()
        print(
            f"\nTimeLapse Creado Con {nn} ScreenShots, A {fpstimlap} Fps. Con Una"
            f" Resolución De {GetSystemMetrics(0)}x{GetSystemMetrics(1)}."
        )
        print(
            "\n((( - Codificación De TimeLapse De Video Realizada A - ))) - ((( -"
            f" {round(nn/(tfine-tcomi),3)} Imágenes/Seg. - )))"
        )
        ttela = (
            "\n((( - Codificación De TimeLapse De Video Realizada A - ))) - ((( - "
            + str(round(nn / (tfine - tcomi), 3))
            + " Imágenes/Seg. - )))\n"
        )
        os.chdir("..")
        os.chdir("Sesión --- " + creadire)
        shutil.move(
            "../M8AX-TimeLapse/M8AX-TimeLapse.Mp4",
            "../../M8AX-Imágenes_Finales/Sesión --- "
            + str(creadire)
            + "/M8AX-TimeLapse - "
            + str(nn)
            + " ScreenShots A "
            + str(fpstimlap)
            + " Fps - "
            + creadire
            + ".Mp4",
        )
        sizetm = get_file_size(
            "M8AX-TimeLapse - "
            + str(nn)
            + " ScreenShots A "
            + str(fpstimlap)
            + " Fps - "
            + creadire
            + ".Mp4",
            SIZE_UNIT.MB,
        )
        print(
            f"\nNombre Del TimeLapse De Video - "
            + "M8AX-TimeLapse - "
            + str(nn)
            + " ScreenShots A "
            + str(fpstimlap)
            + " Fps - "
            + creadire
            + ".Mp4"
        )
        print(f"\nDuración Del Video - " + segahms(nn / fpstimlap, hablo) + ".")
        print(
            "\nTimeLapse De Video, Creado Correctamente. ( FORMATO MP4 )...\n\nTamaño"
            f" Del TimeLapse De Video MP4 - ((( {round(sizetm,3)} MB. )))"
        )
        if fps == 0:
            tamano = tamano + sizetm
            print(
                "\nTamaño De Todas Las Imágenes Generadas + Video MP4 - ((("
                f" {round((tamano+tamano3),3)} MB. )))"
            )
        with open(fichero, "a", encoding="utf-8") as file:
            file.write(
                "\nTimeLapse De Video Realizado Con "
                + str(nn)
                + " ScreenShots Con Un FrameRate De "
                + str(fpstimlap)
                + " Fps. Y Una Resolución De - "
                + str(GetSystemMetrics(0))
                + " x "
                + str(GetSystemMetrics(1))
                + ". ( FORMATO MP4 )...\n"
            )
            file.write(
                "\nNombre Del TimeLapse De Video - "
                + "M8AX-TimeLapse - "
                + str(nn)
                + " ScreenShots A "
                + str(fpstimlap)
                + " Fps - "
                + creadire
                + ".Mp4\n"
            )
            file.write(
                "\nDuración Del Video - " + str(segahms(nn / fpstimlap, hablo)) + ".\n"
            )
            file.write(
                "\nTamaño Del TimeLapse De Video MP4 - ((( "
                + str(round(sizetm, 3))
                + " MB. )))\n"
            )
            if fps == 0:
                file.write(
                    "\nTamaño De Todas Las Imágenes Generadas - ((( "
                    + str(round((tamano2 + tamano3), 3))
                    + " MB. )))\n"
                )
            if fps == 1:
                file.write(
                    "\nTamaño De Todas Las Imágenes Generadas - ((( "
                    + str(round((tamano2 + tamano3), 3))
                    + " MB. )))\n"
                )
            file.close()
            if hablo == 1:
                dime(
                    "TimeLapse Creado, Velocidad De Codificación Del TimeLapse, "
                    + str(round(nn / (tfine - tcomi), 2))
                    + ", Imágenes Por Segundo..."
                )
    if fps > 0:
        nn = 0
        cuantospng = len(glob.glob("*.png"))
        tcomi = time.time()
        if tlapse == 1:
            print(
                f"\nGenerando Video Con {cuan} Imágenes, A Una Resolución De {wwidth} x"
                f" {hheight}, Con Un FrameRate De {fps} Fps. ( FORMATO MP4 )...\n"
            )
        else:
            print(
                f"Generando Video Con {cuan} Imágenes, A Una Resolución De {wwidth} x"
                f" {hheight}, Con Un FrameRate De {fps} Fps. ( FORMATO MP4 )...\n"
            )
        frameSize = (wwidth, hheight)
        out = cv2.VideoWriter(
            "Sesion De Video - "
            + str(cuan)
            + " Imagenes - "
            + str(fps)
            + " Fps - "
            + str(cuan)
            + " Frames --- "
            + creadire
            + ".Mp4",
            cv2.VideoWriter_fourcc(*"h265"),
            fps,
            frameSize,
        )
        print("")
        tiembarra = time.time()
        for filename in sorted(glob.glob("*.png"), key=os.path.getmtime):
            img = cv2.imread(filename)
            out.write(img)
            nn = nn + 1
            barra_progreso_roja((nn * 100) / cuantospng, 100, tiembarra)
        barra_progreso_roja((cuantospng * 100) / cuantospng, 100, tiembarra)
        print("\n")
        print(*sorted(glob.glob("*.png"), key=os.path.getmtime), sep="\n")
        out.release()
        tfine = time.time()
        print(
            "\n((( - Codificación De Video De Imágenes Generadas, Realizada A - ))) -"
            f" ((( - {round(nn/(tfine-tcomi),3)} Imágenes/Seg. - )))"
        )
        ttfps = (
            "\n((( - Codificación De Video De Imágenes Generadas, Realizada A - ))) -"
            " ((( - "
            + str(round(nn / (tfine - tcomi), 3))
            + " Imágenes/Seg. - )))\n"
        )
        print(
            "\nTamaño De Todas Las Imágenes Generadas - ((("
            f" {round((tamano+tamano3),3)} MB. )))"
        )
        print(
            f"\nVideo Realizado Con {cuan} Imágenes, A Una Resolución De {wwidth} x"
            f" {hheight}, Con Un FrameRate De {fps} Fps. ( FORMATO MP4 )..."
        )
        print(
            f"\nNombre Del Fichero De Video - "
            + "Sesion De Video - "
            + str(cuan)
            + " Imagenes - "
            + str(fps)
            + " Fps - "
            + str(cuan)
            + " Frames --- "
            + creadire
            + ".Mp4"
        )
        print(f"\nDuración Del Video - " + segahms(nn / fps, hablo) + ".")
        fint = time.time()
        tiempot = fint - iniciot
        convertido = segahms(tiempot, hablo)
        sizefile = get_file_size(
            "Sesion De Video - "
            + str(cuan)
            + " Imagenes - "
            + str(fps)
            + " Fps - "
            + str(cuan)
            + " Frames --- "
            + creadire
            + ".Mp4",
            SIZE_UNIT.MB,
        )
        tamano = tamano + (sizefile + sizetm)
        print(f"\nTamaño Del Video MP4 - ((( {round(sizefile,3)} MB. )))")
        print(
            "\nTamaño De Todas Las Imágenes Generadas + Video MP4 - ((("
            f" {round((tamano+tamano3),3)} MB. )))"
        )
        with open(fichero, "a", encoding="utf-8") as file:
            file.write(
                "\nVideo Realizado Con "
                + str(cuan)
                + " Imágenes Con Un FrameRate De "
                + str(fps)
                + " Fps. ( FORMATO MP4 )...\n"
            )
            file.write(
                "\nNombre Del Fichero De Video - "
                + "Sesion De Video - "
                + str(cuan)
                + " Imagenes - "
                + str(fps)
                + " Fps - "
                + str(cuan)
                + " Frames --- "
                + creadire
                + ".Mp4\n"
            )
            file.write("\nDuración Del Video - " + segahms(nn / fps, hablo) + ".\n")
            file.write(
                "\nTamaño Del Video MP4 - ((( " + str(round(sizefile, 3)) + " MB. )))\n"
            )
            if tlapse == 0:
                file.write(
                    "\nTamaño De Todas Las Imágenes Generadas - ((( "
                    + str(round((tamano2 + tamano3), 3))
                    + " MB. )))\n"
                )
            file.close()
        if hablo == 1:
            dime(
                "Video Creado, Velocidad De Codificación Del Video, "
                + str(round(nn / (tfine - tcomi), 2))
                + ", Imágenes Por Segundo..."
            )
    if tlapse == 1:
        with open(fichero, "a", encoding="utf-8") as file:
            file.write(ttela)
            file.close()
    if fps > 0:
        with open(fichero, "a", encoding="utf-8") as file:
            file.write(ttfps)
            file.close()
    if fps == 0:
        fint = time.time()
        tiempot = fint - iniciot
        convertido = segahms(tiempot, hablo)
        if tlapse == 0:
            print(
                "Tamaño De Todas Las Imágenes Generadas - ((("
                f" {round((tamano+tamano3),3)} MB. )))"
            )
        else:
            print(
                "\nTamaño De Todas Las Imágenes Generadas - ((("
                f" {round((tamano2+tamano3),3)} MB. )))"
            )
        with open(fichero, "a", encoding="utf-8") as file:
            if gpu == 1:
                if tlapse == 0:
                    file.write(
                        "\nFin De Generación De "
                        + str(cuan)
                        + " Imágenes. Tiempo Total De Cálculo Intensivo De GPU - "
                        + str(round(tiempot, 3))
                        + " Segundos...\n\n"
                        + "Tamaño Total De Imágenes Creadas - ((( "
                        + str(round((tamano2 + tamano3), 3))
                        + " MB. )))\n\n"
                        + "Tiempo Total De Cálculo Intensivo De GPU --- "
                        + str(convertido)
                        + "\n\nBy M8AX - https://youtube.com/m8ax -"
                        " https://oncyber.io/m8ax\n\nPodeis Suscribiros, No Me"
                        " Enfadaré... xD"
                    )
                else:
                    file.write(
                        "\nFin De Generación De "
                        + str(cuan)
                        + " Imágenes. Tiempo Total De Cálculo Intensivo De GPU - "
                        + str(round(tiempot, 3))
                        + " Segundos...\n\n"
                        + "Tamaño Total De Imágenes Creadas + Video MP4 - ((( "
                        + str(round((tamano + tamano3), 3))
                        + " MB. )))\n\n"
                        + "Tiempo Total De Cálculo Intensivo De GPU --- "
                        + str(convertido)
                        + "\n\nBy M8AX - https://youtube.com/m8ax -"
                        " https://oncyber.io/m8ax\n\nPodeis Suscribiros, No Me"
                        " Enfadaré... xD"
                    )
            else:
                if tlapse == 0:
                    file.write(
                        "\nFin De Generación De "
                        + str(cuan)
                        + " Imágenes. Tiempo Total De Cálculo Intensivo De CPU - "
                        + str(round(tiempot, 3))
                        + " Segundos...\n\n"
                        + "Tamaño Total De Imágenes Creadas - ((( "
                        + str(round((tamano2 + tamano3), 3))
                        + " MB. )))\n\n"
                        + "Tiempo Total De Cálculo Intensivo De CPU --- "
                        + str(convertido)
                        + "\n\nBy M8AX - https://youtube.com/m8ax -"
                        " https://oncyber.io/m8ax\n\nPodeis Suscribiros, No Me"
                        " Enfadaré... xD"
                    )
                else:
                    file.write(
                        "\nFin De Generación De "
                        + str(cuan)
                        + " Imágenes. Tiempo Total De Cálculo Intensivo De CPU - "
                        + str(round(tiempot, 3))
                        + " Segundos...\n\n"
                        + "Tamaño Total De Imágenes Creadas + Video MP4 - ((( "
                        + str(round((tamano + tamano3), 3))
                        + " MB. )))\n\n"
                        + "Tiempo Total De Cálculo Intensivo De CPU --- "
                        + str(convertido)
                        + "\n\nBy M8AX - https://youtube.com/m8ax -"
                        " https://oncyber.io/m8ax\n\nPodeis Suscribiros, No Me"
                        " Enfadaré... xD"
                    )
            file.write(
                "\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
            )
            file.close()
    if fps > 0:
        with open(fichero, "a", encoding="utf-8") as file:
            if gpu == 1:
                file.write(
                    "\nFin De Generación De "
                    + str(cuan)
                    + " Imágenes. Tiempo Total De Cálculo Intensivo De GPU - "
                    + str(round(tiempot, 3))
                    + " Segundos...\n\n"
                    + "Tamaño Total De Imágenes Creadas + Video MP4 - ((( "
                    + str(round((tamano + tamano3), 3))
                    + " MB. )))\n\n"
                    + "Tiempo Total De Cálculo Intensivo De GPU --- "
                    + str(convertido)
                    + "\n\nBy M8AX - https://youtube.com/m8ax -"
                    " https://oncyber.io/m8ax\n\nPodeis Suscribiros, No Me"
                    " Enfadaré... xD"
                )
            else:
                file.write(
                    "\nFin De Generación De "
                    + str(cuan)
                    + " Imágenes. Tiempo Total De Cálculo Intensivo De CPU - "
                    + str(round(tiempot, 3))
                    + " Segundos...\n\n"
                    + "Tamaño Total De Imágenes Creadas + Video MP4 - ((( "
                    + str(round((tamano + tamano3), 3))
                    + " MB. )))\n\n"
                    + "Tiempo Total De Cálculo Intensivo De CPU --- "
                    + str(convertido)
                    + "\n\nBy M8AX - https://youtube.com/m8ax -"
                    " https://oncyber.io/m8ax\n\nPodeis Suscribiros, No Me"
                    " Enfadaré... xD"
                )
            file.write(
                "\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
            )
            file.close()
    if zip > 0:
        with open(fichero, "a", encoding="utf-8") as file:
            file.write(
                "\n\nFichero - ((( Sesión --- " + str(creadire) + ".7z ))) Creado."
            )
            file.write(
                "\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
            )
            file.close()
        with py7zr.SevenZipFile("..\Sesión --- " + creadire + ".7z", "w") as archive:
            archive.writeall(
                "..\..\M8AX-Imágenes_Finales\Sesión --- " + creadire,
                "Sesión --- " + creadire,
            )
        sizeff = get_file_size("..\\Sesión --- " + creadire + ".7z", SIZE_UNIT.MB)
        print(
            f"\nFichero - Sesión --- {creadire}.7z Creado.\n\nTamaño Del Fichero 7z -"
            f" ((( {round(sizeff,3)} MB. )))"
        )
        with open(fichero, "a", encoding="utf-8") as file:
            file.write(
                "\n\nTamaño Del Fichero 7z - ((( " + str(round(sizeff, 3)) + " MB. )))"
            )
            file.write(
                "\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
            )
            file.close()
        if hablo == 1:
            dime("Fichero 7 Zip Creado. Ocupa, " + str(round(sizeff, 2)) + ", Megas...")
    if gpu == 1:
        print(
            f"\nFin De Generación De {cuan} Imágenes. Tiempo Total De Cálculo Intensivo"
            f" De GPU - {round(tiempot,3)} Segundos...\n\nTiempo Total De Cálculo"
            f" Intensivo De GPU --- {convertido}\n\nBy M8AX - https://youtube.com/m8ax"
            " - https://oncyber.io/m8ax\n\nPodeis Suscribiros, No Me Enfadaré... xD"
        )
        if hablo == 1:
            dime(
                "Fin De Generación De Imágenes... Se Han Creado, "
                + str(cuan)
                + " Imágenes... Tiempo De Cálculo Total De G P U... "
                + str(round(tiempot, 3))
                + "..."
            )
    else:
        print(
            f"\nFin De Generación De {cuan} Imágenes. Tiempo Total De Cálculo Intensivo"
            f" De CPU - {round(tiempot,3)} Segundos...\n\nTiempo Total De Cálculo"
            f" Intensivo De CPU --- {convertido}\n\nBy M8AX - https://youtube.com/m8ax"
            " - https://oncyber.io/m8ax\n\nPodeis Suscribiros, No Me Enfadaré... xD"
        )
        if hablo == 1:
            dime(
                "Fin De Generación De Imágenes... Se Han Creado, "
                + str(cuan)
                + " Imágenes... Tiempo De Cálculo Total De c P U... "
                + str(round(tiempot, 3))
                + "..."
            )
    if fps > 0:
        print(f"\nPulsa ESC, Para Salir De La Reproducción Del Video.")
        if hablo == 1:
            dime("Reproduciendo Video...")
        while True:
            isclosed = 0
            cap = cv2.VideoCapture(
                "Sesion De Video - "
                + str(cuan)
                + " Imagenes - "
                + str(fps)
                + " Fps - "
                + str(cuan)
                + " Frames --- "
                + creadire
                + ".Mp4"
            )
            titulo = (
                "Sesion De Video - "
                + str(cuan)
                + " Imagenes - "
                + str(fps)
                + " Fps - "
                + str(cuan)
                + " Frames --- "
                + creadire
                + ".Mp4"
            )
            while True:
                ret, frame = cap.read()
                if ret == True:
                    cv2.imshow(titulo, frame)
                    if cv2.waitKey(30) == 27:
                        isclosed = 1
                        break
                else:
                    break
            if isclosed:
                break
        cap.release()
        cv2.destroyAllWindows()
    if mimag == 1:
        while True:
            print(
                "\n¿ Quieres Que Te Haga Un Video Con Las Imágenes Que He Mostrado Por"
                " Pantalla Mientras Las Creaba ?, Es Decir... La Imágen + Predominancia"
                " De Color + HistoGrama... 1 - SI, 2 - NO.\n"
            )
            try:
                hacemos = int(input())
            except:
                continue
            if hacemos > 2 or hacemos < 1:
                print("\nEl Número Solo Puede Ser 1 O 2...")
            else:
                break
        nn = 0
        framesize = ((width * 3), (height))
        if int(hacemos) == 1:
            while True:
                print("\nDime... ¿ A Cuántos FPS, Quieres Que Haga El Video ?\n")
                try:
                    cuantosfps = int(input())
                except:
                    continue
                if cuantosfps > 500:
                    print("\nLos FPS Deben Ser Menores A 500...")
                else:
                    break
            os.chdir("M8AX-Imagenes-Im_Pc_Hs")
            if hablo == 1:
                dime("Creando Video...")
            lanza = time.time()
            cuantospng = len(glob.glob("*.png"))
            print("")
            outv = cv2.VideoWriter(
                "M8AX-Video-Im_Pc_Hs.Mp4",
                cv2.VideoWriter_fourcc(*"h265"),
                cuantosfps,
                framesize,
            )
            print("")
            tiembarra = time.time()
            for filename in sorted(glob.glob("*.png"), key=os.path.getmtime):
                imgv = cv2.imread(filename)
                outv.write(imgv)
                nn = nn + 1
                barra_progreso_roja((nn * 100) / cuantospng, 100, tiembarra)
            barra_progreso_roja((cuantospng * 100) / cuantospng, 100, tiembarra)
            print("\n")
            print(*sorted(glob.glob("*.png"), key=os.path.getmtime), sep="\n")
            outv.release()
            termina = time.time()
            finiph = termina - lanza
            shutil.move(
                "M8AX-Video-Im_Pc_Hs.Mp4",
                "../../../M8AX-Video-Im-Pc-Hs - "
                + str(nn)
                + " Imágenes A "
                + str(cuantosfps)
                + " Fps - "
                + creadire
                + ".Mp4",
            )
            print(
                "\nTrabajo, Realizado Correctamente... Resolución De Video -"
                f" {width*3} x {height}. Duración Del Video -"
                f" {segahms(nn/cuantosfps,hablo)}. Tiempo De Proceso -"
                f" {round(finiph,3)} Segundos... A - {round((nn/finiph),3)} Imágenes,"
                " Procesadas Por Segundo...\n\nEso Es Todo... El Video Lo Encontrarás"
                " En El Directorio Raíz De Tu Virtual Environment...\n\nEspero Que"
                " Este Programa, Sea De Tu Agrado...\n\nSuscribete A Mi Canal De"
                " Youtube - https://youtube.com/m8ax"
            )
            if hablo == 1:
                dime(
                    "Video Creado. Tiempo De Generación,"
                    + str(round(finiph, 2))
                    + ", Segundos. A "
                    + str(round((nn / finiph), 2))
                    + " Imágenes, Procesadas Por Segundo. El Video Está En El"
                    " Directorio Raiz, De Tu Virtual Environment. Espero Que Este"
                    " Programa, Sea De Tu Agrado..."
                )
                dime(
                    "Reproduciendo Video. Por Cierto Dura... "
                    + str(segahms(nn / cuantosfps, hablo))
                    + ". La Resolución Del Video Es, "
                    + str(width * 3)
                    + " Por "
                    + str(height)
                    + "."
                )
            print(f"\nPulsa ESC, Para Salir De La Reproducción Del Video.")
            while True:
                isclosed = 0
                cap = cv2.VideoCapture(
                    "../../../M8AX-Video-Im-Pc-Hs - "
                    + str(nn)
                    + " Imágenes A "
                    + str(cuantosfps)
                    + " Fps - "
                    + creadire
                    + ".Mp4"
                )
                titulo = (
                    "M8AX-Video-Im-Pc-Hs - "
                    + str(nn)
                    + " Imagenes A "
                    + str(cuantosfps)
                    + " Fps - "
                    + creadire
                    + ".Mp4"
                )
                while True:
                    ret, frame = cap.read()
                    if ret == True:
                        cv2.imshow(titulo, frame)
                        if cv2.waitKey(30) == 27:
                            isclosed = 1
                            break
                    else:
                        break
                if isclosed:
                    break
            cap.release()
            cv2.destroyAllWindows()
        else:
            print(
                "\nVale... Pues Ya Está. Hasta Otro Rato... Adiós... Grácias Por Usarme"
                " Y No Te Olvides De Suscribirte, A Mi Canal De Youtube -"
                " https://youtube.com/m8ax"
            )
            if hablo == 1:
                dime("Vale, De Acuerdo...")
    if mimag != 1:
        print(
            "\nGrácias Por Usarme...\n\nSuscribete A Mi Canal De Youtube -"
            " https://youtube.com/m8ax"
        )
    if hablo == 1:
        dime("Grácias Por Usarme...")
    primiregg = np.random.randint(0, 2147483647, dtype=np.int32)
    print("\nTe Dejo Los Números Primos Del Día...\n")
    for k in range(500):
        if m8axPrimo(k + primiregg):
            contandopri = contandopri + 1
            print(str(k + primiregg) + ", ", end="")
            if contandopri % 10 == 0:
                print("\n")
    if contandopri % 10 == 0:
        print(f"\n{contandopri} Primos...")
    else:
        print(f"\n\n{contandopri} Primos...")
    if conso == 1:
        sys.stdout.close()

class SIZE_UNIT(enum.Enum):
    BYTES = 1
    KB = 2
    MB = 3
    GB = 4

def get_latents_from_seed(seed: int, width: int, height: int) -> np.ndarray:
    latents_shape = (1, 4, height // 8, width // 8)
    rng = np.random.default_rng(seed)
    image_latents = rng.standard_normal(latents_shape).astype(np.float32)
    return image_latents

def segahms(segundos, hablo):
    horas = int(segundos / 60 / 60)
    segundos -= horas * 60 * 60
    minutos = int(segundos / 60)
    segundos -= minutos * 60
    if hablo == 1:
        return f"{horas} Horas, {minutos} Minutos Y {int(segundos)} Segundos"
    else:
        return f"{horas}h:{minutos}m:{int(segundos)}s"

def convert_unit(size_in_bytes, unit):
    if unit == SIZE_UNIT.KB:
        return size_in_bytes / 1024
    elif unit == SIZE_UNIT.MB:
        return size_in_bytes / (1024 * 1024)
    elif unit == SIZE_UNIT.GB:
        return size_in_bytes / (1024 * 1024 * 1024)
    else:
        return size_in_bytes

def get_file_size(file_name, size_type=SIZE_UNIT.BYTES):
    size = os.path.getsize(file_name)
    return convert_unit(size, size_type)

def rgb_a_hex(rgb):
    return "%02x%02x%02x".upper() % rgb

def coloreando(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def centroid_histogram(clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)
    hist = hist.astype("float")
    hist /= hist.sum()
    return hist

def plot_colors(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0
    for percent, color in zip(hist, centroids):
        endX = startX + (percent * 300)
        cv2.rectangle(
            bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1
        )
        startX = endX
    return bar

def dime(voice):
    engine = pyttsx3.init()
    voces = engine.getProperty("voices")
    velocidad = engine.getProperty("rate")
    engine.setProperty("rate", velocidad - 10)
    engine.setProperty("voice", voces[5].id)
    engine.say(voice)
    engine.runAndWait()

def m8axPrimo(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1

def barra_progreso_roja(progreso, total, tiembarra):
    porcen = 100 * (progreso / float(total))
    segrestante = 0
    if porcen > 0:
        segrestante = (100 * (tiembarra - time.time()) / porcen) - (
            tiembarra - time.time()
        )
    barra = "█" * int(porcen) + "-" * (100 - int(porcen))
    print(
        (
            f"\r\033[38;2;{255};{0};{0}m|{barra}| - ETA - {segahms(segrestante*-1,0)} -"
            f" {porcen:.2f}%"
        ),
        end="\r\033[0m",
    )

def barra_progreso_vibrante(progreso, total, tiembarra):
    porcen = 100 * (progreso / float(total))
    segrestante = 0
    if porcen > 0:
        segrestante = (100 * (tiembarra - time.time()) / porcen) - (
            tiembarra - time.time()
        )
    barra = "█" * int(porcen) + "-" * (100 - int(porcen))
    print(
        (
            f"\r\033[38;2;{np.random.randint(0, 256)};{np.random.randint(0, 256)};{np.random.randint(0, 256)}m|{barra}|"
            f" - ETA - {segahms(segrestante*-1,0)} - {porcen:.2f}%"
        ),
        end="\r\033[0m",
    )

def capturas(nn, esperatimel, creadire):
    while True:
        captura = pyautogui.screenshot()
        try:
            captura.save(
                str(pathlib.Path().absolute())
                + "\M8AX-Imágenes_Finales"
                + "\M8AX-TimeLapse\M8AX-Captura-"
                + creadire
                + " - "
                + str(nn)
                + ".PnG"
            )
        except:
            captura.save(
                "..\M8AX-TimeLapse\M8AX-Captura-" + creadire + " - " + str(nn) + ".PnG"
            )
        cv2.waitKey(esperatimel)
        nn = nn + 1

if __name__ == "__main__":
    run()