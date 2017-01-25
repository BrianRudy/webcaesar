def alphabet_position(letter):
    letter = letter.lower()
    position = ord(letter) - 97
    return position

def rotate_character(char, rot):
    position = alphabet_position(char)
    rotate = (position + rot) % 26
    if ord(char) > 64 and ord(char) < 91:
        new_char = chr(rotate + 65)
        return new_char
    elif ord(char) > 96 and ord(char) < 123:
        new_char = chr(rotate + 97)
        return new_char
    return char
    
def encrypt(text, rot):

    statement = ""
    text_position = 0
    while text_position < len(text):
        state = rotate_character(text[text_position], rot)
        statement = statement + state
        text_position = text_position + 1

    return statement
