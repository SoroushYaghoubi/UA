from manim import *
import math
import numpy as np

class UA(MovingCameraScene):
    def draw_layer(self, center, R, iteration):
        stroke = 2 * (1 / iteration)

        r = R * math.sin(math.pi/3) / (1 + math.sin(math.pi/3))
        d = R - r
        angles = [math.pi/2, 7*math.pi/6, 11*math.pi/6]

        inner_circles = [
            Circle(radius=r, color=WHITE, stroke_width=stroke).move_to(center + d * np.array([math.cos(a), math.sin(a), 0]))
            for a in angles
        ]
        inner_circles[0].set_color(BLUE_C)

        font_size = R*7
        texts = [
            f"{3**iteration}k",
            f"{3**iteration}k + {1*3**(iteration-1)}",
            f"{3**iteration}k + {2*3**(iteration-1)}"
        ]

        labels = [
            Text(texts[i], font_size=font_size).move_to(inner_circles[i].get_center())
            for i in range(3)
        ]

        self.play(*[Write(label) for label in labels],
                  *[Create(c) for c in inner_circles])

        top_circle = inner_circles[0]
        center = top_circle.get_center()
        radius = top_circle.radius
        return center, radius, labels

    def construct(self):
        center = np.array([0, 0, 0])
        R = 4

        outer = Circle(radius=R, color=WHITE, stroke_width=1).move_to(center)
        self.play(Create(outer))

        v_p = 4
        for i in range(1, v_p):
            center, R, labels = self.draw_layer(center, R, i)
            self.wait(1)
            self.play(
                self.camera.frame.animate.move_to(center).set(height=R * 2),
                run_time=1.5
            )
            if i != v_p-1:
                self.play(*[FadeOut(label) for label in labels])