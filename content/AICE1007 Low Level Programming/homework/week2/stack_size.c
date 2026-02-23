#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// crashes at 8MiB allocated.
// Likely would crash earlier if I was actually using it

int main(void) {
    size_t alloc_ammount = 1;
    while (true) {
        printf("Allocating %lu bytes\n", alloc_ammount);
        char bytes[alloc_ammount];
        alloc_ammount++;
    }
}