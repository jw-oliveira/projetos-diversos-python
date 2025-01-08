import requests

def get_exchange_rate(base: str, symbol: str, api_key: str):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data['conversion_rates'].get(symbol)
        if rate:
            return rate
        else:
            return f'Symbol {symbol} not found.'
    else:
        return f"API access error: {response.status_code}"

def get_coin(coin_type):
    coin_map = {1: 'USD', 2: 'EUR', 3: 'BRL'}
    coin = None

    while coin is None:
        try:
            choice = int(input(f'''SELECT THE {coin_type} COIN
1 - USD
2 - EUR
3 - BRL
YOUR CHOICE: '''))

            coin = coin_map.get(choice)
            if coin is None:
                print("Invalid choice. Please select a valid option (1, 2, or 3).")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

    print('='*40)
    return coin


api_token = ''

print(f'''{"="*40}
{"CURRENCY CONVERTER":^40}
{"="*40}\n''')

selected_base = get_coin('BASE')
selected_symbol = get_coin('SYMBOL')
exchange_rate = get_exchange_rate(selected_base, selected_symbol, api_token)
print(f'1 {selected_base} = {exchange_rate} {selected_symbol}')