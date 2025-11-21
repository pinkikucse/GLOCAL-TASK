import os
import pandas as pd
import re

file=pd.read_csv('practice.csv')
## print the file
print(file)

## Convert Uppercase and Remove whitespaces
def Convert_upper(obj):
    obj = obj.apply(lambda x: x.str.upper() if x.dtype == "object" else x)
    obj = obj.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    return obj

file[['first_name']] = Convert_upper(file[['first_name']])
file[['last_name']] = Convert_upper(file[['last_name']])
file[['email']] = Convert_upper(file[['email']])

## print the file to check the changes
print(file)

## Remove duplicates
file.drop_duplicates(inplace = True)

## print the file to check the changes
print(file)

#email validation and add a new column to show the result True/False
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
file["is_valid_email"] = file["email"].str.fullmatch(email_regex) \
                            .map({True: "TRUE", False: "FALSE"})



## Convert all the column names in uppercase
file.columns=file.columns.str.upper()

## print the file to check the changes
print(file)

## Save the cleaned data into another file

file.to_csv('updated_practice.csv', index = False)
