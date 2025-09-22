from manim import *

class SimpleMathTex(Scene):
    def construct(self):
        math = MathTex(r"E = mc^2")
        self.play(Write(math))
        self.wait(1)
