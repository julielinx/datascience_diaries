import java.awt.*;

public class SquaresC {
   public static void main(String[] args) {
      int width = 400;
      int height = 300;
      DrawingPanel panel = new DrawingPanel(width, height);
      panel.setBackground(Color.CYAN);
      
      Graphics g = panel.getGraphics();
      shape(100, 50, 50, g);
      shape(50, 250, 10, g);
      shape(180, 180, 115, g);
   }
   
   public static void shape(int size, int x, int y, Graphics g) {
      g.setColor(Color.RED);
      int ppad = size / 5;
      for (int s = 1; s<=5; s++) {
         int hw = s * ppad;
         g.drawRect(x, y, hw, hw);
      }
      g.setColor(Color.BLACK);
      int endX = x + size;
      int endY = y + size;
      g.drawLine(x, y, endX, endY);
   }
}