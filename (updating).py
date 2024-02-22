# An example player agent for the Play Nine Solitaire project. This version doesn't
# make any decisions on its own, but asks the human to provide the decisions via
# console input.


# The three functions to implement begin here:
# --------------------------------------------

# Returns a tuple of two strings, the name and the student ID of the author.

def get_author_info():
    return "student name", "123456789"


# Choose the drawing action for the current draw. The return value of this function
# must be either string "k" or "d" for taking the known card from the kitty and for
# drawing a random card from the deck, respectively.

def choose_drawing_action(top_concealed, bottom_concealed, draws_left, kitty_card):
    action = "X"
    if kitty_card == -5 or 0 :
        action = "K"
    else :
        for i in range(len(top_concealed)-1):
            if kitty_card == top_concealed[i] :
                if kitty_card != bottom_concealed[i] :
                    action = "K"
                    break
            elif kitty_card == bottom_concealed[i] :
                if kitty_card != top_concealed[i] :
                    action = "K"
                    break
    if action != "k" :
        if kitty_card <= 5 :
            for j in range(len(top_concealed)-1):
                if top_concealed[j] != bottom_concealed[j] :
                    if top_concealed[j] != "*" :
                        if kitty_card < top_concealed[j] :
                            action = "k"
                            break
                    if bottom_concealed[j] != "*" :
                        if kitty_card < bottom_concealed[j] :
                            action = "k"
                            break   

    if action != "k" :
        action = "d"
    
    return action


# Choose the replacement action for the current card. The return value of this function
# must be a triple of the form (action, row, column) where
# - action is one of the characters "rRtT", "r" for replace and "t" for turn over
# - row is the row number of the card subject to chosen action
# - column is the column number of the card subject to chosen action

def choose_replacement_action(top_concealed, bottom_concealed, draws_left, current_card):
    action = "X"
    row = "r"
    column = "c"
    a=[]
    if current_card == -5 or current_card == 0 :
        action = "r"
    else :
        for i in range (len(top_concealed)-1) :
            if current_card == top_concealed[i] :
                if current_card != bottom_concealed[i] :
                    action = "r"
                    a.append(i)
                    row = 1
                    break
            elif current_card == bottom_concealed[i] :
                if current_card != top_concealed[i] :
                    action = "r"
                    a.append(i)
                    row = 0
                    break

        if action != "r" :
            for j in range (len(top_concealed)-1) : 
                if top_concealed[j] != "*" :
                    if current_card < top_concealed[j] :
                        action = "r"
                        a.append(i)
                        row = 0
                        break
                if bottom_concealed[j] != "*" :
                    if current_card < bottom_concealed[j] :
                        action = "r"
                        a.append(i)
                        row = 1
                        break

        if action != "r" :
            action = "t"

    if action == "r" :
        if current_card != -5 or current_card != 0 :
            column = a[0]
        else :
            for k in range(len(top_concealed)-1) :
                if top_concealed[k] != bottom_concealed[k] :
                    if top_concealed[k] == -5 or top_concealed[k] == 0 :
                        row = 1
                        column = k
                        break
                    if bottom_concealed[k] == -5 or bottom_concealed[k] == 0 :
                        row = 0
                        column = k
                        break
            if row == "r" and column == "c" :
                for l in range(len(top_concealed)-1) :
                    if top_concealed[l] != bottom_concealed[l] :
                        if top_concealed[l] != "*" :
                            if current_card < top_concealed[l] :
                                row = 0
                                column = l
                                break
                        if bottom_concealed[l] != "*" :
                            if current_card < bottom_concealed[l] :
                                row = 1
                                column = l
                                break 
            if row == "r" and column == "c" :    
                for o in range(len(top_concealed)-1) :
                    if top_concealed[o] == "*" and bottom_concealed[o] == "*" :
                        row = 0 
                        column = o 
    if action == "t" :
        for p in range(len(top_concealed)-1) :
            if top_concealed[p] == "*" and bottom_concealed[p] == "*" :
                row = 0
                column = p
                break
        if row == "r" and column == "c" :
                for m in range(len(top_concealed)-1) :
                    if top_concealed[m] != bottom_concealed[m] :
                        if top_concealed[m] == "*" :
                            row = 0
                            column = m
                            break
        if row == "r" and column == "c" :
                for n in range(len(top_concealed)-1) :
                    if top_concealed[n] != bottom_concealed[n] :                
                        if bottom_concealed[n] == "*" :
                            row = 1
                            column = n 
                            break

    action_verb = "replace" if action in "rR" else "turn over"
    row = int(input(f"Enter row number of card to {action_verb}: "))
    column = int(input(f"Enter column number of card to {action_verb}: "))

    return action, row, column
