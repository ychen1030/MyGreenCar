
//Declare variables
const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  9;       // the number of the LED pin
int buttonState = 0;         // variable for reading the pushbutton status
String stringOne = "#y";
String stringTwo = "#n";
//const int percentage2 = Serial.parseInt();

//Start Communication With Serial Ports
void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  // start port communication
  Serial.begin(9600);
}

void loop() {
  //Part 1 
  // read the voltage output of the light sensor
  float input_voltage = 255; //this is millivolts
  float resistor2 = 10; //this is kohms
  float sensorValue = analogRead(A0);
  float voltage_output = map(sensorValue, 0, 1023, 0, input_voltage); //output in millivolts
  Serial.println(voltage_output);
  //Part 2
  //declare an if/else loop to define the two possitions of the buttom
  buttonState = digitalRead(buttonPin);
  delay(1000);

  //Part2.1
  //State and intensity of the light
  if (buttonState == 0) {
    // Part2.2
    //turn LED on with the following conditions
    // This smart light decreases intensity when outside light has high lux. 
    // This smart light increases intensity when outside light has low lux.
    int percent = input_voltage - voltage_output; 
    
    //analogWrite(ledPin, percent);
    analogWrite(ledPin, percent);
    //digitalWrite(LED_BUILTIN, HIGH);
    Serial.println(stringOne);
    delay(5000);
  } 
  else {
    // turn LED off:
    analogWrite(ledPin, 0);
    //digitalWrite(LED_BUILTIN,LOW);
    Serial.println(stringTwo);
    delay(5000);
  }
  int incomingdata = Serial.read();
  if(incomingdata == 49){
    digitalWrite(LED_BUILTIN, HIGH);
    delay(5000);
  }
  else {
    digitalWrite(LED_BUILTIN, LOW);
    delay(5000);
  }

}

