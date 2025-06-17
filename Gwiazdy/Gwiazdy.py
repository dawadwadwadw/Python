import pygame
import sys
import math

pygame.init()

class CStar:
    def __init__(self, X, Y, Rd, Rm, Angle):
        self.X = X
        self.Y = Y
        self.Rd = Rd
        self.Rm = Rm
        self.Angle = Angle

        self.dAngle = math.pi / 100.0
        self.pkty = [(0, 0) for _ in range(12)]

        self.Oblicz()

    def Rysuj(self, screen):
        pygame.draw.lines(screen, (255, 255, 255), True, self.pkty)

    def Obrot(self):
        self.Angle += self.dAngle
        self.Oblicz()

    def Oblicz(self):
        for i in range(6):
            alfa = self.Angle + i * (math.pi / 3)
            self.pkty[i * 2] = (self.X + self.Rd * math.cos(alfa), self.Y + self.Rd * math.sin(alfa))

            alfa += math.pi / 6
            self.pkty[i * 2 + 1] = (self.X + self.Rm * math.cos(alfa), self.Y + self.Rm * math.sin(alfa))

def main():
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Rotating Star")
    stars = []


    clock = pygame.time.Clock()
    G1 = CStar(400, 300, 100, 50, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mousex, mousey = pygame.mouse.get_pos()
                    stars.append(CStar(mousex, mousey, 100, 50, 0))
                if pygame.mouse.get_pressed()[2] and stars:
                    mousex, mousey = pygame.mouse.get_pos()
                    closest_star = min(
                        stars, key=lambda star: math.sqrt((star.X - mousex) ** 2 + (star.Y - mousey) ** 2)
                    )

                    stars.remove(closest_star)

        screen.fill((0, 0, 0))
        for star in stars:

            star.Obrot()


            star.Rysuj(screen)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
