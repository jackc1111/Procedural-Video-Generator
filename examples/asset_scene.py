from manim import *
import sys
import os

# Ensure src is in path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from graphics_helper import GraphicsHelper

class AssetScene(Scene):
    def construct(self):
        # 1. Background
        self.add(GraphicsHelper.create_abstract_background(depth=3))

        # 2. Loading Image
        # Make sure assets/images/logo.png exists
        logo = GraphicsHelper.load_image("logo.png", height=3)
        logo_label = Text("External PNG Asset", font_size=36, color=WHITE).next_to(logo, DOWN)
        
        # 3. Add Glow to Image (Connecting features)
        glow = GraphicsHelper.create_glow(logo, color=BLUE_B, opacity=0.3)

        self.play(
            FadeIn(logo, shift=UP),
            FadeIn(glow),
            Write(logo_label)
        )
        self.wait(2)

        # 4. Connective Transition to Lower Third
        lt = GraphicsHelper.create_lower_third("Branding", "Using custom logos in your videos")
        
        self.play(
            logo.animate.scale(0.3).to_corner(UL),
            FadeOut(logo_label),
            FadeOut(glow),
            FadeIn(lt, shift=RIGHT)
        )
        self.wait(2)
