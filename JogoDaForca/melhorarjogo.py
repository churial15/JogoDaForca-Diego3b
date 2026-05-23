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
    ],

    "Bandas": [
        "gorillaz",
        "imagine dragons",
        "led zeppelin",
        "linkin park",
        "twenty one pilots"
    ],

    "Jogos": [
        "resident evil",
        "silent hill",
        "outlast",
        "the last of us",
        "minecraft",
        "red dead redemption",
        "cyberpunk",
        "the witcher",
        "god of war",
        "hollow knight",
        "dead space",
        "alan wake",
        "amnesia",
        "subnautica",
        "terraria",
        "portal",
        "half life",
        "doom eternal",
        "dark souls",
        "devil may cry",
        "super mario world",
        "cuphead",
        "poppy playtime",
        "lethal company",
        "crash bandicoot",
        "biohazard",
        "granny",
        "alien isolation"
    ],

    "Tecnologia": [
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
        "xml"
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
    print("         ESCOLHA A DIFICULDADE")
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
    print("        ESCOLHA UMA CATEGORIA BRABA")
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
    vidas = 6
    pontos = 0

    print()
    print("=" * 40)
    print("       (ง'̀-'́)ง JOGO DA FORCA TENSO - PYTHON")
    print("=" * 40)
    print("Categoria:", categoria)
    print("Você tem", vidas, "vidas.")
    print()

    while vidas > 0:
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

# Início do programa
jogar()
