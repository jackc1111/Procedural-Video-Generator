from manim import *
import sys
import os
import numpy as np

# Ensure src is in path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from graphics_helper import GraphicsHelper

class CollageScene(Scene):
    def construct(self):
        # 1. Procedural Background
        self.add(GraphicsHelper.create_abstract_background(depth=5))

        # 2. Main Title
        title = Text("FLOATING COLLAGE", font_size=48, weight=BOLD, color=WHITE).to_edge(UP)
        self.play(Write(title))

        # 3. Floating Assets
        # We will create groups and add updaters for floating motion
        
        def make_floating_obj(image_name, shape_type, pos, color):
            img = GraphicsHelper.load_image(image_name, height=2.5)
            if shape_type == "circle":
                shape = Circle(radius=1.3, color=color, stroke_width=6)
            else:
                shape = Square(side_length=2.6, color=color, stroke_width=6)
            
            obj = GraphicsHelper.create_masked_image(img, shape)
            obj.move_to(pos)
            
            # Add random float momentum
            obj.velocity = np.array([np.random.uniform(-0.2, 0.2), np.random.uniform(-0.2, 0.2), 0])
            
            def float_updater(mob, dt):
                mob.shift(mob.velocity * dt)
                # Bounce of edges (approximate)
                if abs(mob.get_x()) > 6: mob.velocity[0] *= -1
                if abs(mob.get_y()) > 3: mob.velocity[1] *= -1
                mob.rotate(0.1 * dt)
            
            obj.add_updater(float_updater)
            return obj

        floating_1 = make_floating_obj("tech.png", "circle", LEFT * 4 + DOWN * 1, BLUE_B)
        floating_2 = make_floating_obj("nature.png", "square", RIGHT * 4 + UP * 1, ORANGE)
        floating_3 = make_floating_obj("cube.png", "circle", ORIGIN + DOWN * 2, GOLD)

        self.play(
            FadeIn(floating_1, shift=UP),
            FadeIn(floating_2, shift=DOWN),
            FadeIn(floating_3, shift=RIGHT)
        )
        
        # 4. Info Overlay
        info = GraphicsHelper.create_lower_third("Dynamic Assets", "Real-time procedural motion with external PNGs")
        self.play(FadeIn(info, shift=UP))
        
        self.wait(5) # Let them float
        
        # 5. Outro
        self.play(
            FadeOut(floating_1),
            FadeOut(floating_2),
            FadeOut(floating_3),
            FadeOut(info),
            FadeOut(title)
        )
        self.wait(1)
