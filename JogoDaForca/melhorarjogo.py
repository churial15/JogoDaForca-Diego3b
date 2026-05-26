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

    os.system("cls" if os.name == "nt" else "clear")


def remover_acentos(texto):

    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )


def escolher_dificuldade():

    print("=" * 40)
    print("      ESCOLHA A DIFICULDADE ATACADA:")
    print("=" * 40)

    print("1 - Fácil   (8 vidas)")
    print("2 - Médio   (6 vidas)")
    print("3 - Difícil (4 vidas)")
    print("4 - Extremo (2 vidas)")
    print()

    while True:

        escolha = input("Digite a dificuldade: ")

        if escolha == "1":
            return 8

        elif escolha == "2":
            return 6

        elif escolha == "3":
            return 4

        elif escolha == "4":
            return 2

        else:
            print("Opção inválida.\n")

def escolher_categoria():

    print("=" * 40)
    print("        ESCOLHA UMA CATEGORIA BRABA:")
    print("=" * 40)

    for categoria in categorias:
        print("-", categoria)

    print()

    while True:

        escolha = input("Digite a categoria: ")

        if escolha in categorias:
            return escolha

        print("Categoria inválida. Tente novamente.\n")

def escolher_palavra(categoria):
    """Escolhe uma palavra aleatória da categoria."""
    return random.choice(categorias[categoria])

def mostrar_palavra(palavra, letras_acertadas):
    """Mostra a palavra com as letras já acertadas."""

    resultado = ""

    for letra in palavra:

        if letra == " ":
            resultado += "  "

        elif letra in letras_acertadas:
            resultado += letra + " "

        else:
            resultado += "_ "

    return resultado

def jogar():
    categoria = escolher_categoria()
    palavra_secreta = escolher_palavra(categoria)
    letras_acertadas = []
    letras_tentadas = []
    vidas = escolher_dificuldade()
    pontos = 0

    print()
    print("=" * 40)
    print(" (ง'̀-'́)ง JOGO DA FORCA TENSO - PYTHON")
    print("=" * 40)
    print("Categoria:", categoria)
    print("Você tem", vidas, "vidas.")
    print()

    while vidas > 0:
        indice_forca = len(forca) - vidas - 1

        if indice_forca < 0:
            indice_forca = 0

        if indice_forca >= len(forca):
            indice_forca = len(forca) - 1
        if indice_forca < 0:
           indice_forca = 0
        print(forca[indice_forca])

        print("Palavra:", mostrar_palavra(palavra_secreta, letras_acertadas))
        print("Letras tentadas:", letras_tentadas)
        print("Vidas:", vidas)
        print("Pontos:", pontos)
        print("-" * 40)
        letra = input("Digite uma letra: ").lower()

        # Validação da entrada
        if len(letra) != 1:
            print("Digite apenas UMA letra.")
            print()
            continue

        if not letra.isalpha():
            print("Digite apenas letras.")
            print()
            continue

        if letra in letras_tentadas:
            print("Você já tentou essa letra. ¯_(ツ)_/¯")
            print()
            continue

        letras_tentadas.append(letra)

        if letra in palavra_secreta:
            print("Boa! A letra existe na palavra. (▀̿Ĺ̯▀̿ ̿)")
            letras_acertadas.append(letra)
            pontos += 10
        else:
            print("Ops! Essa letra não está na palavra. (╯°□°）╯︵ ┻━┻")
            vidas -= 1
            pontos -= 2

        print()

        # Verifica se o jogador venceu
        venceu = True

        for letra_da_palavra in palavra_secreta:

            if letra_da_palavra != " " and letra_da_palavra not in letras_acertadas:
                venceu = False
                break

        if venceu:
            print("=" * 40)
            print("PARABÉNS! VOCÊ VENCEU! ( ͡° ͜ʖ ͡°)")
            print("A palavra era:", palavra_secreta)
            print("Pontuação final:", pontos)
            print("=" * 40)
            break

    if vidas == 0:
        print("=" * 40)
        print("FIM DE JOGO! (－ω－) zzZ")
        print("A palavra era:", palavra_secreta)
        print("Pontuação final:", pontos)
        print("=" * 40)

# ============================================================
# LOOP PRINCIPAL
# ============================================================

while True:

    jogar()

    jogar_novamente = input(
        "Deseja jogar novamente? (⊙_⊙) (s/n): "
    ).lower()

    if jogar_novamente != "s":

        print("\nObrigado por jogar! (^▽^)")

        break
