from manim import config, Scene
import os

class Renderer:
    def __init__(self, quality="high_quality", output_directory="media", snapshot=False):
        self.output_directory = output_directory
        self.quality = quality
        self.snapshot = snapshot
        self._setup_config()

    def _setup_config(self):
        """
        Initializes Manim configuration.
        """
        config.media_dir = self.output_directory
        config.images_dir = os.path.join(self.output_directory, "images")
        config.video_dir = os.path.join(self.output_directory, "videos")

        # Snapshot mode (saves last frame as PNG)
        if self.snapshot:
            config.save_last_frame = True
            config.format = "png"

        # Quality presets
        if self.quality == "low":
            config.quality = "low_quality"
        elif self.quality == "medium":
            config.quality = "medium_quality"
        elif self.quality == "high":
            config.quality = "high_quality"
        elif self.quality == "4k":
            config.quality = "fourk_quality"

    def render_scene(self, scene_class):
        """
        Renders the provided scene class.
        """
        scene = scene_class()
        scene.render()
        if self.snapshot:
            print(f"Snapshot completed. Image saved in {config.images_dir}")
        else:
            print(f"Render completed. Video saved in {config.video_dir}")
