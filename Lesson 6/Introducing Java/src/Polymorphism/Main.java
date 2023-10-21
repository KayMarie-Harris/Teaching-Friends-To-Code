package Polymorphism;

// Main class to test polymorphism
public class Main {
    public static void main(String[] args) {
        // Polymorphism example
//        Shape shape1 = new Circle(); // Reference of Shape, Object of Circle
//        Shape shape2 = new Square(); // Reference of Shape, Object of Square
//
//        shape1.draw(); // Calls the draw() method of Circle class
//        shape2.draw(); // Calls the draw() method of Square class
//
        Animal myDog = new Dog("Buddy"); // Reference of Animal, Object of Dog
        Animal myCat = new Cat("Whiskers"); // Reference of Animal, Object of Cat

        myDog.makeSound(); // Calls the makeSound() method of Dog class
        myDog.sleep(); // Calls the sleep() method of Animal class (inherited by Dog)
        ((Dog) myDog).fetch(); // Calls the fetch() method of Dog class

        myCat.makeSound(); // Calls the makeSound() method of Cat class
        myCat.sleep(); // Calls the sleep() method of Animal class (inherited by Cat)
        ((Cat) myCat).climb(); // Calls the climb() method of Cat class
    }
}
