class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        return input_str[::-1]

    def is_english_vowel(self, character):
        vowels=['a','e','i','o','u','A','E','I','O','U']
        if character in vowels:
            return True
        return False
        

    def find_longest_word(self, sentence):
        longest = max(sentence.split(), key=len)
        
        return longest

    def get_word_lengths(self, text):
        x=text.split()
        arr=[]
        for i in x:
            arr.append(len(i))

       
        return arr

x=StringExercise()
e='e'
text ="foo foo1 foo2 foo3"      
print(x.get_word_lengths(text))