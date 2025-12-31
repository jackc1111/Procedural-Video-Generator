from manim import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from graphics_helper import GraphicsHelper
import numpy as np

class TextMethodsDemo(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # 1. SETUP: Title
        # ---------------------------------------------------------
        title = Text("TEXT METHODS DEMO", font_size=60, weight=BOLD, color=WHITE)
        subtitle = Text("Sequential Rendering of Text Operations", font_size=30, color=YELLOW_A)
        subtitle.next_to(title, DOWN)

        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ---------------------------------------------------------
        # 2. BASIC TEXT CREATION
        # ---------------------------------------------------------
        basic_title = Text("1. Basic Text Creation", font_size=40, color=BLUE)
        self.play(Write(basic_title), run_time=1)

        # Different text styles
        text1 = Text("Simple Text", font_size=36, color=WHITE)
        text2 = Text("Bold Text", font_size=36, weight=BOLD, color=RED)
        text3 = Text("Italic Text", font_size=36, slant=ITALIC, color=GREEN)
        text4 = Text("Colored Text", font_size=36, color=TEAL)

        texts = VGroup(text1, text2, text3, text4).arrange(DOWN, buff=0.5)
        texts.next_to(basic_title, DOWN, buff=1)

        self.play(LaggedStart(*[Write(t) for t in texts], lag_ratio=0.3), run_time=2)
        self.wait(2)
        self.play(FadeOut(basic_title), *[FadeOut(t) for t in texts])

        # ---------------------------------------------------------
        # 3. MATH FORMULAS
        # ---------------------------------------------------------
        math_title = Text("2. Mathematical Formulas", font_size=40, color=BLUE)
        self.play(Write(math_title), run_time=1)

        # LaTeX formulas
        formula1 = MathTex(r"E = mc^2", font_size=48, color=YELLOW)
        formula2 = MathTex(r"\int_0^\infty e^{-x^2} \, dx = \frac{\sqrt{\pi}}{2}", font_size=36, color=ORANGE)
        formula3 = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}", font_size=36, color=PURPLE)

        formulas = VGroup(formula1, formula2, formula3).arrange(DOWN, buff=0.8)
        formulas.next_to(math_title, DOWN, buff=1)

        self.play(LaggedStart(*[Write(f) for f in formulas], lag_ratio=0.5), run_time=3)
        self.wait(2)
        self.play(FadeOut(math_title), *[FadeOut(f) for f in formulas])

        # ---------------------------------------------------------
        # 4. TEXT ANIMATIONS
        # ---------------------------------------------------------
        anim_title = Text("3. Text Animations", font_size=40, color=BLUE)
        self.play(Write(anim_title), run_time=1)

        # Different animation types
        anim_text = Text("Animation Demo", font_size=48, color=WHITE)
        anim_text.move_to(ORIGIN)

        # Sequence of animations
        self.play(Write(anim_text), run_time=1)
        self.wait(0.5)
        self.play(anim_text.animate.scale(1.5).set_color(RED), run_time=1)
        self.wait(0.5)
        self.play(anim_text.animate.rotate(PI/4).set_color(BLUE), run_time=1)
        self.wait(0.5)
        self.play(anim_text.animate.move_to(UP*2).set_color(GREEN), run_time=1)
        self.wait(1)
        self.play(FadeOut(anim_text), FadeOut(anim_title))

        # ---------------------------------------------------------
        # 5. TEXT TRANSFORMATIONS
        # ---------------------------------------------------------
        trans_title = Text("4. Text Transformations", font_size=40, color=BLUE)
        self.play(Write(trans_title), run_time=1)

        text_a = Text("Hello", font_size=48, color=RED)
        text_b = Text("World", font_size=48, color=BLUE)
        text_c = Text("Universe", font_size=48, color=GREEN)

        # Transform sequence
        self.play(Write(text_a), run_time=1)
        self.wait(1)
        self.play(Transform(text_a, text_b), run_time=1)
        self.wait(1)
        self.play(Transform(text_a, text_c), run_time=1)
        self.wait(1)
        self.play(FadeOut(text_a), FadeOut(trans_title))

        # ---------------------------------------------------------
        # 6. GLOW EFFECTS (from GraphicsHelper)
        # ---------------------------------------------------------
        glow_title = Text("5. Glow Effects", font_size=40, color=BLUE)
        self.play(Write(glow_title), run_time=1)

        glow_text = Text("Glowing Text", font_size=48, color=WHITE)
        glow_effect = GraphicsHelper.create_glow(glow_text, color=TEAL_C, opacity=0.8)

        glow_group = VGroup(glow_effect, glow_text)
        self.play(FadeIn(glow_group), run_time=2)
        self.wait(2)

        # Animate glow
        self.play(glow_text.animate.set_color(YELLOW), run_time=1)
        self.wait(1)
        self.play(FadeOut(glow_group), FadeOut(glow_title))

        # ---------------------------------------------------------
        # 7. 3D TEXT
        # ---------------------------------------------------------
        d3_title = Text("6. 3D Text", font_size=40, color=BLUE)
        self.play(Write(d3_title), run_time=1)

        # Create 3D text using Text3D
        d3_text = Text("3D TEXT", font_size=48, color=WHITE)

        self.play(FadeIn(d3_text), run_time=2)
        self.wait(1)

        # Rotate in 3D
        self.play(Rotate(d3_text, angle=PI, axis=UP), run_time=2)
        self.wait(1)
        self.play(FadeOut(d3_text), FadeOut(d3_title))

        # ---------------------------------------------------------
        # 8. FINAL MESSAGE
        # ---------------------------------------------------------
        final_text = Text("Text Methods Demo Complete!", font_size=50, color=YELLOW, weight=BOLD)
        self.play(Write(final_text), run_time=2)
        self.play(Indicate(final_text), run_time=1)
