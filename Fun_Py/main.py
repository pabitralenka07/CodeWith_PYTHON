import pygame
import random
import math
import sys

# ==========================================
# SETTINGS
# ==========================================

WIDTH = 1080
HEIGHT = 1920
FPS = 30
TOTAL_SECONDS = 50
TOTAL_FRAMES = FPS * TOTAL_SECONDS

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flower Animation")

clock = pygame.time.Clock()

# ==========================================
# FONTS
# ==========================================

title_font = pygame.font.SysFont("Times New Roman", 42)
quote_font = pygame.font.SysFont("Arial", 21)

# ==========================================
# COLORS
# ==========================================

BLACK = (3, 3, 4)

STEM_COLORS = [
    (30, 100, 45),
    (35, 115, 50),
    (40, 130, 55)
]

FLOWER_COLORS = [
    (255, 110, 150),
    (255, 150, 185),
    (255, 210, 75),
    (255, 235, 130),
    (245, 240, 235)
]

# ==========================================
# FLOWER CLASS
# ==========================================

class Flower:

    def __init__(self, x, height, size, color, delay, grow_time, curve):

        self.x = x
        self.base_y = HEIGHT - 130
        self.height = height
        self.size = size
        self.color = color
        self.delay = delay
        self.grow_time = grow_time
        self.curve = curve

        self.stem_color = random.choice(STEM_COLORS)
        self.leaf_side = random.choice([-1, 1])

    def get_progress(self, frame):

        if frame < self.delay:
            return 0

        progress = (frame - self.delay) / self.grow_time

        return max(0, min(1, progress))

    def get_position(self, t, current_height):

        y = self.base_y - current_height * t

        x = (
            self.x
            + math.sin(t * math.pi)
            * self.curve
            * 40
        )

        return x, y

    def draw_leaf(self, x, y, direction, progress):

        length = 30 * progress

        pygame.draw.line(
            screen,
            (40, 120, 55),
            (int(x), int(y)),
            (
                int(x + direction * length),
                int(y - 12)
            ),
            3
        )

    def draw_flower(self, x, y, bloom):

        size = max(2, int(self.size * bloom))

        for i in range(6):

            angle = i * math.pi * 2 / 6
            distance = size * 0.65

            petal_x = x + math.cos(angle) * distance
            petal_y = y + math.sin(angle) * distance

            pygame.draw.circle(
                screen,
                self.color,
                (int(petal_x), int(petal_y)),
                max(2, size // 2)
            )

        pygame.draw.circle(
            screen,
            (255, 210, 80),
            (int(x), int(y)),
            max(2, size // 3)
        )

    def draw(self, frame):

        progress = self.get_progress(frame)

        if progress <= 0:
            return

        smooth = progress * progress * (3 - 2 * progress)

        current_height = self.height * smooth

        points = []

        for i in range(36):

            t = i / 35

            x, y = self.get_position(
                t,
                current_height
            )

            points.append((int(x), int(y)))

        pygame.draw.lines(
            screen,
            self.stem_color,
            False,
            points,
            3
        )

        if progress > 0.40:

            leaf_progress = min(
                1,
                (progress - 0.40) / 0.30
            )

            x1, y1 = self.get_position(
                0.45,
                current_height
            )

            self.draw_leaf(
                x1,
                y1,
                self.leaf_side,
                leaf_progress
            )

            x2, y2 = self.get_position(
                0.65,
                current_height
            )

            self.draw_leaf(
                x2,
                y2,
                -self.leaf_side,
                leaf_progress
            )

        if progress < 0.75:
            return

        bloom = min(
            1,
            (progress - 0.75) / 0.25
        )

        top_x, top_y = self.get_position(
            1,
            current_height
        )

        self.draw_flower(
            top_x,
            top_y,
            bloom
        )

# ==========================================
# CREATE FLOWERS
# ==========================================

random.seed(20)

flowers = []

# Tall flowers - middle tak / thoda upar

for i in range(55):

    flowers.append(
        Flower(
            random.randint(40, WIDTH - 40),
            random.randint(650, 950),
            random.randint(10, 18),
            random.choice(FLOWER_COLORS),
            random.randint(0, 500),
            random.randint(750, 1000),
            random.uniform(-1, 1)
        )
    )

# Medium flowers

for i in range(80):

    flowers.append(
        Flower(
            random.randint(30, WIDTH - 30),
            random.randint(350, 700),
            random.randint(10, 20),
            random.choice(FLOWER_COLORS),
            random.randint(100, 700),
            random.randint(700, 1000),
            random.uniform(-1.2, 1.2)
        )
    )

# Short flowers

for i in range(90):

    flowers.append(
        Flower(
            random.randint(20, WIDTH - 20),
            random.randint(150, 450),
            random.randint(10, 22),
            random.choice(FLOWER_COLORS),
            random.randint(250, 850),
            random.randint(600, 900),
            random.uniform(-1.5, 1.5)
        )
    )

# ==========================================
# VIGNETTE EFFECT
# ==========================================

def draw_vignette(fade):

    overlay = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )

    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    max_distance = math.sqrt(
        center_x ** 2 + center_y ** 2
    )

    step = 50

    for y in range(0, HEIGHT, step):

        for x in range(0, WIDTH, step):

            distance = math.sqrt(
                (x - center_x) ** 2
                + (y - center_y) ** 2
            )

            darkness = distance / max_distance

            alpha = int(
                darkness
                * darkness
                * 150
                * fade
            )

            pygame.draw.rect(
                overlay,
                (0, 0, 0, alpha),
                (x, y, step, step)
            )

    screen.blit(overlay, (0, 0))

# ==========================================
# FINAL TEXT
# ==========================================

def draw_final_text(frame):

    TEXT_START = FPS * 42

    if frame < TEXT_START:
        return

    elapsed = frame - TEXT_START

    vignette_fade = min(
        1,
        elapsed / 60
    )

    draw_vignette(vignette_fade)

    WHITE = (255, 255, 255)

    title = "My Love"

    quote_lines = [
        "Every flower blooms with",
        "a little piece of my heart",
        "and all of them lead to you."
    ]

    title_y = 700

    # MY LOVE PEHLE

    title_fade = min(
        1,
        elapsed / 30
    )

    title_surface = title_font.render(
        title,
        True,
        WHITE
    )

    title_surface.set_alpha(
        int(255 * title_fade)
    )

    title_x = (
        WIDTH // 2
        - title_surface.get_width() // 2
    )

    screen.blit(
        title_surface,
        (title_x, title_y)
    )

    # QUOTE LINES ONE BY ONE

    quote_start_y = (
        title_y
        + title_font.get_height()
        + 3
    )

    line_delay = 45

    for i, line in enumerate(quote_lines):

        start_frame = 60 + (i * line_delay)

        if elapsed >= start_frame:

            line_fade = min(
                1,
                (elapsed - start_frame) / 25
            )

            quote_surface = quote_font.render(
                line,
                True,
                WHITE
            )

            quote_surface.set_alpha(
                int(255 * line_fade)
            )

            quote_x = (
                WIDTH // 2
                - quote_surface.get_width() // 2
            )

            quote_y = (
                quote_start_y
                + i * 28
            )

            screen.blit(
                quote_surface,
                (quote_x, quote_y)
            )

# ==========================================
# MAIN LOOP
# ==========================================

frame = 0
running = True

while running:

    clock.tick(FPS)

    if frame < TOTAL_FRAMES:
        frame += 1

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    for flower in flowers:
        flower.draw(frame)

    draw_final_text(frame)

    pygame.display.flip()

pygame.quit()
sys.exit()