// Pins
int TRIG_PIN;
int ECHO_PIN;
int numberOfSensors = 9; //change to the number of sensors being used
const int matrix [9][3] ={ //sensor,trigger,echo
{1, 53, 52},
{2, 51, 50},
{3, 49, 48},
{4, 7, 6},
{5, 5, 4},
{6, 3, 2},
{7, 13, 12},
{8, 11, 10},
{9, 9, 8},
}; 

// Anything over 400 cm (23200 us pulse) is "out of range"
const unsigned int MAX_DIST = 23200;

void setup() {
// We'll use the serial monitor to view the sensor output
Serial.begin(9600);

int count = 0;
int row = 0;
  while (count< numberOfSensors){
  // The Trigger pin will tell the sensor to range find
   
  pinMode(matrix [row][1], OUTPUT);
  digitalWrite(matrix [row][1], LOW);
  count = count + 1;
  row = row + 1;
  } 
}

float SonarDistance(int TRIG_PIN, int ECHO_PIN ){
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
  // Calculate distance in centimeters and inches. The constants
  // are found in the datasheet, and calculated from the assumed speed 
  //of sound in air at sea level (~340 m/s).
  cm = pulse_width / 58.0;
  // Print out results
  if ( pulse_width > MAX_DIST ) {
    cm = 0;
    return cm;
  }   
// Wait at least 60ms before next measurement
  delay(60);
   return cm; 
}

void loop() {

  for (int x=0; x<numberOfSensors;x++){
    float a = SonarDistance(matrix[x][1], matrix[x][2]) ;   
    Serial.print(a);

    if (x==(numberOfSensors -1)){
      Serial.println();
      break;
    }
    Serial.print(','); 
  }
 
  
}



