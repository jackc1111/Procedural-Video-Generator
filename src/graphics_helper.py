from manim import *
import numpy as np
import os

class GraphicsHelper:
    @staticmethod
    def create_lower_third(name: str, description: str, color=BLUE):
        """
        Creates a high-quality lower-third overlay.
        """
        text_name = Text(name, font_size=32, weight=BOLD)
        text_desc = Text(description, font_size=24, color=GRAY_A)
        
        group = VGroup(text_name, text_desc).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        
        background = RoundedRectangle(
            height=group.height + 0.5, 
            width=group.width + 1.0, 
            corner_radius=0.1,
            fill_opacity=0.8,
            fill_color=BLACK,
            stroke_width=2,
            stroke_color=color
        )
        
        lower_third = VGroup(background, group)
        group.move_to(background.get_center())
        
        return lower_third.to_corner(DL, buff=0.5)

    @staticmethod
    def create_progress_bar(width=10, height=0.2, color=BLUE_E):
        """
        Creates an animated progress bar.
        """
        bar_outline = Rectangle(width=width, height=height, stroke_color=WHITE)
        bar_fill = Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_width=0)
        bar_fill.align_to(bar_outline, LEFT)
        
        return VGroup(bar_outline, bar_fill)

    @staticmethod
    def create_glow(mobject, color=None, scale=None, opacity=0.3):
        """
        Creates a glowing halo effect around a mobject using Stroke Width.
        FIXED: Removed .scale() to prevent text character misalignment.
        """
        try:
            glow_color = color if color is not None else mobject.get_color()
            glow_group = VGroup()
            
            # 5 шарів сяйва
            for i in range(1, 6):
                layer = mobject.copy()
                
                # Важливо: прибираємо заливку, залишаємо тільки контур
                layer.set_fill(opacity=0)
                
                # Сяйво створюється товстим напівпрозорим контуром
                # width збільшується з кожним шаром, імітуючи розсіювання світла
                layer.set_stroke(glow_color, width=i * 5, opacity=opacity / i)
                
                glow_group.add(layer)
                
            return glow_group
        except Exception:
            return VGroup()

    @staticmethod
    def create_abstract_background(depth=3):
        """
        Creates a procedural-style abstract background with moving blobs.
        """
        blobs = VGroup()
        for _ in range(depth):
            blob = Circle(
                radius=np.random.uniform(1, 3),
                fill_opacity=0.1,
                fill_color=np.random.choice([BLUE, PURPLE, PINK, BLUE_B, ORANGE, TEAL, YELLOW]),
                stroke_width=0
            )
            blob.move_to([np.random.uniform(-5, 5), np.random.uniform(-3, 3), 0])
            blobs.add(blob)
        return blobs

    @staticmethod
    def load_image(filename: str, height=2):
        """
        Loads an image from the assets/images directory.
        """
        path = os.path.join("assets", "images", filename)
        if not os.path.exists(path):
            # Fallback for running from src or tests
            path = os.path.join("..", "assets", "images", filename)
        
        return ImageMobject(path).set_resampling_algorithm(RESAMPLING_ALGORITHMS["bicubic"]).set_height(height)

    @staticmethod
    def load_svg(filename: str, height=2):
        """
        Loads an SVG from the assets/images directory.
        """
        path = os.path.join("assets", "images", filename)
        if not os.path.exists(path):
            path = os.path.join("..", "assets", "images", filename)
            
        return SVGMobject(path).set_height(height)

    @staticmethod
    def create_masked_image(image_mobject, mask_shape):
        """
        Places an image inside a shape (clipping/masking).
        """
        image_mobject.move_to(mask_shape.get_center())
        frame = mask_shape.copy().set_fill(opacity=0).set_stroke(width=5, color=WHITE)
        return Group(image_mobject, frame)

    @staticmethod
    def create_3d_cube(side_length=2, fill_color=BLUE, fill_opacity=0.75):
        """
        Creates a 3D Cube with customized material.
        """
        cube = Cube(side_length=side_length, fill_color=fill_color, fill_opacity=fill_opacity)
        cube.set_stroke(color=WHITE, width=2)
        return cube

    @staticmethod
    def create_3d_sphere(radius=1, fill_color=PURPLE, fill_opacity=0.75):
        """
        Creates a 3D Sphere.
        """
        sphere = Sphere(radius=radius, fill_color=fill_color, fill_opacity=fill_opacity)
        return sphere
