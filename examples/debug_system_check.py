from manim import *
from graphics_helper import GraphicsHelper

class PVGDiagnosticCheck(ThreeDScene):
    def construct(self):
        # 1. Background
        bg = GraphicsHelper.create_abstract_background(depth=5)
        self.add(bg)
        bg.add_updater(lambda m, dt: m.rotate(0.1 * dt))

        # 2. Intro Title with Glow
        title = Text("PVG STRESS TEST", font_size=60, weight=BOLD)
        glow = GraphicsHelper.create_glow(title, color=BLUE, scale=1.2, opacity=0.4)
        title_group = VGroup(title, glow)
        
        self.play(Write(title), FadeIn(glow), run_time=1.5)
        self.wait(1)

        # 3. Lower Third
        l3 = GraphicsHelper.create_lower_third("Diagnostic", "Verifying all modules...", color=BLUE_B)
        self.play(FadeIn(l3, shift=UP))
        self.wait(1)
        self.play(FadeOut(l3, shift=DOWN))

        # 4. 3D Transition
        cube = GraphicsHelper.create_3d_cube(side_length=2, fill_color=BLUE_D)
        
        # Animate camera to 3D
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, run_time=2)
        
        self.play(
            ReplacementTransform(title_group, cube),
            run_time=2
        )
        
        self.play(Rotate(cube, angle=2*PI, axis=OUT), run_time=2)

        # 5. Image Masking Test
        img = GraphicsHelper.load_image("tech.png", height=3)
        circle_mask = Circle(radius=1.5)
        masked_img = GraphicsHelper.create_masked_image(img, circle_mask)
        
        # Since we are in 3D, we fix the image in frame or let it be 3D
        self.add_fixed_in_frame_mobjects(masked_img)
        
        self.play(
            FadeOut(cube),
            FadeIn(masked_img),
            run_time=2
        )
        
        # Return camera to 2D
        self.move_camera(phi=0, theta=-90*DEGREES, run_time=1)
        
        self.wait(2)
        
        # Cleanup
        self.play(FadeOut(masked_img), FadeOut(bg))
