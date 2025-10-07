#ifndef PLATFORM_H
#define PLATFORM_H

#include <glm/glm.hpp>
using namespace glm;

class Platform {
public:
    vec2 pos; // bottom-left corner
    vec2 size; // width and height
    Platform(vec2 p, vec2 s) : pos(p), size(s) {}
};

#endif