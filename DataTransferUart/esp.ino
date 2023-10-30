#include <Arduino.h>
void setup() {
  Serial.begin(115200); // Initialize the hardware serial port
}
void loop() {
  if (Serial.available()) {
    char data = Serial.read();
    // Process the received data here
    // Echo back the data to the serial port
    Serial.write(data);
  }
}