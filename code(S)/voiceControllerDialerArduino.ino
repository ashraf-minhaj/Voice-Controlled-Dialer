/*  Voice Controlled Call dialer ***
 *  by: Ashraf Minhaj
 *  mail: ashraf_minhaj@yahoo.com
 *  blogpost/ Tutorial: https://ashrafminhajgb.blogspot.com
*/

/*
 * Required:
 * voiceControlledDialer.py script running on raspberry pi or pc
 */

 String x;

 void setup() // put your setup code here, to run once
{
  Serial.begin(9600);
  delay(1000);
  //a bit delay to make let the sim808 connect online
}

void loop()
{
  while(Serial.available() > 0)
  {
    x = Serial.readStringUntil("\n");

    String toSend = "ATD"; //make call "ATDNUMBER"
    toSend += x;

    Serial.println(toSend);
  }

  x = "";
  
}

