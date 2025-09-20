from manim import *

class MyFirstScene(Scene):
    def construct(self):
        text = Text("WELCOME TO TROPICAL GAUSSIANS!")
        self.play(Write(text))
        self.wait(2)