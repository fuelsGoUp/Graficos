// dentro do game loop


// Representação do personagem (pode ser uma classe ou struct)
struct Character {
    glm::vec2 position;
    // ... outros atributos
};

Character player;
Camera2D camera;

void gameLoop() {
    // ...
    // Lógica para mover o personagem
    player.position.x += 1.0f; // Exemplo de movimento

    // Atualiza a posição da câmera
    camera.follow(player.position);

    // Obtém as matrizes atualizadas
    glm::mat4 viewMatrix = camera.getViewMatrix();
    glm::mat4 projectionMatrix = projection;

    // Renderização
    // glUseProgram(...);
    // glUniformMatrix4fv(glGetUniformLocation(shaderProgram, "view"), 1, GL_FALSE, glm::value_ptr(viewMatrix));
    // glUniformMatrix4fv(glGetUniformLocation(shaderProgram, "projection"), 1, GL_FALSE, glm::value_ptr(projectionMatrix));

    // Desenha todos os objetos do jogo
    // glDrawArrays(...);
    // ...
}
