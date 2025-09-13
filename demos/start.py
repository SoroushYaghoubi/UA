from manim import *

class MyFirstScene(Scene):
    def construct(self):
        text = Text("Hello Tropical Gaussians!")
        self.play(Write(text))
        self.wait(2)
