from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import string
import random
import sys
import argparse
import time

screenWidth, screenHeight = pyautogui.size()
browser=Chrome()
browser.get('https://www.cuantocabron.com/login')
browser.maximize_window()
#Rand para crear strings, de largo 10 aleatorios.
def stringR(size=10, chars=string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size))
#Randon para crear strings, que luego al ser concatenados con un @gmail.com, se crea un correo aleatorio.
def correoR(largo): 
    return ''.join(random.choice(string.ascii_letters) for x in range(largo))   
#función para escribir cada letra con delta de tiempo, similar a un humano
def escrituraD(elemento, texto): 
    for character in texto:
        elemento.send_keys(character)
        time.sleep(0.3)
#función creada para poder salir o modificar la contraseña
def dentroLogin(): 
        print ('Ingrese 0 para terminar, o 1 para modificar la contraseña')
        loginop = int(input())
        if (loginop == 0):
             print ('Finalizado')
        elif (loginop == 1):
             browser.get('https://mi.cuantocabron.com/cuenta')
             passwordCCold = browser.find_element_by_id('password1') #contraseña antigua
             passwordCCold.send_keys('admin1')
             passwordCCnueva = browser.find_element_by_id('password2') #nueva contraseña
             passwordNueva = stringR()
             passwordCCnueva.send_keys(passwordNueva)
             rpasswordCCnueva = browser.find_element_by_id('password3') #Repite nueva contraseña
             rpasswordCCnueva.send_keys(passwordNueva)
             button = browser.find_element_by_id('send_profile') # Guardar nueva contraseña
             print ('contraseña cambiada')
        else:
            print ('error')


def RegistroC(): #Registro de cuenta con datos aleatorios en CC.
    pyautogui.click(507, 455) #clickea el botón de registro 
    usuarioCC = browser.find_element_by_id('input-register-username') #Obtiene id de usuario en la página
    escrituraD(usuarioCC, stringR()) # Ingresa un usuario aleatorio
    emailCC = browser.find_element_by_id('input-register-email') #Obtiene el ID de mail
    emailCCunico = correoR(8) + '@gmail.com' #Crea un mail aleatorio y luego lo concatena con @gmail.com
    escrituraD(emailCC, emailCCunico) # Ingresa el mail generado anteriormente
    remailCC = browser.find_element_by_id('input-register-email_confirm') #Obtiene el ID de mail (reingreso)
    escrituraD(remailCC, emailCCunico) # Ingresa el mail generado anteriormente
    passwordCC = browser.find_element_by_id('input-register-password') #Se busca el ID de contraseña
    passwordCCunica = stringR() #Se crea una contraseña aleatoria
    escrituraD(passwordCC, passwordCCunica) # Ingresa la contraseña generada anteriormente
    rpasswordCC = browser.find_element_by_id('input-register-password_confirm') #Se busca el ID de contraseña (reingreso)
    escrituraD(rpasswordCC, passwordCCunica) # Ingresa la contraseña generada anteriormente
    button = browser.find_element_by_id('input-register-privacy') #se busca ubic de los términos y condiciones
    button.click() #Se clickea el botón del ToS
    button = browser.find_element_by_id('input-register-submit') #se busca el botón de registro
    button.click() #Se ingresa a botón de registro luego de ingresar todos los datos, si o si hay que hacer un captcha manualmente
    time.sleep (45) #Hay un rango de 45 segundos para ingresar el captacha manualmente
    try: # Verifica si se paso el captcha o no
        button = browser.find_element_by_id('input-register-submit') 
        print ('Registro completado')
    except NoSuchElementException:
        print ('Registro completado')

def LoginC():
    username = browser.find_element_by_id('input-login-username') #encuentra el id de usuario para login
    escrituraD(username, 'adminset') #con la función escrituraD se escribe lentamente letra por letra
    #username.send_keys('x.chika19@gmail.com') 
    password = browser.find_element_by_id('input-login-password') #encuentra donde poner password en el formulario
    escrituraD(password, 'admin1')
 
    button = browser.find_element_by_id('input-login-submit') #busca el botón para ingresar
    button.click() #lo apreta
    time.sleep(30) #la página pide captcha la primera vez, se dan 30 segundos para ingresarlo (al hacerlo muchas veces con la misma IP, el tiempo de cada captacha sube mucho si estos son fallados)
    try: #verifica si se pudo hacer login luego de completar el captcha
        browser.find_element_by_id('input-login-submit') #si se realizó el captcha manualmente, verifica si existe el botón para nuevamente hacer login
        button.click() #apreta el botón nuevamente luego del captcha
        dentroLogin() #opciones dentro del login para salir o modificar contraseña
    except NoSuchElementException: #en caso de que no vea el botón de login
        dentroLogin() #opciones dentro del login para salir o modificar contraseña


def RestablecerC():
    button = browser.find_element_by_id('tab-reset-password') #se busca el botón de restablecimiento de contraseña
    button.click() #Se clickea en el botón de recuperación de contraseña
    print ('seleccione si poner correo random o uno en específico, con 1 o 2 respectivamente')
    mailopcion = int(input("Ingresa la opción : "))
    if (mailopcion == 1):
        username = browser.find_element_by_id('input-reset-email')
        emailBunicoR = correoR(8) + '@gmail.com' #Crea un mail aleatorio y luego lo concatena con @gmail.com
        escrituraD (username, emailBunicoR)
        button = browser.find_element_by_id('input-reset-submit') #se busca el botón de restablecer contraseña
        button.click() #Se clickea en el botón de reset de contraseña luego de ingresar el correo
    elif (mailopcion == 2):
        correoreal = input("Ingresa el correo al cual se le quiere recuperar la contraseña : ")
        username = browser.find_element_by_id('input-reset-email')
        escrituraD (username, correoreal)
        button = browser.find_element_by_id('input-reset-email') #se busca el botón de restablecer contraseña
        button.click() #Se clickea en el botón de reset de contraseña luego de ingresar el correo
    else:
        print ('error')

print ('Selecciona 1 para Login\n, 2 Para Registro\ 3 para restablecer contraseña')
opcion = int(input("Ingresa la opción : "))
if (opcion == 1):
    LoginC()
elif (opcion == 2):
    RegistroC()
elif (opcion == 3):
    RestablecerC()
else:
    print ('error')