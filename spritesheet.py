import pygame
# from maze_maps import Maze_maps
# from main import MazeGame
# instance = MazeGame(1600,900,Maze_maps.maze_multi)

class SpriteSheet():
	def __init__(self, image):
		
		self.sheet = image

	def get_image(self, frame, width, height, scale, colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (35* scale, 35* scale))
		image.set_colorkey(colour)

		return image
	




