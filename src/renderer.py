from manim import config, Scene
import os
import subprocess

class Renderer:
    def __init__(self, quality="high_quality", output_directory="media", snapshot=False, studio_format=False):
        self.output_directory = output_directory
        self.quality = quality
        self.snapshot = snapshot
        self.studio_format = studio_format
        self._setup_config()

    def _transcode_to_studio_format(self, scene_class):
        """
        Transcodes the rendered video to studio format using FFmpeg.
        """
        video_file = os.path.join(config.video_dir, f"{scene_class.__name__}.mp4")
        studio_file = os.path.join(config.video_dir, f"{scene_class.__name__}_studio.mp4")

        if not os.path.exists(video_file):
            print(f"Warning: Original video file {video_file} not found. Skipping studio format conversion.")
            return

        command = [
            "ffmpeg",
            "-i", video_file,
            "-c:v", "libx264",
            "-profile:v", "main",
            "-level:v", "4.0",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-b:a", "128k",
            "-y",  # Overwrite output file
            studio_file
        ]

        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            print(f"Studio format conversion completed. File saved as {studio_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error during FFmpeg transcode: {e}")
            print(f"FFmpeg stderr: {e.stderr}")
        except FileNotFoundError:
            print("Error: FFmpeg not found. Please install FFmpeg to use studio format conversion.")

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
            if self.studio_format:
                self._transcode_to_studio_format(scene_class)
