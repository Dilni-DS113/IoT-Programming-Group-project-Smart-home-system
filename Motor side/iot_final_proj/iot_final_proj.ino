// Include the AccelStepper Library
#include <AccelStepper.h>

// Define step constant
#define FULLSTEP 8

// Creates an instance
// Pins entered in sequence IN1-IN3-IN2-IN4 for proper step sequence
AccelStepper myStepper(FULLSTEP, 8, 10, 9, 11);

int soundSensor=2;
boolean BlindStatus=false;

void setup() {
  Serial.begin(9600);
  // set the maximum speed, acceleration factor,
  // initial speed and the target position
  myStepper.setMaxSpeed(1000.0);
  myStepper.setAcceleration(50.0);
  myStepper.setSpeed(200);
//  myStepper.moveTo(2038);
  pinMode(soundSensor,INPUT);
}

void loop() {
  myStepper.run();
  if (myStepper.distanceToGo() == 0) {
    int SensorData=digitalRead(soundSensor);
    if(SensorData==1){
      if (BlindStatus==false) {
        BlindStatus=true;
        myStepper.moveTo(2038);
        Serial.println("BlindsClosed");
      }
      else {
        BlindStatus=false;
        myStepper.moveTo(-myStepper.currentPosition());
        Serial.println("BlindsOpen");
        
      }
    }    
  }
}
