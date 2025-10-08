#ifndef PLATFORM_H
#define PLATFORM_H

#include <glm/glm.hpp>
using namespace glm;

class Platform {
public:
    vec2 pos; // borda inferior esquerda
    vec2 size; // largura e altura
    Platform(vec2 p, vec2 s) : pos(p), size(s) {}
};

#endif
