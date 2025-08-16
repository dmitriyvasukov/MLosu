import requests
from auth import get_token
import time

token = get_token()

headers = {
    "Authorization": f"Bearer {token}"
}

# Начальные параметры
params = {
    # Дополнительные параметры, если нужны
    # "sort": "score_desc"  # если требуется сортировка
}

current_cursor = None
max_pages = 5  # Максимальное количество страниц (можно убрать или изменить)
page_count = 0

while True:
    # Если есть курсор, добавляем его в параметры
    if current_cursor:
        params["cursor_string"] = current_cursor
    
    res = requests.get("https://osu.ppy.sh/api/v2/rankings/osu/global", 
                      headers=headers, params=params)
    
    if res.status_code != 200:
        print(f"Ошибка: {res.status_code}")
        break
    
    data = res.json()
    page_count += 1
    
    print(f"\n=== Страница {page_count} ===")

    for i, user_data in enumerate(data['ranking'],1):
        user_id = user_data['user']['id']
        username = user_data['user']['username']
        pp = user_data['pp']
        playcount = user_data['playcount']
        print(f" {user_id} - {username} - {pp}pp")
    current_cursor = data.get('cursor_string')
    
    if not current_cursor:
        print("Достигнут конец списка")
        break
    
    if page_count >= max_pages:
        print(f"Достигнут лимит в {max_pages} страниц")
        break
    
    time.sleep(1)

print("\nЗавершено")