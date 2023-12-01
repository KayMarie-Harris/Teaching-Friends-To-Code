import TicTacToe.TicTacToeBoardImpl;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        TicTacToeBoardImpl board = new TicTacToeBoardImpl();
        System.out.println(board);

        int[] myNums = {1,2,3,4,5,6};
        //     index =  0,1,2,3,4,5

        for(int i = 0; i < 6; i++){ // myNums.length returns 6, i++ == (i = i + 1)
            if(myNums[i] == 5){
                // some logic
                break;
            }
        }

        // break brings you here
        // some logic...
    }
}