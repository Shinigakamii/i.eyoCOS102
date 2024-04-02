#Importing the 'pandas' library as it is efficient in tabulating data

import pandas as pd
data = {
    'Name' : ['Evelyn', 'Jessica', 'Somto', 'Edith', 'Lizo', 'Madonna', 'Waje', 'Tola', 'Aisha', 'Latifa', 'Chinedu', 'Liam', 'Wale', 'Gbenga', 'Abiola', 'Kola', 'Kunle', 'George', 'Thomas', 'Wesley'],
    'Gender' : ['Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male'],
    'Age' : [17, 16, 17, 18, 16, 18, 17, 20, 19, 17, 19, 16, 18, 17, 20, 19, 16, 18, 17, 19],
    'Height' : [5.5, 6.0, 5.4, 5.9, 5.8, 5.5, 6.1, 6.0, 5.7, 5.5, 5.7, 5.8, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.4, 5.8, 5.7],
    'Scores' : [83, 85, 70, 60, 76, 66, 87, 95, 60, 49, 74, 87, 76, 68, 66, 78, 87, 98, 54, 60],
} 

df = pd.DataFrame(data)

print(df)