grudge_list_1 = {
'Abby' : ['CookieMonster', 'Zoe'],
'BigBird' :  ['Telly', 'Zoe'],
'Elmo' : ['Telly'],
'Grover' : ['Bert'],
'Telly' : ['Bert', 'BigBird', 'Elmo', 'Oscar', 'Zoe'],
'Bert' : ['Grover', 'Telly', 'Zoe'],
'CookieMonster' : ['Abby'],
'Ernie' : [],
'Oscar' : ['Telly'],
'Zoe' : ['Abby', 'Bert', 'BigBird', 'Telly']
}
grudge_list_2={
'Animal' : ['Fozzie', 'Gonzo', 'Scooter'],
'Fozzie' : ['Animal'],
'Kermit' : ['MissPiggy'],
'Rizzo' : ['Scooter'],
'Scooter' : ['Animal', 'Chef', 'Rowlf', 'Rizzo'],
'Chef' : ['Scooter'],
'Gonzo' : ['Animal', 'Rowlf'],
'MissPiggy' : ['Kermit'],
'Rowlf' : ['Gonzo', 'Scooter'],
'Walter' : []
}


def assign(grudge_list):
    van = {}  # States which van a student is assigned to. 0 means unassigned, 1 means van 1 and -1 means van 2.
    unassigned = list(grudge_list.keys())  # Get list of students in class.
    for student in unassigned:
        van[student] = 0

    # Enter your code here

    # List is empty
    unassigned = set(unassigned)
    queue_current = []
    queue_alter = []
    current_van = 1

    while unassigned:
        current_van *= -1  # Change van
        if not queue_alter:
            queue_current = [unassigned.pop()]
            print(queue_current)
        else:
            queue_current = queue_alter
            print('qcre')
            print(queue_current)
        queue_alter = []
        while queue_current:
            van[queue_current[0]] = current_van
            for grudge in grudge_list[queue_current[0]]:
                if van[grudge] == current_van:
                    print("Conflict for " + grudge)
                    return None
                if van[grudge] == 0:
                    queue_alter.append(grudge)
                    van[grudge] = current_van * -1
                    unassigned.remove(grudge)
                    # Remove first element
            queue_current = queue_current[1:]
    print(van)
    return van
#assign(grudge_list_1)

def assign2(grudge_list_1):
    import  sys

    sorted_ = sorted(grudge_list_1, key=lambda k: len(grudge_list_1[k]), reverse=True)

    van1 = list()
    van2 = list()

    for key in sorted_:
        for value in grudge_list_1[key]:
            if key in van2:
                if value in van1:
                    pass
                else:
                    van1.append(value)
                if value in van2:
                    print("Not Possible")
                    return

            elif key not in van2:
                if value in van2:
                    pass
                else:
                    van2.append(value)
                if value in van1:
                    print("Not Possible")
                    return
        if grudge_list_1[key] == []:
            if key not in van1:
                van1.append(key)
    return van1, van2
print(assign2(grudge_list_2))