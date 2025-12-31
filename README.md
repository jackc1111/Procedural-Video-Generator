# Procedural Video Generator (PVG)

A Python-based tool for generating high-quality procedural videos, infographics, and connective graphics using Manim.

## Installation

1. Install FFmpeg (and LaTeX for formulas).
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Documentation

- **[USER_GUIDE.md](file:///home/volodymyr/4/USER_GUIDE.md)**: Start here! Step-by-step instructions for beginners.
- **[DOCUMENTATION.md](file:///home/volodymyr/4/DOCUMENTATION.md)**: Technical API reference for all visual effects and helpers.
- **[SYSTEM_PROMPT.md](file:///home/volodymyr/4/SYSTEM_PROMPT.md)**: Master prompt to teach external AI agents how to write scripts for this system.

## Structure

- `src/`: Core logic and modules.
- `examples/`: Sample scene scripts.
- `configs/`: YAML/JSON configuration files.
- `assets/`: External images, fonts, etc.
- `output/`: Generated videos and frames.
