import re

def main():
    with open('input2.txt', 'r') as f:
        sum = 0
        for linea in f.read().splitlines():
            game, *sets = re.split(r'[:;]', linea)
            game_id = game.split()[1]
            cubes_lim = {'red':12, 'green':13, 'blue':14}
            isCorrect = True
            set_dic = {}

            for set_ in sets:
                if isCorrect:
                    cubes = re.split(r'[, ]', str(set_))
                    cubes = list(filter(None, cubes))
                    i = 1

                    while i < len(cubes):
                        color = cubes[i]
                        reps = cubes[i-1]
                        if color not in set_dic:
                            set_dic[color] = int(reps)
                        if set_dic[color] < int(reps):
                            set_dic[color] = int(reps)
                        i += 2

                    for color, reps in set_dic.items():
                        if set_dic[color] > cubes_lim[color]:
                            isCorrect = False
                            break

            if isCorrect:
                sum += int(game_id)

    print(sum)
                    





if __name__=='__main__':
    main()