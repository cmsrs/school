#include <iostream>
using namespace std;

int main() {
    int ile_gruszek_krzys, ile_gruszek_adam, suma_gruszek;

    cout << "Krzysiu, ile masz gruszek? ";
    cin >> ile_gruszek_krzys;

    cout << "Adam, ile masz gruszek? ";
    cin >> ile_gruszek_adam;

    suma_gruszek = ile_gruszek_krzys + ile_gruszek_adam;

    if (suma_gruszek < 5) {
        cout << "Za malo gruszek na kompot" << endl;
    } else {
        cout << "Wystarczjaco gruszek, mozna zrobic kompot" << endl;
    }

    return 0;
}