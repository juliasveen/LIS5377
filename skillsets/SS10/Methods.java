import java.util.Scanner;

/*
class Methods {
    public static void getRequirements() {
        System.out.println("Program uses methods to:\nAdd, subtract, multiply, divide and power floating point numbers, rounded to two decimal places.");
        System.out.println("Note: Program checks for non-numeric values, and division by zero.");
        System.out.println(); 
    }
    
    public static void calculateNumbers() {
        // initialize variables and create Scanner object
        double num1 = 0.0, num2 = 0.0;
        char operation = ' ';
        // note: Scanner: simple string "next" include character--here, space character!
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter mathematical operation (a=addition, s=subtraction, m=multiplication, d=division, e=exponentiation): ");
        operation = sc.next().toLowerCase().charAt(0);
        
        while (operation != 'a' && operation != 's' && operation != 'm' && operation != 'd' && operation != 'e') {
            System.out.println("Incorrect operation. Please enter correct operation: ");
            operation = sc.next().toLowerCase().charAt(0); //captures first character from first token
            //operation = sc.next();
        }
        
        System.out.println("Please enter first number: ");
        while (!sc.hasNextDouble()) {
            System.out.println("Not valid number!");
            sc.next();//Important! If omitted, will go into infinite loop on invalid input!
            System.out.print("Please try again. Enter first number: ");
        }
        num1 = sc.nextDouble();
        
        System.out.println("Please enter second number: ");
        while (!sc.hasNextDouble()) {
            System.out.println("Not valid number!");
            sc.next();//Important! If omitted, will go into infinite loop on invalid input!
            System.out.print("Please try again. Enter second number: ");
        }
        num2 = sc.nextDouble();
        
        //test operation
        if (operation == 'a') {
            Addition(num1, num2);
        }
        else if (operation == 's') {
            Subtraction(num1, num2);
        }
        else if (operation == 'm') {
            Multiplication(num1, num2);
        }
        else if (operation == 'd') {
            if (num2 == 0) {
                System.out.println("Cannot divide by zero!");
            }
            else {
                Division(num1, num2);
            }
        }
        else if (operation == 'e') {
            Exponentiation(num1, num2);
        }
        
        System.out.println(); 
        sc.close(); //close scanner
    }
    
    //create mathematical methods
    public static void Addition(double n1, double n2) {
        System.out.println(n1 + " + " + n2 + " = ");
        System.out.printf("%.2f", (n1 + n2));
    }
    
    public static void Subtraction(double n1, double n2) {
        System.out.println(n1 + " - " + n2 + " = ");
        System.out.printf("%.2f", (n1 - n2));
    }
    
    public static void Multiplication(double n1, double n2) {
        System.out.println(n1 + " * " + n2 + " = ");
        System.out.printf("%.2f", (n1 * n2));
    }
    
    public static void Division(double n1, double n2) {
        System.out.println(n1 + " / " + n2 + " = ");
        System.out.printf("%.2f", (n1 / n2));
    }
    
    public static void Exponentiation(double n1, double n2) {
        //...
    }
}
*/

class Methods {
    public static void getRequirements() {
        System.out.println("Program uses methods to:\nAdd, subtract, multiply, divide and power floating point numbers, rounded to two decimal places.");
        System.out.println("Note: Program checks for non-numeric values, and division by zero.");
        System.out.println(); 
    }
    
    public static void calculateNumbers() {
        // initialize variables and create Scanner object
        double num1 = 0.0, num2 = 0.0;
        char operation = ' ';
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter mathematical operation (a=addition, s=subtraction, m=multiplication, d=division, e=exponentiation): ");
        operation = sc.next().toLowerCase().charAt(0);
        
        while (operation != 'a' && operation != 's' && operation != 'm' && operation != 'd' && operation != 'e') {
            System.out.print("Incorrect operation. Please enter correct operation: ");
            operation = sc.next().toLowerCase().charAt(0);
        }
        
        System.out.print("Please enter first number: ");
        while (!sc.hasNextDouble()) {
            System.out.println("Not valid number!");
            System.out.println(); 
            sc.next();//Important! If omitted, will go into infinite loop on invalid input!
            System.out.print("Please try again. Enter first number: ");
        }
        num1 = sc.nextDouble();
        
        System.out.print("Please enter second number: ");
        while (!sc.hasNextDouble()) {
            System.out.println("Not valid number!");
            System.out.println(); 
            sc.next();//Important! If omitted, will go into infinite loop on invalid input!
            System.out.print("Please try again. Enter second number: ");
        }
        num2 = sc.nextDouble();
        
        // Perform calculation
        if (operation == 'a') {
            Addition(num1, num2);
        } else if (operation == 's') {
            Subtraction(num1, num2);
        } else if (operation == 'm') {
            Multiplication(num1, num2);
        } else if (operation == 'd') {
            if (num2 == 0) {
                System.out.println("Cannot divide by zero!");
            } else {
                Division(num1, num2);
            }
        } else if (operation == 'e') {
            Exponentiation(num1, num2);
        }
        
        System.out.println();
        sc.close();
    }
    
    // Mathematical methods
    public static void Addition(double n1, double n2) {
        System.out.println(n1 + " + " + n2 + " = " + String.format("%.2f", (n1 + n2)));
    }
    
    public static void Subtraction(double n1, double n2) {
        System.out.println(n1 + " - " + n2 + " = " + String.format("%.2f", (n1 - n2)));
    }
    
    public static void Multiplication(double n1, double n2) {
        System.out.println(n1 + " * " + n2 + " = " + String.format("%.2f", (n1 * n2)));
    }
    
    public static void Division(double n1, double n2) {
        System.out.println(n1 + " / " + n2 + " = " + String.format("%.2f", (n1 / n2)));
    }
    
    public static void Exponentiation(double n1, double n2) {
        System.out.println(n1 + " ^ " + n2 + " = " + String.format("%.2f", Math.pow(n1, n2)));
    }
}
