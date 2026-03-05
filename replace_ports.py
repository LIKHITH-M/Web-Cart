import os

def process_directory(root_dir):
    for root, dirs, files in os.walk(root_dir, topdown=False):
        if 'node_modules' in root or '.git' in root or '\\target' in root or '\\dist' in root or '\\.idea' in root:
            continue

        for name in files:
            if name.endswith(('.png', '.jpg', '.webp', '.jpeg', '.gif', '.ico', '.jar', '.class')):
                continue
                
            file_path = os.path.join(root, name)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace ports
                new_content = content.replace('<BACKEND_PORT>', '<BACKEND_PORT>')
                new_content = new_content.replace('<FRONTEND_PORT>', '<FRONTEND_PORT>')
                new_content = new_content.replace('<DB_PORT>', '<DB_PORT>')
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated ports in {file_path}")
            except Exception as e:
                pass

if __name__ == '__main__':
    project_root = r'C:\Desktop\Spring FrameWork'
    process_directory(project_root)
    print("Replacing ports complete.")
