from manim import *
import numpy as np

config.background_color = "#1c1c1c"

class MinSurface3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-2, 2], y_range=[-2, 2], z_range=[-2, 2],
            axis_config={
                "include_tip": False,
                "stroke_color": GRAY_B,
                "stroke_width": 1.5,
                "stroke_opacity": 0.6,
            }
        )

        # Main min-surface
        surface = Surface(
            lambda u, v: axes.c2p(u, v, min(2*u+v, v+1, 5*v)),
            u_range=[-2, 2], v_range=[-2, 2], resolution=(30, 30)
        )
        surface.set_fill(opacity=0)
        surface.set_stroke(color=GRAY_A, width=0.6, opacity=1)

        # Tropical lines as semi-transparent planes
        x_plane = Surface(
            lambda u, v: axes.c2p(0.5, u, v),
            u_range=[-2, 2], v_range=[-2, 2], resolution=(2, 2)
        ).set_fill(opacity=0).set_stroke(color=RED, width=1)

        diag_plane = Surface(
            lambda u, v: axes.c2p(u, u/2, v),  # x=2y -> y=u/2
            u_range=[-2, 2], v_range=[-2, 2], resolution=(2, 2)
        ).set_fill(opacity=0).set_stroke(color=GREEN, width=1)

        y_plane = Surface(
            lambda u, v: axes.c2p(u, 0.25, v),
            u_range=[-2, 2], v_range=[-2, 2], resolution=(2, 2)
        ).set_fill(opacity=0).set_stroke(color=BLUE, width=1)

        self.add(axes, surface, x_plane, diag_plane, y_plane)
        self.set_camera_orientation(phi=65*DEGREES, theta=45*DEGREES, zoom=0.85)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(5)
