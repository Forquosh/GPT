
# Split the data into training and validation sets
print("This script will split a text file into training and validation sets.")
print("The training data will contain the first p% of the text file.")
print("The validation data will contain the remaining (1-p)% of the text file.")
print("The training and validation data will be saved in the same directory as the text file.")
print("For shorter to medium sized texts only.")

while True:
    try:
        file = input("Enter the file name: ")
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()

            percentage = float(input("Enter the percentage of training data (0 < p < 1): "))
            assert 0 < percentage < 1

            n = int(percentage * len(text))
            train_data = text[:n]
            val_data = text[n:]

            print(f"Training data: {len(train_data)} characters")
            print(f"Validation data: {len(val_data)} characters")

            with open("train_split.txt", "w", encoding="utf-8") as train_file:
                train_file.write(train_data)
            with open("val_split.txt", "w", encoding="utf-8") as val_file:
                val_file.write(val_data)
            
        print("Data split successfully.")
        break

    except (ValueError, FileNotFoundError, AssertionError):
        print("Incorrect input. Please try again.")