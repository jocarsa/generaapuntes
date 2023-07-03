import os
import pyautogui
import time
import pyperclip
import win32gui
from pynput.keyboard import Controller

def buscar(texto,anterior):
    encoding = 'utf-8'
    keyboard = Controller()
    
    delay1 = 1
    delay2 = 60
    print(pyautogui.position())
    #nuevo chat
    pyautogui.moveTo(100,100,delay1/2)
    pyautogui.click()
    time.sleep(delay1)
    #click en casilla de pregunta
    pyautogui.moveTo(900,950,delay1/2)
    pyautogui.click()
    time.sleep(delay1)
    #escribir pregunta
    if texto[3] == "folder":
        if texto[2] > 2:
            pregunta = "dame una explicación en lenguajes de marcas, con ejemplos de código si procede (incluyendo el termino 'Jose Vicente Carratala', con respecto a: "
        else:
            pregunta = "dame una explicación en lenguajes de marcas, sin ejemplos de código, con respecto a: "
        pregunta += texto[0].replace("/"," ").replace("C:","").replace("/"," ").replace("-"," ")
        pregunta += ", realiza una explicación de forma impersonal."
        #pyautogui.typewrite(pregunta, interval=0.1, encoding=encoding)
        for char in pregunta:
            keyboard.type(char)
            pyautogui.sleep(0.1)  # Add a slight delay between each character
    if texto[3] == "file":
        if "creaejercicio" in texto[0]:
            pregunta = "crea un ejemplo de código, primero expon el código completo, y luego explícalo paso a paso, usando 'Jose Vicente Carratala', de: "
            pregunta += texto[0].replace("/"," ").replace("C:","").replace("/"," ").replace("-"," ")
            pregunta += ", realiza una explicación de forma impersonal."
            for char in pregunta:
                keyboard.type(char)
                pyautogui.sleep(0.1)  # Add a slight delay between each character
        else:
            if not "jercicio" in texto[0]:
                pregunta = "toma este código en python, realiza una introduccion teorica, luego pon el código, y a continuación realiza un comentario linea a linea, primero mostrando el código y luego poniendo el comentario, simulando, cuando sea posible, la ejecución en la consola:"
                with open(texto[0], "rb") as file:  
                    content = file.read()  
                    decoded_content = content.decode("utf-8")
                    pregunta += decoded_content
                    pyperclip.copy(pregunta)
                    pyautogui.hotkey("ctrl", "v")
            else:
                print(anterior)
                if os.path.isdir(anterior[0]):
                    pregunta = "toma este código en python, realiza una introduccion teorica, luego pon el código, y a continuación realiza un comentario linea a linea, primero mostrando el código y luego poniendo el comentario, simulando, cuando sea posible, la ejecución en la consola:"
                    with open(texto[0], "rb") as file:  
                        content = file.read()  
                        decoded_content = content.decode("utf-8")
                        pregunta += decoded_content
                        pyperclip.copy(pregunta)
                        pyautogui.hotkey("ctrl", "v")
                else:
                    archivo1 = open(texto[0], "rb")
                    archivo2 = open(anterior[0], "rb")
                    pregunta = "indica las diferencias entre este codigo "
                    pregunta += archivo1
                    pregunta += "y este codigo"
                    pregunta += archivo2
                    pyperclip.copy(pregunta)
                    pyautogui.hotkey("ctrl", "v")
            
    pyautogui.press('enter')
    time.sleep(delay2)
    #subir scroll
    pyautogui.moveTo(1918,83,delay1/2)
    pyautogui.click()
    time.sleep(delay1)
    pyautogui.click()
    time.sleep(delay1)
    pyautogui.click()
    time.sleep(delay1)
    #scroll hacia abajo
    for i in range(0,10):
        pyautogui.press('down')
        #copiar texto
        location = pyautogui.locateOnScreen("copiar.png")
        try:
            pyautogui.moveTo(location[0]+15,location[1]+15,0)
            pyautogui.click()
        except:
            pass
        time.sleep(delay1)
    #segunda pestaña
    pyautogui.moveTo(348,12,delay1/2)
    pyautogui.click()
    time.sleep(delay1)
    if texto[3] == "folder":
        # estilos
        pyautogui.moveTo(341,156,delay1/2)
        pyautogui.click()
        time.sleep(delay1)
        # estilo 1
        if texto[2] == 0:
            pyautogui.moveTo(378,284,delay1/2)
        if texto[2] == 1:
            pyautogui.moveTo(378,425,delay1/2)
        if texto[2] == 2:
            pyautogui.moveTo(378,494,delay1/2)
        if texto[2] == 3:
            pyautogui.moveTo(378,568,delay1/2)
        if texto[2] == 4:
            pyautogui.moveTo(378,645,delay1/2)
        if texto[2] == 5:
            pyautogui.moveTo(378,713,delay1/2)
        if texto[2] == 6:
            pyautogui.moveTo(378,777,delay1/2)
        pyautogui.click()
        time.sleep(delay1)
    # final de pagina
    pyautogui.moveTo(1857,1010,delay1/2)
    pyautogui.click()
    time.sleep(delay1)
    # escribir
    if texto[3] == "file":
        pyautogui.hotkey("ctrl", "b")
        time.sleep(delay1)
    if "-" in texto[1]:
        #pyautogui.typewrite(texto[1].split("-")[1], interval=0.1, encoding=encoding)
        for char in texto[1].split("-")[1]:
                keyboard.type(char)
                pyautogui.sleep(0.1)  # Add a slight delay between each character
    else:
        #pyautogui.typewrite(texto[1], interval=0.1, encoding=encoding)
        for char in texto[1]:
                keyboard.type(char)
                pyautogui.sleep(0.1)  # Add a slight delay between each character
    if texto[3] == "file":
        pyautogui.hotkey("ctrl", "b")
        time.sleep(delay1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(delay1)
    #estilos
    pyautogui.moveTo(341,156,delay1/2)
    pyautogui.click()
    time.sleep(delay1)
    #parrafo
    pyautogui.moveTo(378,207,delay1/2)
    pyautogui.click()
    time.sleep(delay1)
    # menu editar
    pyautogui.moveTo(147,117,delay1/2)
    pyautogui.click()
    time.sleep(delay1)
    # menu pegar
    pyautogui.moveTo(171,297,delay1/2)
    pyautogui.click()
    time.sleep(delay1)
    pyautogui.press('enter')
    time.sleep(delay1)
    # pestaña 1
    pyautogui.moveTo(125,14,delay1/2)
    pyautogui.click()
    time.sleep(delay1)

directory = "C:/marcas/001-Lenguajes de marcas y sistemas de gestión de la información/"

def get_last_file_or_folder(path):
    last_item = os.path.basename(path)
    return last_item

def get_files_and_folders(directory, depth=1):
    items = []
    for item in os.listdir(directory):
        if item[0] != ".":
            path = os.path.join(directory, item)
            if os.path.isfile(path):
                items.append((path, get_last_file_or_folder(path),depth,"file"))
                
            else:
                items.append((path, get_last_file_or_folder(path), depth,"folder"))
                items.extend(get_files_and_folders(path, depth + 1))
    return items



raiz = get_files_and_folders(directory)
print(raiz)
for i in range(0,len(raiz)):
    #if elemento[3] == "folder":
        buscar(raiz[i],raiz[i-1])
    
