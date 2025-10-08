// editar classe h
#include <GLM/glm.hpp>
#include <GLM/gtc/matrix_transform.hpp>


    glm::vec2 m_position;
};

#include "Camera2D.h"

Camera2D::Camera2D() : m_position(0.0f) {}

Camera2D::~Camera2D() {}

void Camera2D::setPosition(const glm::vec2& position) {
    m_position = position;
}

// Este é o método principal que fará a câmera seguir o personagem
void Camera2D::follow(const glm::vec2& targetPosition) {
    // Centraliza a câmera no personagem.
    // Lembre-se que o movimento da câmera é o movimento do mundo em sentido oposto.
    m_position.x = targetPosition.x - (SCR_WIDTH / 2.0f);
    m_position.y = targetPosition.y - (SCR_HEIGHT / 2.0f);
    
    // Opcional: Adicione um efeito de "soft zone" para que a câmera não se mova
    // imediatamente, mas sim quando o personagem atinge uma certa margem.
    // Isso cria um movimento mais suave.
    // Exemplo:
    // float deadzoneX = 50.0f;
    // if (abs(targetPosition.x - m_position.x) > deadzoneX) {
    //    m_position.x = targetPosition.x - (SCR_WIDTH / 2.0f);
    // }
}

glm::mat4 Camera2D::getViewMatrix() const {
    // Cria uma matriz de translação com a posição inversa da câmera.
    glm::mat4 view = glm::translate(glm::mat4(1.0f), glm::vec3(-m_position, 0.0f));
    return view;
}
