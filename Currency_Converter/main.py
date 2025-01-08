import requests

# Function to get the exchange rate between two currencies using the ExchangeRate-API
def get_exchange_rate(base: str, target: str, api_key: str):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data['conversion_rates'].get(target)
        if rate:
            return rate
        else:
            return f'Target {target} not found.'
    else:
        return f"API access error: {response.status_code}"

# Function to get the user's choice of currency (base or target)
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
selected_target = get_coin('TARGET')
exchange_rate = get_exchange_rate(selected_base, selected_target, api_token)
# Displays the conversion result
print(f'1 {selected_base} = {exchange_rate} {selected_target}')