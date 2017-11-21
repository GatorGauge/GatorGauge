//******************************************************
// Honor Code: This work is mine unless otherwise cited.
// Austin Bristol
// CMPSC 111 Fall 2015
// Lab #3
// Date: 9/11/15
//
// Purpose:
//******************************************************

/*
Multiline comment
for testing
purposes
*/

import java.util.Date; // needed for printing today's date
import java.util.Scanner; // needed for getting user input

public class TipCalculator
{
    //-------------------------------------------
    // main method: program execution begins here
    //-------------------------------------------
    public static void main(String[] args)
    {
        // Label output with name and date:
        System.out.println("Austin Bristol\n Lab #3\n" + new Date() + "\n");

        Scanner userInput = new Scanner (System.in); // Creates an instance of the scanner class so that the user can input

        System.out.println("\nPlease enter your name: ");
        String name = userInput.nextLine(); //Asks for the user's name and saves it under the variable name

        System.out.println("\nHello " + name + "! Welcome to the Tip Calculator!"); //Welcoming message that uses the name variable

        System.out.println("\nPlease enter the restaurant's bill amount:");
        float billAmount = userInput.nextFloat(); //Asks for the bill amount and saves it as a float under the variable billAmount

        System.out.println("\nPlease enter your desired tip percentage: ");
        float tipPercent = userInput.nextFloat(); //Asks for what percent the user wants and saves it as a float under the variable tipPercent

        float tip = (tipPercent/100) * billAmount; //Creates a new variable, tip, which calculates the tip by dividing the tipPercent by 100 and multiplying that result by the billAmount
        float totalBillAmount = tip + billAmount; //This variable adds the original bill amount with the newly calculated tip

        System.out.println("\nYour original bill amount is $" + billAmount);
        System.out.println("Your additional tip is $" + tip);
        System.out.println("Your bill total is now $" + totalBillAmount); //Prints different values stored in variables


        System.out.println("\nPlease enter how many people will be splitting the check");
        int totalPeople = userInput.nextInt(); //Asks for the amount of people splitting the check and saves it as a variable under totalPeople

        float split = totalBillAmount/totalPeople;
        System.out.println("\nEach person should pay $" + split); //Calculates the amount of money each person should pay and then prints it

        System.out.println("\nThank you! Have a great day!");
    }
}