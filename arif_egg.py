import os
import sys
import time
import random
import termios
import tty
import select

WIDTH = 35


def get_key():
    ready, _, _ = select.select([sys.stdin], [], [], 0)
    if ready:
        return sys.stdin.read(1)
    return ""


def play():
    score = 0
    life = 3
    runner = 1
    target = random.randint(10, WIDTH - 5)

    while life > 0:
        os.system("clear")

        print("=" * WIDTH)
        print("   🥚 ARIF SUMON'S EGG THERAPY")
        print("=" * WIDTH)
        print(f"🏆 Score: {score}    ❤️ Life: {life}")
        print()
        print(" " * runner + "🏃")
        print(" " * runner + "/|\\")
        print(" " * runner + "/ \\")
        print()
        print(" " * target + "😎")
        print()
        print("A = 🥚 THROW     Q = EXIT")

        key = get_key().lower()

        if key == "q":
            return False, score

        if key == "a":
            print("\n🥚💨💨💨")
            time.sleep(0.2)

            if abs(runner - target) <= 3:
                score += 10
                print("💥 HEAD HIT! +10")
            else:
                life -= 1
                print("❌ MISS! -1 LIFE")

            target = random.randint(10, WIDTH - 5)
            time.sleep(0.7)

        runner += 1

        if runner >= WIDTH - 3:
            runner = 1

        time.sleep(0.12)

    return True, score


old = termios.tcgetattr(sys.stdin)

try:
    tty.setcbreak(sys.stdin.fileno())

    while True:
        os.system("clear")

        print("=" * WIDTH)
        print("🥚 ARIF SUMON'S EGG THERAPY")
        print("=" * WIDTH)
        print()
        print("        🎮 START GAME")
        print()
        print("        🥚 Throw eggs")
        print("        🏆 Make high score")
        print("        ❤️ You have 3 lives")
        print()
        print("        Created by Arif Sumon")
        print()
        print("Press A to Start")
        print("Press Q to Quit")

        while True:
            key = get_key().lower()

            if key == "a":
                finished, score = play()
                break

            if key == "q":
                raise KeyboardInterrupt

            time.sleep(0.05)

        if not finished:
            break

        os.system("clear")

        print("=" * WIDTH)
        print("        💥 GAME OVER 💥")
        print("=" * WIDTH)
        print()
        print(f"🏆 Your Score: {score}")
        print()
        print("Press R to Restart")
        print("Press Q to Quit")

        while True:
            key = get_key().lower()

            if key == "r":
                break

            if key == "q":
                raise KeyboardInterrupt

            time.sleep(0.05)

finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old)

os.system("clear")
print("👋 Thanks for playing!")
print("🥚 ARIF SUMON'S EGG THERAPY")
