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

def get_base_coin():
    base = None
    base_coin = int(input('''SELECT THE BASE COIN
1 - USD
2 - EUR
3 - BRL
YOUR CHOICE: '''))

    if 1 <= base_coin <= 3:
        if base_coin == 1:
            base = 'USD'
        elif base_coin == 2:
            base = 'EUR'
        else:
            base = 'BRL'
    else:
        print('Invalid choice')

    return base

def get_symbol_coin():
    symbol = None
    symbol_coin = int(input('''SELECT THE SYMBOL COIN
1 - USD
2 - EUR
3 - BRL
YOUR CHOICE: '''))

    if 1 <= symbol_coin <= 3:
        if symbol_coin == 1:
            symbol = 'USD'
        elif symbol_coin == 2:
            symbol = 'EUR'
        else:
            symbol = 'BRL'
    else:
        print('Invalid choice')

    return symbol

api_token = ''

print(f'''{"="*40}
{"CURRENCY CONVERTER":^40}
{"="*40}\n''')

selected_base = get_base_coin()
selected_symbol = get_symbol_coin()
exchange_rate = get_exchange_rate(selected_base, selected_symbol, api_token)
print(f'1 {selected_base} = {exchange_rate} {selected_symbol}')