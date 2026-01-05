from manim import *
import numpy as np

class BackgroundShowcase(Scene):
    def construct(self):
        # 1. ДИНАМІЧНИЙ ГРАДІЄНТ (Fluid Background)
        # Створюємо прямокутник на весь екран
        bg_gradient = Rectangle(
            width=config.frame_width, 
            height=config.frame_height,
            fill_opacity=1,
            stroke_width=0
        ).set_fill(color=[BLUE_E, PURPLE_E, DARK_BLUE])
        
        self.add(bg_gradient)
        
        # Анімація зміни кольорів градієнту (імітація "живого" фону)
        self.play(
            bg_gradient.animate.set_fill(color=[DARK_BLUE, BLACK, BLUE_E]),
            run_time=3,
            rate_func=linear
        )

        # 2. ПРОЦЕДУРНА СІТКА (Technical Grid)
        # Використовуємо NumberPlane, але стилізуємо його під фон
        grid = NumberPlane(
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.2
            }
        )
        self.play(Create(grid), run_time=2)

        # 3. ЕФЕКТ ЧАСТИНОК / НЕЙРОННОЇ МЕРЕЖІ (Procedural Nodes)
        # Створюємо точки, які рандомно рухаються
        dots = VGroup(*[
            Dot(point=[np.random.uniform(-7, 7), np.random.uniform(-4, 4), 0], 
                radius=0.04, color=WHITE, fill_opacity=0.3)
            for _ in range(50)
        ])
        
        def update_dots(mob, dt):
            for dot in mob:
                dot.shift(np.random.uniform(-0.1, 0.1) * UP + np.random.uniform(-0.1, 0.1) * RIGHT)
                # Утримання в межах екрану
                if abs(dot.get_x()) > 7: dot.set_x(-dot.get_x())
                if abs(dot.get_y()) > 4: dot.set_y(-dot.get_y())

        dots.add_updater(update_dots)
        self.add(dots)
        
        # 4. ЕФЕКТ СКЛА (Glassmorphism)
        # Створюємо матову панель поверх фону
        glass_panel = RoundedRectangle(
            corner_radius=0.3, width=6, height=4,
            fill_color=WHITE, fill_opacity=0.1,
            stroke_color=WHITE, stroke_width=2
        ).set_stroke(width=5, color=WHITE, opacity=0.2)
        
        # Додаємо розмиття (у Manim через затінення)
        label = Text("Procedural Video Gen", font_size=36).move_to(glass_panel.get_center())
        
        self.play(
            FadeIn(glass_panel, scale=0.9),
            Write(label),
            run_time=2
        )

        # 5. ФІНАЛЬНА ДИНАМІКА: Обертання всього фону
        self.play(
            Rotate(grid, angle=PI/24),
            bg_gradient.animate.set_fill(color=[PURPLE_E, DARK_GREY]),
            run_time=5,
            rate_func=smooth
        )
        
        self.wait(2)