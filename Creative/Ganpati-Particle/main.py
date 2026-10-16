import numpy as np
from PIL import Image, ImageFilter
import imageio.v2 as imageio
import random
import math
import os

# ============================================================
# GANPATI — CINEMATIC 20,000 PARTICLE REVEAL
# ============================================================

WIDTH = 720
HEIGHT = 1280
FPS = 30

FORMATION_SECONDS = 60
FINAL_HOLD_SECONDS = 10
TOTAL_SECONDS = 70

PARTICLES = 20000

IMAGE_FILE = "ganpati.png"
OUTPUT_FILE = "ganpati_particle_reel.mp4"

random.seed(42)
np.random.seed(42)


# ============================================================
# LOAD IMAGE
# ============================================================

print("Loading Ganpati image...")

if not os.path.exists(IMAGE_FILE):
    raise FileNotFoundError(
        "ganpati.png not found. Keep it in the same folder as main.py"
    )

img = Image.open(IMAGE_FILE).convert("RGB")

target_ratio = WIDTH / HEIGHT
image_ratio = img.width / img.height

if image_ratio > target_ratio:
    new_height = HEIGHT
    new_width = int(img.width * HEIGHT / img.height)
else:
    new_width = WIDTH
    new_height = int(img.height * WIDTH / img.width)

img = img.resize(
    (new_width, new_height),
    Image.Resampling.LANCZOS
)

canvas = Image.new(
    "RGB",
    (WIDTH, HEIGHT),
    (0, 0, 0)
)

x = (WIDTH - new_width) // 2
y = (HEIGHT - new_height) // 2

canvas.paste(img, (x, y))

gray = np.array(
    canvas.convert("L"),
    dtype=np.float32
)


# ============================================================
# CREATE PARTICLE MASK
# ============================================================

mask = Image.fromarray(
    gray.astype(np.uint8)
)

mask = mask.filter(
    ImageFilter.GaussianBlur(1.4)
)

brightness = np.array(
    mask,
    dtype=np.float32
)

# Stronger particle visibility
brightness = np.maximum(
    brightness - 10,
    0
)

brightness = np.power(
    brightness / 255.0,
    0.62
) * 255

# Remove black background
brightness[gray < 22] = 0


# ============================================================
# CREATE 20,000 TARGET PARTICLES
# ============================================================

print("Creating 20,000 particles...")

flat = brightness.flatten()

total_weight = flat.sum()

if total_weight <= 0:
    raise ValueError(
        "Could not create particle mask from ganpati.png"
    )

probabilities = flat / total_weight

indices = np.random.choice(
    len(flat),
    size=PARTICLES,
    replace=True,
    p=probabilities
)

target_y = (
    indices // WIDTH
).astype(np.float32)

target_x = (
    indices % WIDTH
).astype(np.float32)


# ============================================================
# PARTICLE DEPTH
# ============================================================

depth = np.random.uniform(
    0.2,
    1.0,
    PARTICLES
).astype(np.float32)

# Some particles are closer to camera
depth += np.random.uniform(
    0,
    0.45,
    PARTICLES
).astype(np.float32)

depth = np.clip(
    depth,
    0.15,
    1.45
)


# ============================================================
# START POSITIONS — ALL 4 SIDES
# ============================================================

print("Creating cinematic particle trajectories...")

start_x = np.zeros(
    PARTICLES,
    dtype=np.float32
)

start_y = np.zeros(
    PARTICLES,
    dtype=np.float32
)

sides = np.random.randint(
    0,
    4,
    PARTICLES
)

# LEFT
mask_left = sides == 0

start_x[mask_left] = np.random.uniform(
    -650,
    -30,
    mask_left.sum()
)

start_y[mask_left] = np.random.uniform(
    -250,
    HEIGHT + 250,
    mask_left.sum()
)


# RIGHT
mask_right = sides == 1

start_x[mask_right] = np.random.uniform(
    WIDTH + 30,
    WIDTH + 650,
    mask_right.sum()
)

start_y[mask_right] = np.random.uniform(
    -250,
    HEIGHT + 250,
    mask_right.sum()
)


# TOP
mask_top = sides == 2

start_x[mask_top] = np.random.uniform(
    -250,
    WIDTH + 250,
    mask_top.sum()
)

start_y[mask_top] = np.random.uniform(
    -650,
    -30,
    mask_top.sum()
)


# BOTTOM
mask_bottom = sides == 3

start_x[mask_bottom] = np.random.uniform(
    -250,
    WIDTH + 250,
    mask_bottom.sum()
)

start_y[mask_bottom] = np.random.uniform(
    HEIGHT + 30,
    HEIGHT + 650,
    mask_bottom.sum()
)


# ============================================================
# CURVED TRAJECTORIES
# ============================================================

curve_x = np.random.uniform(
    -150,
    150,
    PARTICLES
).astype(np.float32)

curve_y = np.random.uniform(
    -150,
    150,
    PARTICLES
).astype(np.float32)

speed = np.random.uniform(
    0.68,
    1.22,
    PARTICLES
).astype(np.float32)

delay = np.random.uniform(
    0,
    0.22,
    PARTICLES
).astype(np.float32)


# ============================================================
# PARTICLE SIZE
# ============================================================

particle_size = np.random.choice(
    [1, 1, 1, 1, 2, 2, 2, 3],
    size=PARTICLES,
    p=[
        0.13,
        0.15,
        0.15,
        0.12,
        0.16,
        0.12,
        0.12,
        0.05
    ]
)


# ============================================================
# BACKGROUND PARTICLES
# ============================================================

BG_PARTICLES = 900

bg_x = np.random.uniform(
    0,
    WIDTH,
    BG_PARTICLES
)

bg_y = np.random.uniform(
    0,
    HEIGHT,
    BG_PARTICLES
)

bg_speed = np.random.uniform(
    0.15,
    0.7,
    BG_PARTICLES
)


# ============================================================
# EASING
# ============================================================

def cinematic_ease(t):

    t = np.clip(
        t,
        0,
        1
    )

    # Fast beginning → smooth landing
    return 1 - (1 - t) ** 3


# ============================================================
# DRAW PARTICLE
# ============================================================

def draw_particle(
    frame,
    px,
    py,
    size,
    brightness_value
):

    x = int(px)
    y = int(py)

    if (
        x < 0
        or x >= WIDTH
        or y < 0
        or y >= HEIGHT
    ):
        return

    # ========================================================
    # STRONG GOLDEN / ORANGE LOOK
    # ========================================================

    value = int(
        np.clip(
            brightness_value,
            70,
            255
        )
    )

    r = value

    g = int(
        value * 0.76
    )

    b = int(
        value * 0.32
    )

    if size == 1:

        frame[y, x, 0] = max(
            frame[y, x, 0],
            r
        )

        frame[y, x, 1] = max(
            frame[y, x, 1],
            g
        )

        frame[y, x, 2] = max(
            frame[y, x, 2],
            b
        )

    else:

        radius = max(
            1,
            size // 2
        )

        y1 = max(
            0,
            y - radius
        )

        y2 = min(
            HEIGHT,
            y + radius + 1
        )

        x1 = max(
            0,
            x - radius
        )

        x2 = min(
            WIDTH,
            x + radius + 1
        )

        frame[
            y1:y2,
            x1:x2,
            0
        ] = np.maximum(
            frame[
                y1:y2,
                x1:x2,
                0
            ],
            r
        )

        frame[
            y1:y2,
            x1:x2,
            1
        ] = np.maximum(
            frame[
                y1:y2,
                x1:x2,
                1
            ],
            g
        )

        frame[
            y1:y2,
            x1:x2,
            2
        ] = np.maximum(
            frame[
                y1:y2,
                x1:x2,
                2
            ],
            b
        )


# ============================================================
# VIDEO
# ============================================================

print()
print("Starting cinematic particle animation...")
print()
print("20,000 particles")
print("4-direction particle emission")
print("60 seconds formation")
print("10 seconds final hold")
print()

# writer = imageio.get_writer(
#     OUTPUT_FILE,
#     fps=FPS,
#     codec="libx264",
#     quality=8,
#     pixelformat="yuv420p"
# )
writer = imageio.get_writer(
    OUTPUT_FILE,
    format="FFMPEG",
    fps=FPS,
    codec="libx264",
    quality=8,
    pixelformat="yuv420p"
)

total_frames = (
    TOTAL_SECONDS * FPS
)


# ============================================================
# ANIMATION LOOP
# ============================================================

for frame_number in range(
    total_frames
):

    time_sec = (
        frame_number / FPS
    )

    frame = np.zeros(
        (HEIGHT, WIDTH, 3),
        dtype=np.uint8
    )


    # ========================================================
    # BACKGROUND FLOATING PARTICLES
    # ========================================================

    bg_current_x = (
        bg_x
        + np.sin(
            time_sec * 0.5
            + bg_y * 0.01
        ) * 7
    )

    bg_current_y = (
        bg_y
        - bg_speed * time_sec * 8
    )

    bg_current_y %= HEIGHT
    bg_current_x %= WIDTH

    for i in range(
        BG_PARTICLES
    ):

        bx = int(
            bg_current_x[i]
        )

        by = int(
            bg_current_y[i]
        )

        value = random.randint(
            30,
            85
        )

        frame[
            by,
            bx
        ] = (
            value,
            int(value * 0.72),
            int(value * 0.30)
        )


    # ========================================================
    # FORMATION
    # ========================================================

    progress = (
        time_sec
        / FORMATION_SECONDS
    )


    if progress < 1:

        local_t = (
            progress
            - delay
        )

        local_t = np.clip(
            local_t,
            0,
            1
        )

        local_t *= speed

        local_t = np.clip(
            local_t,
            0,
            1
        )

        eased = cinematic_ease(
            local_t
        )


        # ====================================================
        # MOVE FROM OUTSIDE → GANPATI
        # ====================================================

        px = (
            start_x
            + (
                target_x
                - start_x
            ) * eased
        )

        py = (
            start_y
            + (
                target_y
                - start_y
            ) * eased
        )


        # ====================================================
        # NATURAL CURVE
        # ====================================================

        curve = np.sin(
            local_t * math.pi
        )

        px += (
            curve_x
            * curve
            * (1 - eased)
        )

        py += (
            curve_y
            * curve
            * (1 - eased)
        )


        # ====================================================
        # 3D CAMERA THROW
        # ====================================================

        center_x = WIDTH / 2
        center_y = HEIGHT / 2

        perspective = (
            1
            + (
                1 - eased
            )
            * (
                depth - 0.5
            )
            * 1.35
        )

        px = (
            center_x
            + (
                px
                - center_x
            )
            * perspective
        )

        py = (
            center_y
            + (
                py
                - center_y
            )
            * perspective
        )


        # ====================================================
        # PARTICLE BRIGHTNESS
        # ====================================================

        sample_x = np.clip(
            target_x.astype(int),
            0,
            WIDTH - 1
        )

        sample_y = np.clip(
            target_y.astype(int),
            0,
            HEIGHT - 1
        )

        particle_brightness = (
            brightness[
                sample_y,
                sample_x
            ]
        )


        # KEEP PARTICLES STRONG
        particle_brightness *= (
            0.82
            + 0.35 * eased
        )

        particle_brightness *= (
            0.82
            + 0.28 * depth
        )


        # ====================================================
        # DRAW
        # ====================================================

        for i in range(
            PARTICLES
        ):

            # Don't remove too many particles
            if random.random() > 0.96:
                continue

            x_pos = px[i]
            y_pos = py[i]

            if (
                x_pos < -20
                or x_pos > WIDTH + 20
                or y_pos < -20
                or y_pos > HEIGHT + 20
            ):
                continue

            value = (
                particle_brightness[i]
            )

            # Bright particles
            if depth[i] > 1.0:
                value *= 1.25

            draw_particle(
                frame,
                x_pos,
                y_pos,
                int(
                    particle_size[i]
                ),
                value
            )


    # ========================================================
    # FINAL GANPATI
    # ========================================================

    else:

        # Very subtle breathing effect
        breathing = np.sin(
            time_sec * 1.7
            + target_x * 0.012
            + target_y * 0.009
        )

        final_x = (
            target_x
            + breathing * 0.35
        )

        final_y = (
            target_y
            + breathing * 0.35
        )


        sample_x = np.clip(
            target_x.astype(int),
            0,
            WIDTH - 1
        )

        sample_y = np.clip(
            target_y.astype(int),
            0,
            HEIGHT - 1
        )

        particle_brightness = (
            brightness[
                sample_y,
                sample_x
            ]
        )


        for i in range(
            PARTICLES
        ):

            if random.random() > 0.95:
                continue

            value = (
                particle_brightness[i]
                * 1.15
            )

            pulse = (
                0.92
                + 0.10
                * math.sin(
                    time_sec * 2
                    + i * 0.002
                )
            )

            value *= pulse

            draw_particle(
                frame,
                final_x[i],
                final_y[i],
                int(
                    particle_size[i]
                ),
                value
            )


    # ========================================================
    # STRONG GLOW
    # ========================================================

    pil_frame = Image.fromarray(
        frame
    )

    glow1 = pil_frame.filter(
        ImageFilter.GaussianBlur(
            2.0
        )
    )

    glow2 = pil_frame.filter(
        ImageFilter.GaussianBlur(
            6.0
        )
    )

    glow1_array = np.array(
        glow1,
        dtype=np.uint16
    )

    glow2_array = np.array(
        glow2,
        dtype=np.uint16
    )

    frame16 = frame.astype(
        np.uint16
    )

    # Strong close glow
    frame16 += (
        glow1_array * 0.24
    ).astype(np.uint16)

    # Soft cinematic glow
    frame16 += (
        glow2_array * 0.08
    ).astype(np.uint16)

    frame = np.clip(
        frame16,
        0,
        255
    ).astype(
        np.uint8
    )


    # ========================================================
    # WRITE
    # ========================================================

    writer.append_data(
        frame
    )


    # ========================================================
    # PROGRESS
    # ========================================================

    if frame_number % FPS == 0:

        percent = (
            frame_number
            / total_frames
            * 100
        )

        print(
            f"Rendering: "
            f"{percent:5.1f}% | "
            f"{time_sec:5.1f}s / "
            f"{TOTAL_SECONDS}s"
        )


# ============================================================
# FINISH
# ============================================================

writer.close()

print()
print("==========================================")
print("GANPATI PARTICLE VIDEO CREATED!")
print("==========================================")
print()
print(f"Output: {OUTPUT_FILE}")
print("Particles: 20,000")
print("Duration: 70 seconds")
print("Resolution: 720 x 1280")
print("Particle entry: 4 directions")
print("Glow: Strong golden/orange")
print() 