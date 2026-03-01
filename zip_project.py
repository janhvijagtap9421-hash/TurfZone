
import os
import zipfile
from pathlib import Path

def zip_project(output_filename="TurfBooking_Project.zip"):
    # Current directory
    source_dir = Path.cwd()
    output_path = source_dir / output_filename
    
    # Files/Dirs to exclude
    exclude_dirs = {
        '__pycache__', 
        'venv', 
        'env', 
        '.git', 
        '.idea', 
        '.vscode', 
        'node_modules',
        'media'  # Optional: exclude media if too large, but verify first. Keeping it for now.
    }
    
    exclude_files = {
        output_filename,
        'db.sqlite3', # Exclude the old broken one
        '*.pyc',
        '*.pyo',
        '*.pyd',
        '.DS_Store'
    }

    print(f"Zipping project to {output_filename}...")
    
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            # Modify dirs in-place to skip excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                if file in exclude_files or file.endswith('.pyc'):
                    continue
                    
                file_path = Path(root) / file
                archive_name = file_path.relative_to(source_dir)
                
                print(f"Adding: {archive_name}")
                zipf.write(file_path, archive_name)
                
    print(f"\n✅ Project successfully zipped: {output_path}")
    print(f"File size: {output_path.stat().st_size / (1024*1024):.2f} MB")

if __name__ == "__main__":
    zip_project()
