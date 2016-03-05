#define buttonPin 7
#define feedPin 10

bool wasTouching = false;
String value;
String receivedText;
int feedTime = 1000; //default = 1000ms
bool feederOn = false;
unsigned long feederStartTime;


void setup() {
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
    //checking the button state, possibly sending PUSHED signal
    if (digitalRead(buttonPin) == LOW && wasTouching == false)
    {
      Serial.print("PUSHED");
      wasTouching = true;
      delay(50); //simple debounce?
    }
    if (digitalRead(buttonPin) == HIGH)
    {
      wasTouching = false;
    }

    //checking if some command was received
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
        digitalWrite(feedPin, HIGH);
        feederOn = true;
        feederStartTime = millis();
      }

      /*else if (receivedText.startsWith("SETFEEDTIME"))
      {
        char tempFeedTime = receivedText.substring(11,12)
        feedTime = (tempFeedTime - '0')*1000;
      }
      */
      
      else if (receivedText == "SETFEEDTIME")
      {
        delay(500);
        int givenTime = Serial.readString().toInt();
        if (givenTime > 500)
        {
          feedTime = givenTime;
        }
        
        //flush remaining stuff
        while (Serial.available() > 0)
        {
          Serial.read();
        }
      }

      else if (receivedText == "TELLFEEDTIME")
      {
        Serial.print(feedTime);
      }
    }

    //if feeder is on longer that feedTime, shut it down
    if ((feederOn == true) && (millis() - feederStartTime > feedTime))
    {
      digitalWrite(feedPin, LOW);
      feederOn = false;
    }
    delay(20);
    
  }
}

void loop() {
  if (Serial.available()>0)
  {
    value = Serial.readString();
    if (value == "STOP")
    {
      working();
    }
  }
  Serial.print("CX37");
  delay(1000);
}
