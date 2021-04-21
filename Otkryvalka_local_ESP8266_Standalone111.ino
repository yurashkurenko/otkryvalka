//*************************************************************
//  Download latest Blynk library here:
//    https://github.com/blynkkk/blynk-library/releases/latest
//
//  Blynk is a platform with iOS and Android apps to control
//  Arduino, Raspberry Pi and the likes over the Internet.
//  You can easily build graphic interfaces for all your
//  projects by simply dragging and dropping widgets.
//
//    Downloads, docs, tutorials: http://www.blynk.cc
//    Sketch generator:           http://examples.blynk.cc
//    Blynk community:            http://community.blynk.cc
//    Follow us:                  http://www.fb.com/blynkapp
//                                http://twitter.com/blynk_app
//
//  Blynk library is licensed under MIT license
//  This example code is in public domain.
//
// *************************************************************
//  This example runs directly on ESP8266 chip.
//
//  Note: This requires ESP8266 support package:
//    https://github.com/esp8266/Arduino
//
//  Please be sure to select the right ESP8266 module
//  in the Tools -> Board menu!
//
//  Change WiFi ssid, pass, and Blynk auth token to run :)
//  Feel free to apply it to any other example. It's simple!
// *************************************************************/

/* Comment this out to disable prints and save space */
#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "Pgwp0VQRgM_lUN_ai-o3z9YW5c7cRCrK";

// Your WiFi credentials.
// Set password to "" for open networks.
const int BUTTON = 4;     // номер входа, подключенный к кнопке
const int LED =  2;      // номер выхода светодиода
const int BLOCK = 12;
const int UNBLOCK = 14;
const int RELE = 2;
int rele = 0;
int engon = 1;
int buttonState = 0;         // переменная для хранения состояния кнопки
char ssid[] = "OnePlus 8 Pro";
char pass[] = "fb85954e4b1b";
IPAddress ipown  (192,168,178,103);
BlynkTimer timer;
BlynkTimer timer2;
// This function tells Arduino what to do if there is a Widget
// which is requesting data for Virtual Pin (5)
BLYNK_WRITE(V8)
{
  // This command writes Arduino's uptime in seconds to Virtual Pin (5)
  Blynk.virtualWrite(V0, 1);
  digitalWrite(UNBLOCK, engon);
}
BLYNK_WRITE(V9)
{
  // This command writes Arduino's uptime in seconds to Virtual Pin (5)
  Blynk.virtualWrite(V0, 0);
  digitalWrite(BLOCK, engon);
}
void myTimerEvent()
{
  // You can send any value at any time.
  // Please don't send more that 10 values per second.
  Blynk.virtualWrite(V8, 0);
  digitalWrite(BLOCK, !engon);
  Blynk.virtualWrite(V9, 0);
  digitalWrite(UNBLOCK, !engon);
}
void myTimerEvent2()
{
  // You can send any value at any time.
  // Please don't send more that 10 values per second.
  
  // считываем значения с входа кнопки
  pinMode(BUTTON, INPUT);
  pinMode(LED, OUTPUT);
  buttonState = digitalRead(BUTTON);
  // проверяем нажата ли кнопка
  // если нажата, то buttonState будет HIGH:
  buttonState=!buttonState;
  digitalWrite(LED, buttonState); 
  Blynk.virtualWrite(V10, buttonState);
 }




void setup()
{
  // Debug console
  // инициализируем пин, подключенный к светодиоду, как выход
  pinMode(LED, OUTPUT);     
  pinMode(BLOCK, OUTPUT);
  pinMode(UNBLOCK, OUTPUT);
  // инициализируем пин, подключенный к кнопке, как вход
  pinMode(BUTTON, INPUT);   

  Serial.begin(9600);

//#  Blynk.begin(auth, ssid, pass);
  Blynk.begin(auth, ssid, pass, ipown, 8080);
  timer.setInterval(3000L, myTimerEvent);
  timer2.setInterval(1000L, myTimerEvent2);
}

void loop()
{
  Blynk.run();
  timer.run(); // Initiates BlynkTimer
  timer2.run(); // Initiates BlynkTimer
}
