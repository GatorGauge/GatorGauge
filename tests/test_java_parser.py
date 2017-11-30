
import java_parser
import javalang


def test_getNumberOfClasses():
    """ test if the function gets the gets the number of
    classes"""
    javaString = '''
        class Computer {
      Computer() {
        System.out.println("Constructor of Computer class.");
      }

      void computer_method() {
        System.out.println("Power gone! Shut down your PC soon...");
      }

      public static void main(String[] args) {
        Computer my = new Computer();
        Laptop your = new Laptop();

        my.computer_method();
        your.laptop_method();
      }
    }

    class Laptop {
      Laptop() {
        System.out.println("Constructor of Laptop class.");
      }

      void laptop_method() {
        System.out.println("99% Battery available.");
      }
    }
        '''
    actualString = java_parser.getNumberOfClasses(javaString)
    correctString = 2
    assert actualString == correctString

def test_getNumberOfLines():
    """ Test if the function gets the number of lines in a javaString"""
    javaString = '''
        public class Factorial
    {
    public static void main(String[] args)
    {	final int NUM_FACTS = 100;
        for(int i = 0; i < NUM_FACTS; i++)
            System.out.println( i + "! is " + factorial(i));
    }

    public static int factorial(int n)
    {	int result = 1;
        for(int i = 2; i <= n; i++)
            result *= i;
        return result;
    }
    '''
    actualString = java_parser.getNumberOfLines(javaString)
    correctString = 14
    assert actualString == correctString
