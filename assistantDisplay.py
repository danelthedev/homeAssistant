import pygame

class AssistantDisplay:
    def __init__(self):
        pygame.init()

        # Set up the window
        self.screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        pygame.display.set_caption("Assistant Display")

        # Load images
        self.silent_image = pygame.image.load("resources/silent.png")
        self.talking_images = [
            pygame.image.load("resources/talking1.png"),
            pygame.image.load("resources/talking2.png"),
        ]

        self.current_image_index = 0

    def show_silent(self):
        scaled_image = pygame.transform.scale(self.silent_image, self.screen.get_size())
        self.screen.blit(scaled_image, (0, 0))
        pygame.display.flip()

    def show_talking(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.talking_images)
        scaled_image = pygame.transform.scale(self.talking_images[self.current_image_index], self.screen.get_size())
        self.screen.blit(scaled_image, (0, 0))
        pygame.display.flip()

    def cleanup(self):
        pygame.quit()
