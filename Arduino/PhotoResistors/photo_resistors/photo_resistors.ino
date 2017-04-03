#include <Filters.h>

void setup() {
 Serial.begin(9600);
}

// filters out changes faster that 5 Hz.
float filterFrequency = 2.0;  

// create a one pole (RC) lowpass filter
FilterOnePole lowPassFilter( LOWPASS, filterFrequency );
FilterOnePole lowPassFilter2( LOWPASS, filterFrequency );
FilterOnePole lowPassFilter3( LOWPASS, filterFrequency );
//FilterOnePole lowPassFilter4( LOWPASS, filterFrequency );
//FilterOnePole lowPassFilter5( LOWPASS, filterFrequency );  
//FilterOnePole lowPassFilter6( LOWPASS, filterFrequency ); 

void loop() {
 int sensorValue = lowPassFilter.input (analogRead(A0));
 int sensorValue2 = lowPassFilter2.input (analogRead(A1));
 int sensorValue3 = lowPassFilter3.input (analogRead(A2));
// int sensorValue4 = lowPassFilter4.input (analogRead(A3));
// int sensorValue5 = lowPassFilter5.input (analogRead(A4));
// int sensorValue6 = lowPassFilter6.input (analogRead(A5));
 Serial.print(sensorValue);
 Serial.print(",");
 Serial.print(sensorValue2);
 Serial.print(",");
 Serial.println(sensorValue3);
// Serial.print(",");
// Serial.print(sensorValue4);
// Serial.print(",");
// Serial.print(sensorValue5);
// Serial.print(",");
// Serial.println(sensorValue6);
}
