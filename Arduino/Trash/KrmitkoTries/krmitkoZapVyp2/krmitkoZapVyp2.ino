#define feedPin 10

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
Serial.setTimeout(20);
pinMode(feedPin, OUTPUT);
digitalWrite(feedPin, LOW);
}

bool state = false;

void loop() {
  // put your main code here, to run repeatedly:
String ard;
while (Serial.available() == 0)
{}

ard = Serial.readString();

if (ard == "zap")
  {
    digitalWrite(feedPin, HIGH);
    if (state == false)
    {
      Serial.println("ZAPINAM");
      state = true;
    }
  }

if (ard == "vyp")
  {
    digitalWrite(feedPin, LOW);
    if (state == true)
    {
      Serial.println("VYPINAM");
      state = false;
    }
  }
}
