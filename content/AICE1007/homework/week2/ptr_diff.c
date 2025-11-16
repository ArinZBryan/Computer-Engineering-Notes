#include <stdlib.h>

size_t myfun(int *arr, int *loc) {
    return (loc - arr) >> 2;
}

int main(void)
{
    int x[100] = {0};
    return myfun(x, &x[67]);  /* Returns 67 */
}