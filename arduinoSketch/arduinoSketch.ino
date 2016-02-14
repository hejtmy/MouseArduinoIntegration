#define buttonPin 7
#define feedPin 10

bool wasTouching = false;
String value;
String receivedText;
int feedTime = 1000; //default = 1000ms
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
      Serial.print("PUSHED\n");
      wasTouching = true;
      //delay(100); //to eliminate multiple times push?
    }
    
    if (digitalRead(buttonPin) == HIGH)
    {
      wasTouching = false;
    }

    if (Serial.available() > 0)
    {
      receivedText = Serial.readString();
      if (receivedText == "REPEAT\n")
      {
        wasTouching = false;
        break;
        //alternatively loop()
      }
      else if (receivedText == "FEEDMOUSE\n")
      {
        feed();
      }
      else if (receivedText == "SETFEEDTIME\n")
      {
        delay(500);
        feedTime = (Serial.read() * 1000)
        while (Serial.available() > 0)
        {
          Serial.read()
        }
      }
    }
    delay(50);
  }
}

void feed()
{
  digitalWrite(feedPin, HIGH); //start feeder
  delay(feedTime); //time of feeder rotation
  digitalWrite(feedPin, LOW); //stop feeder

  while (Serial.available() > 0)
  {
    Serial.read()
    //flush any signal, that was received meanwhile, for example more signals to feed the mouse (unwanted multiple button push)
  }

}

void loop() {
  Serial.print("CX37\n");
  
  if (Serial.available()>0)
  {
    value = Serial.readString();
    if (value == "STOP\n")
    {
      working();
    }
  }
  delay(1000);
}
