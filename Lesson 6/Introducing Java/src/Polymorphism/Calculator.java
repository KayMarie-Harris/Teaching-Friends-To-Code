package Polymorphism;

// Method Overloading
class Calculator {
    static int add(int a, int b) {
        return a + b;
    }

    static int add(int a) {
        return a + a;
    }

    static double add(double a, double b) {
        return a + b;
    }

    public static void main(String[] args) {
        System.out.println(add(6, 7));
        System.out.println(add(6.9, 4.2));
        System.out.println(add(6));
    }
}

