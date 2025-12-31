from manim import *
from graphics_helper import GraphicsHelper

class CleanTextCheck(ThreeDScene):
    def construct(self):
        # 1. Фон (без змін, працює добре)
        bg = GraphicsHelper.create_abstract_background(depth=5)
        self.add(bg)
        # Повільне обертання для динаміки
        bg.add_updater(lambda m, dt: m.rotate(0.05 * dt))

        # ---------------------------------------------------------
        # ВИПРАВЛЕННЯ ТЕКСТУ
        # ---------------------------------------------------------
        title = Text("SHARP QUALITY", font_size=70, weight=BOLD)
        
        # Створюємо сяйво
        # Зменшуємо opacity, щоб воно не "забивало" текст
        glow = GraphicsHelper.create_glow(title, color=BLUE, scale=1.1, opacity=0.3)
        
        # ! КРИТИЧНА ПРАВКА !
        # Явно задаємо порядок відображення: Текст завжди зверху (z_index=10)
        # Сяйво залишається позаду (z_index=0 за замовчуванням)
        title.set_z_index(10)
        
        # Групуємо так, щоб glow йшов першим (задній план), а title другим (передній)
        title_group = VGroup(glow, title)
        
        # Анімація
        # Використовуємо LaggedStart для більш "кінематографічного" ефекту
        self.play(
            LaggedStart(
                FadeIn(glow),
                Write(title),
                lag_ratio=0.2
            ),
            run_time=2
        )
        self.wait(1)

        # ---------------------------------------------------------
        # ТЕСТ 3D (Покращений перехід)
        # ---------------------------------------------------------
        # Замість простого куба використовуємо групу кубів для складності
        cube = GraphicsHelper.create_3d_cube(side_length=2.5, fill_color=BLUE_E, fill_opacity=0.8)
        
        # Підготовка камери
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, run_time=2)
        
        # Використовуємо FadeTransform замість ReplacementTransform
        # Це часто виглядає чистіше для переходу "Текст -> 3D об'єкт"
        self.play(ReplacementTransform(title_group, cube), run_time=1.5)
        
        self.play(Rotate(cube, angle=PI/2, axis=UP), run_time=2)
        
        self.wait(1)
        self.play(FadeOut(cube), FadeOut(bg))