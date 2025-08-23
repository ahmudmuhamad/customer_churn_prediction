import os
from pathlib import Path

def create_directory_structure():
    # Define the base directory and structure
    base_dir = Path("src")
    structure = {
        "src/churn": [
            "__init__.py",
            "api/__init__.py",
            "api/main.py",
            "api/deps.py",
            "api/model_loader.py",
            "api/routers/__init__.py",
            "api/routers/predict.py",
            "api/routers/health.py",
            "api/schemas.py",
            "core/config.py",
            "tests/test_predict.py"
        ]
    }
    
    # Create directories and files
    for directory, files in structure.items():
        for file_path in files:
            full_path = Path(directory) / file_path
            # Create parent directories if they don't exist
            full_path.parent.mkdir(parents=True, exist_ok=True)
            # Create empty file
            full_path.touch()
            print(f"Created: {full_path}")

if __name__ == "__main__":
    create_directory_structure()
    print("Directory structure created successfully!")