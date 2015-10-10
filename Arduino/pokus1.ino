int buttonState;
int previousState = 0;

void setup()
{
pinMode(2, INPUT);
Serial.begin(9600);
}

void loop() 
{
buttonState = digitalRead(2);
if(buttonState==1 && previousState==0)
{
  Serial.println(buttonState);
}
previousState=buttonState;
delay(100);
}
