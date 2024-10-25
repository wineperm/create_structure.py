import os

def create_file(path, content):
    if os.path.exists(path):
        overwrite = input(f"File {path} already exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print(f"Skipping {path}")
            return
    dir_path = os.path.dirname(path)
    if dir_path:  # Проверка, что директория не пустая
        os.makedirs(dir_path, exist_ok=True)
    with open(path, 'w') as file:
        file.write(content)

def parse_and_create_files(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_file_path = None
    current_file_content = []

    for line in lines:
        if line.startswith('#'):
            if current_file_path:
                create_file(current_file_path, ''.join(current_file_content))
            current_file_path = line.strip('# ').strip()
            if not current_file_path:
                continue
            current_file_content = []
        else:
            current_file_content.append(line)

    if current_file_path:
        create_file(current_file_path, ''.join(current_file_content))

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    info_tai_path = os.path.join(script_dir, 'info.tai')

    if not os.path.exists(info_tai_path):
        print(f"File {info_tai_path} not found.")
    else:
        parse_and_create_files(info_tai_path)
