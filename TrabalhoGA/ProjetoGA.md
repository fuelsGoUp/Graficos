# PlataOrigin

## Equipe
- Vitor Hugo Silva  
---

## Descrição do Projeto

> Este programa/projeto foi feito para a disciplina Processamento Grafico e demonstra o uso de C++ junto a OpenGL e outras bibliotecas, criando um ambiente basico para testes de colisão, graficos e shaders.

---

## Estrutura do Projeto

| Arquivo                  | Descrição                                                                 |
|--------------------------|---------------------------------------------------------------------------|
| `Game.cpp`               | Ponto de entrada do programa; inicialização do contexto OpenGL e loop.    |
| `Sprite.h / Sprite.cpp`  | Classe utilitaria para criar o sprite e os metodos do player.             |
| `Plataform.h             | Cria as plataformas                                                       |
| `Camera2d.h / Camera.cpp`| Classe para seguir jogador. ainda em desenvolvimento                      |

---

## Informações Técnicas

- **Linguagem:** C++ (C++11 ou superior)  
- **API Gráfica:** OpenGL 4.6 (core profile)  
- **Dependências:** GLFW, GLAD, stb_image, glm (outras, se utilizadas)  
- **IDE/Compilador:** Visual Studio Code / MinGW / CMake (ou equivalente)  
- **Plataforma-alvo:** Windows  

---

## Checklist de Requisitos

- [x] Criação de janela e contexto OpenGL  
- [x] Configuração de shaders e pipeline programável  
- [X] Implementação de transformações (model, view, projection)  
- [X] Controle de movimentação do personagem/câmera  
- [X] Renderização de múltiplos objetos 
- [X] Detecção de colisão - De pulo

---

## Referências e/ou créditos

Caso o projeto utilize assets, texturas, bibliotecas externas ou seja inspirado em tutoriais, cite as fontes aqui.  

- Tutorial seguido — [https://www.youtube.com/watch?v=_-s5apOO_7I]  Inspirado
- Assets do craftPix

---

## Comentários Finais

O projeto é uma inicialização de um jogo 2d de plataforma, uma demonstração de uso de OpenGl.
