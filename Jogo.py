import time
import random 

vida = 200
pont = 0
armanome = ""

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~ Olá guerreiro ~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

nom = str(input("Insira seu nick name: "))

print("Pronto guerreiro", nom, ", agora você está quase pronto")

time.sleep(2)
print("Mas antes de começar a aventura precisamos escolher o seu personagem!")

time.sleep(2)
print("Qual personagem você escolhe o 1,2,3 ou 4?")

skin = int(input("Insira aqui: "))

if skin == 1:
    armanome = "o seu chapéu"

    print("       /\\")
    print("      /  \\")
    print("   __/____\\__")
    print("     | o o |")
    print("     |  ^  |")
    print("     | --- |")
    print("      \\___/")
    print("       | |")
    print("      /| |\\")
    print("     / | | \\")
    print("       | |")
    print("      /   \\")

elif skin == 2:
    armanome = "o seu arco"

    print("      _____       /|")
    print("     | o o |     / |")
    print("     |  ^  |    /  |")
    print("     | --- |   /   |")
    print("      \\___/    \\   |")
    print("       | |      \\  |")
    print("      /| |\\      \\ |")
    print("     / | | \\      \\|")
    print("       | |")
    print("      /   \\")

elif skin == 3:
    armanome = "a sua espada"

    print("       _____")
    print("      | o o |            /\\")
    print("      |  ^  |            ||")
    print("      | --- |            ||")
    print("       \\___/             ||")
    print("         |               ||")
    print("        /|\\           ===[]===")
    print("       / | \\             ||")
    print("         |               ||")
    print("        / \\              []")
    print("       /   \\")

elif skin == 4:
    armanome = "o seu capacete"

    print("        _______")
    print("       /  _|_  \\")
    print("      /____|____\\")
    print("      | | o o | |")
    print("      | |  ^  | |")
    print("       \\| --- |/")
    print("        |_____|")
    print("          | |")
    print("         /| |\\")
    print("        / | | \\")
    print("          | |")
    print("         /   \\")
    print("        /     \\")

time.sleep(1)
print("Pronto agora com o pesonagem escolhidos, a sua primeira missão é sair da cadeia")

time.sleep(4)
print("Para isso Você vai ter que ganhar de um prisoneiro em uma aposta.")

time.sleep(4)
print("Ele apostou que o número que vai ser sortiado um número par, e sobrou os número ímpares para você")

time.sleep(4)
print("Então vai la, o número ta sendo sortiado é...")

time.sleep(2)
print("...")


time.sleep(1)
num1sort = random.randint(1,50)
print("\nO número sortiado é", num1sort)

if num1sort % 2 == 0:
    
    time.sleep(2)
    print("O número sortiado é par, infelizmente como você não tinha uma moeda de troca então apostou a sua alma.")
    
    time.sleep(1)
    print("  GAME  ")
    print("  OVER  ")

    time.sleep(0.5)
    print("~~~~~~~~~~~~~~~~~~~~~")
    print("Seu desempenho foi de")
    print("~~~~~",pont,"pontos ~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~")
    exit()

else:    
    time.sleep(2)
    print("Uau Você ganhou dele, mesmo a sua probabilidade sendo de 50%")
    pont += 10

time.sleep(2)
print("Agora você vai ter que sair da ilha de onde você está")

time.sleep(2)
print("Você tem 2 opções, 1° fazer uma balsa com as madeiras da costa ou")

time.sleep(2)
print("ou 2° ir nadando até a costa")

esco = int(input("Qual você escolheu 1 para 1° ou 2 para 2°: "))

if esco == 1:
    pont += 15

    time.sleep(0.5)
    print("Boa escolha, agora você tem que ser rapido antes que seja pego, boa sorte!!")

    time.sleep(2)
    print("Você monta a balsa e quase é pego mas foi por pouco!")

else:
    pont -= 3

    time.sleep(2)
    print("Que escolha ruim e boa, você vai ter que nadar um oceano inteiro, sem comida e água")
    
time.sleep(2)
print("No meio do oceano você é surpreendido com uma onda enorme, ela leva você muito longe")

time.sleep(2)
print("Agora você está boiando no meio do oceano e a vista um navio pirata")

time.sleep(2)
print("Você grita por ajuda e eles escutam, e te tiram do oceano, mas agora você tem uma ecolha a fazer.")

time.sleep(2)

print("1- Derrotar todos do navio e verejar sozinho ")
print("2- Ser amigavel com todos e ir com eles até a costa")

esc2 = int(input("Qual vai ser?: "))

if esc2 == 2:
    pont += 7

    print("Boa escolha, agora você festeja com eles, mas não se esqueça NUNCA CONTE SEU PASSADO PARA ELES!")

    time.sleep(2)
    print("Agora que você fez algumas amizades, eles te levam até a costa")

    time.sleep(2)
    print("Parabéns você fez uma aliança :) ")

else:
    pont -= 1
    print("Que escolha cruel, mas você ainda tem que derrotar o BOSS")

    time.sleep(2)
    print("Ele sai do quarto dele, pronto pra te massacrar, o que você faz?")
    print("1- Se esconde no navio e espera ele ficar de costas e finalizar ele.")
    print("2- Chamar ele para um duelo mano a mano.")

    esc3 = int(input("Insira aqui: "))

    if esc3 == 1:

        print("Você morreu, esqueceu que ele é um BOSS, e não um qualquer.")

        
        time.sleep(1)
        print("  GAME  ")
        print("  OVER  ")

        time.sleep(0.5)
        print("~~~~~~~~~~~~~~~~~~~~~")
        print("Seu desempenho foi de")
        print("~~~~~",pont,"pontos ~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~")
        exit()

    else:
        print("Ele aceita o seu desafio e ja vai com tudo pra cima de você")

        time.sleep(2)
        print("Você esquiva mas ele te acerta um golpe no seu braço, machucando muito você")
        print("VIDA = 170[/////////////////   ]200")
        vida -= 30

        time.sleep(2)
        print("Você vê ele de costa totalmente vunerável")
        
        time.sleep(2)
        print("O que você faz?")

        time.sleep(1)
        print("1- Pega uma estaca que está no chão e enfia ela nas costas dele")
        print("2- Corre com tudo e da um soco no rosto dele")
        print("3- Nada e espera ele olhar para frente de novo")

        esc4 = int(input("Insira aqui: "))

        if esc4 == 1:
            print("Boa escolha, causou um bom dano nele!")
            print("VIDA BOSS = 250[/////////////////////////     ]300")
            pont += 5

            time.sleep(2)
            print("Agora ele está muito furioso e sangrando muito, ele tenta te atacar")
            
            time.sleep(2)
            print("Só que você desvia dele, e enfia a estaca muito mais fundo quase acertanto um orgão dele")
            print("VIDA BOSS = 210[/////////////////////         ]300")
            pont += 3

            time.sleep(2)
            print("Ele está muito fraco a estaca foi um golpe preciso, ele se ajoelha")

            time.sleep(2)
            print("E você percebe que agora é a hora de atacar, com", armanome,", você ataca ele")

            time.sleep(2)
            print("Causando muito dano nele, ele tem muita vida ainda, mas está fraco")
            print("VIDA BOSS = 180[//////////////////            ]300")
            pont += 4

            time.sleep(2)
            print("Só que tem um problema ele consegue tirar a estaca e solta uma mágia que faz ele ficar muito forte")
            
            time.sleep(2)
            print("Você convicto que já estava ganho a batalha nem percebeu o que ele tiha feito")

            time.sleep(2)
            print("E ele vai com tudo pra cima de você, ele pega a espada dele e corta o seu braço.")

            time.sleep(2)
            print("VIDA = 110[///////////         ]200")
            vida -= 60

            time.sleep(2)
            print("Você também está machucado agora, mas com o feitiço dele ele fica muito forte")

            time.sleep(2)
            print("E começa uma rajada de ataques, por todos os lado, você cansa mais por um milagre")

            time.sleep(2)
            print("Não sofre nenhum dano, ele também cansou e está mais lento")

            time.sleep(2)
            print("Então você se depara com um dos canhões do navio do seu lado e tem uma ideia")

            time.sleep(2)
            print("Com ele cansado você pega o canhão e ")

            print("1- Atira com tudo nele")
            print("2- Acerta um palanque com ele")

            esc5 = int(input("Insira aqui: "))

            if esc5 == 1:
                print("Boa escolha, você causou muito dano nele")
                print("VIDA BOSS = 80[////////                      ]300")
                pont += 15

                time.sleep(2)
                print("Ele ficou noucauteado, agora você tem que finalizar ele")

                time.sleep(2)
                print("Você pega", armanome,"e com um único golpe na cabeça você executa ele")
                pont += 20

                time.sleep(2)
                print("Como um premio você ganha a habilidade pirata, você cosegue controlar os oceanos.")

            else:
                print("Por que? sinceramente por que?")

                time.sleep(2)
                print("Ele foi lá e te deu um soco, tão forte que você morreu na hora.")

                time.sleep(1)
                print("  GAME  ")
                print("  OVER  ")

                time.sleep(0.5)
                print("~~~~~~~~~~~~~~~~~~~~~")
                print("Seu desempenho foi de")
                print("~~~~~",pont,"pontos ~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~")
                exit()




        elif esc4 == 2:
            print("Boa iniciativa mas ele é um BOSS, ele é muito forte, nem causou dano nele.")

            time.sleep(3)
            print("Ele ficou irritado, e invocou uma magia, o que você faz?")

            time.sleep(3)
            print("1- Desvia da magia e contra ataca com", armanome)
            print("2- Apenas desista e sai do jogo")
            

            



time.sleep(2)
print("Agora com você na costa você entra na selva")