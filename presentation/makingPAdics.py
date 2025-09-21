from manim import *

class UA(Scene):
    def construct(self):
        numbers = [Text(str(i)).scale(0.5) for i in range(0, 23)]
        dots = Text("...").scale(0.5)
        all_objs = numbers + [dots]
        group = VGroup(*all_objs).arrange(RIGHT, buff=0.3)

        multiples = VGroup(*[numbers[i] for i in range(len(numbers)) if i % 3 == 0])
        residues = VGroup(*[numbers[i] for i in range(len(numbers)) if i % 3 != 0])

        self.play(Write(group))
        self.wait(0.5)
        self.play(multiples.animate.set_color(BLUE_C))
        self.wait(0.5)

        # create new dots and position them relative to groups
        dots_multiples = Text("...", color=BLUE_C).scale(0.5)
        dots_residues = Text("...").scale(0.5)

        dots_multiples.next_to(multiples, RIGHT, buff=0.9)
        dots_residues.next_to(residues, RIGHT, buff=0.3)

        multiples.add(dots_multiples)
        residues.add(dots_residues)

        self.play(
            FadeOut(dots),
            FadeIn(dots_multiples),
            FadeIn(dots_residues),
            multiples.animate.shift(UP*0.5),
            residues.animate.shift(DOWN*0.5),
        )
        self.wait(2)

        p0 = Circle(3.5, WHITE)
        p1 = Circle(1.5, BLUE_C)

        R_multiples = 1
        R_residues = 3
        angles_multiples = np.linspace(0, TAU, len(multiples), endpoint=False)
        angles_residues = np.linspace(0, TAU, len(residues), endpoint=False)
        self.play(
            *[m.animate.move_to(R_multiples*np.array([np.cos(a), np.sin(a), 0])) for m, a in zip(multiples, angles_multiples)],
            *[m.animate.move_to(R_residues*np.array([np.cos(a), np.sin(a), 0])) for m, a in zip(residues, angles_residues)],
            Create(p0),
            Create(p1),
        )
        self.wait(2)