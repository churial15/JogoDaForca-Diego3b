# ============================================================
# Disciplina: Programação no Desenvolvimento de Sistemas
# Turma: 3º Ano do Ensino Médio Técnico
# ============================================================

# Lista inicial de palavras
# MISSÃO DOS ALUNOS:
# - Adicionar mais palavras
# - Separar por temas: jogos, tecnologia, escola, filmes etc.

import random
import os
import unicodedata

categorias = {
    "Musicas": [
        "feel good inc",
        "bones",
        "cracker island",
        "clint eastwood",
        "immigrant song",
        "enemy",
        "eyes closed",
        "natural",
        "rhinestone eyes",
        "new gold",
        "believe",
        "lonely",
        "warriors",
        "in the end",
        "back in black",
        "highway to hell",
        "tnt",
        "master of puppets",
        "song two"
        "numb",
        "faint",
        "what ive done",
        "bleed it out",
        "burn it down",
        "castle of glass",
        "papercut",
        "one step closer",
        "somewhere i belong",
        "crawling",
        "demons",
        "radioactive",
        "thunder",
        "believer",
        "sharks",
        "whatever it takes",
        "bad liar",
        "follow you",
        "dirty harry",
        "dare",
        "on melancholy hill",
        "saturnz barz",
        "19-2000",
        "kids with guns",
        "stylo",
        "tomorrow comes today",
        "stairway to heaven",
        "black dog",
        "kashmir",
        "whole lotta love",
        "ramble on",
        "thunderstruck",
        "hells bells",
        "shoot to thrill",
        "you shook me all night long",
        "dirty deeds done dirt cheap",
        "enter sandman",
        "nothing else matters",
        "one",
        "seek and destroy",
        "fuel",
        "for whom the bell tolls",
        "beetlebum",
        "girls and boys",
        "coffee and tv",
        "charmless man"
        ],
    
        "Bandas": [
            "gorillaz",
            "imagine dragons",
            "led zeppelin",
            "linkin park",
            "twenty one pilots"
        ],
    
        "Jogos": [
            "alien isolation",
            "alan wake",
            "amnesia",
            "among us",
            "bald basics",
            "biohazard",
            "bloodborne",
            "chained together",
            "crash bandicoot",
            "cuphead",
            "cyberpunk",
            "dark souls",
            "dead space",
            "Detroit Become Human",
            "devil may cry",
            "devour",
            "doom eternal",
            "elden ring",
            "fortnite",
            "forza horizon",
            "god of war",
            "granny",
            "gta v",
            "half life",
            "hollow knight",
            "lethal company",
            "little nightmares",
            "mario kart deluxe",
            "marvels spider man",
            "minecraft",
            "outlast",
            "overwatch",
            "phasmophobia",
            "poppy playtime",
            "portal",
            "pratfall",
            "red dead redemption",
            "repo",
            "resident evil",
            "rocket clank",
            "rocket league",
            "silent hill",
            "stray",
            "subnautica",
            "sonic the hedgehog",
            "super mario world",
            "terraria",
            "the last of us",
            "The Legend of Zelda",
            "the mortuary assistant",
            "the witcher",
            "undertale",
            "until dawn",
            "valorant",
            "the evil within",
            "days gone",
            "dying light",
            "sons of the forest",
            "the forest",
            "Cry of Fear",
            "soma",
            "visage",
            "layers of fear",
            "dark deception",
            "backrooms",
            "buckshot roulette",
            "iron lung",
            "fears to fathom",
            "tomb raider",
            "level devil",
            "bomberman",
            "kirby",
            "the legend of zelda",
            "street fighter",
            "mortal kombat"
    ],

    "Tecnologia": [
        "computacao grafica",
        "desenvolvimento de sistemas",
        "fullstack",
        "ciencia de dados",
        "analise e projeto de sistemas",
        "python",
        "programacao",
        "sistema",
        "algoritmo",
        "internet",
        "computador",
        "desenvolvedor",
        "software",
        "terminal",
        "hardware",
        "codigo",
        "processador",
        "banco de dados",
        "inteligencia artificial",
        "rede",
        "servidor",
        "aplicativo",
        "interface",
        "api",
        "framework",
        "biblioteca",
        "compilador",
        "script",
        "classe",
        "github",
        "backend",
        "frontend",
        "html",
        "css",
        "javascript",
        "java",
        "sql",
        "linux",
        "windows",
        "robotica",
        "bluetooth",
        "gpu",
        "cpu",
        "devops",
        "json",
        "xml",
        "typescript",
        "nodejs",
        "react",
        "vue",
        "angular",
        "django",
        "flask",
        "firebase",
        "docker",
        "kubernetes",
        "cloud",
        "aws",
        "azure",
        "machine learning",
        "deep learning",
        "chatbot",
        "automacao",
        "criptografia",
        "ciberseguranca",
        "firewall",
        "wifi",
        "ethernet",
        "kernel",
        "ubuntu",
        "android",
        "ios",
        "virtualizacao",
        "microchip",
        "arduino",
        "engenharia de software",
        "orientacao a objetos",
        "estrutura de dados",
        "debug",
        "teste",
        "deploy",
        "git",
        "gitlab",
        "open source",
        "mobile",
        "desktop",
        "nuvem",
        "streaming",
        "web",
        "website",
        "responsividade",
        "pixel",
        "monitor",
        "mouse",
        "teclado",
        "ssd",
        "memoria ram"
    ]
}

# ============================================================
# FORCA VISUAL
# ============================================================

forca = [

"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",

"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",

"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",

"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",

"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",

"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",

"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]

def limpar_tela():

    # Limpa a tela do terminal dependendo do sistema operacional.
    # "cls" funciona no Windows e "clear" no Linux/Mac.
    os.system("cls" if os.name == "nt" else "clear")


def remover_acentos(texto):

    # Remove acentos do texto usando normalização Unicode.
    # Exemplo: "ação" vira "acao".
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )


def escolher_dificuldade():

    # Exibe o menu de dificuldades.
    print("=" * 43)
    print("┴┬┴┤(･_├┬┴┬┴ ESCOLHA A DIFICULDADE ATACADA:")
    print("=" * 43)

    print("1 - Fácil   (8 vidas)")
    print("2 - Médio   (6 vidas)")
    print("3 - Difícil (4 vidas)")
    print("4 - Extremo (2 vidas)")
    print()

    # Loop infinito até o jogador digitar uma opção válida.
    while True:

        escolha = input("Digite a dificuldade: ")

        # Se escolher 1, retorna 8 vidas.
        if escolha == "1":
            return 8

        # Se escolher 2, retorna 6 vidas.
        elif escolha == "2":
            return 6

        # Se escolher 3, retorna 4 vidas.
        elif escolha == "3":
            return 4

        # Se escolher 4, retorna 2 vidas.
        elif escolha == "4":
            return 2

        # Caso digite algo inválido.
        else:
            print("Opção inválida.\n")


def escolher_categoria():

    # Mostra o menu de categorias disponíveis.
    print("==" * 22)
    print("┬─┬ノ( º _ ºノ) ESCOLHA UMA CATEGORIA BRABA:")
    print("==" * 22)

    # Percorre todas as categorias do dicionário.
    for categoria in categorias:
        print("-", categoria)

    print()

    # Continua perguntando até digitar uma categoria válida.
    while True:

        escolha = input("Digite a categoria: ")

        # Verifica se a categoria existe.
        if escolha in categorias:
            return escolha

        print("Categoria inválida. Tente novamente.\n")


def escolher_palavra(categoria):

    """
    Escolhe uma palavra aleatória da categoria.
    """

    # random.choice escolhe um item aleatório da lista.
    return random.choice(categorias[categoria])


def mostrar_palavra(palavra, letras_acertadas):

    """
    Mostra a palavra com as letras já acertadas.
    """

    # Variável que vai guardar a palavra formatada.
    resultado = ""

    # Percorre cada letra da palavra secreta.
    for letra in palavra:

        # Se for espaço, adiciona um espaço maior.
        if letra == " ":
            resultado += "  "

        # Se a letra já foi acertada, mostra ela.
        elif letra in letras_acertadas:
            resultado += letra + " "

        # Caso contrário, mostra "_".
        else:
            resultado += "_ "

    # Retorna a palavra formatada.
    return resultado


def jogar():

    # Escolhe a categoria do jogo.
    categoria = escolher_categoria()

    # Escolhe uma palavra aleatória da categoria.
    palavra_secreta = escolher_palavra(categoria)

    # Lista que guarda letras corretas.
    letras_acertadas = []

    # Lista que guarda todas as letras tentadas.
    letras_tentadas = []

    # Define quantidade de vidas pela dificuldade.
    vidas = escolher_dificuldade()

    # Pontuação inicial do jogador.
    pontos = 0

    # Cabeçalho do jogo.
    print()
    print("=" * 40)
    print(" (ง'̀-'́)ง JOGO DA FORCA TENSO - PYTHON")
    print("=" * 40)
    print("Categoria:", categoria)
    print("Você tem", vidas, "vidas.")
    print()

    # O jogo continua enquanto houver vidas.
    while vidas > 0:

        # Calcula qual desenho da forca será mostrado.
        indice_forca = len(forca) - vidas - 1

        # Evita índice negativo.
        if indice_forca < 0:
            indice_forca = 0

        # Evita ultrapassar o tamanho da lista.
        if indice_forca >= len(forca):
            indice_forca = len(forca) - 1

        # Segurança extra para evitar erro.
        if indice_forca < 0:
           indice_forca = 0

        # Mostra o desenho da forca.
        print(forca[indice_forca])

        # Mostra a palavra parcialmente descoberta.
        print("Palavra:", mostrar_palavra(palavra_secreta, letras_acertadas))

        # Mostra letras já tentadas.
        print("Letras tentadas:", letras_tentadas)

        # Mostra vidas restantes.
        print("Vidas:", vidas)

        # Mostra pontuação atual.
        print("Pontos:", pontos)

        print("-" * 40)

        # Pede uma letra ao jogador.
        letra = input("Digite uma letra: ").lower()

        # Validação da entrada
        # Verifica se o jogador digitou mais de uma letra.
        # Exemplo inválido: "ab"
        if len(letra) != 1:

            print("Digite apenas UMA letra.")
            print()

            # Volta para o início do loop sem continuar o restante.
            continue


        # Verifica se o caractere digitado é realmente uma letra.
        # Impede números e símbolos.
        if not letra.isalpha():

            print("Digite apenas letras.")
            print()

            # Reinicia o loop.
            continue


        # Verifica se a letra já foi tentada antes.
        if letra in letras_tentadas:

            print("Você já tentou essa letra. ¯_(ツ)_/¯")
            print()

            # Volta para o início do loop.
            continue


        # Adiciona a letra na lista de tentativas.
        letras_tentadas.append(letra)


        # Verifica se a letra existe na palavra secreta.
        if letra in palavra_secreta:

            print("Boa! A letra existe na palavra. (▀̿Ĺ̯▀̿ ̿)")

            # Guarda a letra correta.
            letras_acertadas.append(letra)

            # Adiciona pontos ao jogador.
            pontos += 10


        # Caso a letra não exista na palavra.
        else:

            print("Ops! Essa letra não está na palavra. (╯°□°）╯︵ ┻━┻")

            # Remove uma vida.
            vidas -= 1

            # Remove pontos do jogador.
            pontos -= 2


        # Apenas pula uma linha para organizar o terminal.
        print()

        # Verifica se o jogador venceu
        # Assume inicialmente que o jogador venceu.
        venceu = True


        # Percorre cada letra da palavra secreta.
        for letra_da_palavra in palavra_secreta:


            # Verifica se ainda existe alguma letra
            # que não foi descoberta pelo jogador.
            # O espaço é ignorado.
            if letra_da_palavra != " " and letra_da_palavra not in letras_acertadas:

                # Se encontrar uma letra não acertada,
                # o jogador ainda não venceu.
                venceu = False

                # Interrompe o loop imediatamente.
                break


        # Se venceu continuar como True,
        # significa que todas as letras foram descobertas.
        if venceu:

            print("=" * 40)
            print("PARABÉNS! VOCÊ VENCEU! ( ͡° ͜ʖ ͡°)")
            print("A palavra era:", palavra_secreta)
            print("Pontuação final:", pontos)
            print("=" * 40)

            # Encerra o loop principal do jogo.
            break


    # Verifica se as vidas chegaram a zero.
    if vidas == 0:

        print("=" * 40)
        print("FIM DE JOGO! (－ω－) zzZ")

        # Mostra a palavra correta ao jogador.
        print("A palavra era:", palavra_secreta)

        # Mostra a pontuação final.
        print("Pontuação final:", pontos)
        print("=" * 40)

# ============================================================
# LOOP PRINCIPAL
# ============================================================

# Loop infinito para permitir jogar várias partidas.
while True:


    # Chama a função principal do jogo.
    jogar()


    # Pergunta ao jogador se deseja jogar novamente.
    # .lower() transforma a resposta em minúscula.
    # Exemplo: "S" vira "s".
    jogar_novamente = input(
        "Deseja jogar novamente? (⊙_⊙) (s/n): "
    ).lower()


    # Verifica se a resposta é diferente de "s".
    # Se for diferente, o jogo será encerrado.
    if jogar_novamente != "s":


        # Mensagem de despedida.
        print("\nObrigado por jogar! (^▽^)")


        # Encerra o loop infinito.
        break
