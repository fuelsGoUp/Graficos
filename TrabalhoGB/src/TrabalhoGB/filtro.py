import cv2
import glfw
import numpy as np
from OpenGL.GL import *
import os

# ======================================================
#  Filtros Instagram Style (OpenCV)
# ======================================================

def filtro_normal(img):
    return img

def filtro_pb(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def filtro_sepia(img):
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    return cv2.transform(img, kernel)

def filtro_vintage(img):
    return cv2.GaussianBlur(img, (11, 11), 10)

def filtro_edges(img):
    edges = cv2.Canny(img, 80, 200)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

def filtro_invert(img):
    return 255 - img

def filtro_cartoon(img):
    blur = cv2.bilateralFilter(img, 9, 75, 75)
    edges = cv2.adaptiveThreshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                                  255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY,
                                  9, 2)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    return cv2.bitwise_and(blur, edges)

def filtro_azul(img):
    b, g, r = cv2.split(img)
    return cv2.merge([b, g * 0, r * 0])

def filtro_calor(img):
    lut = np.interp(np.arange(256), [0, 128, 255], [0, 180, 255]).astype("uint8")
    return cv2.LUT(img, lut)

def filtro_frio(img):
    lut = np.interp(np.arange(256), [0, 128, 255], [0, 70, 255]).astype("uint8")
    b, g, r = cv2.split(img)
    return cv2.merge([cv2.LUT(b, lut), g, r])

filtros = [
    ("Normal", filtro_normal),
    ("Preto e Branco", filtro_pb),
    ("Sépia", filtro_sepia),
    ("Vintage", filtro_vintage),
    ("Bordas", filtro_edges),
    ("Invertido", filtro_invert),
    ("Cartoon", filtro_cartoon),
    ("Azul", filtro_azul),
    ("Calor", filtro_calor),
    ("Frio", filtro_frio)
]

# ======================================================
#  Função OpenGL para exibir imagem
# ======================================================

def draw_texture(frame):
    h, w = frame.shape[:2]

    # Corrige imagem invertida!
    frame = cv2.flip(frame, 0)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.ascontiguousarray(frame)

    glDrawPixels(w, h, GL_RGB, GL_UNSIGNED_BYTE, frame)

# ======================================================
#  Carrega imagens da pasta
# ======================================================

def carregar_imagens(pastas):
    imagens = []
    for pasta in pastas:
        if os.path.exists(pasta):
            for arquivo in os.listdir(pasta):
                if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                    imagens.append(os.path.join(pasta, arquivo))
    return imagens

# ======================================================
#  Menu interativo PowerShell
# ======================================================

def menu():
    print("\n====== MENU ======")
    print("1 - Usar câmera")
    print("2 - Carregar imagens da pasta /imagens")
    print("3 - Sair")
    escolha = input("Escolha: ")
    return escolha

# ======================================================
#  Loop principal com OpenGL + Filtros
# ======================================================

def executar(video_source):

    if not glfw.init():
        print("Erro ao inicializar janela GLFW")
        return
    
    janela = glfw.create_window(800, 600, "Filtros Instagram - OpenCV + OpenGL", None, None)
    glfw.make_context_current(janela)
    glfw.focus_window(janela)
    filtro_id = 0
    total_filtros = len(filtros)

    cap = None
    imagens = None
    index_imagem = 0

    if isinstance(video_source, int):
        cap = cv2.VideoCapture(video_source)
    else:
        imagens = video_source

    while not glfw.window_should_close(janela):

        glfw.poll_events()

        if cap:
            ret, frame = cap.read()
            if not ret:
                break
        else:
            frame = cv2.imread(imagens[index_imagem])

        frame = filtros[filtro_id][1](frame)

        glClear(GL_COLOR_BUFFER_BIT)
        draw_texture(frame)
        glfw.swap_buffers(janela)

        # Comandos do teclado
        if glfw.get_key(janela, glfw.KEY_RIGHT) == glfw.PRESS:
            filtro_id = (filtro_id + 1) % total_filtros
            print("Filtro:", filtros[filtro_id][0])
            glfw.wait_events_timeout(0.2)

        if glfw.get_key(janela, glfw.KEY_LEFT) == glfw.PRESS:
            filtro_id = (filtro_id - 1) % total_filtros
            print("Filtro:", filtros[filtro_id][0])
            glfw.wait_events_timeout(0.2)

        if not cap:  # navegação entre imagens
            if glfw.get_key(janela, glfw.KEY_UP) == glfw.PRESS:
                index_imagem = (index_imagem + 1) % len(imagens)
                print("Imagem:", imagens[index_imagem])
                glfw.wait_events_timeout(0.2)

            if glfw.get_key(janela, glfw.KEY_DOWN) == glfw.PRESS:
                index_imagem = (index_imagem - 1) % len(imagens)
                print("Imagem:", imagens[index_imagem])
                glfw.wait_events_timeout(0.2)

    glfw.terminate()
    if cap:
        cap.release()

# ======================================================
#  Programa Principal
# ======================================================

if __name__ == "__main__":
    while True:
        esc = menu()
        
        if esc == "1":
            executar(0)

        elif esc == "2":
            pastas_do_projeto = ["imagens", "Graficos/TrabalhoGB/outras_imagens", "Caminho/Absoluto/etc"]
            imgs = carregar_imagens(pastas_do_projeto)
            if not imgs:
                print("Nenhuma imagem na pasta /imagens")
            else:
                executar(imgs)

        elif esc == "3":
            break

        else:
            print("Opção inválida.")
