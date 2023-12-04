file = open('../input.txt')
lines = file.readlines()

colors = ["red", "green", "blue"]
impossibleGameIDS = 0
impossibleGames = []
maxIDS = 5050
for line in lines:
    games = line.split("; ")
    for game in games:
        maxRed = 12
        maxGreen = 13
        maxBlue = 14
        if(":" in game):
            gameName = game.split(": ")[0]
            game = game.split(": ")[1]
        if(", " in game):
            game = game.split(", ")
        for color in colors:
            for gameColors in game:
                if(color in gameColors):
                    if(color == "red"):
                        maxRed -= int(gameColors.replace(" red", ""))
                    if(color == "green"):
                        maxGreen -= int(gameColors.replace(" green", ""))
                    if(color == "blue"):
                        maxBlue -= int(gameColors.replace(" blue", ""))
        if(maxRed < 0 or maxGreen < 0 or maxBlue < 0):
            if(gameName not in impossibleGames):
                impossibleGames.append(gameName)
                impossibleGameIDS += int(gameName.split(" ")[1])
                print(gameName.split(" ")[1])
                print(impossibleGameIDS)

print("result:", maxIDS - impossibleGameIDS)
    