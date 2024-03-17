def dictConcatenation(dict1,dict2,dict3,):
    return {**dict1,**dict2,**dict3}



if __name__ == "__main__":

    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50, 6:60}

    newDict=dictConcatenation(dict1=dic1,dict2=dic2,dict3=dic3)
    print(newDict)
