/////////////// pin initilisation /////////////
// LED pin intlisation 
const int Ledpin = 5; 

// Distance sensor pins intlisation 
const int echopin =  2; 
const int triggerpin =  3; 

// Light resistor pins intlisation 
const int LDRpin = A3;

void setup() 
{
  Serial.begin(9600);


  // Instructs pins to ouput 
  pinMode(Ledpin ,OUTPUT); // output --> turn light on/off
  pinMode(triggerpin,OUTPUT); // output --> Outputs a trigger an ultrasonic sound pluse
  pinMode(echopin,INPUT);// This outputs the pluse 
  }
  void loop() 
  {
    /////////////// Measruing light level outside/////////////// 
    //reading the light resistor analog pin 
    int LDRvalue = analogRead(LDRpin);

    /////////////// Triggering sound waves/////////////// 
  //Rseating the trigger pin for 2 microseconds
  digitalWrite(triggerpin,LOW);
  delayMicroseconds(2);
  //Trigger the ultrasonic sound pluses for 10 microseconds
  digitalWrite(triggerpin,HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerpin,LOW);

  /////////////// Distance calculation/////////////// 
  // Setting Time to the echo pin 
  long Time = pulseIn(echopin,HIGH);
  int Distance = Time * 0.034/ 2; 

  int expected_distance = 100; // Distance of room when empty --> limitation as it inaccuracte 
  
  if(Distance < expected_distance && LDRvalue < 100)
  { 
      digitalWrite(Ledpin,HIGH);
      
     // Serial.print(" on ");

      Serial.print(Distance);
      Serial.println(" cm ");
      Serial.print(LDRvalue);
      
  }

  else
  {
    digitalWrite(Ledpin,LOW); 
    //Serial.print(" off ");
    Serial.print(LDRvalue);
    Serial.print(Distance);
    Serial.println(" cm "); 
   
  }


}
