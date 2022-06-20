student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    # print(key)
    # print(value)
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    # if row.student == "Lily":
    #     print(index)
    # print(row)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
nato_words = pandas.read_csv("nato_phonetic_alphabet.csv")

# rough:
# for (k,v) in nato_words.iterrows():
    # print(v.code)
# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
my_dict = {d_val.letter: d_val.code for (d_letter, d_val) in nato_words.iterrows() }
# print(my_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_val=input("Enter your name: ").upper()
new_val_list=[my_dict[val] for val in user_val if val in my_dict]
print(new_val_list)
# result=[k for (k,v) in my_dict.items() if  k in new_val_list]
# print(result)
