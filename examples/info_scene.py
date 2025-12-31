from manim import *
import sys
import os

# Ensure src is in path if running directly
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from graphics_helper import GraphicsHelper

class InfoScene(Scene):
    def construct(self):
        # 1. Background (Procedural feel)
        grid = NumberPlane(background_line_style={"stroke_opacity": 0.2})
        self.add(grid)

        # 2. Lower Third
        lt = GraphicsHelper.create_lower_third("Antigravity PVG", "Procedural Video Generation System")
        self.play(FadeIn(lt, shift=UP))
        self.wait(1)

        # 3. Informative Graphics (Data Viz)
        chart = BarChart(
            values=[10, 30, 55, 20, 40],
            bar_names=["Q1", "Q2", "Q3", "Q4", "Total"],
            y_range=[0, 60, 10],
            y_length=5,
            x_length=8,
            axis_config={"font_size": 24},
        )
        chart_title = Text("Performance Statistics", font_size=36).next_to(chart, UP)

        self.play(Create(chart), Write(chart_title))
        self.wait(2)

        # 4. Connective Transition (Zoom in on a detail)
        self.play(
            FadeOut(chart), 
            FadeOut(chart_title),
            lt.animate.scale(0.5).to_corner(UR)
        )
        
        # 5. Connective element: Animated connection
        dot_a = Dot(LEFT*3)
        dot_b = Dot(RIGHT*3)
        line = Line(dot_a.get_center(), dot_b.get_center(), stroke_width=2)
        
        label_a = Text("Step A", font_size=20).next_to(dot_a, DOWN)
        label_b = Text("Step B", font_size=20).next_to(dot_b, DOWN)

        self.play(Create(dot_a), Write(label_a))
        self.play(Create(line))
        self.play(Create(dot_b), Write(label_b))
        
        # Connective flow
        moving_dot = Dot(color=YELLOW).move_to(dot_a)
        self.play(moving_dot.animate.move_to(dot_b), run_time=2, rate_func=slow_into)
        
        self.wait(2)
