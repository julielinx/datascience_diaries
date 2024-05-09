import java.awt.*;

public class Doodle {
   public static void main(String[] args) {      
      int rocketsize = 100;
      int rocketSegments = 3;
      int winWidth = rocketsize * 12;
      int winHeight = rocketsize * 7;

      DrawingPanel panel = new DrawingPanel(winWidth, winHeight);
      Color lightBlue = new Color(125, 209, 250);
      Color grassGreen = new Color(70, 193, 9);
      panel.setBackground(lightBlue);
      
      Graphics g = panel.getGraphics();
      
      for (int i = 1; i < winHeight; i++) {
         panel.clear();
         g.setColor(grassGreen);
         g.fillRect(0, winHeight - 40, winWidth, 40);
         g.setColor(Color.BLACK);
         g.drawLine(0, winHeight - 40, winWidth, winHeight - 40);
         int startHeight = (winHeight + rocketsize/5) - i;
         rocket(g, winWidth, startHeight, rocketsize, rocketSegments);
         panel.sleep(winHeight/i);
      }
   }
   
   public static void rocket(Graphics g, int winWidth, int winHeight,
    int rocketsize, int rocketSegments) {
      rTop(g, winWidth, winHeight, rocketsize, rocketSegments);
      plume(g, winWidth, winHeight, rocketsize, rocketSegments);
      rocketBody(g, winWidth, winHeight, rocketsize, rocketSegments);
   }
   
   public static void rocketBody(Graphics g, int winWidth, int winHeight,
    int rocketsize, int rocketSegments) {
      for (int b = 0; b < rocketSegments; b++) {
         int x1 = winWidth/2 - rocketsize/2;
         int y1 = winHeight - 2 * rocketsize - rocketsize * b;
         g.setColor(Color.LIGHT_GRAY);
         g.fillRect(x1, y1, rocketsize, rocketsize);
         g.setColor(Color.BLACK);
         //g.drawRect(x1, y1, rocketsize, rocketsize);
         g.drawLine(x1, y1, x1 + rocketsize/2, y1 + rocketsize);
         g.drawLine(x1 + rocketsize/2, y1 + rocketsize, x1 + rocketsize, y1);
         g.drawLine(x1, y1 + rocketsize, x1 + rocketsize/2, y1);
         g.drawLine(x1 + rocketsize/2, y1, x1 + rocketsize, y1 + rocketsize);
      }
   }
   
   public static void rTop(Graphics g, int winWidth, int winHeight, int rocketsize, int rocketSegments) {
      int nbrLines = 4;
      for (int t = 0; t < rocketsize/nbrLines; t++) {
         int midpoint = winWidth/2;
         int xRight = midpoint + rocketsize/2 - (t * nbrLines/2) + rocketsize/10;
         int xLeft = midpoint - rocketsize/2 + (t * nbrLines/2) - rocketsize/10;
         int yHigh = winHeight - (rocketsize * (rocketSegments + 2)) + (t*nbrLines);
         int yLow = winHeight - (rocketsize * (rocketSegments + 1));
         g.setColor(Color.BLACK);
         g.drawLine(midpoint, yHigh, xRight, yLow);
         g.drawLine(midpoint, yHigh, xLeft, yLow);
      }
   }
      
   public static void plume(Graphics g, int winWidth, int winHeight, int rocketsize, int rocketSegments) {
      int nbrLines = 3;
      for (int t = 0; t < rocketsize/nbrLines; t++) {
         int midpoint = winWidth/2;
         int xRight = midpoint + rocketsize/2 - (t * nbrLines/2) + rocketsize/2;
         int xLeft = midpoint - rocketsize/2 + (t * nbrLines/2) - rocketsize/2;
         int yHigh = winHeight - rocketsize + (t*nbrLines) - rocketsize/3;
         int yLow = winHeight - rocketsize/3;
         g.setColor(Color.ORANGE);
         g.drawLine(midpoint, yHigh, xRight, yLow);
         g.drawLine(midpoint, yHigh, xLeft, yLow);
      }
   }
}