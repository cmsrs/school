import os
import zipfile
import re  # do sprawdzania wzorca katalogu

# bieżący katalog, w którym są foldery z zestawami
source_folder = "."
# folder docelowy na ZIP-y
output_folder = "./zipy"

# utwórz folder docelowy, jeśli nie istnieje
os.makedirs(output_folder, exist_ok=True)

# wzorzec katalogu
pattern = re.compile(r"^zestaw_(\d\d)$")

# przejdź po katalogach w source_folder
for item in os.listdir(source_folder):
    dir_path = os.path.join(source_folder, item)
    if os.path.isdir(dir_path) and pattern.match(item):
        zip_path = os.path.join(output_folder, f"{item}.zip")
        print(f"Tworzę ZIP: {zip_path}")
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    # zachowaj strukturę wewnątrz katalogu
                    arcname = os.path.relpath(file_path, dir_path)
                    zipf.write(file_path, arcname)

print("Gotowe! Wszystkie katalogi zestaw_0X spakowane do folderu 'zipy'.")
