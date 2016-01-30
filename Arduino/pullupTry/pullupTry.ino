void setup() {
  // put your setup code here, to run once:
pinMode(7, INPUT_PULLUP);
Serial.begin(9600);
}

int value;

void loop() {
  // put your main code here, to run repeatedly:
value = digitalRead(7);
Serial.println(value);
delay(100);
}
