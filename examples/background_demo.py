from manim import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from graphics_helper import GraphicsHelper
import numpy as np

class BackgroundDemo(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # 1. SETUP: Title
        # ---------------------------------------------------------
        title = Text("BACKGROUND METHODS DEMO", font_size=60, weight=BOLD, color=WHITE)
        subtitle = Text("Testing Different Background Techniques", font_size=30, color=YELLOW_A)
        subtitle.next_to(title, DOWN)

        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ---------------------------------------------------------
        # 2. ABSTRACT BACKGROUND (Procedural)
        # ---------------------------------------------------------
        abstract_title = Text("1. Abstract Background", font_size=40, color=BLUE)
        self.play(Write(abstract_title), run_time=1)

        # Create abstract background
        abstract_bg = GraphicsHelper.create_abstract_background(depth=5)
        # Add rotation animation
        abstract_bg.add_updater(lambda m, dt: m.rotate(0.01 * dt))

        self.play(FadeIn(abstract_bg), run_time=2)

        # Add text over background
        text_over_bg = Text("Text over Abstract Background", font_size=36, color=WHITE)
        self.play(Write(text_over_bg), run_time=1)
        self.wait(3)

        self.play(FadeOut(abstract_bg), FadeOut(text_over_bg), FadeOut(abstract_title))

        # ---------------------------------------------------------
        # 3. SOLID COLOR BACKGROUND
        # ---------------------------------------------------------
        solid_title = Text("2. Solid Color Background", font_size=40, color=BLUE)
        self.play(Write(solid_title), run_time=1)

        # Create solid color background
        solid_bg = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=BLUE_E,
            fill_opacity=0.8,
            stroke_width=0
        )

        self.play(FadeIn(solid_bg), run_time=2)

        text_solid = Text("Text over Solid Background", font_size=36, color=WHITE)
        self.play(Write(text_solid), run_time=1)
        self.wait(2)

        self.play(FadeOut(solid_bg), FadeOut(text_solid), FadeOut(solid_title))

        # ---------------------------------------------------------
        # 4. GRADIENT BACKGROUND
        # ---------------------------------------------------------
        gradient_title = Text("3. Gradient Background", font_size=40, color=BLUE)
        self.play(Write(gradient_title), run_time=1)

        # Create gradient background using multiple rectangles
        gradient_bg = VGroup()
        colors = [BLUE_E, PURPLE_E, PINK, RED_E]
        for i, color in enumerate(colors):
            rect = Rectangle(
                width=config.frame_width,
                height=config.frame_height / len(colors),
                fill_color=color,
                fill_opacity=0.6,
                stroke_width=0
            )
            rect.shift(UP * (config.frame_height / len(colors) * (len(colors) - 1 - 2*i) / 2))
            gradient_bg.add(rect)

        self.play(FadeIn(gradient_bg), run_time=2)

        text_gradient = Text("Text over Gradient Background", font_size=36, color=WHITE)
        self.play(Write(text_gradient), run_time=1)
        self.wait(2)

        self.play(FadeOut(gradient_bg), FadeOut(text_gradient), FadeOut(gradient_title))

        # ---------------------------------------------------------
        # 5. ANIMATED PARTICLE BACKGROUND
        # ---------------------------------------------------------
        particle_title = Text("4. Animated Particle Background", font_size=40, color=BLUE)
        self.play(Write(particle_title), run_time=1)

        # Create particle background
        particles = VGroup()
        for _ in range(20):
            particle = Circle(
                radius=np.random.uniform(0.05, 0.15),
                fill_color=np.random.choice([WHITE, YELLOW, BLUE, TEAL]),
                fill_opacity=np.random.uniform(0.3, 0.7),
                stroke_width=0
            )
            particle.move_to([
                np.random.uniform(-config.frame_width/2, config.frame_width/2),
                np.random.uniform(-config.frame_height/2, config.frame_height/2),
                0
            ])
            particles.add(particle)

        # Add floating animation
        particles.add_updater(lambda m, dt: m.shift(UP * 0.01 * dt).rotate(0.005 * dt))

        self.play(FadeIn(particles), run_time=2)

        text_particles = Text("Text over Particle Background", font_size=36, color=WHITE)
        self.play(Write(text_particles), run_time=1)
        self.wait(3)

        self.play(FadeOut(particles), FadeOut(text_particles), FadeOut(particle_title))

        # ---------------------------------------------------------
        # 6. COMBINED BACKGROUND EFFECTS
        # ---------------------------------------------------------
        combined_title = Text("5. Combined Background Effects", font_size=40, color=BLUE)
        self.play(Write(combined_title), run_time=1)

        # Combine abstract + particles
        combined_bg = GraphicsHelper.create_abstract_background(depth=3)
        combined_bg.add_updater(lambda m, dt: m.rotate(0.005 * dt))

        # Add some glowing particles
        glow_particles = VGroup()
        for _ in range(10):
            particle = Circle(radius=0.1, fill_color=YELLOW, fill_opacity=0.8, stroke_width=0)
            glow = GraphicsHelper.create_glow(particle, color=YELLOW, opacity=0.5)
            group = VGroup(glow, particle)
            group.move_to([
                np.random.uniform(-4, 4),
                np.random.uniform(-2, 2),
                0
            ])
            glow_particles.add(group)

        glow_particles.add_updater(lambda m, dt: m.rotate(0.01 * dt))

        self.play(FadeIn(combined_bg), FadeIn(glow_particles), run_time=2)

        text_combined = Text("Text over Combined Background", font_size=36, color=WHITE)
        glow_text = GraphicsHelper.create_glow(text_combined, color=TEAL_C, opacity=0.6)
        text_group = VGroup(glow_text, text_combined)

        self.play(FadeIn(text_group), run_time=1)
        self.wait(3)

        self.play(FadeOut(combined_bg), FadeOut(glow_particles), FadeOut(text_group), FadeOut(combined_title))

        # ---------------------------------------------------------
        # 7. FINAL MESSAGE
        # ---------------------------------------------------------
        final_text = Text("Background Methods Demo Complete!", font_size=50, color=YELLOW, weight=BOLD)
        self.play(Write(final_text), run_time=2)
        self.play(Indicate(final_text), run_time=1)
        self.wait(2)
</xai:function_call