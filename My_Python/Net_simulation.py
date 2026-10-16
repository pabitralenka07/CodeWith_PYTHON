import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Net Simulation")

clock = pygame.time.Clock()

cols = 25
rows = 18
spacing = 30

points = []

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.original_x = x
        self.original_y = y

        self.vx = 0
        self.vy = 0

        self.pinned = False

    def update(self):
        if self.pinned:
            return


        dx = self.original_x - self.x
        dy = self.original_y - self.y

        self.vx += dx * 0.002
        self.vy += dy * 0.002


        self.vx *= 0.92
        self.vy *= 0.92

        self.x += self.vx
        self.y += self.vy


start_x = 25
start_y = 50

for row in range(rows):

    for col in range(cols):

        x = start_x + col * spacing
        y = start_y + row * spacing

        point = Point(x, y)

        # Pin top row
        if row == 0:
            point.pinned = True

        points.append(point)


def get_point(row, col):
    return points[row * cols + col]


def interact_with_mouse():

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:

        for point in points:

            dx = point.x - mouse_x
            dy = point.y - mouse_y

            distance = math.sqrt(dx * dx + dy * dy)

            if distance < 100:

                if distance == 0:
                    distance = 0.1

                force = (100 - distance) / 100

                point.vx += (dx / distance) * force * 8
                point.vy += (dy / distance) * force * 8


def apply_springs():

    spring_strength = 0.08

    for row in range(rows):

        for col in range(cols):

            point = get_point(row, col)

            if col < cols - 1:

                right = get_point(row, col + 1)

                dx = right.x - point.x
                dy = right.y - point.y

                distance = math.sqrt(dx * dx + dy * dy)

                if distance != 0:

                    difference = distance - spacing

                    force = difference * spring_strength

                    fx = (dx / distance) * force
                    fy = (dy / distance) * force

                    if not point.pinned:
                        point.vx += fx
                        point.vy += fy

                    if not right.pinned:
                        right.vx -= fx
                        right.vy -= fy

            if row < rows - 1:

                below = get_point(row + 1, col)

                dx = below.x - point.x
                dy = below.y - point.y

                distance = math.sqrt(dx * dx + dy * dy)

                if distance != 0:

                    difference = distance - spacing

                    force = difference * spring_strength

                    fx = (dx / distance) * force
                    fy = (dy / distance) * force

                    if not point.pinned:
                        point.vx += fx
                        point.vy += fy

                    if not below.pinned:
                        below.vx -= fx
                        below.vy -= fy


def draw_mesh():

    for row in range(rows):

        for col in range(cols):

            point = get_point(row, col)

            if col < cols - 1:

                right = get_point(row, col + 1)

                pygame.draw.line(
                    screen,
                    (100, 180, 190),
                    (int(point.x), int(point.y)),
                    (int(right.x), int(right.y)),
                    1
                )

            if row < rows - 1:

                below = get_point(row + 1, col)

                pygame.draw.line(
                    screen,
                    (100, 180, 190),
                    (int(point.x), int(point.y)),
                    (int(below.x), int(below.y)),
                    1
                )

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:

                for point in points:

                    point.x = point.original_x
                    point.y = point.original_y

                    point.vx = 0
                    point.vy = 0

    interact_with_mouse()

    apply_springs()

    for point in points:
        point.update()

    screen.fill((5, 8, 10))

    draw_mesh()

    pygame.display.flip()

    clock.tick(60)


pygame.quit()

