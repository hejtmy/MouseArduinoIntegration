void setup()
{
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  digitalWrite(2, LOW);
}

String repeat;
int opakovani;
bool prev = 1;

void flash(int repeat) //funkce ktera zablika pozadovanym poctem
{
  for (int i=0; i<repeat; i++)
  {
    digitalWrite(2, HIGH);
    delay(200);
    digitalWrite(2, LOW);
    delay(200);
  }
}

void loop() 
{
  if (prev == 1)
  {
    Serial.println("Arduino vola python! Zadat hodnotu!");
    prev = 0;
  }
  
  if (Serial.available() > 0) //pokud jsou v bufferu data
  {
      repeat = Serial.readString(); //precist string od pythonu, musi to byt int
      opakovani = repeat.toInt(); //ziskat ze stringu integer
      flash(opakovani); //zavolat funkci blikani
      prev = 1;
  }
}
