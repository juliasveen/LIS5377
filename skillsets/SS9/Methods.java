import java.util.Scanner;

public class Methods{
    public static void getRequirements()
    {
        System.out.println("Developer: Julia Sveen");
        System.out.println("Program Requirements:");
        System.out.println("\t1. Write an application that displays integer equivalents of uppercase letters.");
        System.out.println("\t2. Display character equivalents of ASCII values 48 - 122.");
        System.out.println("\t Display the character equivalent of ASCII value user input.");

        System.out.println("\tNote: Compare answers to http://www.asciitable.com");
        System.out.println();
    }

    public static void getScore()
    {
        Scanner sc = new Scanner(System.in);
        double score = 0.0;

        System.out.print("Please enter grade between 0 to 100, inclusive: ");
        while(!sc.hasNextDouble())
        {
           System.out.println("Not valid number!\n");
           sc.next();
           System.out.print("Please try again. Enter grade between 0 to 100, inclusive: ");
        }
        score = sc.nextDouble();
        getGrade(score);

        sc.close();
    }

    public static void getGrade(double score)
    {
        String grade = "";

        if(score < 0 || score > 100)
        {
            System.out.println("\nOut of range!");
            //sc.next();
            getScore();
        }
        else
        {
            if(score < 60 && score >= 0)
            {
                grade = "F";
            }

            else if(score < 63 && score >= 60)
            {
                grade = "D-";
            }
            else if(score < 67 && score >= 63)
            {
                grade = "D";
            }
            else if(score < 70 && score >= 67)
            {
                grade = "D+";
            }

            else if(score < 73 && score >= 70)
            {
                grade = "C-";
            }
            else if(score < 77 && score >= 73)
            {
                grade = "C";
            }
            else if(score < 80 && score >= 77)
            {
                grade = "C+";
            }

            else if(score < 83 && score >= 80)
            {
                grade = "B-";
            }
            else if(score < 87 && score >= 83)
            {
                grade = "B";
            }
            else if(score < 90 && score >= 87)
            {
                grade = "B+";
            }

            else if(score < 93 && score >= 90)
            {
                grade = "A-";
            }
            else if(score < 97 && score >= 93)
            {
                grade = "A";
            }

            else
            {
                grade = "A+";
            }
        System.out.printf("\nScore entered: %f%n", score);
        System.out.printf("Final grade: %s%n", grade);
        }
    }
}