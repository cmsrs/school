#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Podaj pierwsza liczbe: ";
    cin >> a;    
    cout << "Podaj druga liczbe: ";
    cin >> b;

    cout << endl;
    int suma = a + b;
    cout << "Suma tych liczb to: " << suma;

    if (b != 0) {
        cout << "\nDzielenie tych liczb to: " << static_cast<float>(a) / b << endl;
    } else {
        cout << "\nNie mozna dzielic przez zero!" << endl;
    }

    return 0;
}
