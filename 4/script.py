with open('input.txt') as f:
    lines=f.readlines()

    class Card:
        def __init__(self,number,copies,points):
            self.num=number
            self.copies=copies
            self.points=points

    # Populate cards        
    cards={}
    for l in lines:
        cnum,clean=l.split(':')
        cnum=int(cnum.split()[-1])
        winners,mine=clean.split('|')
        # Convert to set in case of repeats
        winners=set(winners.split()) 
        matching=0
        for n in winners:
            if n in mine.split():
                matching+=1
        cards[cnum]=Card(cnum,1,matching)
    print(len(cards.keys()))

    ### Part 1
    pt1=0
    for c in cards.keys():
        pt1+=int(2**(cards[c].points-1))
    print(pt1)

    ### Part 2
    pt2=0
    for c in cards.keys():
        for i in range(cards[c].copies):
            for j in range(1,cards[c].points+1):
                cards[c+j].copies+=1
        pt2+=cards[c].copies
    print(pt2)