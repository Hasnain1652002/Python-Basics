def ListComp1(List):
    return [i.lower() for i in List if len(i)>4 ]



if __name__ == "__main__":

    List=['Red', 'Green', 'Black', 'Pink', 'Yellow','Teapink']

    newList=ListComp1(List)
    print(newList)
