import pandas as pd

# Load the Excel file
def readAndConvertToDict(pathToExcel):
    file_path = pathToExcel
    df = pd.read_excel(file_path, engine='openpyxl', header=None)

    # Convert the first row to a list of keys
    keys = df.iloc[0].values

    # Initialize an empty list to hold the dictionaries
    data_list = []

    # Iterate over the remaining rows and create a dictionary for each row
    for index, row in df[1:].iterrows():
        # Use zip to pair each key with its corresponding row value
        row_dict = dict(zip(keys, row.values))
        data_list.append(row_dict)

    # # Display the list of dictionaries
    # for item in data_list:
    #     print(item)
    with open("xlsxOutput.txt","w")as file:
        for item in data_list:
            for key in item:
                file.write(str(key))
                file.write(str(item[key]))
                file.write("\n")
    return data_list

