from random import randint

def roll_dice():
    dice = []
    for i in range(5):
        dice.append(randint(1,6))
    return dice

def reroll_dice():
    dice = roll_dice()
    print(dice)
    for k in range(3):
      a = input("Do you want to change the dice (Enter yes/no): ")
      if(a == 'yes'):
        x = int(input("Enter the number of dice: "))
        for i in range(x):
          z=int(input("Enter the number: "))
          a = dice.index(z)
          dice[a] = randint(1,6)
        print(dice)
      else:
        break
    return dice

def get_score(dice, category):
    dice.sort()
    if category == "ones":
      return dice.count(1)
    elif category== "twos":
        return dice.count(2)*2
    elif category == "threes":
        return dice.count(3)*3
    elif category == "fours":
        return dice.count(4)*4
    elif category == "fives":
        return dice.count(5)*5
    elif category == "sixes":
        return dice.count(6)*6
    elif category == "chance":
        return sum(dice)
    elif category == "yahtzee":
      if len(set(dice)) == 1:
        return 50
      else:
        return 0
    elif category == "small straight":
      if dice == [1,2,3,4,5]:
        return 30
      return 0
    elif category == "large straight": 
      if dice == [2,3,4,5,6]:
        return 40 
      return 0
    elif category == "full house":
      if((dice[0] == dice[1]) and (dice[2] == dice[4])) or ((dice[0] == dice[2])  and (dice[3] == dice[4])):
        return 25
      return 0
    elif category == "three of a kind":
      if(dice[0] == dice[2]) or (dice[1] == dice[3]) or (dice[2]==dice[4]):
        return sum(dice)
      else: 
        return 0
    elif category == "four of a kind":
      if (dice[0]==dice[3]) or dice[1] == dice[4]:
        return sum(dice)
      else: 
        return 0
    else:
        return 0

def play_yahtzee():
    scores = {}
    count = 0
    print("Categories are:\nUPPERSECTION:\n Ones:\n Twos:\n Threes:\n Fours:\n Fives:\n Sixes:\nLOWERSECTION:\n Three of a kind:\n Four of a kind:\n Small straight:\n Large straight:\n Yahtzee:\n Chance:\n Full House:\n")
    categories = [ "ones", "twos", "threes", "fours", "fives", "sixes" , "chance" , "yahtzee" , "large straight" , "small straight" , "full house" , "three of a kind" , "four of a kind"]

    for category in categories:
      scores[category] = 0
    
    for i in range(13):
        print("Round", i+1)
        dice = reroll_dice()

        category = input("Enter your choice (please use all lowercase): ")

        while category not in categories:
          print("Invalid Category/ Already Filled")
          category = input("Enter your choice:\n ")
        
        if scores[category] != 0:
          if category == "yahtzee" and len(set(dice)) == 1:
            count=count+1
          else:
            print("Category already filled")
            
        score = get_score(dice,category)
        scores[category] = score
        print("Scored  points",score ," in category ", category)
        print("Current Scores:")
        list1 = ["ones", "twos", "threes", "fours", "fives", "sixes"]
        points_in_upper = []
  
        for i in list1:
          print(i, ":",scores[i])
          points_in_upper.append(scores[i])
        x = sum(points_in_upper)
        
  
        if x>=63:
          print("UPPER SECTION SCORE: ", x)
          bonus = 35
          print("BONUS :", bonus)
          x1 = x+bonus
          print("UPPER SECTION TOTAL: ",x1 )
        else:
          print("UPPER SECION SCORE: " ,x)
          bonus = 0
          print("BONUS :", bonus)
          x1 = x+bonus
          print("UPPER SECTION TOTAL: ", x1)
        list2 = ["chance", "yahtzee","small straight", "large straight", "full house", "three of a kind", "four of a kind"]
        points_in_lower = []
        for m in list2:
          print(m,":",scores[m])
          points_in_lower.append(scores[m])
          y = sum(points_in_lower)
          y1=y+100*count
        print("LOWER SECTION SCORE: ", y)
        print("YAHTZEE BONUS: ",100*count)
        print("LOWER SECTION TOTAL: ", y+100*count)
        if x>=63:
          total = sum(scores.values())+35+ 100*count
        else: 
          total = sum(scores.values())+100*count
        print("THE GRAND TOTAL: ", total)
  

play_yahtzee()