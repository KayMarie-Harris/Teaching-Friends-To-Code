package Polymorphism;

// Animal class (Parent class)
class Animal {
    private String name;

    Animal(String name){
        this.name = name;
    }

    void makeSound(){
        System.out.println("some sound");
    }

    void sleep() {
        System.out.println(name + " is sleeping");
    }

    String getName() {
        return name;
    }
}

// Child

class Dog extends Animal {
    Dog(String name) {
        super(name);
    }

    @Override
    void makeSound() {
        System.out.println(getName() + " says woof! woof!");
    }

    void fetch() {
        System.out.println(getName() + " is fetching the ball");
    }
}

class Cat extends Animal {
    Cat(String name) {
        super(name);
    }

    @Override
    void makeSound() {
        System.out.println(getName() + " says meow");
    }

    void climb() {
        System.out.println(getName() + " is climbing the tree");
    }
}

