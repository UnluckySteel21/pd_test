# returns True if checksum is valid, otherwise returns False
def Luhn_checks_my_card(card_number):
    #initialize all variables i need
    cardDigits1 = []
    cardDigits1_sum = 0
    cardDigits2 = []
    cardDigits2_sum = 0

    #finds all digits in card_number that are second to last with a step of 2
    startLoction = len(card_number) - 2
    for i in card_number:
        if startLoction >= 0:
            cardDigits1.append(card_number[startLoction])
            startLoction -= 2

    #goal was to make the sum of the digits found before. Somehow it works.
    for i in cardDigits1:
        #DO NOT TOUCH
        j = int(i)*2
        if len(str(j)) == 2:
            j = str(j)
            for k in j:
                k = int(k)
                cardDigits1_sum += k
        else:
            cardDigits1_sum += j

    #finding the rest of the digits
    startLoction = len(card_number) - 1
    for i in card_number:
        if startLoction >= 0:
            cardDigits2.append(card_number[startLoction])
            startLoction -= 2

    #summing up the rest of the digits
    for i in cardDigits2:
        i = int(i)
        cardDigits2_sum += i

    #calculating the total sum and checking if ends with "0"
    digit_summ = str(cardDigits1_sum + cardDigits2_sum)
    if digit_summ[-1] == "0":
        return True
    else:
        return False

# returns name of card if digits are valid, otherwise returns "INVALID"
def check_card_type(card_number):
    #checks for the start of the card_number to see if valid
    card_number_list = []
    for i in card_number:
        card_number_list.append(i)

    if card_number_list[0] == "3":
        if card_number_list[1] == "7" or card_number_list[1] == "3":
            return "AMEX"
    
    if card_number_list[0] == "5":
        if card_number_list[1] == "1" or card_number_list[1] == "2" or card_number_list[1] == "3" or card_number_list[1] == "4" or card_number_list[1] == "5":
            return "MasterCard"
    
    if card_number_list[0] == "4":
        return "VISA"
    
    else:
        return "INVALID"

# main logic
def main():
    card_number = input("Card number: ")
    if Luhn_checks_my_card(card_number):
        print(check_card_type(card_number))
    else:
        print("INVALID")

if __name__ == "__main__":
    main()