file = open('../input.txt')
lines = file.readlines()

colors = ["red", "green", "blue"]

globalSum = 0
for line in lines:
    games = line.split("; ")
    minRed = 0
    minGreen = 0
    minBlue = 0
    for game in games:
        if(":" in game):
            gameName = game.split(": ")[0]
            game = [game.split(": ")[1]][0].split(", ")
        if(", " in game):
            game = game.split(", ")
        if(type(game) == str):
            game = [game]
        for color in colors:
            for gameColors in game:
                if(color in gameColors):
                    if(color == "red"):
                        numberOfRed = int(gameColors.replace(" red", ""))
                        if(numberOfRed > minRed):
                            minRed = numberOfRed
                    if(color == "green"):
                        numberOfGreen = int(gameColors.replace(" green", ""))
                        if(numberOfGreen > minGreen):
                            minGreen = numberOfGreen
                    if(color == "blue"):
                        numberOfBlue = int(gameColors.replace(" blue", ""))
                        if(numberOfBlue > minBlue):
                            minBlue = numberOfBlue
    gamePower = minRed * minGreen * minBlue
    print(gameName, "red:",minRed, "green:", minGreen,"blue:", minBlue, "power:",gamePower)
    globalSum += gamePower
    # print(gamePower)
    print(gameName, globalSum)