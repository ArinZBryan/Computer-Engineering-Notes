#include <stdio.h>
#include <stdint.h>
#include <stddef.h>
#include <string.h>

#pragma pack(push, 1)
struct RGBA {
    uint16_t r;
    uint16_t g;
    uint16_t b;
    uint16_t a;
};
#pragma pack(pop)

int main(int argc, char** argv) {
    FILE* input;
    if (argc < 3) { fputs("Missing Required Fields\n", stderr); return 1; }
    if ((input = fopen(argv[1], "rb")) == NULL) { fputs("Could Not Open Non-Existent File\n", stderr); return 1; }
    
    uint8_t magic_expected[8] = {'f', 'a', 'r', 'b', 'f', 'e', 'l', 'd'};
    uint8_t magic_recieved[8];
    fread(magic_recieved, sizeof(uint8_t), 8, input);
    if (!memcmp(magic_expected, magic_recieved, 8)) { fputs("Not a farbfeld image\n", stderr); return 1; }

    uint32_t width, height;
    fread(&width, sizeof(uint32_t), 1, input);
    fread(&height, sizeof(uint32_t), 1, input);
    printf("Reading Image %s...\n\tWidth: %d\n\tHeight: %d\n", argv[1], width, height);

    FILE* output;
    if ((output = fopen(argv[2], "wb")) == NULL) { fputs("Could Not Open File For Writing\n", stderr); return 1; }
    fwrite(magic_expected, sizeof(uint8_t), 8, output);
    fwrite(&width, sizeof(uint32_t), 1, output);
    fwrite(&height, sizeof(uint32_t), 1, output);

    for (int pixel = 0; pixel < width * height; pixel++) {
        struct RGBA pixel;
        fread(&pixel, sizeof(pixel), 1, input);
        pixel.r = 0xffff - pixel.r;
        pixel.g = 0xffff - pixel.g;
        pixel.b = 0xffff - pixel.b;
        fwrite(&pixel, sizeof(pixel), 1, output);
    }
    printf("Successfully wrote %ld bytes.\n", ftell(output));
    return 0;
}