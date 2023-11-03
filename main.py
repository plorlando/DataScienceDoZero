# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


users = [
    {'id': 0, 'name': 'Hero'},
    {'id': 1, 'name': 'Dunn'},
    {'id': 2, 'name': 'Sue'},
    {'id': 3, 'name': 'Chi'},
    {'id': 4, 'name': 'Thor'},
    {'id': 5, 'name': 'Clive'},
    {'id': 6, 'name': 'Hicks'},
    {'id': 7, 'name': 'Devin'},
    {'id': 8, 'name': 'Kate'},
    {'id': 9, 'name': 'Klein'}
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Inicialize o dict com uma lista vazia para cada id de usuário:
friendships = {user['id']: [] for user in users}

# Em seguida, execute um loop pelos pares de amigos para preenchê-la:
for i, j in friendship_pairs:
    friendships[i].append(j) # Adicione j como amigo do usuário i
    friendships[j].append(i) # Adicione i como amigo do usuário j

print(friendships)

def number_of_friends(user):
    # Quantos amigos tem o _user_?
    user_id = user['id']
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users) # 24

num_users = len(users) # tamanho da lista de usuários
avg_connections = total_connections / num_users # 24 / 10 == 2.4

# Crie uma lista (user_id, number_of_friends).
num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]
num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)
# do maior para o menor
# Cada par é (user_id, num_friends):
# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3),
# (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]


def foaf_ids_bad(user):
    return [foaf_id for friend_id in friendships[user['id']]] 

users[0]