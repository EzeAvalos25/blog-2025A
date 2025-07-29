def validate_env(file_path='.env'):
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' not in line:
                print(f"❌ Línea {i} sin '=': {line}")

validate_env()

