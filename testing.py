if action != "r" :
    for j in range (len(top_concealed)) : 
        if top_concealed[j] != "*" :
            if current_card < top_concealed[j] :
                action = "r"
                column = j
                row = 0
                break
        if bottom_concealed[j] != "*" :
            if current_card < bottom_concealed[j] :
                action = "r"
                column = j
                row = 1
                break

        if action != "r" :
            max_t = int(max(top_concealed))
            max_b = int(max(bottom_concealed))
            if max_t >= max_b :
                for q in range (len(top_concealed)) : 
                    if top_concealed[q] != "*" :
                        if current_card < top_concealed[q] :
                            action = "r"
                            column = q
                            row = 0
                            break
            else :
                for w in range (len(top_concealed)) : 
                    if bottom_concealed[w] != "*" :
                        if current_card < bottom_concealed[w] :
                            action = "r"
                            column = w
                            row = 1
                            break
                        



