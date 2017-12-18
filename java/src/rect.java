import java.util.Scanner;
public class rect {
    public static void main(String[] args) {
        double width, height, perimeter;
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the width and the height: ");
        width = scan.nextFloat();
        height = scan.nextFloat();
        perimeter = width*2+height*2;
        System.out.print("The perimeter is "+perimeter);
    }
}