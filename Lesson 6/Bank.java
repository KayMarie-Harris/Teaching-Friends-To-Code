public class Bank {
    // Attributes
    private String accountNumber;
    private double balance;
    private String ownerName;

    // Setters
    public void setAccountNumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public void setOwnerName(String ownerName) {
        this.ownerName = ownerName;
    }

    // Getters
    public String getAccountNumber() {
        return accountNumber;
    }

    public double getBalance() {
        return balance;
    }

    public String getOwnerName() {
        return ownerName;
    }

    // Example usage
    public static void main(String[] args) {
        // Creating a Bank object
        Bank bankAccount = new Bank();

        // Setting attributes using setter methods
        bankAccount.setAccountNumber("123456789");
        bankAccount.setBalance(1000.0);
        bankAccount.setOwnerName("Alice");

        // Getting and displaying attributes using getter methods
        String accountNumber = bankAccount.getAccountNumber();
        double balance = bankAccount.getBalance();
        String ownerName = bankAccount.getOwnerName();

        System.out.println("Account Number: " + accountNumber);
        System.out.println("Balance: $" + balance);
        System.out.println("Owner Name: " + ownerName);
    }
}
