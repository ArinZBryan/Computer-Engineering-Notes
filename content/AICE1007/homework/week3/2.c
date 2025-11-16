#include <stdio.h>
#include <stddef.h>
#include <stdbool.h>
#include <math.h>

struct {
    double radius;
    double x;
    double y;
    double z;
} typedef sphere;

bool overlaps(const sphere* restrict a , const sphere* restrict b) {
    double dist_x = a->x - b->x;
    double dist_y = a->y - b->y;
    double dist_z = a->z - b->z;
    double dist = sqrt(dist_x * dist_x + dist_y * dist_y + dist_z * dist_z);
    return dist <= (a->radius + b->radius);
}

bool any(bool* conditions, size_t n) {
    bool res = false;
    for (size_t i = 0; i < n; i++) {
        res |= conditions[i];
    }
    return res;
}

bool anyoverlap(const sphere* spheres, size_t n) {
    bool res = false;
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
            if (i == j) { continue; }
            res |= overlaps(&spheres[i], &spheres[j]);
        }
    }
    return res;
}

int main() {

    return 0;
}