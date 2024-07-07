m = [[2,3,1,0,0,6],[3,7,0,1,0,12],[-7,-12,0,0,1,0]]
no_row = 3
no_column = 6

##-----to find most negative number for pivot column-----##
def FindingPivotColumn ():
    no_row=len(m)
    no_column=len(m[0])
    f=0
    for i in range (no_row):
        PivotColumn="NO Negative Numbers"
        for j in range (no_column):
            if m[i][j]<f :
                f=m[i][j]
                PivotColumn=j
    if  PivotColumn=="NO Negative Numbers" :
        print("Input Matrix Again")
    return (PivotColumn)            
            
##-----to find pivot row by dividing------##
def FindingPivotRow (PivotColumn):
    no_row=len(m)
    RatioList=[]
    LastLength=len(m[0])-1
    for b in range (no_row):
        LastElement=m[b][LastLength]
        if m[b][PivotColumn]>0 :
            ratio,PivotRow=LastElement/m[b][PivotColumn],b
            RatioList.append(ratio)
            print (ratio)
                
    LeastRatio=min(RatioList)
    PivotRow=RatioList.index(LeastRatio)
    return(PivotRow)

##-----pivot element------##
PivotElement=m[PivotRow][PivotColumn]
            
        
            
        
