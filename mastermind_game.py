from turtle import Turtle, Screen
from marble import Marble
import datetime
import traceback
import random
main_colors = ["red", "blue", "green", "yellow", "purple", "black"]
#filled_list = ["red", "blue", "green", "yellow"]
empty_rows = []
selection_rn = []
current_row_rn = [1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,9,9,9,9,9,9,10,10,10,10, 10, 11, 11, 11, 11, 11, 11]
filled_row = []

class Initializer:
    """
    Class for initializing the Mastermind game.
    """
    def __init__(self):
        '''
        Initialize the Mastermind game.

        This function sets up the game environment, including the turtle screen, marbles, and necessary shapes.
        It prompts the player for their name and initializes other game-related attributes.

        Parameters:
        None
        
        Returns:
        None
        '''
        self.turtle = Turtle()
        self.turtle.screen = Screen()
        self.name = self.turtle.screen.textinput("CS5001 Mastermind", "Name of first player:")
        self.gamemode = shuffle(main_colors)
        print(self.gamemode)
        self.turtle.marbles = []
        self.turtle.screen.setup(width= 700, height=1100)
        self.turtle.screen.bgcolor("white")
        self.turtle.screen.title("Mastermind")
        self.turtle.screen.register_shape("checkbutton.gif")
        self.turtle.screen.register_shape("quit.gif")
        self.turtle.screen.register_shape("xbutton.gif")
        self.turtle.screen.register_shape("winner.gif")
        self.turtle.screen.register_shape("quitmsg.gif")
        self.turtle.screen.register_shape("Lose.gif")
        self.turtle.screen.register_shape("leaderboard_error.gif")
        self.turtle.screen.register_shape("file_error.gif")
    
    def add_checkbutton(self):
        '''
        Add a check button to the game interface.

        This function stamps a check button shape on the turtle screen.

        Parameters:
        None

        Returns:
        None
        '''
        self.turtle.penup()
        self.turtle.goto(-20, -250)
        self.turtle.pendown()
        self.turtle.speed(10)
        self.turtle.hideturtle()
        self.turtle.shape("checkbutton.gif")
        self.turtle.stamp()

    def add_cross(self):
        '''
        Add a cross button to the game interface meant for deleting a
        chosen selection of 4 colors on the gameboard.

        Parameters:
        None

        Returns:
        None
        '''
        self.turtle.penup()
        self.turtle.goto(50,- 250)
        self.turtle.pendown()
        self.turtle.speed(10)
        self.turtle.hideturtle()
        self.turtle.shape("xbutton.gif")
        self.turtle.stamp() 

    def add_quit(self):
        '''
        Add a quit button to the game interface.

        This function stamps a quit button shape on the turtle screen.

        Parameters:
        None

        Returns:
        None
        '''
        self.turtle.penup()
        self.turtle.goto(200,- 250)
        self.turtle.pendown()
        self.turtle.speed(10)
        self.turtle.hideturtle()
        self.turtle.shape("quit.gif")
        self.turtle.stamp()

    def grid_maker(self):
        '''
        Create the 3 game grids.

        This function draws the game grid on the turtle screen.

        Parameters:
        None

        Returns:
        None
        '''
        self.turtle.penup()
        self.turtle.goto(-300,330) # top left corner
        self.turtle.pendown()
        self.turtle.speed(10)
        self.turtle.color("black")
        self.turtle.forward(400)
        self.turtle.right(90)
        self.turtle.forward(500)
        self.turtle.right(90)
        self.turtle.forward(400)
        self.turtle.right(90)
        self.turtle.forward(500)
        self.turtle.right(90)
        self.turtle.penup()
        self.turtle.goto(120,330) # mid right corner
        self.turtle.pendown()
        self.turtle.speed(10)
        self.turtle.color("blue")
        self.turtle.forward(170)
        self.turtle.right(90)
        self.turtle.forward(500)
        self.turtle.right(90)
        self.turtle.forward(170)
        self.turtle.right(90)
        self.turtle.forward(500)
        self.turtle.right(90)
        self.turtle.penup()
        self.turtle.goto(-300,-180) # bottom left corner
        self.turtle.pendown()
        self.turtle.speed(10)
        self.turtle.color("black")
        self.turtle.forward(600)
        self.turtle.right(90)
        self.turtle.forward(130)
        self.turtle.right(90)
        self.turtle.forward(600)
        self.turtle.right(90)
        self.turtle.forward(130)
        self.turtle.right(90)
        
    def log_error(self, error_type):
        '''
        This function logs error information, including
        the timestamp and error type, to a file named "mastermind_errors.err".

        Parameters:
        error_type (str): The type of error.

        Returns:
        None
        '''
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_info = f"Date/Time: {timestamp}\nError Type: {error_type}\n\n"
        with open("mastermind_errors.err", "a") as error_file:
            error_file.write(error_info)
        
    def empty_marbles(self):
        '''

        This function initializes the empty 4 x 10 marbles on the game board,
        as well as, the 2x2 pointer circles for each row.

        Parameters:
        None

        Returns:
        None
        '''
        start_x_marbles = -270
        start_y_marbles = 280
        self.turtle.penup()
        self.turtle.speed("fastest")  
        i = 0
        while i < 4:
            j = 0
            while j < 10:
                marble = Marble(start_x_marbles + i * 60, start_y_marbles - j * 45, "white", 20)
                marble.draw_empty(start_x_marbles + i * 60, start_y_marbles - j * 45, 20)
                if i == 3:  # Draw pointers only after the last marble in a row
                    k = 0
                    while k < 2:
                        l = 0
                        while l < 2:
                            pointer = Marble(start_x_marbles + (i+1) * 60 + k * 20, start_y_marbles - j * 45 - l * 20 + 30, "white", 5)
                            pointer.draw_empty(start_x_marbles + (i+1) * 60 + k * 20, start_y_marbles - j * 45 - l * 20 + 30, 5)
                            l += 1
                        k += 1
                j += 1
            i += 1
        self.turtle.getscreen().update()

    def quitting(self):
        '''
        This function adds a quit button to the game
        to exit when clicked on. Can only be activated
        if the game is first played atleast one guess.

        Parameters:
        None

        Returns:
        None
        '''
        self.turtle.penup()
        self.turtle.goto(0,0)
        self.turtle.pendown()
        self.turtle.shape("quitmsg.gif")
        self.turtle.stamp()
        turtle.quit()

    def leaderboard_initial(self):
        '''
        This function writes out the leaderboard.
        It maintains contunuity after the program
        is re-run by storing results in a txt file.
        It also handles filenotfound error and
        creates a blank file for it.

        Parameters:
        None

        Returns:
        None
        '''
        try:
            self.turtle.penup()
            self.turtle.goto(140, 250)
            self.turtle.pendown()
            self.turtle.write("Leaders:", align="left", font=("Arial", 25, "bold normal"))

            with open("leaderboard.txt", "r") as infile:
                filler = infile.read().splitlines()

            self.turtle.penup()
            self.turtle.goto(140, 80)
            self.turtle.pendown()
            self.turtle.write("\n".join(filler[::-1]), align="left", font=("Arial", 20, "normal"))

        except FileNotFoundError as file_not_found:
            self.turtle.penup()
            self.turtle.goto(0, 0)
            self.turtle.pendown()
            self.turtle.shape("leaderboard_error.gif")
            error_message = f"FileNotFoundError: {str(file_not_found)}"
            self.log_error(error_message)

            with open("leaderboard.txt", "w") as outfile:
                pass  # Goes on to create an empty file if file not found

            filler = []  

            self.turtle.penup()
            self.turtle.goto(140, 200)
            self.turtle.pendown()
            self.turtle.write("\n".join(filler[::-1]), align="left", font=("Arial", 20, "normal"))


    def leaderboard(self, score):
        '''
        This function updates the leaderboard.
        It maintains contunuity after the program
        is re-run by storing results in a txt file
        and making sure to update it for the best score
        and rank scores within.

        Parameters:
        None

        Returns:
        None
        '''
        leaderboard_data = []
        scores = []
        player_names = []

        try:
            with open("leaderboard.txt", "r") as infile:
                leaderboard_data = infile.readlines()
        except FileNotFoundError:
            pass  # Ignores the error if the file doesn't exist

        # Extracts existing scores and player names from leaderboard data
        for line in leaderboard_data:
            points, player_name = line.strip().split(":")
            scores.append(int(points))
            player_names.append(player_name)

        # Adds the current score and player name to the lists
        scores.append(score)
        player_names.append(self.name)

        # Inserts the new score at the correct position in the lists
        index = len(scores) - 1
        while index > 0 and scores[index - 1] > score:
            scores[index], scores[index - 1] = scores[index - 1], scores[index]
            player_names[index], player_names[index - 1] = player_names[index - 1], player_names[index]
            index -= 1

        # Writes the updated leaderboard data to the file
        with open("leaderboard.txt", "w") as outfile:
            for points, player_name in zip(reversed(scores), reversed(player_names)):
                outfile.write(f"{points}:{player_name}\n")
        
    def selectors(self):
        '''
        Draws 6 different colors selectors for the game as buttons.
        '''
        colors = ["blue", "red", "green", "yellow", "purple", "black"]
        start_x_selectors = -270
        start_y_selectors = -270
        self.turtle.marble_selectors = []
        for index, value in enumerate(colors):
            selector = Marble(start_x_selectors + index * 40, start_y_selectors, value, 20)
            selector.draw(start_x_selectors + index * 40, start_y_selectors, value, 20)
            

    def marbles_filler(self, color_choice, current_row, current_number):
        '''
        This function fills in marbles in a row according to position provided
        by the current row, current column (current_number) and color choice.

        Parameters:
        color_choice(string), current_row(int), current_number(int)

        Returns:
        None
        '''
        
        start_x_marbles = -270 
        start_y_marbles = 280
        marble_filled = Marble(start_x_marbles + (current_number - 1) * 60, start_y_marbles - (current_row - 1) * 45, "white", 20)
        marble_filled.draw(start_x_marbles + (current_number - 1) * 60, start_y_marbles - (current_row - 1) * 45, color_choice, 20)

    def scorer(self, filled_list):
        '''
        This function takes in a filled_list list for the filled row and matches
        it with the correct row set up before the game in the main. Accordingly,
        it processes the score to the leaderboard.
        
        Parameters:
        filled_list(list)

        Returns:
        None
        '''
        
        if filled_list == self.gamemode:
            score = current_row_rn[0] - 1 
            self.leaderboard(score)
            self.turtle.penup()
            self.turtle.goto(0, 0)
            self.turtle.pendown()
            self.turtle.shape("winner.gif")
            self.turtle.stamp()
        if current_row_rn[1] == 11 and filled_list != self.gamemode:
            self.turtle.penup()
            self.turtle.goto(0, 0)
            self.turtle.pendown()
            self.turtle.shape("Lose.gif")
            self.turtle.stamp()
        
    def pointer_filler(self, filled_list, current_row):
        '''
        This function takes in a filled_list list for the filled row and matches
        it with the correct row set up before the game in the main. Accordingly,
        it fills in the score in terms of black and red pegs
        to the pointers of the relevant row to indicate exact color & placement
        match or just color match (but wrong position) accordingly. It fills
        the pegs top left, bottom left, top right and then bottom right for the
        order.
        
        Parameters:
        filled_list(list), current_row (int)

        Returns:
        None
        '''
        correct_filled_list = self.gamemode
        start_x_marbles = -270
        start_y_marbles = 280
        self.turtle.penup()
        self.turtle.speed("fastest")  

        for i in range(len(filled_list)):
            k = i // 2
            l = i % 2
            x = start_x_marbles + (3 + 1) * 60 + k * 20
            y = start_y_marbles - (current_row - 2) * 45 - l * 20 + 30

            if filled_list[i] == correct_filled_list[i]:
                color = "black"
            elif filled_list[i] in correct_filled_list:
                color = "red"
            elif filled_list[i] not in correct_filled_list[i]:
                pointer = Marble(x, y, "white", 5)
                pointer.draw_empty(x, y, 5)
                continue
            pointer = Marble(x, y, "white", 5)
            pointer.draw(x, y, color, 5)
        
    def selector(self, x, y):
        '''
        This function acts as a clicker for the 6 colored selectors made previously.
        It also makes sure that it keeps track of the current row and modifies the
        global list for it according to game progression. 
        
        Parameters:
        None

        Returns:
        None
        '''
        selection_x = x
        selection_y = y
        current_row = current_row_rn.pop(0) # removes values to maintain game continuity to next row when function re-run
        selection = selection_rn.pop(0)
        try:
            if selection_x < -250 and selection_x > -290 and selection_y < -230 and selection_y > -270:
                filled_row.append("blue")
                selector_vanish = Marble(-270, -265, "black", 16)
                selector_vanish.draw(-270, -265, "white", 16)
                self.marbles_filler("blue", current_row, selection)
            elif selection_x < -210 and selection_x > -250 and selection_y < -230 and selection_y > -270:
                filled_row.append("red")
                selector_vanish = Marble(-230, -265, "white", 16)
                selector_vanish.draw(-230, -265, "white", 16)
                self.marbles_filler("red", current_row, selection)
            elif selection_x < -170 and selection_x > -210 and selection_y < -230 and selection_y > -270:
                filled_row.append("green")
                selector_vanish = Marble(-190, -265, "white", 16)
                selector_vanish.draw(-190, -265, "white", 16)
                self.marbles_filler("green", current_row, selection)
            elif selection_x < -130 and selection_x > -170 and selection_y < -230 and selection_y > -270:
                filled_row.append("yellow")
                selector_vanish = Marble(-150, -265, "white", 16)
                selector_vanish.draw(-150, -265, "white", 16)
                self.marbles_filler("yellow", current_row, selection)
            elif selection_x < -90 and selection_x > -130 and selection_y < -230 and selection_y > -270:
                filled_row.append("purple")
                selector_vanish = Marble(-110, -265, "white", 16)
                selector_vanish.draw(-110, -265, "white", 16)
                self.marbles_filler("purple", current_row, selection)
            elif selection_x < -50 and selection_x > -90 and selection_y < -230 and selection_y > -270:
                filled_row.append("black")
                selector_vanish = Marble(-70, -265, "white", 16)
                selector_vanish.draw(-70, -265, "white", 16)
                self.marbles_filler("black", current_row, selection)
            else:
                pass
        except IndexError as error:
            self.log_error("Index Error in Selector-- click was made out of bounds", str(error))

    
    def button_pusher(self, x, y):
        '''
        This function acts as a clicker for check, cross and exit buttons.
        
        Parameters:
        None

        Returns:
        None
        '''
        selection_x = x
        selection_y = y
        current_row = current_row_rn[0]
        if len(filled_row) % 4 == 0 and selection_x < 8 and selection_x > -48 and selection_y < -220 and selection_y > -280:
            current_operations = filled_row[-4:] # takes most recent selection of 4
            self.pointer_filler(current_operations, current_row)
            self.scorer(current_operations)
            filled_row.clear()
        elif selection_x < 80 and selection_x > 20 and selection_y > -280 and selection_y < -220:
            for i in range(0, 4):
                start_x_marbles = -270 
                start_y_marbles = 280
                vanisher = Marble(start_x_marbles + i * 60, start_y_marbles - (current_row - 2) * 45, "white", 20)
                vanisher.draw(start_x_marbles + i * 60, start_y_marbles - (current_row - 2) * 45, "white", 20)
            if current_row != 1:
                numerical = 5 - (len(current_row_rn) % 5)
                for i in range(numerical):
                    current_row_rn.insert(0, current_row - 1)
            elif current_row == 1:
                numerical = 4 - (len(current_row_rn) % 5)
                for i in range(numerical):
                    current_row_rn.insert(0, current_row - 1)
            filled_row.clear()
        elif selection_x > 150 and selection_x < 250 and selection_y > -275 and selection_y < -225:
            self.quitting()
        else:
            pass


    def click_decider(self, x, y):
        '''
        This function directs clicks to either the
        color selector or buttons functions.
        
        Parameters:
        None

        Returns:
        None
        '''
        selection = 1
        while selection < 5:
            if -290 < x < -50 and -270 < y < -230:
                selection_rn.append(selection)
            selection += 1
        self.selector(x, y)
        if -48 < x < 250 and -280 < y < -220:
            self.button_pusher(x, y)
            selection_rn.clear()
        else:
            pass
            
            
    def start(self):
        '''
        This function sets up the gameboard.
        
        Parameters:
        None

        Returns:
        None
        '''
        self.grid_maker()
        self.add_checkbutton()
        self.add_quit()
        self.add_cross()
        self.leaderboard_initial()
        self.empty_marbles()
        self.leaderboard_initial()

    def choices(self):
        '''
        This function sets up the selector colors.
        
        Parameters:
        None

        Returns:
        None
        '''
        self.selectors()

    def click_handler(self):
        '''
        This function sets up the positional arguments
        for click_decider
        
        Parameters:
        None

        Returns:
        x (float), y (float)
        '''
        self.turtle.screen.onclick(self.click_decider)
    

def shuffle(color_list: list) -> list:
    '''
    This function shuffles a list of colors
    
    Parameters: list of colors
    
    Returns: list of shuffled colors
    '''
    shuffled_deck = list(color_list)  
    n = len(list(color_list))

    for i in range(n): 
        j = random.randint(0, i)  
        shuffled_deck[i], shuffled_deck[j] = shuffled_deck[j], shuffled_deck[i]  
    shuffled_deck.pop()
    shuffled_deck.pop()
    return shuffled_deck


def main():
    try:
        initial = Initializer()
        initial.start()
        initial.choices()
        current_row = 1
        while current_row < 200: # arbitrarily high number indicating potential game moves
            initial.click_handler()
            initial.choices()
            current_row += 1
    except Exception as error: #logs all errors enountered during game
        initial.log_error(str(error))
        traceback.print_exc()
        
if __name__ == "__main__":
    main() 
