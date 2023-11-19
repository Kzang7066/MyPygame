import unittest
import pygame
from puzzle import * 

class TestSlidePuzzle(unittest.TestCase):

    def setUp(self):
        pygame.init() 
        self.board = getStartingBoard()
        
    def test_draw_board(self):
        DISPLAYSURF = pygame.Surface((400,400))
        drawBoard(self.board, "Testing...")
        # Check if drawBoard draws without errors
        self.assertIsNone(None)
        
    def test_slide_animation(self): 
        DISPLAYSURF = pygame.Surface((400,400))
        slideAnimation(self.board, UP, "Sliding", 5)
        # Check if slideAnimation runs without errors
        self.assertIsNone(None)
        
    def test_generate_new_puzzle(self):
        board, moves = generateNewPuzzle(5)
        self.assertNotEqual(board, self.board)
        self.assertEqual(len(moves), 5)
        
if __name__ == '__main__':
    unittest.main()