from manim import *

class MyItChannelIntro(Scene):
    def construct(self):
        # Кольорова палітра
        ACCENT_COLOR = "#00FFCC" # Неоновий бірюзовий (дуже IT)
        BG_COLOR = "#0F0F0F"     # Глибокий темно-сірий
        self.camera.background_color = BG_COLOR

        # 1. ТЕКСТ ТА ЕЛЕМЕНТИ
        # Назва каналу
        channel_name = Text(
            "MyItChannel",
            font="Orbitron", # Якщо немає Orbitron, Manim використає стандартний Sans
            font_size=72,
            weight=BOLD
        )
        channel_name.set_color_by_gradient(WHITE, ACCENT_COLOR)

        # 2. АНІМАЦІЯ

        # Крок 1: Ефект друку тексту
        self.play(
            AddTextLetterByLetter(channel_name),
            run_time=1.5,
            rate_func=linear
        )
        self.wait(0.2)

        # Крок 2: "Пульсація" тексту
        self.play(
            channel_name.animate.scale(1.1),
            run_time=0.3
        )
        self.play(
            channel_name.animate.scale(1.0),
            run_time=0.3
        )

        # Крок 2.5: Додавання 3D сфери зверху над назвою
        sphere = Sphere(radius=0.3, color=ACCENT_COLOR, fill_opacity=0.7).move_to(channel_name.get_top() + UP * 1.5)

        def rotate_sphere(sphere, dt):
            sphere.rotate(angle=dt * 2, axis=UP)  # Повільне обертання

        sphere.add_updater(rotate_sphere)
        self.add(sphere)

        # Крок 3: Створення рамки для коду
        code_frame = RoundedRectangle(
            width=6, height=2,
            corner_radius=0.2,
            fill_color=BG_COLOR,
            fill_opacity=0.8,
            stroke_color=ACCENT_COLOR,
            stroke_width=3
        ).to_edge(DOWN)

        self.play(FadeIn(code_frame), run_time=0.5)

        # Набір коду Python всередині рамки
        code_text = Text(
            """print("Hello, AI!")
def neural_net():
    return "Learning\"""",
            font="Monospace",
            font_size=24,
            color=ACCENT_COLOR
        ).move_to(code_frame.get_center())

        self.play(
            AddTextLetterByLetter(code_text),
            run_time=3,
            rate_func=linear
        )
        self.wait(0.5)

        # Крок 3.5: Створення рамки справа для генерації зображення
        image_frame = RoundedRectangle(
            width=4, height=3,
            corner_radius=0.2,
            fill_color=BG_COLOR,
            fill_opacity=0.8,
            stroke_color=ACCENT_COLOR,
            stroke_width=3
        ).to_edge(RIGHT)

        self.play(FadeIn(image_frame), run_time=0.5)

        # Набір тексту "prompt: generate image" всередині рамки
        prompt_text = Text(
            "prompt: generate image",
            font="Monospace",
            font_size=20,
            color=ACCENT_COLOR
        ).move_to(image_frame.get_center() + UP * 0.5)

        self.play(
            AddTextLetterByLetter(prompt_text),
            run_time=2,
            rate_func=linear
        )
        self.wait(0.5)

        # Імітація дифузії зображення (поки що плейсхолдер)
        # Коли зображення буде додано в assets, замінити на:
        # image = ImageMobject("assets/images/generated_image.png").scale_to_fit_width(3).move_to(image_frame.get_center() + DOWN * 0.5)
        # self.play(FadeIn(image), run_time=2)

        # Тимчасовий плейсхолдер: прямокутник, що "генерується"
        generated_placeholder = Rectangle(
            width=2.5, height=1.5,
            fill_color=ACCENT_COLOR,
            fill_opacity=0.5,
            stroke_color=WHITE,
            stroke_width=2
        ).move_to(image_frame.get_center() + DOWN * 0.5)

        self.play(FadeIn(generated_placeholder), run_time=1.5)
        self.wait(0.5)

        # 4. ДЕКОРАТИВНІ ЕЛЕМЕНТИ (Цифровий дощ/Частинки)
        particles = VGroup(*[
            Dot(radius=0.02, color=ACCENT_COLOR, fill_opacity=0.5)
            for _ in range(20)
        ])
        for p in particles:
            p.move_to([np.random.uniform(-4, 4), np.random.uniform(-2, 2), 0])

        self.play(
            LaggedStart(*[
                p.animate.shift(UP * 0.5).set_opacity(0) 
                for p in particles
            ], lag_ratio=0.1),
            run_time=2
        )

        # Фінальний вихід (опціонально для переходу в контент)
        self.play(
            channel_name.animate.scale(2).set_opacity(0),
            sphere.animate.set_opacity(0),
            code_frame.animate.set_opacity(0),
            code_text.animate.set_opacity(0),
            image_frame.animate.set_opacity(0),
            prompt_text.animate.set_opacity(0),
            generated_placeholder.animate.set_opacity(0),
            run_time=1
        )