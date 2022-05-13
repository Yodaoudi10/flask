import RPi.GPIO as GPIO             #Importe la bibliothèque pour contrôler les GPIOs
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)            #Définit le mode de numérotation (Board)
GPIO.setwarnings(False)             #On désactive les messages d'alerte
LED = 7                             #Définit le numéro du port GPIO qui alimente la led
GPIO.setup(LED, GPIO.OUT)           #Active le contrôle du GPIO
GPIO.output(LED, GPIO.LOW)          #On l’éteint
@app.route("/")
def main():
    etat_led = GPIO.input(LED)      # Lire l'etat de la LED
    if(etat_led == 0):              # Si l'etat de la LED == 0 , on affiche "OFF"
        etat_led = "OFF"
    else:                           # Sinon, on affiche "ON"
        etat_led = "ON"
        
    templateData = {
      'etat' : etat_led
      }
    # Transmettez les données du templateData dans le template index.html et renvoyez-le à l'utilisateur
    return render_template('index.html', **templateData)

@app.route("/<Pin>/<action>")
def action(Pin, action):
    Pin = int(Pin)

    if action =="on":               # Si on clique sur Turn on 
        GPIO.output(Pin, GPIO.HIGH) #On l'allume
    if action =="off":              # Si on clique sur Turn off
        GPIO.output(Pin, GPIO.LOW)  #On l'éteint

    etat_led = GPIO.input(Pin)      # Lire l'etat de la LED

    if(etat_led == 0):              # Si l'etat de la LED == 0 , on affiche "OFF"
        etat_led = "OFF"
    else:                           # Sinon, on affiche "ON"
        etat_led = "ON"
        
    templateData = {
        'etat' : etat_led
    }
    # Transmettez les données du templateData dans le template index.html et renvoyez-le à l'utilisateur
    return render_template('index.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)

    

