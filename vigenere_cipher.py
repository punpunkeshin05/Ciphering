def decode_vi(message, keyword):
    alphabets_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #create a keyword phrase
    keyword_phrase = ''
    keyword_count = 0
    # loop through index for the length of message
    for index in range(len(message)):
        # if letter is alphabets
        if message[index] in alphabets_list:
            #creating keyword_phrase
            keyword_phrase = keyword_phrase + keyword[keyword_count]
            keyword_count += 1
            if keyword_count >= len(keyword):
                keyword_count = 0
        else:
            keyword_phrase = keyword_phrase + message[index]
    #getting postion for both message and keyword phrase and shifting them.
    position_message = 0
    position_keyword = 0
    cleaned = ''
    for i in range(len(keyword_phrase)):
        if message[i] in alphabets_list or keyword_phrase[i] in alphabets_list:
            if message[i] in alphabets_list:
                for index in range(len(alphabets_list)):
                    if message[i] == alphabets_list[index]:
                        position_message = index
            if keyword_phrase[i] in alphabets_list:
                for index in range(len(alphabets_list)):
                    if keyword_phrase[i] == alphabets_list[index]:
                        position_keyword = index
            total_index = (position_message + position_keyword)%26
            cleaned = cleaned + alphabets_list[total_index]
        else:
            cleaned = cleaned + message[i]
    print(cleaned)
    
    
def encode_vi(message, keyword):
    alphabets_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #create a keyword phrase
    keyword_phrase = ''
    keyword_count = 0
    # loop through index for the length of message
    for index in range(len(message)):
        # if letter is alphabets
        if message[index] in alphabets_list:
            #creating keyword_phrase
            keyword_phrase = keyword_phrase + keyword[keyword_count]
            keyword_count += 1
            if keyword_count >= len(keyword):
                keyword_count = 0
        else:
            keyword_phrase = keyword_phrase + message[index]
    #getting postion for both message and keyword phrase and shifting them.
    position_message = 0
    position_keyword = 0
    cleaned = ''
    for i in range(len(keyword_phrase)):
        if message[i] in alphabets_list or keyword_phrase[i] in alphabets_list:
            if message[i] in alphabets_list:
                for index in range(len(alphabets_list)):
                    if message[i] == alphabets_list[index]:
                        position_message = index
            if keyword_phrase[i] in alphabets_list:
                for index in range(len(alphabets_list)):
                    if keyword_phrase[i] == alphabets_list[index]:
                        position_keyword = index
            total_index = (position_message - position_keyword)%26
            cleaned = cleaned + alphabets_list[total_index]
        else:
            cleaned = cleaned + message[i]
    print(cleaned)      

