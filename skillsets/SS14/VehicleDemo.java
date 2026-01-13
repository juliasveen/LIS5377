import java.util.Scanner;

//Note:
//superclass = parent = base
//subclass = child = derived

class VehicleDemo
{
    public static void main(String[] args)
    {
        // initialize variables and create Scanner object
        String mk = "";
        String md = "";
        int yr = 0;
        Scanner sc = new Scanner(System.in);
        
        System.out.println("\n/////Below are default constructor values://///");
        Vehicle v1 = new Vehicle(); //create default object
        System.out.println("Make = " + v1.getMake());
        System.out.println("Model = " + v1.getModel());
        System.out.println("Year = " + v1.getYear());
        
        System.out.println("\n/////Below are user-entered values://///");
        
        // get user input
        System.out.print("\nMake: ");
        mk = sc.nextLine();
        
        System.out.print("Model: ");
        md = sc.nextLine();
        
        System.out.print("Year: ");
        yr = sc.nextInt();
        
        Vehicle v2 = new Vehicle(mk, md, yr);
        System.out.println("Make = " + v2.getMake());
        System.out.println("Model = " + v2.getModel());
        System.out.println("Year = " + v2.getYear());
        //or...
        //v2.print();
        
        System.out.println("\n/////Below using setter methods to pass literal values, then print() method to display values://///");
        v2.setMake("Chevrolet");
        v2.setModel("Corvette Z06");
        v2.setYear(2023);
        v2.print();
        
        //also, demo
        //v2.setModel("Cougar");
        //System.out.println("Model = " + v2.getModel());
    }
}