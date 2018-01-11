// DEPLOYMENT CODE BEGINS
char previous='0';
char theanswer[200];
char temp;
int RightState=1;
int LeftState=1;
int UpState=1;
int DownState=1;
int FrontState=1;
int BackState=1;
void uno(int pina,int pinb,int pinc,int pind){
   digitalWrite(pina,HIGH);
   digitalWrite(pinb,HIGH);
   digitalWrite(pinc,LOW);
   digitalWrite(pind,LOW);
}
void dous(int pina,int pinb,int pinc,int pind){
   digitalWrite(pina,LOW);
   digitalWrite(pinb,HIGH);
   digitalWrite(pinc,HIGH);
   digitalWrite(pind,LOW);
}

void tres(int pina,int pinb,int pinc,int pind){
   digitalWrite(pina,LOW);
   digitalWrite(pinb,LOW);
   digitalWrite(pinc,HIGH);
   digitalWrite(pind,HIGH);
}

void quad(int pina,int pinb,int pinc,int pind){
   digitalWrite(pina,HIGH);
   digitalWrite(pinb,LOW);
   digitalWrite(pinc,LOW);
   digitalWrite(pind,HIGH);
}
void zilch(int pina,int pinb,int pinc,int pind){
    digitalWrite(pina, LOW);
    digitalWrite(pinb, LOW);
    digitalWrite(pinc, LOW);
    digitalWrite(pind, LOW);
}
//DEPLOYMENT CODE ENDS
void thesteps(int pina,int pinb,int pinc,int pind, bool twice,int isrev){
  int stepnums=0;
  if (twice) {
    /* steps for 180deg */
    stepnums=254;

  } else {
    /* steps 8 times */
    switch (isrev){
      case 0:
      stepnums=127;
      break;
      case 1:
      stepnums=127;
      break;
    }
  }

  /*switch(state) {
   case 1  :
            for (int i = 0; i <=stepnums; i++) {
            dous(pina,pinb,pinc,pind);
            delay(3);
            tres(pina,pinb,pinc,pind);
            delay(3);
            quad(pina,pinb,pinc,pind);
            delay(3);
            uno(pina,pinb,pinc,pind);
            delay(3);
          }
          return 1;
          
      break;
   case 2  :
       for (int i = 0; i <=stepnums; i++) {
            tres(pina,pinb,pinc,pind);
            delay(3);
            quad(pina,pinb,pinc,pind);
            delay(3);
            uno(pina,pinb,pinc,pind);
            delay(3);
            dous(pina,pinb,pinc,pind);
            delay(3);
          }
          return 2;
      break;
   case 3 :
          for (int i = 0; i <=stepnums; i++) {
            quad(pina,pinb,pinc,pind);
            delay(3);
            uno(pina,pinb,pinc,pind);
            delay(3);
            dous(pina,pinb,pinc,pind);
            delay(3);
            tres(pina,pinb,pinc,pind);
            delay(3);
          }
          return 3;
      break;
   case 4 :
             for (int i = 0; i <=stepnums; i++) {
            uno(pina,pinb,pinc,pind);
            delay(3);
            dous(pina,pinb,pinc,pind);
            delay(3);
            tres(pina,pinb,pinc,pind);
            delay(3);
            quad(pina,pinb,pinc,pind);
            delay(3);
          }
          return 4;
      break;
} */
             for (int i = 0; i <=stepnums; i++) {
            uno(pina,pinb,pinc,pind);
            delay(3);
            dous(pina,pinb,pinc,pind);
            delay(3);
            tres(pina,pinb,pinc,pind);
            delay(3);
            quad(pina,pinb,pinc,pind);
            delay(3);
          }

}

//EXPERIMENTAL START
void twosteps(int pina,int pinb,int pinc,int pind,int pinw,int pinx,int piny,int pinz,bool twice1,bool twice2){
  uno(pina,pinb,pinc,pind);
  uno(pinw,pinx,piny,pinz); //NOTE:check the time taken should be min 2ms
  dous(pina,pinb,pinc,pind);
  dous(pinw,pinx,piny,pinz);
  tres(pina,pinb,pinc,pind);
  tres(pinw,pinx,piny,pinz);
  quad(pina,pinb,pinc,pind);
  quad(pinw,pinx,piny,pinz);
}
//EXPERIMENTAL ENDS



void Right(bool anticlockwise,bool twice){
    //code to step motor R on pin 13 12 11 10

    //Serial.print("--RIGHT--"); //TESTINGSNIPPET
    if(anticlockwise){
      //Serial.print("ANTICLOCKWISE--"); //TESTINGSNIPPET
         /*   switch(RightState){
        case 1:
            RightState=3;
        break;
        case 3:
            RightState=1;
        break;

      }*/
      thesteps(10, 11, 12, 13, twice,RightState);
      /*switch(RightState){
        case 1:
            RightState=3;
        break;
        case 3:
            RightState=1;
        break;

      }*/
    }else{
      //Serial.print("CLOCKWISE--"); //TESTINGSNIPPET
      thesteps(13, 12, 11, 10, twice, 0);
    }
}
void Left(bool anticlockwise,bool twice){
    //code to step motor L on pin 9 8 7 6
    //Serial.print("--LEFT--"); //TESTINGSNIPPET
    if(anticlockwise){
    //Serial.print("ANTICLOCKWISE--"); //TESTINGSNIPPET
      /*    switch(LeftState){
        case 1:
            LeftState=3;
        break;
        case 3:
            LeftState=1;
        break;

      }*/
      thesteps(6, 7, 8, 9, twice, LeftState);
      /*switch(LeftState){
        case 1:
            LeftState=3;
        break;
        case 3:
            LeftState=1;
        break;

      }*/
    }else{
    //Serial.print("CLOCKWISE--"); //TESTINGSNIPPET
      thesteps(9, 8, 7, 6, twice, 0);
    }
}
void Up(bool anticlockwise,bool twice){
    //code to step motor U on pin 5 4 3 2
    //Serial.print("--UP--"); //TESTINGSNIPPET
    if(anticlockwise){
    //Serial.print("ANTICLOCKWISE--"); //TESTINGSNIPPET
          /*switch(UpState){
        case 1:
            UpState=3;
        break;
        case 3:
            UpState=1;
        break;
      }*/
      thesteps(2, 3, 4, 5, twice, UpState);
      /*switch(UpState){
        case 1:
            UpState=3;
        break;
        case 3:
            UpState=1;
        break;
      }*/
    }else{
    //Serial.print("CLOCKWISE--"); //TESTINGSNIPPET
      thesteps(5, 4, 3, 2, twice, 0);
    }
}
void Down(bool anticlockwise,bool twice){
    //code to step motor R on pin 22 24 26 28
    //Serial.print("--DOWN--"); //TESTINGSNIPPET
    if(anticlockwise){
    //Serial.print("ANTICLOCKWISE--"); //TESTINGSNIPPET
          /*switch(DownState){
        case 1:
            DownState=3;
        break;
        case 3:
            DownState=1;
        break;
      }*/
      thesteps(28, 26, 24, 22, twice, DownState);
      /*switch(DownState){
        case 1:
            DownState=3;
        break;
        case 3:
            DownState=1;
        break;
      }*/
    }else{
    //Serial.print("CLOCKWISE--"); //TESTINGSNIPPET
      thesteps(22, 24, 26, 28, twice, 0);
    }
}
void Front(bool anticlockwise,bool twice){
    //code to step motor R on pin 30 32 34 36
    //Serial.print("--FRONT--"); //TESTINGSNIPPET
    if(anticlockwise){
    //Serial.print("ANTICLOCKWISE--"); //TESTINGSNIPPET
         /* switch(FrontState){
        case 1:
            FrontState=3;
        break;
        case 3:
            FrontState=1;
        break;
      }*/
      thesteps(36, 34, 32, 30, twice, DownState);
      /*switch(FrontState){
        case 1:
            FrontState=3;
        break;
        case 3:
            FrontState=1;
        break;
      }*/
    }else{
    //Serial.print("CLOCKWISE--"); //TESTINGSNIPPET
      thesteps(30, 32, 34, 36, twice, 0);
    }
}
void Back(bool anticlockwise,bool twice){
    //code to step motor R on pin 40 42 44 46
    //Serial.print("--BACK--"); //TESTINGSNIPPET
    if(anticlockwise){
    //Serial.print("ANTICLOCKWISE--"); //TESTINGSNIPPET
         /* switch(BackState){
        case 1:
            BackState=3;
        break;
        case 3:
            BackState=1;
        break;
      }*/
      thesteps(46, 44, 42, 40, twice, BackState);
      /*switch(BackState){
        case 1:
            BackState=3;
        break;
        case 3:
            BackState=1;
        break;
      }*/
    }else{
    //Serial.print("CLOCKWISE--"); //TESTINGSNIPPET
      thesteps(40, 42, 44, 46, twice, 0);
    }
}
void setup() {
  //DEPLOYMENT CODE STARTS
    pinMode(13 , OUTPUT); //R
    pinMode(12 , OUTPUT); //R
    pinMode(11 , OUTPUT); //R  //abc
    pinMode(10 , OUTPUT); //R

    pinMode(9 , OUTPUT); //L
    pinMode(8 , OUTPUT); //L
    pinMode(7 , OUTPUT); //L  //def
    pinMode(6 , OUTPUT); //L

    pinMode(5 , OUTPUT); //U
    pinMode(4 , OUTPUT); //U
    pinMode(3 , OUTPUT); //U  //ghi
    pinMode(2 , OUTPUT); //U

    pinMode(22 , OUTPUT); //D
    pinMode(24 , OUTPUT); //D
    pinMode(26 , OUTPUT); //D  //jkl
    pinMode(28 , OUTPUT); //D

    pinMode(30 , OUTPUT); //F
    pinMode(32 , OUTPUT); //F
    pinMode(34 , OUTPUT); //F  //mno
    pinMode(36 , OUTPUT); //F

    pinMode(40 , OUTPUT); //B
    pinMode(42 , OUTPUT); //B
    pinMode(44 , OUTPUT); //B  //pqr
    pinMode(46 , OUTPUT); //B

    uno(13,12,11,10);
    uno(9,8,7,6);
    uno(5,4,3,2);
    uno(22,24,26,28);
    uno(30,32,34,36);
    uno(40,42,44,46);
  //DEPLOYMENT CODE ENDS
  
    Serial.begin(9600); 
}

void loop() {
    /*make sure to terminate with 'z'
        a - R       d - L      g - Up      j - Dwn      m - Frnt     p-bk
        b - Rinv    e - Linv   h - Upinv   k - Dwninv   n - Frntinv  q-bkinv
        c - Rtwo    f - Ltwo   i - Uptwo   l - Dwntwo   o - Frnttwo  r-bk2
    */

    if(Serial.available() > 0){
        int lengthj = Serial.readBytesUntil('\n',theanswer,200);
        for(int i=0;i<=lengthj;i++){
            temp=theanswer[i];
          
            if (previous == '0') {
              previous=temp;
            } else {
              /*condition to check if doublerot possible
              if (
                ((prev=='a'||prev=='b'||prev=='c')&&(temp=='d'||temp=='e'||temp=='f'))||
                ((prev=='d'||prev=='e'||prev=='f')&&(temp=='a'||temp=='b'||temp=='c'))||
          ((prev=='g'||prev=='h'||prev=='i')&&(temp=='j'||temp=='k'||temp=='l'))||
          ((prev=='j'||prev=='k'||prev=='l')&&(temp=='g'||temp=='h'||temp=='i'))||
          ((prev=='m'||prev=='n'||prev=='o')&&(temp=='p'||temp=='q'||temp=='r'))||
          ((prev=='p'||prev=='q'||prev=='r')&&(temp=='m'||temp=='n'||temp=='o'))||
              ) {
    
              } else { */
                /*movements depending on character read if not possible double rotation goes here*/
                if (previous=='a') {
                  /* R */
                  Right(false, false);
                } else if (previous=='b') {
                  /* R' */
                  Right(true, false);
                } else if (previous=='c') {
                  /* R2 */
                  Right(false,true);
                } else if (previous=='d') {
                  /* L */
                  Left(false, false);
                } else if (previous=='e') {
                  /* L' */
                  Left(true, false);
                } else if (previous=='f') {
                  /* L2 */
                  Left(false, true);
                } else if (previous=='g') {
                  /* U */
                  Up(false,false);
                } else if (previous=='h') {
                  /* U' */
                  Up(true,false);
                } else if (previous=='i') {
                  /* U2 */
                  Up(false,true);
                } else if (previous=='j') {
                  /* D */
                  Down(false,false);
                } else if (previous=='k') {
                  /* D' */
                  Down(true,false);
                } else if (previous=='l') {
                  /* D2 */
                  Down(false,true);
                } else if (previous=='m') {
                  /* F */
                  Front(false,false);
                } else if (previous=='n') {
                  /* F' */
                  Front(true,false);
                } else if (previous=='o') {
                  /* F2 */
                  Front(false,true);
                } else if (previous=='p') {
                  /* B */
                  Back(false,false);
                } else if (previous=='q') {
                  /* B' */
                  Back(true,false);
                } else if (previous=='r') {
                  /* B2 */
                  Back(false,true);
                }
                else {  
                }
                
                /*end of movements*/
              }
              previous=temp;
              Serial.println(temp);
            }
        }
    /*} closing of the double check*/
    delay(1000);
}


