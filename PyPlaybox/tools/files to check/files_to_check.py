import os
import hashlib
import Levenshtein

def find_files(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def find_similar_names(files, threshold=0.8):
    print("Checking for similar names...")
    similar_names = {}
    for i, file_path in enumerate(files, 1):
        file_name = os.path.basename(file_path)
        for name in similar_names:
            similarity = Levenshtein.ratio(file_name, name)
            if similarity >= threshold:
                similar_names[name].append(file_path)
                break
        else:
            similar_names[file_name] = [file_path]
        print(f"Processed {i}/{len(files)} files...")
    print("Name similarity check completed.")
    return {k: v for k, v in similar_names.items() if len(v) > 1}

def find_files_with_same_md5(files):
    print("Calculating MD5 hashes...")
    md5_values = {}
    for i, file_path in enumerate(files, 1):
        md5 = calculate_md5(file_path)
        if md5 in md5_values:
            md5_values[md5].append(file_path)
        else:
            md5_values[md5] = [file_path]
        print(f"Processed {i}/{len(files)} files...")
    print("MD5 calculation completed.")
    return {k: v for k, v in md5_values.items() if len(v) > 1}

def remove_numeric_prefix(file_name):
    # Utilizza espressione regolare per rimuovere i primi caratteri numerici
    return file_name.lstrip("0123456789")

def rename_files(directory):
    print("Renaming files...")
    for i, filename in enumerate(os.listdir(directory), 1):
        file_path = os.path.join(directory, filename)
        new_name = remove_numeric_prefix(filename)
        new_path = os.path.join(directory, new_name)
        os.rename(file_path, new_path)
        print(f"Renamed file {i}/{len(os.listdir(directory))}")
    print("Files renamed successfully.")

if __name__ == "__main__":
    directory_to_check = "path/to/your/directory"  # Replace with the target directory path

    files_in_directory = find_files(directory_to_check)
    similar_names = find_similar_names(files_in_directory)
    files_with_same_md5 = find_files_with_same_md5(files_in_directory)

    duplicates = {**similar_names, **files_with_same_md5}

    rename_files(directory_to_check)
