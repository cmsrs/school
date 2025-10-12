print('Krzysiu, ile masz gruszek?')
ile_gruszek_krzys = int(input())


print('Adam, ile masz gruszek?')
ile_gruszek_adam = int(input())

suma_gruszek = ile_gruszek_krzys + ile_gruszek_adam  
if suma_gruszek < 5:
    print('Za malo gruszek na kompot')
else:
    print('Wystarczjaco gruszek, mozna zrobic kompot')
