public class Vehicle {
    // Attributes
    private String brand;
    private String model;
    private int year;

    // Constructors
    public Vehicle(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    // Getter and Setter methods
    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    // Method to display vehicle information
    public void displayInfo() {
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
        System.out.println("Year: " + year);
    }

    // Example usage
    public static void main(String[] args) {
        // Creating a Vehicle object
        Vehicle myCar = new Vehicle("Toyota", "Corolla", 2022);

        // Displaying vehicle information
        myCar.displayInfo();

        // Modifying vehicle information using setter methods
        myCar.setYear(2023);
        myCar.displayInfo();
    }
}
