#include <Filters.h>
// Pins
int TRIG_PIN;
int ECHO_PIN;
// Anything over 400 cm (23200 us pulse) is "out of range"
const unsigned int MAX_DIST = 23200;
int numberOfSensors = 9; //change to the number of sensors being used

float filterFrequency = 2.0;  
FilterOnePole lowPassFilterA( LOWPASS, filterFrequency );
FilterOnePole lowPassFilterB( LOWPASS, filterFrequency );
FilterOnePole lowPassFilterC( LOWPASS, filterFrequency );
FilterOnePole lowPassFilterD( LOWPASS, filterFrequency );
FilterOnePole lowPassFilterE( LOWPASS, filterFrequency );
FilterOnePole lowPassFilterF( LOWPASS, filterFrequency );
FilterOnePole lowPassFilterG( LOWPASS, filterFrequency );
FilterOnePole lowPassFilterH( LOWPASS, filterFrequency );
FilterOnePole lowPassFilterI( LOWPASS, filterFrequency );

const int matrix [18][3] ={ //sensor,echo,trigger
  // 14L8E
  {0, 8, 9},
  {1, 2, 3},
  {2, 50, 51},
  {3, 10, 11},
  {4, 4, 5},
  {5, 50, 51},
  {6, 12, 13},
  {7, 6, 7},
  {8, 52, 53},
};

void setup() {
  
Serial.begin(9600);

int count = 0;
int row = 0;
 while (count< numberOfSensors){
  pinMode(matrix [row][2], OUTPUT);
  digitalWrite(matrix [row][2], LOW);
  count = count + 1;
  row = row + 1;
  } 
}

float SonarDistance(int ECHO_PIN, int TRIG_PIN ){
  unsigned long t1;
  unsigned long t2;
  unsigned long pulse_width;
  float cm;
  // Hold the trigger pin high for at least 10 us
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  // Wait for pulse on echo pin
  while ( digitalRead(ECHO_PIN) == 0 );
  // Measure how long the echo pin was held high (pulse width)
  // Note: the micros() counter will overflow after ~70 min
  t1 = micros();
  while ( digitalRead(ECHO_PIN) == 1);
  t2 = micros();
  pulse_width = t2 - t1;
  // Calculate distance in cm
  cm = pulse_width / 58.0;
  if ( pulse_width > MAX_DIST ) {
    cm = 0;
  }   
  // Wait at least 60ms before next measurement
  delay(60);
   return cm; 
}

int PRLumens(String port){
  return 1;  
}

void loop() {

  Serial.print("US:");
  for (int x=0; x<numberOfSensors;x++){
  float a = SonarDistance(matrix[x][1], matrix[x][2]) ;  
  Serial.print(a);
  
  if (x==(numberOfSensors -1)){
    Serial.println();
    break;
  }
  Serial.print(',');
  }
  
  float a = lowPassFilterA.input (analogRead(A0)) ;  
  float b = lowPassFilterB.input (analogRead(A1)) ;
  float c = lowPassFilterC.input (analogRead(A2)) ;  
  float d = lowPassFilterD.input (analogRead(A3)) ;  
  float e = lowPassFilterE.input (analogRead(A4)) ;  
  float f = lowPassFilterF.input (analogRead(A5)) ;  
  float g = lowPassFilterG.input (analogRead(A6)) ;
  float h = lowPassFilterH.input (analogRead(A7)) ;    
  float i = lowPassFilterI.input (analogRead(A8)) ; 
  
  Serial.print("PR:");
  Serial.print(a);Serial.print(",");
  Serial.print(b);Serial.print(",");
  Serial.print(c);Serial.print(",");
  Serial.print(d);Serial.print(",");
  Serial.print(e);Serial.print(",");
  Serial.print(f);Serial.print(",");
  Serial.print(g);Serial.print(",");
  Serial.print(h);Serial.print(",");
  Serial.println(i);
}
