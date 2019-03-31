import random
CharAdventure = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': 'Shield, Bread Loaf',
    'Gold': 100,
    'Level': 2
}
CharAdventure['Gold']+= 50
CharAdventure['Backpack']+= 'FlintStone'
CharAdventure['Pocket'] = 'MonsterDex, Flashlight'

Skill1 = {
    'Name': 'Tackle',
    'Minimum level': 1,
    'Damage': 5,
    'Hit rate': 0.3, 
}


Skill2 = {
    'Name': 'Quick attack',
    'Minimum level': 2,
    'Damage': 3,
    'Hit rate': 0.5, 
}

Skill3 = {
    'Name': 'Strong Kick',
    'Minimum level': 4,
    'Damage': 9,
    'Hit rate': 0.2, 
}
SkillList = [Skill1,Skill2,Skill3]
for i in SkillList:
    print("Level",str(i['Minimum level']) + ":",i['Name'])

print("Your level now is", CharAdventure['Level'])

SkillUsed = []
for i in SkillList:
    if CharAdventure['Level'] >= i['Minimum level']:
        SkillUsed.append(i['Name'])
        print("Level",str(i['Minimum level']) + ":",i['Name'])
        
SkillInput = str(input("Enter the initial of the skill: "))
HitRate = random.randint(0,1)
for n in SkillUsed:
    hit = True
    if n[0] == SkillInput.upper():
        for i in SkillList:
            if CharAdventure['Level'] >= i['Minimum level']:
                if HitRate <= i['Hit rate']:
                    print("You hit",i['Damage'])
                    hit = True
                    break
                else: 
                    print("You missed!")
                    hit = False
                    break
    elif hit == True:
        break
    elif hit == False:
        break
    else:
        print("There are no such skills")
        break


