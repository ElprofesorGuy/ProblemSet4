# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
import random

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[::]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        cipher_dictionnary={}
        #creation d'une liste qui contiendra toutes les lettres(majuscules comme minuscules)
        list_of_letters = list(string.ascii_letters)
        #je parcours chaque élément de la liste en vue de lui faire correspondre un encodage qui dépendra 
        #de la valeur du shift
        for position in range(len(list_of_letters)):
            if position<26: # in this case list_of_letters[position] is a lower letter
                if position+shift<26:#cece c'est pour empêcher qu'une lettre minuscule ne soit encodé par une majuscule et vice versa
                    cipher_dictionnary[list_of_letters[position]]=list_of_letters[position+shift]
                #lsit_of_letters[position] est tout simplement un élément de list_of _letters
                #au départ position vaut 0 ce qui correspond à la lettre a, quand position=1, ça correspond à b
                else:
                    cipher_dictionnary[list_of_letters[position]]=list_of_letters[position+shift-26]
            else: 
                if position+shift<52:
                    cipher_dictionnary[list_of_letters[position]]=list_of_letters[position+shift]
                else:
                    cipher_dictionnary[list_of_letters[position]]=list_of_letters[position+shift-26]
        return cipher_dictionnary


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shifted_message_text=[]
        #je charge le dictionnaire qui contient toutes les 52 lettres et leurs encodages correspondants 
        #peut importe la valeur du shift. De cette façon, une fois le shift donné, je n'ai plus qu'à 
        #récupérer l'encodage correspondant dans mon dictionnaire
        cipher_text_dictionnary=self.build_shift_dict(shift)
        for elt in self.message_text:
            if elt in string.ascii_letters:
                shifted_message_text.append(cipher_text_dictionnary[elt])
            else:
                shifted_message_text.append(elt)
        return ''.join(shifted_message_text)

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)
        self.shift=shift
        self.encryption_dict= self.build_shift_dict(shift)
        self.message_text_encrypted=self.apply_shift(shift)
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        temp=shift
        self.shift=temp


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        best_shift=0
        dict={}
        counter_real_words=0
        decrypted_dict={}
        max_real_words=0
        for shift in range(26):
            decrypted_message=self.apply_shift(shift)
            dict[decrypted_message]=shift#je cree un dictionnaire qui va contenir chaque décodage et la 
#valeur du shift correspondant
        dict_copy=dict.copy()
#ici, je compte le nombre de mots valides dans chaque décodage, et je ne vais conserver que ceux dont 
#le nombre de mots valides est maximal
        for elt in dict_copy.keys():
            for word in elt.split():
                if is_word(self.valid_words, word):
                    counter_real_words+=1
            decrypted_dict[elt]=counter_real_words
            counter_real_words=0
        max_real_words=max(decrypted_dict.values())
        for elt in decrypted_dict.keys():#je stocke l'ensemble des décodages qui ont le maximum de mots 
#contenus dans la liste des mots
            if decrypted_dict[elt] < max_real_words:
                del(dict[elt])
        list_message=[elt for elt in dict.keys()]#je transforme cet ensemble en liste pour pouvoir choisir un des décodages au hasard
        choix=random.choice(list_message)
        tuple=(choix,dict[choix] )#et je retourne un tuple qui contient un des décodages pris au hasard
        #et la valeur du shift qui a servi au decryptage
        return tuple
                



        

if __name__ == '__main__':


#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 
    
    
    """plaintext = PlaintextMessage('hello', 2)
    print("Plaintext : ", plaintext.apply_shift(plaintext.get_shift()))
    print('Actual Output:', plaintext.get_message_text_encrypted())
    ciphertext = CiphertextMessage('jgnnq')
    print("ciphertext : ", ciphertext.decrypt_message())"""
    file_message=CiphertextMessage(get_story_string())
    print("Decryption of story.txt : ", file_message.decrypt_message())
