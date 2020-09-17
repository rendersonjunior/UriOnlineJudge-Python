# Grenais
"""

The Federação Gaúcha de Futebol invited you to write a program to present a statistical result of several GRENAIS. Write a program that read the number of goals scored by Inter and the number of goals scored by Gremio in a GRENAL. Write the message "Novo grenal (1-sim 2-nao)" and request a response. If the answer is 1, two new numbers must be read (another input case) asking the number of goals scored by the teams in a new departure, otherwise the program must be finished, printing:

- How many GRENAIS were part of the statistics.
- The number of victories of Inter.
- The number of victories of Gremio.
- The number of Draws.
- A message indicating the team that won the largest number of GRENAIS (or the message: "Não houve vencedor" if both team won the same quantity of GRENAIS).

Input
The input contains two integer values​​, corresponding to the goals scored by both teams. Then there is an integer (1 or 2), corresponding to the repetition of the algorithm.

Output
After each reading of the goals it must be printed the message "Novo grenal (1-sim 2-nao)". When the program is finished, the program must print the statistics as the example below.

Input Sample
3 2
1
2 3
1
3 1
2

Output Sample
Novo grenal (1-sim 2-nao)
Novo grenal (1-sim 2-nao)
Novo grenal (1-sim 2-nao)
3 grenais
Inter:2
Gremio:1
Empates:0
Inter venceu mais
"""


def main():
    vic_inter = 0
    vic_gremio = 0
    empate = 0

    while True:
        inter, gremio = input().split(' ')
        inter = int(inter)
        gremio = int(gremio)

        if inter > gremio:
            vic_inter += 1
        elif gremio > inter:
            vic_gremio += 1
        else:
            empate += 1
        print("Novo grenal (1-sim 2-nao)")
        n = int(input())
        if n == 2:
            break
    print("%d grenais" % (vic_inter + vic_gremio + empate))
    print("Inter:%d" % vic_inter)
    print("Gremio:%d" % vic_gremio)
    print("Empates:%d" % empate)
    if vic_inter > vic_gremio:
        print("Inter venceu mais")
    elif vic_gremio > vic_inter:
        print("Gremio venceu mais")
    else:
        print("Não houve vencedor")


if __name__ == "__main__":
    main()
