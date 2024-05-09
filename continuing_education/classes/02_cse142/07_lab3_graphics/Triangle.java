import java.awt.*;

public class Triangle {   
   public static void main(String[] args) {
      int width = 600;
      int height = 200;
      int vSpace = 10;
      

      DrawingPanel panel = new DrawingPanel(width, height);
      panel.setBackground(Color.YELLOW);
      
      Graphics g = panel.getGraphics();
      shape(g, width, height, vSpace);
  }
  
   public static void shape(Graphics g, int width, int height, int vSpace) {
      g.setColor(Color.BLUE);      
      g.drawLine(0, 0, width/2, height);
      g.drawLine(width/2, height, width, 0);
      
      int numLines = height / vSpace;
      int xOffset = (width / 2) / numLines;
      for (int l=1; l< numLines; l++) {
         int x1 = l * xOffset;
         int x2 = width - x1;
         int y = l*vSpace;
         g.drawLine(x1, y, x2, y);
      }
  }

}