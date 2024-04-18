void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT_PULLUP); // Button for left click
  pinMode(3, INPUT_PULLUP); // Button for right click
  pinMode(5, INPUT_PULLUP); // Button for space 2
  pinMode(7, INPUT_PULLUP); // Button for space 4
}

void loop() {
  int xAxisValue = analogRead(A0);
  int yAxisValue = analogRead(A1);
  int leftClickState = digitalRead(2);
  int rightClickState = digitalRead(3);
  int space2State = digitalRead(5);
  int space4State = digitalRead(7);
  
  Serial.print(xAxisValue);
  Serial.print(",");
  Serial.print(yAxisValue);
  Serial.print(",");
  Serial.print(leftClickState);
  Serial.print(",");
  Serial.print(rightClickState);
  Serial.print(",");
  Serial.print(space2State);
  Serial.print(",");
  Serial.print(space4State);
  Serial.println();
  
  delay(125); // Introduce a delay of 125 milliseconds
}
