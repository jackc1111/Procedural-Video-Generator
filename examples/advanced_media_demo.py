from manim import *
from graphics_helper import GraphicsHelper

class AdvancedMediaDemo(Scene):
    def construct(self):
        # Фон
        bg = GraphicsHelper.create_abstract_background(depth=3)
        self.add(bg)

        # 1. Вбудовування зображення
        # Припустимо, є зображення в assets/images/
        try:
            image = ImageMobject("assets/images/sample_image.png").scale(0.5).to_edge(LEFT)
            self.play(FadeIn(image), run_time=1)
        except:
            # Якщо зображення немає, створимо плейсхолдер
            placeholder = Rectangle(width=2, height=1.5, color=BLUE, fill_opacity=0.5).to_edge(LEFT)
            text = Text("Image Placeholder", font_size=24).move_to(placeholder.get_center())
            image_group = VGroup(placeholder, text)
            self.play(FadeIn(image_group), run_time=1)

        # 2. Вбудовування відео (використовуємо реальний файл)
        try:
            video = VideoMobject("output/videos/MyItChannelIntro.mp4").scale(0.3).to_edge(RIGHT)
            self.play(FadeIn(video), run_time=1)
            # Відтворити відео (якщо підтримується)
            self.wait(5)  # Час для відтворення вбудованого відео
        except Exception as e:
            print(f"Video embedding failed: {e}")
            video_placeholder = Rectangle(width=2, height=1.5, color=GREEN, fill_opacity=0.5).to_edge(RIGHT)
            video_text = Text("Video Failed", font_size=24).move_to(video_placeholder.get_center())
            video_group = VGroup(video_placeholder, video_text)
            self.play(FadeIn(video_group), run_time=1)

        # 3. 3D об'єкти
        # Створимо групу 3D об'єктів
        sphere = Sphere(radius=0.5, color=RED, fill_opacity=0.8).move_to(UP * 1.5)
        cube = Cube(side_length=1, fill_color=BLUE, fill_opacity=0.8).move_to(DOWN * 1.5)

        # Додамо обертання
        def rotate_sphere(sphere, dt):
            sphere.rotate(angle=dt * 2, axis=UP)

        def rotate_cube(cube, dt):
            cube.rotate(angle=dt * 1.5, axis=RIGHT)

        sphere.add_updater(rotate_sphere)
        cube.add_updater(rotate_cube)

        self.play(FadeIn(sphere), FadeIn(cube), run_time=1)
        self.wait(3)  # Дозволимо обертатися

        # 4. Комбінація з текстом
        title = Text("Advanced Media Demo", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title), run_time=2)

        # Фінальна анімація
        self.play(
            title.animate.scale(1.2).set_color(ORANGE),
            run_time=1
        )
        self.wait(1)