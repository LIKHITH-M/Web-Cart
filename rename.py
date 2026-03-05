import os
import re

def process_directory(root_dir):
    for root, dirs, files in os.walk(root_dir, topdown=False):
        # Prevent accessing node_modules and target/dist dirs to speed up and avoid replacing built artifacts
        if 'node_modules' in root or '.git' in root or '\\target' in root or '\\dist' in root or '\\.idea' in root:
            continue

        for name in files:
            if name.endswith(('.png', '.jpg', '.webp', '.jpeg', '.gif', '.ico', '.jar', '.class')):
                continue
                
            file_path = os.path.join(root, name)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace 'likhith' -> 'likhith' and 'Likhith' -> 'Likhith'
                new_content = content.replace('likhith', 'likhith')
                new_content = new_content.replace('Likhith', 'Likhith')
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated content in {file_path}")
            except Exception as e:
                print(f"Skipping {file_path} due to error: {e}")

        # Rename directories
        for name in dirs:
            if name == 'likhith':
                old_dir = os.path.join(root, name)
                new_dir = os.path.join(root, 'likhith')
                try:
                    os.rename(old_dir, new_dir)
                    print(f"Renamed directory {old_dir} to {new_dir}")
                except Exception as e:
                    print(f"Failed to rename directory {old_dir}: {e}")

if __name__ == '__main__':
    project_root = r'C:\Desktop\Spring FrameWork'
    process_directory(project_root)
    print("Renaming complete.")
