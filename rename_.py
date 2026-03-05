import os
import re

def process_directory(root_dir):
    for root, dirs, files in os.walk(root_dir, topdown=False):
        if 'node_modules' in root or '.git' in root or '\\target' in root or '\\dist' in root or '\\.idea' in root:
            continue

        # 1. Process files
        for name in files:
            if name.endswith(('.png', '.jpg', '.webp', '.jpeg', '.gif', '.ico', '.jar', '.class')):
                continue
                
            file_path = os.path.join(root, name)
            old_name = name
            new_name = name.replace('', '').replace('', '').replace('', '')
            
            # Rename the file if it has  in the name (like SpringSecExApplication.java)
            if new_name != old_name:
                new_file_path = os.path.join(root, new_name)
                try:
                    os.rename(file_path, new_file_path)
                    print(f"Renamed file {file_path} to {new_file_path}")
                    file_path = new_file_path # Update the path to process contents
                except Exception as e:
                    print(f"Failed to rename file {file_path}: {e}")
                    
            # Update contents
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace variations of 
                new_content = content.replace('', '')
                new_content = new_content.replace('', '')
                new_content = new_content.replace('', '')
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated content in {file_path}")
            except Exception as e:
                pass

        # 2. Process directories
        for name in dirs:
            old_dir = os.path.join(root, name)
            new_name = name.replace('', '').replace('', '').replace('', '')
            
            if new_name != name:
                new_dir = os.path.join(root, new_name)
                try:
                    os.rename(old_dir, new_dir)
                    print(f"Renamed directory {old_dir} to {new_dir}")
                except Exception as e:
                    print(f"Failed to rename directory {old_dir}: {e}")

if __name__ == '__main__':
    project_root = r'C:\Desktop\Spring FrameWork'
    process_directory(project_root)
    print("Renaming  complete.")
