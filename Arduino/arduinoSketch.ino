#define buttonPin 7
#define feedPin 10

bool wasTouching = false;
String value;
String receivedText;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
Serial.setTimeout(20);
pinMode(buttonPin, INPUT_PULLUP);
pinMode(feedPin, OUTPUT);
digitalWrite(feedPin, LOW);
}

void working()
{
  while(true)
  {
    if (digitalRead(buttonPin) == LOW && wasTouching == false)
    {
      Serial.print("PUSHED");
      wasTouching = true;
    }
    
    if (digitalRead(buttonPin) == HIGH)
    {
      wasTouching = false;
    }

    if (Serial.available() > 0)
    {
      receivedText = Serial.readString();
      if (receivedText == "REPEAT")
      {
        wasTouching = false;
        break;
        //alternatively loop()
      }
      else if (receivedText == "FEEDMOUSE")
      {
        feed();
      }
    }
    delay(50);
  }
}

void feed()
{
  digitalWrite(feedPin, HIGH); //start feeder
  delay(2000); //time of feeder rotation
  digitalWrite(feedPin, LOW); //stop feeder

  //smazat, jen kontrola prijmuti signalu pro krmeni
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
  delay(200);
  digitalWrite(13, LOW);
//  while (Serial.available() > 0)
//  {
//    Serial.read()
//    //flush any signal, that was received meanwhile, for example more signals to feed the mouse (unwanted multiple button push)
//  }
}

void loop() {
  Serial.print("CX37");
  
  if (Serial.available()>0)
  {
    value = Serial.readString();
    if (value == "STOP")
    {
      working();
    }
  }
  delay(1000);
}
