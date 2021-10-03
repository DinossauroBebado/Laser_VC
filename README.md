# Laser
## This repo is about a wireless laser that is  controled remotely by Serial Comunication
### I'm using with openCv to track a tennis ball 
![image off the laser with a red flare and blue background](https://cdn.discordapp.com/attachments/884602011708969020/893654496377450516/tumb.png)

<p> In this case I'm using a Python sript </p> 
<p>Work's with two Esp 8266 and the ESP-NOW protocol</p>
So there is an Esp Main that is conected to the computer via USB and it's job is to receive the serial data parse it and send to the ESP Child via the protocol
<p> When received the data is maped to the servos degres of operation and send it to the X and Y Servos </p> 

![alt text](https://cdn.discordapp.com/attachments/884602011708969020/893654554577600522/img2.png)

### Eletronics

<p>The eletronics is a laser diode controled by an transistor and a analog level converter because the laser and the servos works best with 5v while the eso is 3.3V even so it´s powered by 5V </p>

#### Parts List

* Esp 8266 NodeMCU
* 2 MG90S Tower Pro Micro Servo (Metal gears are importante for my heart) 
* I2C Logic Converter Biderecional Module 5V<->3.3V
* 300 Ω resistor 
* 0.1 micro Faraday more than 5v Resistor
* A Switch of your choice 
* Laser Diode with internal resistor 

![alt text](https://cdn.discordapp.com/attachments/884602011708969020/893654528354844693/img1.png)

### Code

| Code          | About        
| ------------- |:-------------:|
| [Master.cpp](https://github.com/DinossauroBebado/Laser/tree/main/VisualRec_Torret_MASTER/src)     |Code uploaded  to the masters ESP | 
| [Chield.cpp](https://github.com/DinossauroBebado/Laser/tree/main/VisualRec_Torret_SLAVE/src)      |Code uploaded  to the child |
| [Main.py](https://github.com/DinossauroBebado/Laser/blob/main/InterfaceVC/main.py)      |Main code with the integration : Begin Here|
| [SerialComMouse.py](https://github.com/DinossauroBebado/Laser/blob/main/InterfaceVC/SerialComMouse.py) |If you want to control the laser with your mouse|
| [Indentificar.py](https://github.com/DinossauroBebado/Laser/blob/main/InterfaceVC/identificar.py) |The function for face and the ball recognition |
| [FindHSVValues.PY](https://github.com/DinossauroBebado/Laser/blob/main/InterfaceVC/FindHSVValues.PY)|Code to adjust the HSV values for the ball recognition function otmization|

## Dependencies

Here i'm using Platoform.io to upload to the microcontroler so this is because there is so much set up files.And you will need to install some things to make the esp and servo libs to work  some quick google should work.In case you want to use the Arduino IDE just delet the #include <Arduino.h> and install the servo.h lib with the esp in the IDE
### ESP 
    #include <ESP8266WiFi.h>
    #include <espnow.h>
    #include <Servo.h>
### Python 
    pip pip install opencv-python
    pip install tkinter
#SetUp

In the python code you need to change the usb port in the SerialComunication.py

In the esp master  change the `int8_t broadcastAddress[]` variable to the Child mac adress to figure this out [HERE](https://github.com/DinossauroBebado/Laser/blob/main/SetUp/FindMacEsp82.ino)
<br>
<br>
<br>
PS: This is my first try at writing documentacion so any problem feel free to contact me. :P

