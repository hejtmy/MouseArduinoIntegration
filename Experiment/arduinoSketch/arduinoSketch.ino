void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(7, INPUT_PULLUP);
}

bool sendCode = true;
bool wasTouching = false;
String value = "";

void sendTouch()
{
  while(true)
  {
    if (digitalRead(7) == LOW && wasTouching == false)
    {
      Serial.print("PUSHED\n");
      wasTouching = true;
    }
    
    if (digitalRead(7) == HIGH)
    {
      wasTouching = false;
    }
    
    if (Serial.available()>0 && Serial.readString()=="REPEAT")
    {
        wasTouching = false;
        break;
        //alternatively loop()
    }
    delay(50);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  if (sendCode == true)
  {
    Serial.print("CX37\n");
    if (Serial.available()>0)
    {
      value = Serial.readString();
      if (value == "STOP")
      {
        sendTouch();
      }
    }
    delay(1000);
  }
}
