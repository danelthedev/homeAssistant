import pygame
import time

class AssistantDisplay:
    def __init__(self):
        """
        Initialize the display window and load resources.
        """
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
        """
        Display the silent image on the window, stretched to fill the window.
        """
        scaled_image = pygame.transform.scale(self.silent_image, self.screen.get_size())
        self.screen.blit(scaled_image, (0, 0))
        pygame.display.flip()

    def show_talking(self):
        """
        Alternate between talking images on the window, stretched to fill the window.
        This ensures smooth alternation using a fixed frame update interval.
        """
        start_time = time.time()
        while pygame.mixer.music.get_busy():
            self.current_image_index = (self.current_image_index + 1) % len(self.talking_images)
            scaled_image = pygame.transform.scale(self.talking_images[self.current_image_index], self.screen.get_size())
            self.screen.blit(scaled_image, (0, 0))
            pygame.display.flip()
            time.sleep(0.5 - ((time.time() - start_time) % 0.5))

    def cleanup(self):
        """
        Clean up resources and quit pygame.
        """
        pygame.quit()
