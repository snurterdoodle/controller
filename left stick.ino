void setup() {
  Serial.begin(9600);
}

void loop() {
  int xAxisValue = analogRead(A0);
  int yAxisValue = analogRead(A1);
  
  Serial.print(xAxisValue);
  Serial.print(",");
  Serial.print(yAxisValue);
  Serial.println();  // Add a newline character to separate each reading
  
  delay(50);
}
