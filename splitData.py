import random

def split_data(input_file, train_file, test_file, val_file, train_percent=0.75, test_percent=0.20):
    # Read the input data file
    with open(input_file, 'r') as f:
        data = f.readlines()

    # Calculate the number of rows for each split
    total_rows = len(data)
    print("totalrows:", total_rows)
    train_rows = int(train_percent * total_rows)
    print("training rows:", train_rows)
    test_rows = int(test_percent * total_rows)
    val_rows = total_rows - train_rows - test_rows

    # Randomly shuffle the data
    random.shuffle(data)

    # Write data to train, test, and validation files
    with open(train_file, 'w') as f:
        f.writelines(data[:train_rows])

    with open(test_file, 'w') as f:
        f.writelines(data[train_rows:train_rows + test_rows])

    with open(val_file, 'w') as f:
        f.writelines(data[train_rows + test_rows:])

# File paths
input_file = "merged_data.txt" #testing performed with 1000.txt
train_file = "train_data.txt"
test_file = "test_data.txt"
val_file = "val_data.txt"

# Split data into train, test, and validation files
split_data(input_file, train_file, test_file, val_file, train_percent=0.75, test_percent=0.20) #values can be changed to 80 train, and 20 test
