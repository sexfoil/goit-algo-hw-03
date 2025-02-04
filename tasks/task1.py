import shutil
import argparse
from pathlib import Path

def parse_directory(src_path: Path, dest_path: Path):
    try:
        for item in src_path.iterdir():
            if item.is_dir():
                parse_directory(item, dest_path)
            elif item.is_file():
                ext = item.suffix[1:] if item.suffix else "no_extension"
                target_folder = dest_path / ext
                target_folder.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target_folder / item.name)
                print(f"Copied: {item} -> {target_folder / item.name}")
    except Exception as e:
        print(f"Error processing {src_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Copy and sort files by extension.")
    parser.add_argument("source", help="Path to the source directory")
    parser.add_argument("target", nargs="?", default="dist", help="Path to the destination directory (default: dist)")
    args = parser.parse_args()

    src_path = Path(args.source)
    dest_path = Path(args.target)
    
    if not src_path.exists():
        print(f"Error: Source directory '{src_path}' does not exist.")
        return
    
    parse_directory(src_path, dest_path)

if __name__ == "__main__":
    main()
