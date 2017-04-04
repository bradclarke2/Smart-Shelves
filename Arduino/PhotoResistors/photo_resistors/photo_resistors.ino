#include <Filters.h>

void setup() {
 Serial.begin(9600);
}

// filters out changes faster that 5 Hz.
float filterFrequency = 2.0;  

// create a one pole (RC) lowpass filter
FilterOnePole lowPassFilter( LOWPASS, filterFrequency );

void loop() {
 int sensorValue = lowPassFilter.input (analogRead(A0));
 Serial.println(sensorValue);
}
