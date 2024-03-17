def countNumberodStrings(List):
    count=0
    for i in List:
        if len(i)>=2 and i[0]==i[-1]:
            count+=1
        else:
            continue

    print(f"Result:{count}") 

if __name__ == "__main__":

    List=['abc', 'xyz', 'aba', '1221']
    countNumberodStrings(List=List)
