user_input = input("Enter the filename to analyze: ")

with open(user_input, "r") as file:
    total_characters = len(file.read())
    print("Total amount of characters: ", total_characters)

    file.seek(0)

    total_lines = sum(1 for line in file)
    print("Total amount of lines: ", total_lines)

    file.seek(0)

    total_used_lines = sum(1 for line in file if line.strip())
    print("Total amount of used lines: ", total_used_lines)

    file.seek(0)

    total_words = sum(len(line.split()) for line in file)
    print("Total amount of words: ", total_words)

    file.seek(0)

    total_sentences = sum(line.count('.') + line.count('?') + line.count('!') for line in file)
    print("Total amount of sentences: ", total_sentences)

    file.seek(0)