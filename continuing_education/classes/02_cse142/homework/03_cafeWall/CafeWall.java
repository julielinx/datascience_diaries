import java.awt.*;

public class CafeWall {
   public static void main(String[] args) {
      int winWidth = 650;
      int winHeight = 400;
      int PADDING = 2;
      
      DrawingPanel panel = new DrawingPanel(winWidth, winHeight);
      panel.setBackground(Color.GRAY);
      Graphics g = panel.getGraphics();
      wallRow(g, 0, 0, 4, 20);
      wallRow(g, 50, 70, 5, 30);
      cafeWall(g, 10, 150, 4, 25, 0);
      cafeWall(g, 250, 200, 3, 25, 10);
      cafeWall(g, 425, 180, 5, 20, 10);
      cafeWall(g, 400, 20, 2, 35, 35);
   }
   
   public static void cafeWall(Graphics g, int startX, int startY,
     int nbrPairs, int size, int rowOffset) {
      for (int r = 0; r < nbrPairs; r++) {
          int sizeUpdate = 2 * (size + 2) * r;
         rowPair(g, startX, startY + sizeUpdate, nbrPairs, size, rowOffset);
      }
   }
   
   public static void rowPair(Graphics g, int startX, int startY,
     int nbrPairs, int size, int rowOffset) {
     wallRow(g, startX, startY, nbrPairs, size);
     wallRow(g, startX + rowOffset, startY + size + 2, nbrPairs, size);
   }
   
   public static void wallRow(Graphics g, int startX, int startY,
     int nbrPairs, int size) {
      for (int p = 0; p < nbrPairs; p++) {
         int sizeUpdate = 2 * size * p;
         boxBlock(g, startX + sizeUpdate, startY, size);
      }
   }
   
   public static void boxBlock(Graphics g, int startX, int startY, int size) {
      g.setColor(Color.BLACK);
      g.fillRect(startX, startY, size, size);
      g.setColor(Color.BLUE);
      g.drawLine(startX, startY, startX + size, startY + size);
      g.drawLine(startX, startY + size, startX + size, startY);
      g.setColor(Color.WHITE);
      g.fillRect(startX + size, startY, size, size);
   }
   
} 