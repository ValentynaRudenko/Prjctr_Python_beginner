# create a list of cats - "cats" 1-100
# "cat" means cat without hat, "hat" - cat with hat
# create a loop for "putting on a hat"
#   set range 100
#   create outer loop for going througth the list number of times == rounds
#   create inner loop for iteration by element
#       set increment == to round (round = 1, increment = 1)
#       read through the list by increment
#       check elements:
#           if element == "cat" -> change it to "hat"
#           if element == "hat" -> change it to "cat"

# get the indexes of "hat"
     

def cat_hat():
    # create a list of cats - "cats" 1-100
    n = 100
    cats = ["cat"] * n
    
    # create a loop for "putting on a hat"
    # create outer loop for going througth the list number of times == rounds
    round = 1
    for rounds in range(1, 100):
        # create inner loop for iteration by element
        for i in range(1, 100, round):
            if cats[i] == "cat":
                cats[i] = "hat"
            else:
                cats[i] = "cat"
        round += 1
    print(cats)
    # get the indexes of "hat"
    hat_indexes = [i for i, element in enumerate(cats) if element == "hat"]
    print(hat_indexes)
    return hat_indexes


cat_hat()

#the complexity of the algorithm is O(n^2)