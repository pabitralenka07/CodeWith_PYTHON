
import sys
import time

# ===== SETTINGS =====
typing_speed = 0.075
line_pause = 1.4
start_pause = 2

# Lyrics excerpt from your screenshot
lyrics = [
    "जादूगरनी हूँ, जादू करती हूँ",
    "हो, जादूगरनी हूँ, जादू करती हूँ",
    "किसी शहज़ादे पे मैं भी मरती हूँ",
    "मैंने उसको अपना माना",
    "पर ना जाने वो अनजाना",
    "आई परदेस से परियों की रानी",
    "छम-छमा-छम-छम",
    "छम-छमा-छम-छम, हाय",
    "आई परदेस से परियों की रानी",
    "आई परदेस से परियों की रानी",
    "खुशबू के संग चलूँ, बन के जुगनूँ मैं रात जलूँ",
    "कोई मुझे जाने नहीं, मैं हूँ बड़ी अनजानी",
    "छम-छमा-छम-छम ❤️"
]

# ===== COLORS =====
PINK = "\033[95m"
RESET = "\033[0m"

def type_line(line):
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(typing_speed)
    print()

def main():
    print(PINK + "🎧 Aayee Pardes Se ❤️" + RESET)
    print()

    time.sleep(start_pause)

    for line in lyrics:
        type_line(PINK + line + RESET)
        time.sleep(line_pause)

    print("\n✨ End of lyrics ✨")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⏹ Animation stopped.")
