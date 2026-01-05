import argparse
import sys
import os

# Add src to path for local imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scene_loader import SceneLoader
from renderer import Renderer

def main():
    parser = argparse.ArgumentParser(description="Procedural Video Generator CLI")
    parser.add_argument("script", help="Path to the scene script file (.py)")
    parser.add_argument("scene_name", help="Name of the Scene class to render")
    parser.add_argument("--quality", choices=["low", "medium", "high", "4k"], default="high", help="Render quality")
    parser.add_argument("--output", default="output", help="Output directory")
    parser.add_argument("--snapshot", action="store_true", help="Save the last frame as a PNG snapshot instead of rendering a video")
    parser.add_argument("--studio-format", action="store_true", help="Create a studio-optimized MP4 copy with specific encoding settings")
    parser.add_argument("--composite-video", help="Path to video file to composite over the animation (e.g., for embedding videos)")

    args = parser.parse_args()

    try:
        print(f"--- PVG: Loading {args.scene_name} from {args.script} ---")
        scene_class = SceneLoader.load_scene_class(args.script, args.scene_name)
        
        print(f"--- PVG: Starting Render (Quality: {args.quality}) ---")
        renderer = Renderer(quality=args.quality, output_directory=args.output, snapshot=args.snapshot, studio_format=args.studio_format, composite_video=args.composite_video)
        renderer.render_scene(scene_class)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
