#include <stdio.h>  
#include <stdlib.h>
#include <time.h>


int fib_rec(int n) {
    if (n <= 1) {
        return n;
    }
    return fib_rec(n - 1) + fib_rec(n - 2);
}

/**
run:
gcc  fib_rec.c
*/
int main() {
    int n = 44; // Maksymalny indeks Fibonacciego

    for (int i = 30; i <= n; i++) {
        clock_t start = clock();  // start pomiaru

        int result = fib_rec(i);

        clock_t end = clock();    // koniec pomiaru

        double time_taken = (double)(end - start) / CLOCKS_PER_SEC;

        printf("Fibonacci of %d is %d\t| Time: %.6f seconds\n", i, result, time_taken);
    }

    return 0;
}