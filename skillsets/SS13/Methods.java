import java.io.File; // provides input/output streams used to write/read data to input/output sources
import java.io.IOException; // handles input/output exceptions
import java.io.FileNotFoundException; // checked exception indicates attempt to access file that does not exist/cannot be found
import java.io.PrintWriter; // more versatile than FileWriter, also provides methods for printing formatted output
import java.io.FileReader; // both FileReader/BufferedReader classes used to read file line by line
import java.io.BufferedReader;

import java.util.Scanner; // capture user input from console

public class Methods
{
    public static void getRequirements()
    {
        // display operational messages
        System.out.println("Author: Julia Sveen");
        System.out.println("Program Requirements:");
        System.out.println("Program captures user input, writes to and reads from same file, and counts number of words in file.");
        System.out.println("Hint: use hasNext() method to read number of words (tokens).");
        System.out.println(); // print blank line
    }

    public static File fileWrite() {
        Scanner sc = new Scanner(System.in);
        File file = new File("myFile.txt");

        try (PrintWriter writer = new PrintWriter(file)) {
            System.out.println("Write text to file (type ‘exit’ to quit):");
            String input;

            while (!(input = sc.nextLine()).equals("exit")) {
                writer.println(input);
            }

        } catch (IOException e) {
            System.out.println("Error writing to file: " + e.getMessage());
        }

        return file;
    }

    public static void fileRead(File myFile) {
        // reads text from a character-based input stream, buffering characters for efficient reading.
        // improves performance by reducing the number of disk access operations
    
        // declare object variables here to be seen by both try and finally blocks
        BufferedReader br = null;
        Scanner sc = null;
    
        try {
            FileReader fr = new FileReader(myFile);
            br = new BufferedReader(fr);
            sc = new Scanner(myFile);
    
            System.out.println("\nReading from file: " + myFile.getAbsolutePath());
    
            // print file contents
            String line;
            while ((line = br.readLine()) != null) {
                // print each line
                System.out.println(line);
            }
    
            // count number of tokens
            int count = 0;
            while (sc.hasNext()) {
                sc.next();
                count++;
            }
    
            System.out.println("\nNumber of tokens: " + count);
            // (closes Scanner object (Or, see "finally" block))
            sc.close();
        }
    
        catch (FileNotFoundException e) {
            // System.err.println("File not found: " + e.getMessage()); // only for testing!
            System.err.println("File not found");
        }
        catch (IOException e) {
            // e.printStackTrace(); // only for testing!
            // System.out.println("Error reading file: " + e.getMessage()); // only for testing!
            System.out.println("Error reading file.");
        }
    
        finally {
            // ensure BufferedReader and Scanner objects closed to prevent resource leaks
            if (br != null || sc != null) {
                try {
                    br.close();
                    sc.close();
                }
                catch (IOException e) {
                    System.err.println("Error closing file: " + e.getMessage());
                }
            }
        }
    }

}