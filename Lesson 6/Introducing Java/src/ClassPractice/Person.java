package ClassPractice;

public class Person {
    // Attributes
    private String name;
    private int age;
    private String address;

    // Constructor
    public Person(String name, int age, String address){
        this.name = name;
        this.age = age;
        this.address = address;
    }

    // Getter and Setter Methods
    public String getName() {
        return name;
    }
    public int getAge() {
        return age;
    }
    public String getAddress() {
        return address;
    }

    public void setName(String name) {
        this.name = name;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public void setAddress(String address) {
        this.address = address;
    }

    public static void main(String[] args) {
        // Create a Person Object
        Person person = new Person("Alice",30, "123 Main St");
        // person.setName("Bob");
        System.out.println(person.getName());

    }

}
