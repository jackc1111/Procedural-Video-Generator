from manim import *

class SampleScene(Scene):
    def construct(self):
        # 1. Title Screen
        title = Text("Procedural Video Generator", font_size=72)
        subtitle = Text("Powered by Manim & Python", font_size=36, color=BLUE)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        # 2. Informative Graphic (Connective)
        circle = Circle(radius=2, color=ORANGE)
        square = Square(side_length=3, color=GREEN)
        
        label_circle = Text("Start", font_size=24).next_to(circle, UP)
        label_square = Text("Transform", font_size=24).next_to(square, UP)

        self.play(Create(circle), Write(label_circle))
        self.wait(0.5)
        
        # Connective transition
        self.play(
            ReplacementTransform(circle, square),
            ReplacementTransform(label_circle, label_square)
        )
        self.wait(1)
        
        # 3. Final message
        final_text = Text("Ready for Production", color=YELLOW)
        self.play(ReplacementTransform(square, final_text), FadeOut(label_square))
        self.play(Indicate(final_text))
        self.wait(2)
