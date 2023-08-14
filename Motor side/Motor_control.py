import serial
import time
from flask import Flask, render_template
import pymysql
# import paho.mqtt.publish as publish
# import paho.mqtt.client as mqtt

app = Flask(__name__)

# Dictionary of pins with name of pin and state ON/OFF
pins = {

    2  : {'name' : 'motor', 'state' : 0 }
    }
    
# Main function when accessing the website
@app.route("/")
def index():
    # TODO: Read the status of the pins ON/OFF and update dictionary
    
    #This data wii be sent to index.html (pins dictionary)
    templateData = { 'pins' : pins }
    # Pass the template data into the template index.html and return it
    return render_template('index.html', **templateData)

# Function with buttons that toggle depending on the status
@app.route("/<changePin>/<toggle>")
def toggle_function(changePin, toggle):
#     get_data()
    # Convert the pin from the URL into an interger:
    changePin = int(changePin)
    # Get the device name for the pin being chnaged:
    # If the action part of the URL is "on," execute the code intended below:
    if (toggle == "on" or sql == "BlindsClosed"):
                #Set the pin high
        if changePin == 2:
            ser.write(b"1")
            pins[changePin]['state'] = 1
        #Save the status message to be passed into the template:
        message = "The blinds are now closed" 

    if (toggle == "off" or sql == "BlindsOpen"):
        if changePin == 2:
            ser.write(b"2")
            pins[changePin]['state'] = 0
        #Set the pin low
        message = "The blinds are now open" 
    
    #This data wii be sent to index.html (pins dictionary)
    templateData = { 'pins' : pins }
    
    # Pass the template data into the template index.html and return it
    return render_template('index.html', **templateData)

#Function to send simple commands
# @app.route("/<action>")
# def action(action):
#     if action == 'action3':
#         ser.write(b"3")
#         pins[2]['state'] = 0
#     if action == 'action4':
#         ser.write(b"4")
#         pins[2]['state'] = 1
# #     
# #     #This data wii be sent to index.html (pins dictionary)
#     templateData = { 'pins' : pins }
# #     
# #     # Pass the template data into the template index.html and return it
#     return render_template('index.html', **templateData    # Main function, set up serial bus, indicate port for the webserver,
# ans start the service.
        
def get_data():
    try:
        dbConn = pymysql.connect(host = 'localhost', user='pi', password='', database='motorstate_db') or die("Connection failed")
        with dbConn: 
            cursor = dbConn.cursor()
            sql = "SELECT TOP 1 'state' FROM 'motorLog' ORDER BY 'stateId' DESC"
            cursor.execute(sql)
            return sql
    except Exception as e:
        print(e)
        return "nothing"

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyS0', 9600, timeout = 1)
    ser.flush()
    app.run(host='0.0.0.0', port = 80, debug = True)

