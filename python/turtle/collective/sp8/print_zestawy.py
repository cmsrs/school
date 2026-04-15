# folder, użytkownik i repo
user = "cmsrs"
repo = "school"
branch = "main"
path_in_repo = "python/turtle/collective/sp8/patterns8sp"

print("### 📥 Pobierz swój zestaw danych\n")

for i in range(1, 37):  # od 01 do 36
    file_name = f"pattern_{i}.png"
    url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/{path_in_repo}/{file_name}"
    print(f"- Zestaw {i} → [Pobierz {file_name}]({url})")

