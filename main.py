import sys
import pygame

from src.play import play
from src.start_screen import start_screen
from src.terminate import terminate


def main() -> None:
    pygame.init()
    pygame.display.set_caption('Vampire Survivors Fanmade v.1.0')

    FPS = 60
    size = 1920, 1080

    display_info = pygame.display.Info()
    pygame.display.set_mode((display_info.current_w, display_info.current_h))
    screen = pygame.display.set_mode(size)

    # start_screen(screen)
    play(screen, FPS)
    terminate()


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
