

/* ros node running in arduino of chippu
subscribes to topic "drive" 
and makes decisions based on the control signals received



written by achuwilson
achu_wilson@rediffmail.com
achuwilson.wordpress.com
*/

 
#include "WProgram.h" //include the Arduino library
#include <stdlib.h>
#include <Servo.h>

Servo pan;
Servo tilt;
Servo r_arm;
Servo l_arm;



int posx = 0;
int posy = 0;
int posr = 0;
int posl = 0;
 char cmd;
#include <ros.h>
#include <std_msgs/String.h>



void forward(void)
{
  digitalWrite(9,HIGH);
  digitalWrite(3,HIGH);
  digitalWrite(8,LOW);
  digitalWrite(2,LOW);
  delay(25);
 
}


void reverse(void)
{
  digitalWrite(8,HIGH);
  digitalWrite(2,HIGH);
  digitalWrite(9,LOW);
  digitalWrite(3,LOW);
  delay(25);
 
}

void left(void)
{
  digitalWrite(9,HIGH);
  digitalWrite(3,HIGH);
  digitalWrite(8,LOW);
  digitalWrite(2,HIGH);
  delay(25);
 
}

void right(void)
{
  digitalWrite(9,HIGH);
  digitalWrite(3,HIGH);
  digitalWrite(8,HIGH);
  digitalWrite(2,LOW);
  delay(25);
 
}

void halt(void)
{
  digitalWrite(9,HIGH);
  digitalWrite(3,HIGH);
  digitalWrite(8,HIGH);
  digitalWrite(2,HIGH);
}


void control(const std_msgs::String& control_cmd)
{
 
  cmd = control_cmd.data[0];

  switch (cmd)
  {
  case 'x':
    halt();
    break;  
  case 'f':
    forward();
    break;
  case 'b':
    reverse();
    break;
  case 'l':
    left();
    break;
  case 'r':
    right();
    break;
  case 'w':
    if (posy<=165)
    {
      posy=posy+15;
      tilt.write(posy);
      //delay(2);
    }
    break;
  case 's':
    if (posy>=15)
    {
      posy=posy-15;
      tilt.write(posy);
      //delay(2);
    }
    break;
  case 'a':
    if(posx<=165)
    {
      posx=posx+15;
      pan.write(posx);
      //delay(2);
    }
    break;
  case 'd':
    if (posx>=15)
    {
      posx=posx-15;
      pan.write(posx);
      //delay(2);
    }
    break;
  case 't':
    if (posl<=160)
    {
      posl=posl+20;
      l_arm.write(posl);
      //delay(2);
    }
    break;
    case 'g':
    if (posl>=20)
    {
      posl=posl-20;
      l_arm.write(posl);
      //delay(2);
    }
    break;
  case 'y':
    if (posr<=160)
    {
      posr=posr+20;
      r_arm.write(posr);
      //delay(2);
    }
    break;
    case 'h':
    if (posr>=20)
    {
      posr=posr-20;
      r_arm.write(posr);
      //delay(2);
    }
    break;
  //default:
    //halt();
    //break;

  }
}    




ros::NodeHandle  nh;
ros::Subscriber<std_msgs::String> sub("drive" , control);

void setup()
{

  pinMode(8, OUTPUT); //set up the LED
  pinMode(9, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);

  pan.attach(4);
  tilt.attach(5);
  l_arm.attach(6);
  r_arm.attach(7);
  /*
  digitalWrite(9,HIGH);
  digitalWrite(11,HIGH);
  digitalWrite(8,HIGH);
  digitalWrite(10,HIGH);
  delay(1000);
  digitalWrite(9,LOW);
  digitalWrite(11,LOW);
  digitalWrite(8,LOW);
  digitalWrite(10,LOW);
  
  */nh.initNode();
  nh.subscribe(sub);
}

void loop()
{
 
  nh.spinOnce();
  delay(1);
}




