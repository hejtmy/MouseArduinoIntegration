void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(7, INPUT);
}

bool sendCode = true;
bool wasTouching = false;
String value = "";

void sendTouch()
{
  while(true)
  {
    if (digitalRead(7) == HIGH && wasTouching == false)
    {
      Serial.println("pushed");
      wasTouching = true;
      if (digitalRead(7) == LOW)
      {
        wasTouching = false;
      }
    }
    if (Serial.available()>0 && Serial.readString()=="REPEAT")
      {
        break;
        //alternatively loop()
      }
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  if (sendCode == true)
  {
    Serial.print("CX37\n");
    delay(1000);
    if (Serial.available()>0)
    {
      String value = Serial.readString();
      if (value == "STOP")
      {
        sendTouch();
      }
    }
  }
}
