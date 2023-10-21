package Polymorphism;
// Method Overriding

// Shape class (Parent class)
class Shape {
    public void draw() {
        System.out.println("Drawing a Shape");
    }
}

// Child Class 1
class Circle extends Shape {
    @Override
    public void draw() {
        System.out.println("Drawing a circle");
    }
}

// Square class (Child class 2)
class Square extends Shape {
    @Override
    public void draw() {
        System.out.println("Drawing a square");
    }
}

