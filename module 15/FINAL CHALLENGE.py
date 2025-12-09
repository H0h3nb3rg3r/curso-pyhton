#Write a program that will take a text message and tranlate it into words your grandparents could understand, e.g.:
#So funny LOL ROTFL
#becomes:
#So funny laughing out loud rolling on the floor laughing
#For this scenario we will start with a file lists all the text message abbreviations and the traslations:

# Dictionary of abbreviations and their meanings
abbrev = {
    "LOL": "laughing out loud",
    "ROTFL": "rolling on the floor laughing",
    "BRB": "be right back",
    "TTYL": "talk to you later",
    "IDK": "I don't know"
}

# Ask the user for a text message
message = input("Enter your text message: ")

# Split the message into words
words = message.split()

# Translate each word if it's in the dictionary
translated = []
for word in words:
    # Remove punctuation for safety
    clean_word = word.strip(",.!?")

    if clean_word.upper() in abbrev:
        translated.append(abbrev[clean_word.upper()])
    else:
        translated.append(word)

# Print the translated message
print(" ".join(translated))
