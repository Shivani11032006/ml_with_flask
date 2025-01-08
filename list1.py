import pandas as pd 
less_stress =[2,5,6]
making_notes =[4,5,3]
stu_name =["Shivani","Thanishka","Vidya"]
dict1 = {
    "less_stress":less_stress,
    "making_notes":making_notes,    
    "stu_name":stu_name
    }
print(dict1)
df = pd.DataFrame(dict1)
print(df)