import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

    }

    public static void matrix() {
        try (Scanner scanner = new Scanner(System.in)) {
            int rows = 0, cols = 0;
            int[][] matrix;
            int sumOfsubArrayThatIs0 = 0;

            while (rows < 5 || cols < 5) { // asking for 2 numbers that are equal to or grater then 5
                System.out.println("Please enter two numbers (5 and above):");
                rows = scanner.nextInt();

                System.out.println("just one more please:");
                cols = scanner.nextInt();
            }

            matrix = create2DMatrix(rows, cols); // creating the metrix

            printMatrix(matrix);
            sumOfsubArrayThatIs0 = findSubMatrixThatIs0(matrix); // counts submatrix that its sum is 0

            System.out.println("amount of submatrixes with sum 0: " + sumOfsubArrayThatIs0);
        }
    }

    public static int[][] create2DMatrix(int number1, int number2) {
        /**
         * Returns a 2D matrix.
         * rows and cols determent by a two number reciving.
         * Each cell will contain a random integer between -2 and 2.
         */

        int[][] matrix = new int[number1][number2]; // initiate matrix

        Random random = new Random();

        for (int i = 0; i < number1; i++) {
            for (int j = 0; j < number2; j++) {
                matrix[i][j] = random.nextInt(5) - 2;
            }
        }

        return matrix;
    }

    public static boolean isZeroSubmatrix(int[][] matrix, int startRow, int startCol, int endRow, int endCol) {
        /**
         * checking if the sum of cels in 2D matrix in a specific sub array is 0
         */
        int sum = 0;
        for (int i = startRow; i <= endRow; i = i + 1) { // going through every dimension (every row)
            for (int j = startCol; j <= endCol; j = j + 1) { // looping every number and adding to sum
                int currentValue = matrix[i][j];
                sum = sum + currentValue;
            }
        }
        return sum == 0; // true is it is 0
    }

    public static int findSubMatrixThatIs0(int[][] matrix) {
        /**
         * return amount of sub matrixs that their sum is 0
         */

        int rows = matrix.length; // end of rows
        int cols = matrix[0].length; // end of cols
        int count = 0;

        for (int startRow = 0; startRow < rows; startRow++) { // the first rows index for current submatrix
            for (int endRow = startRow; endRow < rows; endRow++) { // index of all the following rows

                for (int startCol = 0; startCol < cols; startCol++) { // the first cols index for current submatrix
                    for (int endCol = startCol; endCol < cols; endCol++) { // index of all the following cels

                        if (isZeroSubmatrix(matrix, startRow, startCol, endRow, endCol)) { // checking if sum = 0 and
                                                                                           // counting
                            count++;
                        }
                    }
                }
            }
        }
        return count;
    }

    public static void printMatrix(int[][] matrix) {
        /**
         * prints matrix
         */
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }

    public static int findSmalestNumber(int[] numbers) {
        int min = Integer.MAX_VALUE;
        int idx = 0;
        return recurciveFindMin(min, idx, numbers);
    }


    public static int[] sortArray(int[] numbers) {
        /**
         * returns array sorted
         */
        int idx = 0;
        return recurciveSelectionSort(numbers, idx);
    }

    public static int[] recurciveSelectionSort(int[] numbers, int currentIndex) {
        /**
         *  recurcive function for sorting array of ints - using selection sort method
         */
        if (currentIndex == numbers.length) {
            return numbers;
        }

        int min = recurciveFindMin(Integer.MAX_VALUE, currentIndex, numbers);

        int tempIndex = findIndex(numbers, currentIndex, min);
        int temp = numbers[currentIndex];

        numbers[currentIndex] = numbers[tempIndex]; // switching the minimum with the next available index
        numbers[tempIndex] = temp;

        return recurciveSelectionSort(numbers, currentIndex + 1);
    }

    public static int recurciveFindMin(int min, int idx, int[] numbers) {
        /**
         *  recurcive function finds the lower int in array
         */
        if (idx == numbers.length) {
            return min;
        }

        if (numbers[idx] < min) {
            min = numbers[idx];
        }

        return recurciveFindMin(min, idx + 1, numbers);
    }

    public static int findIndex(int[] numbers, int index, int value) {
        /**
         *  recurcive function finds index of a value in array
         */
        if (numbers[index] == value) {
            return index;
        }

        return findIndex(numbers, index + 1, value);
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

}
