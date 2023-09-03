input_message = '"Please input which function you want to run" \n'
input_message = ' Type "0" to exit \n'
input_message += '1/. download hkma exchange rate file'

run_function = -1
while run_function != 0:
    run_function = int(input(input_message))


    if (run_function == 1) :
        import wget
        url = 'https://api.hkma.gov.hk/public/market-data-and-statistics/monthly-statistical-bulletin/er-ir/er-eeri-daily'
        filename = wget(wget)

    if (run_function == 2) :
        currency_message = input("What currency do you want to select? ")
        if currency_message == 'jpy':
            pass

