dark = 0
pub = 100
pp = 0
increase = 0
variable = '. Your hp increased by 100, SKELETOn HP: '
var = '. Your hp increased by 100, DRAGOR HP: '
player = input('Enter Your Name: ')
points = 0
Player = 100
Boss1 = 101
Boss2 = 205
Boss3 = 700
FinalBoss = 1000
Powers = {
    'Fire' : 'Fire Ball',
    'Water': 'Hydro Blast',
    'Grass': 'Nature Beam',
    'Mystic': 'Mythical Power',
    'Evil': 'Dark Pulse',
    'Legendary': 'Collapsing Star Fire'
}

print('The tree Demon Appeared ! TREE DEMON HP: 101 \n')
while Boss1 > 0 and Player > 0:
    x = input('Enter Fire Ball, Hydro Blast, or Nature Beam to Defeat it!: ')
    if x == Powers['Fire']:

        Boss1 = Boss1 - 40
        print('\n'+ player + ' used ' + Powers['Fire'] +  ', it is Super Effective! Tree Demon Lost 40 hp. TREE DEMON HP: ' + str(Boss1) + '\n')
    elif x == Powers['Water']:
        Boss1 += 40
        print('\n' + player + ' used ' + Powers['Water'] +
        ', it was ineffective, Tree Monster Regained 40 hp. TREE DEMON HP: ' + str(Boss1) + '\n')
    elif x == Powers['Grass']:
        Boss1 = Boss1 - 10
        print('\n' + player + ' used ' + Powers['Grass'] +  ', it was weak, Tree Monster lost 10 hp. TREE DEMON HP: ' + str(Boss1) + '\n')
    else:
        print('Invalid Attack Spell! ' + ' TREE DEMON HP: ' + str(Boss1) + '\n')
        Player = Player + 30

    Player = Player - 30
    print('Tree Demon Attacks, ' + player + ' loses 30 hp!' + player + ' Hp: ' + str(Player) + '\n')

if Player <= 0:
    print('Game Over')

else:
    Player = 100
    print('Your Hp is restored!' + player + ' HP: 100 \n')
    print('TreeBeard is defeated, but wait, here comes another monster, AquaLord!')
    print('Aqua Lord HP: ' + str(Boss2) + '\n')

while Boss2 > 0 and Player > 0:
    x = input('Enter Fire Ball, Hydro Blast, Nature Beam or Dark Pulse to Defeat it!: ')
    if x == Powers['Fire']:
        Boss2 = Boss2 - 20
        print("\n" + player + ' used ' + Powers[
            'Fire'] + ', it is Not Very Effective! AquaLord Lost 20 hp. AQUALORD HP: ' + str(Boss2) + '\n')
    elif x == Powers['Grass']:
        Boss2 = Boss2 - 60
        print(player + ' used ' + Powers[
            'Grass'] + ', it was Super Effective, AquaLord lost 60 hp. AquaLord HP: ' + str(Boss2) + ' \n')
    elif x == Powers['Water']:
        Boss2 = Boss2 - 25
        print(player + ' used ' + Powers['Water'] + ', it was weak, AquaLord lost 25 hp. AQUALORD HP: ' + str(
            Boss2) + '\n')
    elif x == Powers['Evil']:
        Boss2 = Boss2 - 130
        Player = Player - 9
        dark = dark + 1
        print(player + ' used ' + Powers['Evil'] + ', AquaLord lost 130 hp. AQUALORD HP: ' + str(Boss2) + '\n')
        print(player + ' lost 9 hp. ' + player + ' HP: ' + str(Player) + '\n')
    else:
        print('Invalid Attack Spell! AQUALORD HP: ' + str(Boss2) + '\n')
        Player = Player + 40

    Player = Player - 40
    print('AquaLord summons a wave, ' + player + ' loses 40 hp! ' + player + ' HP: ' + str(Player) + '\n')

if Player <= 0 and Boss2 <= 0:
    Player = 100
    print('Your Hp is restored!' + player + ' HP: 100\n')
    print('AquaLord is defeated, but wait, here comes another monster, Dragor The Evil Dragon!')
    print('Dragor: ' + str(Boss3) + '\n')

elif Player > 0:
    Player = 100
    print('Your Hp is restored!' + player + ' HP: 100\n')
    print('AquaLord is defeated, but wait, here comes another monster, Dragor The Evil Dragon!')
    print('Dragor: ' + str(Boss3) + '\n')

else:
    print('Game Over' + '\n')

while Boss3 > 0 and Player > 0:
    x = input('Enter Fire Ball, Hydro Blast, Nature Beam, Mythical Power or Dark Pulse to Defeat it!: ')
    if x == Powers['Fire']:
        Boss3 = Boss3 - 1
        print(player + ' used ' + Powers['Fire'] + ' it was weak against Dragor, Dragor lost 1 hp. DRAGOR HP: ' + str(Boss3) + '\n' )
    elif x == Powers['Water']:
        Boss3 = Boss3 - 340
        print(player + ' used ' + Powers['Water'] + ' it was Super Powerful against Dragor, Dragor lost 350 hp. DRAGOR HP: ' + str(
            Boss3) + '\n')
    elif x == Powers['Mystic']:
        if points == 3:
            var = ' Your hp did not increase, out of Mystical Power! DRAGOR HP: '
            pub = 0
            print(player + ' used ' + Powers['Mystic'] + var + str(Boss3) + '\n')
        else:
            Player = Player + pub
            points = points + 1
            print(player + ' used ' + Powers['Mystic'] + var + str(Boss3) + '\n')

    elif x == Powers['Evil']:
        Boss3 = Boss3 - 200
        Player = Player - 10
        dark = dark + 1
        print(player + ' used ' + Powers['Evil'] + '. Your hp Decreased by 10, Dragor lost 200 Hp! DRAGOR HP: ' + str(Boss3) + '\n')
    elif x == Powers['Grass']:
        Boss3 = Boss3 - 0.5
        print(player + ' used ' + Powers['Grass'] + ' It was weak, Dragor lost 0.5 Hp. DRAGOR HP: ' + str(Boss3) + '\n')

    else:
        print('Invalid Attack Spell! DRAGOR HP: ' + str(Boss3) + '\n')
        Player = Player + 50

    Player = Player - 50
    print('Dragor Shot Flames, ' + player + ' loses 50 hp! ' + player + ' HP: ' + str(Player) + '\n')


if Player <= 0 and Boss3 <= 0:
    Player = 100
    print('Your Hp is restored!' + player + ' HP: 100\n')
    print('Dragor is defeated, but wait, here comes the Final Demon, Skeleton, The DeathBringer!')
    print('SKELETON HP: ' + str(FinalBoss) + '\n')

elif Player > 0:
    Player = 100
    print('Your Hp is restored!' + player + ' HP: 100\n')
    print('Dragor is defeated, but wait, here comes the Final Demon, Skeleton, The DeathBringer!')
    print('SKELETON HP: ' + str(FinalBoss) + '\n')

else:
    print('Game Over' + '\n')


while FinalBoss > 0 and Player > 0:
    x = input('Enter Fire Ball, Hydro Blast, Nature Beam, Mythical Power, Dark Pulse or Collapsing Star Fire  to Defeat it!: ')
    if x == Powers['Fire']:
        FinalBoss = FinalBoss - 0
        print('\n' + player + ' used ' + Powers['Fire'] + ' it did nothing to Skeleton. SKELETON HP: ' + str(FinalBoss) + '\n' )
    elif x == Powers['Water']:
        FinalBoss = FinalBoss - 0.0
        print(player + ' used ' + Powers['Water'] + ' it did 0 damage, Skeleton HP: ' + str(
            FinalBoss) + '\n')
    elif x == Powers['Grass']:
        FinalBoss = FinalBoss - 0.0
        print(player + ' used ' + Powers['Grass'] + ' it did 0 damage, Skeleton HP: ' + str(
            FinalBoss) + '\n')
    elif x == Powers['Evil']:
        dark = dark + 2
        FinalBoss += 100
        Player = Player - 10
        print(player + ' used ' + Powers['Evil'] + ' Skeleton\'s Hp Increased by 100! Skeleton HP: ' + str(FinalBoss) + '\n')
        print(player + ' lost 10 hp. ' + player + ' HP: ' + str(Player) )
    elif x == Powers['Legendary']:
        FinalBoss -= 999
        print(player + ' used ' + Powers['Legendary'] + ' Skeleton took 999 Damage! Skeleton HP: ' + str(FinalBoss) + '\n')
    elif x == Powers['Mystic']:
        if pp == 2:
            Player = Player + 0
            print(player + ' used ' + Powers['Mystic'] + ' There is no more power to use this move! Skeleton HP: ' + str(
                FinalBoss) + '\n')
        else:
            pp = pp + 1
            Player = Player + 101
            print(player + ' used ' + Powers['Mystic'] + player + ' Hp increased by 100! Skeleton HP: ' + str(
                    FinalBoss) + '\n')
    else:
        print('Invalid Attack Spell! SKELETON HP: ' + str(FinalBoss) + '\n')
        Player = Player + 90

    Player = Player - 100
    print('Skeleton Brought Down Upon you The DeathReaper!, ' + player + ' loses 100 hp! ' + player + ' HP: ' + str(Player) + '\n')


if Player <= 0 and FinalBoss <= 0 and dark >= 3:
    Player = 100
    print('Your Hp is restored!' + player + ' HP: 100\n')
    print('SKELETON is defeated, and the Dark Demons are gone. However, your usage of darkness has darkened you and you slowly descend into madness...')
    print('\n LOST TO INSANITY ENDING...')
elif Player > 0 and dark >= 3:
    Player = 100
    print('Your Hp is restored!' + player + ' HP: 100\n')
    print('SKELETON is defeated, and the Dark Demons are gone. However, your usage of darkness has darkened you and you slowly descend into madness...')
    print('\n LOST TO INSANITY ENDING...')


elif Player <= 0 and FinalBoss <= 0:
    Player = 100
    print('Your Hp is restored!' + player + ' HP: 100\n')
    print('SKELETON is defeated, with the Dark Demons gone, the world is once more at peace and it is all thanks To you!')
    print('\n THE WORLD IS IN PEACE ENDING')

elif Player > 0:
    Player = 100
    print('Your Hp is restored!' + player + ' HP: 100\n')
    print('SKELETON is defeated, with the Dark Demons gone, the world is once more at peace and it is all thanks To you!')
    print('\n THE WORLD IS IN PEACE ENDING')

else:
    print('Game Over' + '\n')