from manim import *
from graphics_helper import GraphicsHelper
import random

class CryptoInsight(ThreeDScene): # ТЕПЕР ThreeDScene
    def construct(self):
        # 1. Налаштування камери для 3D простору
        # phi - кут нахилу, theta - кут повороту навколо осі Z
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # 2. Налаштування процедурного фону
        bg = GraphicsHelper.create_abstract_background(depth=6)
        # Фіксуємо фон, щоб він не обертався разом з камерою (якщо буде рух камери)
        self.add_fixed_in_frame_mobjects(bg)
        self.add(bg)

        # 3. Створення 3D-об'єктів (Куби та Сфери)
        crypto_objects = VGroup()
        for i in range(6):
            if i % 2 == 0:
                obj = GraphicsHelper.create_3d_cube(side_length=0.7, fill_color=BLUE_B)
            else:
                obj = GraphicsHelper.create_3d_sphere(radius=0.5, fill_color=BLUE_E)
            
            obj.move_to([random.uniform(-4, 4), random.uniform(-2, 2), random.uniform(-1, 1)])
            
            # Додаємо обертання
            obj.rot_speed = 0.6
            obj.add_updater(lambda m, dt: m.rotate(m.rot_speed * dt, axis=UP))
            crypto_objects.add(obj)
        
        self.add(crypto_objects)

        # 4. Головний заголовок з Glow
        main_title = Text("BITCOIN ANALYSIS", font_size=60, weight=BOLD)
        title_glow = GraphicsHelper.create_glow(main_title, color=ORANGE, scale=1.3, opacity=0.4)
        title_group = VGroup(main_title, title_glow)
        
        # Щоб 2D текст коректно відображався у 3D сцені, ми "фіксуємо" його відносно екрану
        self.add_fixed_in_frame_mobjects(title_group)

        # 5. Анімація появи
        self.play(
            Write(main_title),
            FadeIn(title_glow),
            run_time=2
        )
        self.wait(1)

        # 6. Підготовка та трансформація в Lower Third
        lower_third = GraphicsHelper.create_lower_third(
            "Bitcoin (BTC)", 
            "Price: $67,420.50 | Vol: 32.1B", 
            color=ORANGE
        )
        self.add_fixed_in_frame_mobjects(lower_third)

        # Прискорення об'єктів
        def speed_up_objects():
            for obj in crypto_objects:
                obj.rot_speed = 5.0

        self.play(
            ReplacementTransform(title_group, lower_third),
            UpdateFromFunc(crypto_objects, lambda m: speed_up_objects()),
            run_time=2
        )
        
        # Легкий нахил камери в кінці для динаміки
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(3)