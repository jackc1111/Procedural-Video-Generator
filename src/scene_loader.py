import importlib.util
import os
import sys

class SceneLoader:
    @staticmethod
    def load_scene_class(file_path: str, class_name: str):
        """
        Dynamically imports a class from a given file path.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Script file not found: {file_path}")

        # Add the script's directory to sys.path to allow relative imports within the script
        script_dir = os.path.dirname(os.path.abspath(file_path))
        if script_dir not in sys.path:
            sys.path.insert(0, script_dir)

        module_name = os.path.splitext(os.path.basename(file_path))[0]
        
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is None:
            raise ImportError(f"Could not load spec for: {file_path}")
            
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if not hasattr(module, class_name):
            raise AttributeError(f"Class '{class_name}' not found in {file_path}")

        return getattr(module, class_name)
