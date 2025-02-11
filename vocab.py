
# Generate a vocabulary file from a text file.
print("This script will generate a vocabulary file from a text file.")
print("The vocabulary file will contain all the unique characters in the text file.")
print("The vocabulary file will be saved in the same directory as the text file.")
print("For shorter to medium sized texts only.")

while True:
    try:
        file = input("Enter the file name: ")
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            chars = sorted(list(set(text)))
            
            with open("vocab.txt", "w", encoding="utf-8") as vfile:
                for char in chars:
                    vfile.write(char + "\n")
        
        print("Vocabulary file generated successfully.")
        break
    except (ValueError, FileNotFoundError):
        print("File not found. Please try again.")