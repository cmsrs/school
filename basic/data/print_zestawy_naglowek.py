# folder, użytkownik i repo
user = "cmsrs"
repo = "school"
branch = "main"
path_in_repo = "basic/data/obrazy_rozpakowane"

print("### 📥 Pobierz swój naglówek\n")

for i in range(1, 51):  # od 01 do 35
    num = str(i) 
    head_name = f"naglowek{num}.png"
    url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/{path_in_repo}/{head_name}"
    print(f"- Zestaw {num} → [Pobierz {head_name}]({url})")

