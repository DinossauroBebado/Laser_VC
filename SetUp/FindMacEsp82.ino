//--------------------------------------------------------------------------------------------
//-----Projeto: Find MAC ESP82                                                                     ---------
//-----Titulo:                                                                       ---------
//-----Autor:@dinossauro.bebado/@DinossauroBbad1                                     ---------
//-----Objetivo :                                                                    ---------
//-----Data :                                                                        ---------
//--------------------------------------------------------------------------------------------
#include <ESP8266WiFi.h>

void setup(){
  Serial.begin(115200);
  Serial.println();
  Serial.print("ESP8266 Board MAC Address:  ");
  Serial.println(WiFi.macAddress());
}
 
void loop(){

}
