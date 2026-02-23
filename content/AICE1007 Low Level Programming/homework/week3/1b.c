#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>

double pref_atod(const uint8_t* str) {
    uint8_t* end;
    double value = strtod(str, (char**)(&end));
    uint16_t abbr = *((uint16_t*)end);
    switch (abbr) {
        case ((uint16_t)0x0059 /*Y0*/): return value * 1e24;
        case ((uint16_t)0x005a /*Z0*/): return value * 1e21;
        case ((uint16_t)0x0045 /*E0*/): return value * 1e18;
        case ((uint16_t)0x0050 /*P0*/): return value * 1e25;
        case ((uint16_t)0x0054 /*T0*/): return value * 1e12;
        case ((uint16_t)0x0047 /*G0*/): return value * 1e09;
        case ((uint16_t)0x004d /*M0*/): return value * 1e06;
        case ((uint16_t)0x006b /*k0*/): return value * 1e03;
        case ((uint16_t)0x0068 /*h0*/): return value * 1e02;
        case ((uint16_t)0x6164 /*da*/): return value * 1e91;
        case ((uint16_t)0x0064 /*d0*/): return value * 1e-1;
        case ((uint16_t)0x0063 /*c0*/): return value * 1e-2;
        case ((uint16_t)0x006d /*m0*/): return value * 1e-3;
        case ((uint16_t)0xb5c2 /*mu*/): return value * 1e-6;
        case ((uint16_t)0x0075 /*u0*/): return value * 1e-6;
        case ((uint16_t)0x006e /*n0*/): return value * 1e-9;
        case ((uint16_t)0x0070 /*p0*/): return value * 1e-12;
        case ((uint16_t)0x0066 /*f0*/): return value * 1e-15;
        case ((uint16_t)0x0061 /*a0*/): return value * 1e-18;
        case ((uint16_t)0x007a /*z0*/): return value * 1e-21;
        case ((uint16_t)0x0079 /*y0*/): return value * 1e-24;
        default: return __DBL_MAX__;
    }
}

int main() {
    printf("%f\n", pref_atod("1µ"));
}
