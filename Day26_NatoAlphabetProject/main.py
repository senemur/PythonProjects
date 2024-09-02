# Sometimes what we say when talking on the phone is not understood and we have to spell it out. For example, a for ankara. this is a kind of program that does this with the NATO alphabet.

# /////////////////////////////////////////////////////////////
# student_dict = {
#     "student": ["angela", "james", "lily"],
#     "score": [56, 76, 98]
# }
# LOOP through dictionaries:
# for (key,value) in student_dict.items():
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)


# LOOP through a data frame
# for (key,value) in student_data_frame.items():
#     pass

# LOOP through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# ////////////////////////////////////////////////////////////
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()

