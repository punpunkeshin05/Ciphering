def caesar_decode(message,offset):
    alphabets_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    his_message_cleaned = ''
#finding the position
    for letter in message:
            if letter in alphabets_list:
                position_i = 0
                for position in range(len(alphabets_list)):
                    if letter == alphabets_list[position]:
                        position_i = position
                        position_i = (position_i + offset) % 26
                        his_message_cleaned = his_message_cleaned + alphabets_list[position_i]
            else:
                his_message_cleaned = his_message_cleaned + letter
    print(his_message_cleaned)

def caesar_encode(message, offset):
    alphabets_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    his_message_cleaned = ''
    #finding the position
    for letter in message:
        if letter in alphabets_list:
            position_i = 0
            for position in range(len(alphabets_list)):
                if letter == alphabets_list[position]:
                    position_i = position
                    position_i = (position_i - offset) % 26
                    his_message_cleaned = his_message_cleaned + alphabets_list[position_i]
        else:
            his_message_cleaned = his_message_cleaned + letter
    print(his_message_cleaned)
