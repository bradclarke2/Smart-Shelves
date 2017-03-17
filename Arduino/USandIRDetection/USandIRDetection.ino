#include <SharpIR.h>

// Sonar Definitions
// Pins

// Anything over 400 cm (23200 us pulse) is "out of range"
const unsigned int MAX_DIST = 23200;

// IR Definitions
#define ir A0
#define model 1080
SharpIR sharp(ir, 25, 93, model); // ir: sesnsor port, 25: number of readings. 93: % difference between two measurements. model: 1080 for GP2Y0A21Y or 20150 for GP2Y0A02Y


int TableSizeX = 3;
int TableSizeY = 3;

// Sonar Definitions
const int SonarPinConfig[TableSizeX * TableSizeY][3] = 
{ 
{1, 1, 2},
{2, 3, 4},
{3, 5, 6},
{4, 7, 8},
{5, 9, 10},
{6, 11, 12},
{7, 13, 14},
{8, 15, 16},
{9, 17, 18},
};
  
void setup(){
  Serial.begin(9600);
  
  for (int h = 0; h < TableSizeX * TableSizeY; h++){
    int SensorName = SonarPinConfig[h][0];
    int TRIG_PIN = SonarPinConfig[h][1];
    int ECHO_PIN = SonarPinConfig[h][2];
    
    pinMode(TRIG_PIN, OUTPUT);
    digitalWrite(TRIG_PIN, LOW);
  }

  // IR Setup
  pinMode (ir, INPUT);
}

String getFillStatus(float sensorDistance){
  String fillStatus;
  if (sensorDistance > 20 ){
   fillStatus = "0";
 }
   else {
   fillStatus = "1";
 }
 return fillStatus; 
 }
 
float SonarDistance(int TRIG_PIN, int ECHO_PIN){
  
   Serial.println(ECHO_PIN);
   Serial.println(TRIG_PIN);
   Serial.println(digitalRead(TRIG_PIN));
  
  unsigned long t1, t2, pulse_width;
  float cm;
  // Hold the trigger pin high for at least 10 us
  digitalWrite(TRIG_PIN, HIGH);
  Serial.println(digitalRead(TRIG_PIN));
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  Serial.println("running...");
  // Wait for pulse on echo pin
  Serial.println(digitalRead(ECHO_PIN));
  while ( digitalRead(ECHO_PIN) == 0 ){
  Serial.println("running2...");
  // Measure how long the echo pin was held high (pulse width)
  // Note: the micros() counter will overflow after ~70 min
  t1 = micros();
  }
  while ( digitalRead(ECHO_PIN) == 1);
  t2 = micros();
  pulse_width = t2 - t1;
  cm = pulse_width / 58.0;
  if ( pulse_width > MAX_DIST ) {
    Serial.println("Out of range");
  } else {
    Serial.print("Sonar distance: ");
    Serial.println(cm);
  }
  return cm;
}

float IRDistance(){
  float dis=sharp.distance();  // this returns the distance to the object you're measuring
  Serial.print("IR distance: "); // returns it to the serial monitor
  Serial.println(dis);
  return dis;
  }
void loop(){

  String pinMatrix[TableSizeY][TableSizeX];

    int min = 0;
    int max = 40; 

   

   // give each element a random number and decide if empty or full 
   for (int i = 0; i < TableSizeY; i++) {
       for (int j = 0; j < TableSizeX; j++) {
          int h = 3*i + j;
//          Serial.println(SonarPinConfig[h][0]);
//          Serial.println(SonarPinConfig[h][1]);
//          Serial.println(SonarPinConfig[h][2]);
          pinMatrix[i][j] = SonarDistance(12,11);
//          Serial.println(pinMatrix[i][j]);
       }
   }

   Serial.println("Pin table");
   for (int i = 0; i < TableSizeY; i++) {
       for (int j = 0; j < TableSizeX; j++) {
           Serial.print("  ");Serial.print(pinMatrix[i][j]);
       }
       Serial.println();
   }
   Serial.println();
 
  delay(300000000);
 }
