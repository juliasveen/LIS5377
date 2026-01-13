class Main
{
    public static void main(String args[])
    {
        Methods.getRequirements();
        
        String[] userArray = Methods.createArray(); //Java style array
        
        //prints pseudo-randomly generated numbers, determined by number user inputs
        Methods.copyArray(userArray); //pass array
        
        System.out.println("Thank you for using our program!");
    }
}