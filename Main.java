import java.util.Random;
import java.util.Scanner;

/**
 * Main class for simple Java demo
 */
public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number1 = 0, number2 = 0;

        System.out.println("Please enter two integers (>= 5):");
        number1 = scanner.nextInt();
        number2 = scanner.nextInt();

        matrix = createMatrixFrom2Numbers(number1, number2);
    }

    public static int[][] createMatrixFrom2Numbers(int number1, int number2) {
        int[][] matrix = new int[2][]; // initiate matrix

        matrix[0] = new int[number1]; 
        matrix[1] = new int[number2];

        Random random = new Random();

        for (int i = 0; i < number1; i++) {
            matrix[0][i] = random.nextInt(5) - 2; // filling up each row with random numbers from -2 to 2
        }

        for (int i = 0; i < number2; i++) {
            matrix[1][i] = random.nextInt(5) - 2; // filling up each row with random numbers from -2 to 2
        }

        return matrix;
    }


    // returns the received string - upper-case low, and lower-case up (the rest
    // stays the same)
    public static String ManipulateString(String string) {
        StringBuilder result = new StringBuilder(); // the string that carries the result

        for (char c : string.toCharArray()) { // looping every character
            if (Character.isLowerCase(c)) {
                result.append(Character.toUpperCase(c));
            } else if (Character.isUpperCase(c)) {
                result.append(Character.toLowerCase(c));
            } else {
                result.append(c);
            }
        }

        return result.toString();
    }

    // checking if the sum of number in 2 dimension matrix in a specific sub array
    // is 0
    public static boolean isZeroSubmatrix(int[][] matrix, int startRow, int startCol, int endRow, int endCol) {
        int sum = 0;
        for (int i = startRow; i <= endRow; i = i + 1) { // going through every dimension (every row)
            for (int j = startCol; j <= endCol; j = j + 1) { // looping every number and adding to sum
                int currentValue = matrix[i][j];
                sum = sum + currentValue;
            }
        }
        return sum == 0; // true is it is 0
    }

    

}
