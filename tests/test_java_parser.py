import java_parser
import javalang


def test_getNumberOfClasses():
    """ test if the function gets the gets the number of
    classes"""

    javaSting = '''
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
    print("Actucal: ", actualString)
    assert False
