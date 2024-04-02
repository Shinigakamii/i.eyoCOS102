data = [
    {'Name': 'Evelyn', 'Gender': 'Female', 'Age': 17,  'Height' : 5.5, 'Scores' :83},
    {'Name': 'Jessica', 'Gender': 'Female', 'Age': 16,  'Height' : 6.0, 'Scores' :85},
    {'Name': 'Somto', 'Gender': 'Female', 'Age': 17,  'Height' : 5.4, 'Scores' :70},
    {'Name': 'Edith', 'Gender': 'Female', 'Age': 18,  'Height' : 5.9, 'Scores' :60},
    {'Name': 'Lizo', 'Gender': 'Female', 'Age': 16,  'Height' : 5.8, 'Scores' :76},
    {'Name': 'Madonna', 'Gender': 'Female', 'Age': 18,  'Height' : 5.5, 'Scores' :66},
    {'Name': 'Waje', 'Gender': 'Female', 'Age': 17,  'Height' : 6.1, 'Scores' :87},
    {'Name': 'Tola', 'Gender': 'Female', 'Age': 20,  'Height' : 6.0, 'Scores' :95},
    {'Name': 'Aisha', 'Gender': 'Female', 'Age': 19,  'Height' : 5.7, 'Scores' :60},
    {'Name': 'Latifa', 'Gender': 'Female', 'Age': 17,  'Height' : 5.5, 'Scores' :49},
    {'Name': 'Chinedu', 'Gender': 'Male', 'Age': 19,  'Height' : 5.7, 'Scores' :74},
    {'Name': 'Liam', 'Gender': 'Male', 'Age': 16,  'Height' : 5.8, 'Scores' :87},
    {'Name': 'Wale', 'Gender': 'Male', 'Age': 18,  'Height' : 5.8, 'Scores' :76},
    {'Name': 'Gbenga', 'Gender': 'Male', 'Age': 17,  'Height' : 6.1, 'Scores' :68},
    {'Name': 'Abiola', 'Gender': 'Male', 'Age': 20,  'Height' : 5.9, 'Scores' :66},
    {'Name': 'Kola', 'Gender': 'Male', 'Age': 19,  'Height' : 5.5, 'Scores' :78},
    {'Name': 'Kunle', 'Gender': 'Male', 'Age': 19,  'Height' : 6.1, 'Scores' :87},
    {'Name': 'George', 'Gender': 'Male', 'Age': 18,  'Height' : 5.4, 'Scores' :98},
    {'Name': 'Thomas', 'Gender': 'Male', 'Age': 17,  'Height' : 5.8, 'Scores' :54},
    {'Name': 'Wesley', 'Gender': 'Male', 'Age': 19,  'Height' : 5.7, 'Scores' :60},
    
]

# Extracting column names
columns = list(data[0].keys())

# Printing column names
print(" | ".join(columns))

# Printing data rows
for row in data:
    print(" | ".join(str(row[column]) for column in columns))