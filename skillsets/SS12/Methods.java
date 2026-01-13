
import java.util.Scanner;

public class Methods {
    public static void getRequirements() {
        System.out.println("Author: Julia Sveen");
        System.out.println("Program Requirements:");
        System.out.println("1. Create a string array (str1), based upon users' number of preferred programming languages, limit 5.");
        System.out.println("2. Create a second string array (str2) based upon the length of str1 array.");
        System.out.println("3. Copy str1 array elements into str2.");
        System.out.println("4. Print elements of both arrays using Java's *enhanced* for loop.");
        System.out.println();
    }

    public static String[] createArray() {
        Scanner sc = new Scanner(System.in);
        int arraySize = 0;

        // Prompt user for number of languages
        System.out.print("\nHow many favorite programming languages do you have (min 1)? ");
        while (!sc.hasNextInt()) {
            System.out.println("Please enter valid integer.");
            sc.next();
            System.out.print("\nHow many favorite programming languages do you have (min 1)? ");
        }
        arraySize = sc.nextInt();

        while (arraySize < 1 || arraySize > 5) {
            System.out.println("Number must be between 1 and 5, inclusive. Please try again.");
            System.out.print("\nHow many favorite programming languages do you have (min 1)? ");
            while (!sc.hasNextInt()) {
                System.out.println("Please enter valid integer.");
                sc.next();
                System.out.print("\nHow many favorite programming languages do you have (min 1)? ");
            }
            arraySize = sc.nextInt();
        }

        sc.nextLine(); // Consume leftover newline
        return new String[arraySize];
    }

    public static void copyArray(String[] str1) {
        Scanner sc = new Scanner(System.in);

        // Populate str1
        System.out.println("\nPlease enter your " + str1.length + " favorite programming languages:");
        for (int i = 0; i < str1.length; i++) {
            str1[i] = sc.nextLine().trim(); // Trim whitespace to avoid blank entries
        }

        // Create and copy elements to str2
        String[] str2 = new String[str1.length];
        System.arraycopy(str1, 0, str2, 0, str1.length);

        System.out.println("\nPrinting str1 array:");
        for (String language : str1) {
            System.out.println(language);
        }

        System.out.println("\nPrinting str2 array:");
        for (String language : str2) {
            System.out.println(language);
        }

        System.out.println();
        sc.close();
    }
}




/* 
import java.util.Scanner;

public class Methods
{
    public static void getRequirements()
    {
        System.out.println("Author: Julia Sveen");
        System.out.println("Program Requirements:");
        System.out.println("1. Create a string array (str1), based upon users\' number of preferred programming languages, limit 5.");
        System.out.println("2. Create a second string array (str2) based upon the length of str1 array.");
        System.out.println("3. Copy str1 array elements into str2.");
        System.out.println("4. Print elements of both arrays using Java\'s *enhanced* for loop.");
        
        System.out.println(); 
    }
    
    //value-returning method (static requires no object)
    public static String[] createArray()
    {
        Scanner sc = new Scanner(System.in);
        int arraySize = 0;
        
        //prompt user for favorite programming languages
        //hasNext(): Returns true if scanner object has token input
        System.out.print("\nHow many favorite programming languages do you have (min 1)? ");
        while (!sc.hasNextInt())
        {
            System.out.println("Please enter valid integer.");
            sc.next();//Important! If omitted, will go into infinite loop on invalid input!
            System.out.print("\nHow many favorite programming languages do you have (min 1)? ");
        }
        arraySize = sc.nextInt(); //valid input
        
        while(arraySize < 1 || arraySize > 5)
        {
            //include data validation
            System.out.println("Number must be between 1 and 5, inclusive. Please try again.");
            System.out.print("\nHow many favorite programming languages do you have (min 1)? ");
            while (!sc.hasNextInt())
            {
                System.out.println("Please enter valid integer.");
                sc.next();
                System.out.print("\nHow many favorite programming languages do you have (min 1)? ");
            }
            arraySize = sc.nextInt(); //valid int between 1 and 5
        }
        
        String yourArray[] = new String[arraySize];
        return yourArray;
    }
    
    //nonvalue-returning method accepts int array arg (static requires no object)
    public static void copyArray(String [] str1)
    {
        Scanner sc = new Scanner(System.in);
        //populate array
        System.out.println("\nPlease enter your " + str1.length + " favorite programming languages:");
        
        // Clear the scanner buffer
        sc.nextLine();
        
        for (int i = 0; i < str1.length; i++)
        {
            str1[i] = sc.nextLine();
        }
        
        //set array size of
        String str2[] = new String[str1.length];
        
        int myCounter=0;
        for(String myIterator: str1)
        {
            str2[myCounter++] = myIterator;
        }
        
        System.out.println();
        
        // print arrays using enhanced for loop
        System.out.println("Printing str1 array:");
        for (String myIterator: str1)
        {
            System.out.println(myIterator);
        }
        
        System.out.println("\nPrinting str2 array:");
        for (String myIterator: str2)
        {
            System.out.println(myIterator);
        }
        
        //print vertical space
        System.out.println();
        
        sc.close(); //close scanner
    }
    
} 
*/