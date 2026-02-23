#include <stdio.h>
#include <stdbool.h>

short int calc(short int arg1, short int arg2, char operator) {
    switch (operator) {
        case '+': return arg1 + arg2;
        case '-': return arg1 - arg2;
        case '*': return arg1 * arg2;
        case '/': return arg1 / arg2;
        case '^': return arg1 ^ arg2;
        default: return 0;
    }
}

int main(void) {
    return 0;
}