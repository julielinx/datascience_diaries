public class FigureModular {
    public static void main(String[] args) {
        top();
        bottom();
        System.out.println();
        bottom();
        endBreak();
        System.out.println();
        stopSign();
        System.out.println();
        top();
        endBreak();
    }

    public static void stopSign() {
        top();
        midStop();
        bottom();
    }

    public static void top() {
        System.out.println("  ______");
        System.out.println(" /......\\");
        System.out.println("/........\\");
    }

    public static void midStop() {
        System.out.println("|  STOP  |");
    }

    public static void bottom() {
        System.out.println("\\......../");
        System.out.println(" \\______/");
    }

    public static void endBreak() {
        System.out.println("+--------+");
    }
}