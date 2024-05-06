public class ComplexFigure {
    public static void main(String[] args) {
    drawFigure();
    }
    
    public static final int SIZE = 5;
    
    public static void drawFigure() {
    // multiples of 8
        for (int i = 1; i<=SIZE; i++) {
            //System.out.println(i);
            for (int j = (SIZE-i)*4; j>0; j--) {
            //System.out.print(j);
                System.out.print("/");
            }
            for (int j = 1; j <=(i-1)*8; j++) {
                System.out.print("*");
            }
            for (int j = (SIZE-i)*4; j>0; j--) {
                //System.out.print(j);
                System.out.print("\\");
            }
            System.out.println();
        }
    }
}