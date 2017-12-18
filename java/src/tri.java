import java.util.Scanner;
public class tri {
    public static void main(String[] args) {
        double base, height, hyp;
        Scanner scan = new Scanner(System.in);
        System.out.print("Input the base and height of a triangle");
        base = scan.nextFloat();
        height = scan.nextFloat();
        hyp = Math.sqrt(base*base + height*height);
        double rounded = Math.round(hyp * 1000.0) / 1000.0; // https://stackoverflow.com/questions/11701399/round-up-to-2-decimal-places-in-java

        System.out.print("The Hypotenuse is "+ rounded);
    }
}
