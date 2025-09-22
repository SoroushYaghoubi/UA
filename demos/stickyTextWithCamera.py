from manim import *

class StickyTextExample(MovingCameraScene):
    def construct(self):
        text = Text("I'm fixed to the screen")
        text.add_updater(lambda m: m.move_to(self.camera.frame.get_center() + UP*3))
        self.add(text)

        square = Square().shift(LEFT)
        self.add(square)
        self.play(self.camera.frame.animate.scale(0.5).move_to(square))
        self.wait()
