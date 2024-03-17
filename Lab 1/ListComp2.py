def ListComp2(List):
    return [i for count,i in enumerate(List) if count not in [0,4,5]]



if __name__ == "__main__":

    List=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Teapink']

    newList=ListComp2(List)
    print(newList)
