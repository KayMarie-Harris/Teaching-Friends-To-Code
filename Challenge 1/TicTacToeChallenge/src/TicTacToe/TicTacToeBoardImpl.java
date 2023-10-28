package TicTacToe;

public class TicTacToeBoardImpl implements TicTacToeBoard{
    // Symbolics:
    protected static final int NO_MOVE = -1;
    protected static final int NO_MATCH = -1;

    protected int[] movesArray;

    public TicTacToeBoardImpl() {
        final int CELL_COUNT = ROW_COUNT*COLUMN_COUNT;
        movesArray = new int[CELL_COUNT];
        for(int i = 0; i < CELL_COUNT; i++) {
            movesArray[i] = NO_MOVE;
        }
    }

    public Mark getMark(int row, int column) {

        if(column < 0 || column >= COLUMN_COUNT || row < 0 || row >= ROW_COUNT)
        {
            throw new AssertionError("Target out of bounds.");
        }

        int placement = getMarkPlacement(row, column);
        Mark markAtPlacement = null;

        for(int i = 0; i < 9; i++)
        {
            if(movesArray[i] == placement && placement != -1)
            {
                if ( i % 2 == 0)
                {
                    markAtPlacement = Mark.X;
                }
                else // i % 2 != 0
                {
                    markAtPlacement = Mark.O;
                }
            }
        }
        return markAtPlacement;
    }

    public void setMark(int row, int column) {
        if(isGameOver())
        {
            throw new AssertionError("Game over! Mark cannot be set.");
        }
        else if(getMark(row,column) != null)
        {
            throw new AssertionError("Space Occupied!");
        }
        else if(row < 0 || row >= ROW_COUNT || column < 0 || column >= COLUMN_COUNT)
        {
            throw new AssertionError("Out of bounds");
        }
        else {
            int placement = getMarkPlacement(row,column);

            // sets moves array representation
            for(int i = 0; i < 9; i++)
            {
                if(movesArray[i] == NO_MOVE)
                {
                    movesArray[i] = placement;
                    break;
                }
            }
        }

    }

    public Mark getTurn() {
        Mark turn = null;
        int turnIndex = 0;

         for(int i = 0; i < 9; i++) {
             if(movesArray[i] == -1){
                 turnIndex = i;
                 break;
             }
         }

        if (turnIndex % 2 == 0 && !isGameOver())
        {
            turn = Mark.X;
        }
        else if(turnIndex % 2 != 0 && !isGameOver())
        {
            turn = Mark.O;
        }

        return turn;
    }

    public boolean isGameOver() {
        boolean gameOver = false;

        if(movesArray[8] != NO_MOVE) // checks to see if movesArray is full
        {
            gameOver = true;
        }
        else if(movesArray[4] != NO_MOVE) // Determines if a win is possible
        {
            if(getWinner() == Mark.X || getWinner() == Mark.O)
            {
                gameOver = true;
            }
        }

        return gameOver;
    }

    public Mark getWinner(){
        Mark winner = null;

        // throws assertion error at the event of an empty board or if less than 5 moves have taken place
        if(movesArray[0] == NO_MOVE || movesArray[4] == NO_MOVE)
        {
            throw new AssertionError("No Winner!");
        }


        // Row winners
        // X
        if(getMark(0,0) == Mark.X && getMark(0,1) == Mark.X && getMark(0,2) == Mark.X)
        {
            winner = Mark.X;
        }
        else if(getMark(1,0) == Mark.X && getMark(1,1) == Mark.X && getMark(1,2) == Mark.X)
        {
            winner = Mark.X;
        }
        else if(getMark(2,0) == Mark.X && getMark(2,1) == Mark.X && getMark(2,2) == Mark.X)
        {
            winner = Mark.X;
        }
        // O
        else if(getMark(0,0) == Mark.O && getMark(0,1) == Mark.O && getMark(0,2) == Mark.O)
        {
            winner = Mark.O;
        }
        else if(getMark(1,0) == Mark.O && getMark(1,1) == Mark.O && getMark(1,2) == Mark.O)
        {
            winner = Mark.O;
        }
        else if(getMark(2,0) == Mark.O && getMark(2,1) == Mark.O && getMark(2,2) == Mark.O)
        {
            winner = Mark.O;
        }

        // Column Winners
        // X
        else if(getMark(0,0) == Mark.X && getMark(1,0) == Mark.X && getMark(2,0) == Mark.X)
        {
            winner = Mark.X;
        }
        else if(getMark(0,1) == Mark.X && getMark(1,1) == Mark.X && getMark(2,1) == Mark.X)
        {
            winner = Mark.X;
        }
        else if(getMark(0,2) == Mark.X && getMark(1,2) == Mark.X && getMark(2,2) == Mark.X)
        {
            winner = Mark.X;
        }
        // O
        else if(getMark(0,0) == Mark.O && getMark(1,0) == Mark.O && getMark(2,0) == Mark.O)
        {
            winner = Mark.O;
        }
        else if(getMark(0,1) == Mark.O && getMark(1,1) == Mark.O && getMark(2,1) == Mark.O)
        {
            winner = Mark.O;
        }
        else if(getMark(0,2) == Mark.O && getMark(1,2) == Mark.O && getMark(2,2) == Mark.O)
        {
            winner = Mark.O;
        }

        // Diagonal Winners
        // Diag1
        else if(getMark(0,0) == Mark.X && getMark(1,1) == Mark.X && getMark(2,2) == Mark.X)
        {
            winner = Mark.X;
        }
        else if(getMark(0,0) == Mark.O && getMark(1,1) == Mark.O && getMark(2,2) == Mark.O)
        {
            winner = Mark.O;
        }
        // Diag2
        else if(getMark(0,2) == Mark.X && getMark(1,1) == Mark.X && getMark(2,0) == Mark.X)
        {
            winner = Mark.X;
        }
        else if(getMark(0,2) == Mark.O && getMark(1,1) == Mark.O && getMark(2,0) == Mark.O)
        {
            winner = Mark.O;
        }


        return winner;
    }

    // Helper Method Checks row position, then column position
    // each position corresponds on the board as follows:
    // (0,0) is 0, (0,1) is 1, (0,2) is 2,
    // (1,0) is 3, (1,1) is 4, (1,2) is 5,
    // (2,0) is 6, (2,1) is 7, (2,2) is 8,
    // where board representation is
    // 0|1|2
    //-------
    // 3|4|5
    //-------
    // 6|7|8
    private int getMarkPlacement(int row, int column) {
        int placement = NO_MATCH;
        if (row == 0)
        {
            if (column == 0)
            {
                placement = 0;
            }
            else if (column == 1)
            {
                placement = 1;
            }
            else if (column == 2)
            {
                placement = 2;
            }
        }
        else if (row == 1)
        {
            if (column == 0)
            {
                placement = 3;
            }
            else if (column == 1)
            {
                placement = 4;
            }
            else if (column == 2)
            {
                placement = 5;
            }
        }
        else if (row == 2)
        {
            if (column == 0)
            {
                placement = 6;
            }
            else if (column == 1)
            {
                placement = 7;
            }
            else if (column == 2)
            {
                placement = 8;
            }
        }
        return placement;
    }


    @Override
    public String toString()
    {
        String TicTacToeBoard = "";
        if (getMark(0,0) == null)
        {
            TicTacToeBoard += " |";
        }
        else
        {
            TicTacToeBoard += getMark(0,0) + "|";
        }
        if (getMark(0,1) == null)
        {
            TicTacToeBoard += " |";
        }
        else
        {
            TicTacToeBoard += getMark(0,1) + "|";
        }
        if (getMark(0,2) == null)
        {
            TicTacToeBoard += " \n";
        }
        else
        {
            TicTacToeBoard += getMark(0,2) + "\n";
        }

        TicTacToeBoard += "_ _ _ \n";

        if (getMark(1,0) == null)
        {
            TicTacToeBoard += " |";
        }
        else
        {
            TicTacToeBoard += getMark(1,0) + "|";
        }
        if (getMark(1,1) == null)
        {
            TicTacToeBoard += " |";
        }
        else
        {
            TicTacToeBoard += getMark(1,1) + "|";
        }
        if (getMark(1,2) == null)
        {
            TicTacToeBoard += " \n";
        }
        else
        {
            TicTacToeBoard += getMark(1,2) + "\n";
        }

        TicTacToeBoard += "_ _ _ \n";

        if (getMark(2,0) == null)
        {
            TicTacToeBoard += " |";
        }
        else
        {
            TicTacToeBoard += getMark(2,0) + "|";
        }
        if (getMark(2,1) == null)
        {
            TicTacToeBoard += " |";
        }
        else
        {
            TicTacToeBoard += getMark(2,1) + "|";
        }
        if (getMark(2,2) == null)
        {
            TicTacToeBoard += " \n";
        }
        else
        {
            TicTacToeBoard += getMark(2,2) + "\n";
        }

        return TicTacToeBoard;
    }


}
