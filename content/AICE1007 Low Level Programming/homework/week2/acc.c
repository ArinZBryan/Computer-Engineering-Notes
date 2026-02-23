#include <stdio.h>



void acc_sub(int a[], int b[], size_t count) {
    for (size_t i = 0; i < count; i++) {
        a[i] += b[i];
    }
}

void acc_ptr(int* a, int* b , size_t count) {
    for (size_t i = 0; i < count; i++) {
        *(a + i) += *(b + i);
    }
}

int main(void)
{
    int a[6] = {1, 2, 3, 4, 5, 6};
    int b[6] = {6, 5, 4, 3, 2, 0};
    acc_ptr(a, b, sizeof(a)/sizeof(int));
    /* a now contains 7, 7, 7, 7, 7, 6 */
    return 0;
}