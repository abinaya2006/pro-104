import csv
from collections import Counter

# Mean Calculation
def get_mean(total_sum,total_values):
    mean=total_sum/total_values
    print("Mean (Average) is : ",mean)


# Median Calculation
def get_median(total_values,new_data):
    if(total_values % 2 ==0):
        median1=float(new_data[total_values//2])
        median2=float(new_data[total_values//2+1])
        median=float(median1+median2)/2
    
    else:
        median=float(new_data[total_values//2])

    print("Median is : ",median)

# Mode Calculation:
def get_mode(new_data):
    data=Counter(new_data)
    data_for_range={
        "75-85":0,
        "85-95":0,
        "95-105":0,
        "105-115":0,
        "115-125":0,
        "125-135":0,
        "135-145":0,
        "145-155":0,
        "155-165":0,
        "165-175":0,
    }

    for weight,occurence in data.items():
        if(75<float(weight)<85):
            data_for_range["75-85"]+=occurence
        
        elif(85<float(weight)<95):
            data_for_range["85-95"]+=occurence
        
        elif(95<float(weight)<105):
            data_for_range["95-105"]+=occurence
        
        elif(105<float(weight)<115):
            data_for_range["105-115"]+=occurence

        elif(115<float(weight)<125):
            data_for_range["115-125"]+=occurence

        elif(125<float(weight)<135):
            data_for_range["125-135"]+=occurence

        elif(135<float(weight)<145):
            data_for_range["135-145"]+=occurence
        
        elif(145<float(weight)<155):
            data_for_range["145-155"]+=occurence
        
        elif(155<float(weight)<165):
            data_for_range["155-165"]+=occurence

        elif(165<float(weight)<175):
            data_for_range["165-175"]+=occurence

    mode_range,mode_occurence=0,0

    
    for range,occurence in data_for_range.items():
        if(occurence>mode_occurence):
            mode_range,mode_occurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence

    mode=float((mode_range[0]+mode_range[1])/2)
    print(f"Mode is : {mode} and it has occured {mode_occurence} times")



with open("height_weight.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

sum_weight=0
total_values=len(file_data)
new_data=[]

for data_of_person in file_data:
    sum_weight+=float(data_of_person[2])
    new_data.append(float(data_of_person[2]))


new_data.sort()

get_mean(sum_weight,total_values)
get_median(total_values,new_data)
get_mode(new_data)


            

        





