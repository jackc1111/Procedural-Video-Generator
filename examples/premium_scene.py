from manim import *
import sys
import os
import numpy as np

# Ensure src is in path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from graphics_helper import GraphicsHelper

class PremiumScene(Scene):
    def construct(self):
        # 1. Procedural Background
        bg_blobs = GraphicsHelper.create_abstract_background(depth=5)
        self.add(bg_blobs)
        
        # Animate background blobs slowly
        for blob in bg_blobs:
            blob.generate_target()
            blob.target.move_to([
                np.random.uniform(-7, 7),
                np.random.uniform(-4, 4),
                0
            ])
            self.play(MoveToTarget(blob), run_time=10, rate_func=linear, remover=False),
            # Note: In a real scene we would use self.add_updater for constant motion
        
        self.remove(*self.mobjects) # Clear for main intro
        self.add(bg_blobs)

        # 2. Premium Title with Glow
        title_text = Text("PREMIUM VISUALS", font_size=72, weight=BOLD, color=WHITE)
        glow = GraphicsHelper.create_glow(title_text, color=BLUE_B, opacity=0.4)
        
        self.play(
            Write(title_text),
            FadeIn(glow, scale=1.1)
        )
        self.play(Indicate(title_text, color=BLUE_B))
        self.wait(1)
        
        # 3. Dynamic Connective Overlay
        lt = GraphicsHelper.create_lower_third("UPCOMING SCENE", "In-depth Technical Analysis", color=PURPLE)
        self.play(FadeIn(lt, shift=RIGHT))
        self.wait(2)
        
        # 4. Final Transition
        final_circle = Circle(radius=1.5, color=GOLD_A).set_fill(GOLD_E, opacity=0.5)
        self.play(
            ReplacementTransform(title_text, final_circle),
            FadeOut(glow),
            FadeOut(lt)
        )
        self.play(final_circle.animate.scale(10), FadeOut(bg_blobs), run_time=2)
        self.wait(1)
