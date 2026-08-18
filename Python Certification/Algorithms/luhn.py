def verify_card_number(number):
    
    if isinstance(number, int):
        s = str(number)

    else:
        s = number.replace(' ', '')
        s = s.replace('-', '')
    
    total = 0

    digits = map(int, s)
    
    for i, d in enumerate(digits):
        print(i,d)
        if (len(s) - i) % 2 == 0:
            d = d * 2
            if d > 9:
                d -= 9
        total += d

    if total % 10 != 0:
        return 'INVALID!'
    else:
        return 'VALID!'


    


verify_card_number('453-91 4889')
verify_card_number('4111-1111-1111-1111')