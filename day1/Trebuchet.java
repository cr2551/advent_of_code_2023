import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.lang.Character;
import java.util.Arrays;


public class Trebuchet {
    public static void main(String args[]) {
        // initialize array to hold an arbitrary number of values. In this case, 20.
        String filePath = "input.txt";
        try (BufferedReader in = new BufferedReader(new FileReader(filePath))) {
            int[] digitsArray = new int[10];
            int digitsIndex = 0;
            String line = in.readLine();
            while (line != null) {
                char[] charDigitsArray = new char[2];
                char [] charArr = line.toCharArray();
                // start looking from the beginning for a digit and break when you find one.
                for (int i = 0; i < charArr.length; i++) {
                    // System.out.print(charArr[i]);
                    char c = charArr[i];
                    if (Character.isDigit(c)) {
                        // append to charDigitsArray
                        charDigitsArray[0] = c;
                        break;
                    }
                }
                // now do the same starting from the end
                for (int i = charArr.length - 1; i >= 0; i--) {
                    char c = charArr[i];
                    if (Character.isDigit(c)) {
                        charDigitsArray[1] = c;
                        break;
                    }
                }
                // convert charArray to String
                String stringDigits = new String(charDigitsArray);
                int num = Integer.parseInt(stringDigits);
                // System.out.println(num);
                // check if the digitsIndex is greater than or equal to the length of the array, in which case we need 
                // to make a new one
                if (digitsIndex >= digitsArray.length) {
                    int[] newArray = new int[digitsArray.length + 1];
                    System.arraycopy(digitsArray, 0, newArray, 0, digitsArray.length);
                    digitsArray = newArray;
                }
                digitsArray[digitsIndex] = num;
                line = in.readLine();
                // increment the digitsIndex for the digitsArray
                // System.out.println(digitsIndex);
                
                digitsIndex++;
                // System.out.println(digitsArray);
            }
            // the Arrays.toString method is necessary to view the content of the arrray.
            // System.out.println(Arrays.toString(digitsArray));

            // use Arrays.stream to add up all the numbers
            int total = Arrays.stream(digitsArray).sum();
            System.out.println(total);
            
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}