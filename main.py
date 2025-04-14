import requests

def get_binance_time():
    url = "https://api.binance.com/api/v3/time"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ Binance API работает!")
            print(response.json())
        else:
            print(f"⚠️ Ошибка: {response.status_code}")
            print(response.text)
    except Exception as e:
        print("❌ Ошибка:", e)

if __name__ == "__main__":
    get_binance_time()


