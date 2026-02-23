#include <stdio.h>
#include <stdbool.h>

bool bruteforce_prime(int p) {
    bool non_prime = false;
    for (int i = p - 1; i > 1; i--) {
        if (p % i == 0) non_prime = true;
    }
    return !non_prime;
}

int main(void) {
    for (int i = 2; i < 50; i++) {
        printf("%d\t", i);
        if (bruteforce_prime(i)) printf("is prime\n");
        else printf("is not prime\n");
    }
    return 0;
}

