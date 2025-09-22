from manim import *

class UA(Scene):
    def construct(self):
        numbers = [Text(str(i)).scale(0.5) for i in range(0, 23)]
        numbers = self.categorizePAdically(numbers, init=True)
        numbers = self.categorizePAdically(numbers)
        self.categorizePAdically(numbers, reopen=False)

    def categorizePAdically(self, numbers, init=False, reopen=True, extend=13):
        ##### > all possible numbers
        dots = Text("...").scale(0.5)
        all_objs = numbers + [dots]
        group = VGroup(*all_objs).arrange(RIGHT, buff=0.3)

        if (init):
            self.play(Write(group))
            self.wait(0.5)

        ##### > separate residues and multiples of pk
        multiples = VGroup(*[numbers[i] for i in range(len(numbers)) if i % 3 == 0])
        residues = VGroup(*[numbers[i] for i in range(len(numbers)) if i % 3 != 0])
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
            multiples.animate.shift(UP*0.5).set_color(BLUE_C),
            residues.animate.shift(DOWN*0.5),
        )
        self.wait(2)


        ##### > categorize them into the deeper circle and the current one
        p0 = Circle(3.5, WHITE).set_fill(opacity=0)
        p1 = Circle(1.5, BLUE_C).set_fill(opacity=0)
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

        ##### > zoom in for the new pov
        self.play(
            p0.animate.scale(3).set_stroke(opacity=0.25),
            *[m.animate.move_to(3*R_residues*np.array([np.cos(a), np.sin(a), 0])).set_opacity(0.25) for m, a in zip(residues, angles_residues)],
            p1.animate.scale(2),
            *[m.animate.move_to(2*R_multiples*np.array([np.cos(a), np.sin(a), 0])) for m, a in zip(multiples, angles_multiples)],
        )
        self.wait(1)
        
        if reopen:
            self.play(FadeOut(p1))
            self.wait(1)

            numbers = multiples
            numbers.set_color(WHITE)
            pk = int(numbers[1].text) - int(numbers[0].text)
            base = int(numbers[-2].text)

            for i in range(1, extend):
                num = Text(str(i*pk + base)).scale(0.5)
                numbers.submobjects.insert(-1, num) ##### > here we are insering before last because the last one is Text("...")
                self.play(
                    Write(num),
                    numbers.animate.arrange(RIGHT, buff=0.3).move_to(ORIGIN),
                    run_time=0.3
                )

        self.wait(4)

        numbers.submobjects.pop()
        return numbers