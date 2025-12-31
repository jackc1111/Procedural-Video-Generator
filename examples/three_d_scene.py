from manim import *
import sys
import os

# Ensure src is in path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from graphics_helper import GraphicsHelper

class ThreeDExample(ThreeDScene):
    def construct(self):
        # 1. Setup 3D Camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        # 2. Add 3D Objects
        cube = GraphicsHelper.create_3d_cube(side_length=2, fill_color=BLUE_B)
        sphere = GraphicsHelper.create_3d_sphere(radius=1, fill_color=ORANGE)
        sphere.next_to(cube, RIGHT, buff=1)
        
        title = Text("3D VISUALIZATION", font_size=48, color=WHITE).to_corner(UL)
        self.add_fixed_in_frame_mobjects(title) # Keeps text flat on screen

        # 3. Animations
        self.play(Create(cube), Create(sphere))
        self.play(Write(title))
        self.wait(1)
        
        # Dynamic Camera Movement (reveals depth)
        self.begin_ambient_camera_rotation(rate=0.2)
        
        self.play(
            cube.animate.rotate(PI/4, axis=UP),
            sphere.animate.shift(OUT * 2),
            run_time=3
        )
        
        self.wait(2)
        self.stop_ambient_camera_rotation()
        
        # 4. Outro
        self.play(FadeOut(cube), FadeOut(sphere), FadeOut(title))
        self.wait(1)
