import os
import shutil
import argparse


def copy_files_recursive(src_dir, dest_dir):
    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)

        if os.path.isdir(item_path):
            copy_files_recursive(item_path, dest_dir)

        elif os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1].lstrip('.').lower()
            if not file_extension:
                file_extension = 'no_extension'

            new_folder = os.path.join(dest_dir, file_extension)
            os.makedirs(new_folder, exist_ok=True)

            dest_file_path = os.path.join(new_folder, item)
            print(f"Копіюємо {item_path} до {dest_file_path}")
            try:
                shutil.copy2(item_path, dest_file_path)
            except Exception as e:
                print(f"Помилка при копіюванні файлу {item_path}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Рекурсивне копіювання та сортування файлів за розширенням."
        )
    )
    parser.add_argument('src', help="Шлях до вихідної директорії")
    parser.add_argument(
        'dest',
        nargs='?',
        default='dist',
        help="Шлях до директорії призначення (за замовчуванням 'dist')")
    args = parser.parse_args()

    src_dir = args.src
    dest_dir = args.dest

    if not os.path.exists(src_dir):
        print(f"Вихідна директорія {src_dir} не існує.")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    copy_files_recursive(src_dir, dest_dir)
    print("Копіювання завершено.")


if __name__ == "__main__":
    main()
