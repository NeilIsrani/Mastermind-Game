import unittest

class TestMastermind(unittest.TestCase):
    def setUp(self):
        self.secret_guess = ["red", "blue", "green", "yellow"]
        self.simulated_user_guess = ["blue", "red", "purple", "yellow"]

    def test_count_correct_color_correct_placement(self):
        '''
        Checks for "correct color/correct placement" based on logic
        of pointer_fller in my mastermind game of forming the black
        pointers for matching color and position.
        '''
        correct_placement = 0
        for i in range(len(self.secret_guess)):
            if self.secret_guess[i] == self.simulated_user_guess[i]:
                correct_placement += 1
        self.assertEquals(correct_placement, 1, " 1 correct placements of colors")

    def test_count_correct_color_incorrect_placement(self):
        '''
        Checks for "correct color/correct placement" based on logic
        of pointer_fillerin my mastermind game of forming red pointers
        indicating wrong placement but inclusive color in secret_guess.
        '''
        # Check for "correct color/incorrect placement"
        correct_color = 0
        for user_color in self.simulated_user_guess:
            if user_color in self.secret_guess:
                correct_color += 1
        self.assertEquals(correct_color, 3, "3 colors common")

if __name__ == "__main__":
    unittest.main(verbosity=3)
main()
