from random import randint
game_running = True
game_results = []

def calculate_monster_attack():
    return randint(monster['attack_min'],monster['attack_max'])
def game_end(winner_name):
    print( f'{winner_name} has won the game')

while(game_running == True):
    counter = 0
    new_round = True
    
    player = {'name':'default','attack':13,'heal':16,'health':100}
    monster = {'name':'Monster','attack_min':10,'attack_max':20,'health':100}
    player['name'] = input('Enter your name:')

    print(player['name']+' has '+ str(player['health']) +' health')
    print(monster['name']+' has '+ str(monster['health']) +' health')
    
    while(new_round == True):
        counter = counter +1
        player_won = False
        monster_won = False

        print('-------------'*3)
        print('Select Action \n (1)Attack\n (2)Heal \n (3)Exit \n (4) Show Result')
        player_choice = input()

        if player_choice == '1':
            #attack logic
            monster['health'] = monster['health']-player['attack']
            if monster['health'] <=0:
                player_won = True
                
            else:
                player['health'] = player['health']- calculate_monster_attack()
                if player['health'] <=0:
                    monster_won = True

        

        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']

            player['health'] = player['health']- calculate_monster_attack()
            if player['health'] <=0:
                monster_won = True



        elif player_choice == '3':
            print('Exit')
            print('******************')
            new_round = False
            game_running = False
        elif player_choice =='4':
            for item in game_results:
                print(item)

        else:
            print('Invalid input')


        if (player_won == False and monster_won == False):
            print(player['name'] +' has ' +str(player['health']) +' health')
            print(monster['name'] +' has ' +str(monster['health']) +' health')
        
        elif player_won:    
            game_end(player['name'])
            round_result = {'name':player['name'],'health' :player['health'],'round':counter}
            game_results.append(round_result)
            new_round = False

        elif monster_won == True:
            game_end(monster['name'])
            round_result = {'name':player['name'],'health' :player['health'],'round':counter}
            game_results.append(round_result)
            new_round = False



