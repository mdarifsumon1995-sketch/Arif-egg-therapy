from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.clock import Clock
from kivy.core.window import Window
from random import randint


class EggGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.score = 0
        self.lives = 3
        self.running = False

        with self.canvas:
            Color(0.08, 0.08, 0.12)
            self.bg = Rectangle(pos=(0, 0), size=Window.size)

        self.title = Label(
            text="🥚 ARIF SUMON'S EGG THERAPY",
            font_size="24sp",
            pos_hint={"center_x": 0.5, "top": 0.98},
        )
        self.add_widget(self.title)

        self.info = Label(
            text="Score: 0     Lives: ❤️❤️❤️",
            font_size="20sp",
            pos_hint={"center_x": 0.5, "top": 0.88},
        )
        self.add_widget(self.info)

        self.message = Label(
            text="Press START to play!",
            font_size="22sp",
            pos_hint={"center_x": 0.5, "center_y": 0.65},
        )
        self.add_widget(self.message)

        self.start_button = Button(
            text="START GAME",
            font_size="24sp",
            size_hint=(0.65, 0.15),
            pos_hint={"center_x": 0.5, "center_y": 0.35},
        )
        self.start_button.bind(on_press=self.start_game)
        self.add_widget(self.start_button)

        self.egg_button = Button(
            text="🥚 THROW EGG",
            font_size="22sp",
            size_hint=(0.75, 0.15),
            pos_hint={"center_x": 0.5, "y": 0.05},
        )
        self.egg_button.bind(on_press=self.throw_egg)
        self.add_widget(self.egg_button)

    def start_game(self, instance):
        self.score = 0
        self.lives = 3
        self.running = True

        self.start_button.text = "RESTART"
        self.message.text = "Hit the target! 🎯"
        self.update_info()

    def throw_egg(self, instance):
        if not self.running:
            self.message.text = "Press START GAME first!"
            return

        hit = randint(1, 2)

        if hit == 1:
            self.score += 10
            self.message.text = "💥 EGG HIT! +10"
        else:
            self.lives -= 1
            self.message.text = "🥚 MISS! Try again!"

            if self.lives <= 0:
                self.running = False
                self.message.text = (
                    f"GAME OVER!\nFinal Score: {self.score}"
                )

        self.update_info()

    def update_info(self):
        hearts = "❤️" * self.lives
        self.info.text = f"Score: {self.score}     Lives: {hearts}"


class EggTherapyApp(App):
    def build(self):
        Window.clearcolor = (0.08, 0.08, 0.12, 1)
        return EggGame()


if __name__ == "__main__":
    EggTherapyApp().run()
