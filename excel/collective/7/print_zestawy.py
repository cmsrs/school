# folder, użytkownik i repo
user = "cmsrs"
repo = "school"
branch = "main"
path_in_repo = "excel/collective/7/zestawy_dla_uczniow"

print("### 📥 Pobierz swój zestaw danych\n")

for i in range(1, 51):  # od 01 do 35
    num = f"{i:03}"  #  numer: 000, 001, 002 ...
    file_name = f"zestaw_{num}.xlsx"
    url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/{path_in_repo}/{file_name}"
    print(f"- Zestaw {num} → [Pobierz {file_name}]({url})")

