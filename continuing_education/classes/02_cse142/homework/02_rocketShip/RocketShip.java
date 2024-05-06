public class Main {
    public static void main(String[] args) {
        topPlume();
        bodyDivider();
        topBody();
        bodyDivider();
        bottomBody();
        bodyDivider();
        topPlume();
    }
    
    public static final int SIZE = 6;
    public static final int HEIGHT = SIZE * 2;
    
    public static void topPlume() {
        for (int r = 1; r < HEIGHT; r++) {
            for (int v = HEIGHT  - r; v > 0; v--) {
                System.out.print(" ");
            }
            for (int v = 1; v <= r; v++) {
                System.out.print("/");
            }
            System.out.print("**");
            for (int v = 1; v <= r; v++) {
                System.out.print("\\");
            }
            System.out.println();
        }
    }
    
    public static void bodyDivider() {
        System.out.print("+");
        for (int r = 1; r<= SIZE*2; r++) {
            System.out.print("=*");
        }
        System.out.println("+");
    }
    
    public static void diamondTop() {
        for (int r = 1; r <= SIZE; r++) {
            System.out.print("|");
            for (int c = r; c < SIZE; c++) {
                System.out.print(".");
            }
            for (int c = 1; c<=r; c++) {
                System.out.print("/\\");
            }
            for (int c = r; c < SIZE; c++) {
                System.out.print("..");
            }
            for (int c = 1; c<=r; c++) {
                System.out.print("/\\");
            }
            for (int c = r; c < SIZE; c++) {
                System.out.print(".");
            }
            System.out.println("|");
        }
    }
    
    public static void diamondBottom() {
            for (int r = 1; r <= SIZE; r++) {
                System.out.print("|");
            for (int c = 1; c < r; c++) {
                System.out.print(".");
            }
            for (int c = r; c<=SIZE; c++) {
                System.out.print("\\/");
            }
            for (int c = 1; c<r; c++) {
                System.out.print("..");
            }
            for (int c = r; c<=SIZE; c++) {
                System.out.print("\\/");
            }
            for (int c = 1; c < r; c++) {
                System.out.print(".");
            }
            System.out.println("|");
        }
    }
    
    public static void topBody() {
        diamondTop();
        diamondBottom();
    }
    
    public static void bottomBody() {
        diamondBottom();
        diamondTop();
    }
 }
 