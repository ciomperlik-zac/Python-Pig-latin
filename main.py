def message_to_words(message):
  words = []
  word = ""
  for i in message.lower():
    if i != " ":
      word += i
    else:
      words.append(word)
      word = ""
  words.append(word)
  return words

def words_to_latin(words):
  vowels = "aeiou"
  end = ""
  final_message = ""

  for word in words:
    #does word have y as vowel?
    if not any(char in vowels for char in word):
      vowels += "y"
    
    #is first letter vowel with/without punctuation?
    if word[0] in vowels and any(char in ".,?!" for char in word):
      final_message += word[:-1] + "yay" + word[-1] + " "
    elif word[0] in vowels:
      final_message += word + "yay "
    
    #is word a number?
    elif any(char.isdigit() for char in word):
      final_message += word + " "
      
    #if word is normal word with/without punctuation
    else:
      for i in word:
        if i in vowels:
          if any(char in ".,?!" for char in word):
            final_message += word[:-1] + end + "ay" + word[-1] + " "
          else:
            final_message += word + end + "ay "
          vowels = "aeiou"
          end = ""
          break
        else:
          end += i
          word = word[1:]
  return final_message

message = input("Enter text to be converted into Pig Latin: ")
print("\n")

print(words_to_latin(message_to_words(message)))
