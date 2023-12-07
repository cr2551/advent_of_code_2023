package day4;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ScratchCards {
    public static void main(String args[]) {

        String file_path = "input";
        try (BufferedReader bf = new BufferedReader(new FileReader(file_path))) {
            String line = bf.readLine();
                System.out.println(line);
                line = bf.readLine();
            
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
