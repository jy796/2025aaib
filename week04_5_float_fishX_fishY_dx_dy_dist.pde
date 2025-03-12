// week04_5_float_fishX-fishY-dx_dy_dist
void setup(){
  size(600, 400);
}
int x, y;
float fishX = 300, fishY = 200;
void draw(){
  background(#C0ffee);//裡面是零0,不是字母0
  if(x>0){
    y +=2;
    if(y>400) x = 0; // 超過畫面範圍，就把x變成0
    ellipse(x, y, 8, 8);//畫出小飼料
    float dx = x-fishX, dy = y - fishY;//向量
    float d = dist(x, y, fishX, fishY);//距離
    fishX += dx / d * 4;//往飼料靠過去
    fishY += dy / d* 4; 
  }
}
void mousePressed(){
  x = mouseX;
  y = mouseY;
}
