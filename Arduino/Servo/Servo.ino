#include <Servo.h>
Servo ser;
void setup() {
  // put your setup code here, to run once:
ser.attach(11);
Serial.begin(9600);
}
int analog;
int x;
void loop() {
  // put your main code here, to run repeatedly:
analog = analogRead(A0);
x = map(analog, 0, 1023, 180, 0);
Serial.println(x);
ser.write(x);
delay(10);
}
