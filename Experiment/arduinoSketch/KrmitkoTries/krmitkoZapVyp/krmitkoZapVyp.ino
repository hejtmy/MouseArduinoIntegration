void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(7, OUTPUT);
digitalWrite(7, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
String ard;
bool state = false;
while (Serial.available() == 0)
{}

ard = Serial.readString();
if (ard == "zap")
  {
    digitalWrite(7, HIGH);
    if (state == false)
    {
      Serial.println("ZAPINAM");
      state = true;
    }
  }

if (ard == "vyp")
  {
    digitalWrite(7, LOW);
    if (state == true)
    {
      Serial.println("VYPINAM");
      state = false;
    }
  }
}
