# folder, użytkownik i repo
user = "cmsrs"
repo = "school"
branch = "main"
path_in_repo = "sql/access/zestawienia/zipy"

print("### 📥 Pobierz swój zestaw danych\n")

for i in range(1, 51):  # od 01 do 35
    num = f"{i:02}"  # dwucyfrowy numer: 00, 01, 02 ...
    zip_name = f"zestaw_{num}.zip"
    url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/{path_in_repo}/{zip_name}"
    print(f"- Zestaw {num} → [Pobierz {zip_name}]({url})")

