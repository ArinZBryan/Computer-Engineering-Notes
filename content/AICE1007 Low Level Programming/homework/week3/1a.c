#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* unpack_string(const char* packed_string) {
    size_t length = strlen(packed_string);
    char* num_end = (char*)packed_string;
    unsigned int repeats = strtoul(packed_string, &num_end, 10);
    size_t content_len = length - (num_end - packed_string);
    char* ret = malloc(repeats * content_len + 1);
    for (unsigned int i = 0; i < repeats; i++) {
        strcpy(ret + (content_len * i), num_end);
    }
    return ret;
}

int main() {
    const char* test_data = "7apple";
    const char* returned = unpack_string(test_data);
    printf("%s\n", returned);

    return 0;
}