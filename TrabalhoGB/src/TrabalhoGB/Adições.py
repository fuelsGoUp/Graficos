def carregar_imagens(pastas_lista=["imagens"]): # Agora espera uma lista, padrão é ["imagens"]
    arquivos = []
    # Itera sobre cada pasta fornecida na lista
    for pasta in pastas_lista:
        if os.path.exists(pasta):
            for f in os.listdir(pasta):
                if f.lower().endswith((".png", ".jpg", ".jpeg")):
                    arquivos.append(os.path.join(pasta, f))
    return arquivos

# Crie uma lista de todas as pastas que você deseja escanear
pastas_do_projeto = ["imagens", "Graficos/TrabalhoGB/outras_imagens", "Caminho/Absoluto/etc"]

# Quando você precisar carregar as imagens (por exemplo, na função menu() ou executar()):

# Opção 1: Chame a função modificada com sua lista de pastas
lista_de_arquivos_completos = carregar_imagens(pastas_do_projeto)

# Opção 2: Se você quiser apenas usar a pasta padrão ["imagens"]
# lista_de_arquivos = carregar_imagens() 
