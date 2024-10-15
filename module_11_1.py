import requests #запросить данные с сайта и вывести их в консоль.
import matplotlib.pyplot as plt #визуализировать данные
import numpy as np #считать данные из файла, выполнить простой анализ
                    # данных (на своё усмотрение) и вывести результаты в консоль
print('-----------------------------------------------------------------------')
url = 'https://yandex.ru'  # Указываем URL, на который будем отправлять GET-запрос

response = requests.get(url)

if response.status_code == 200:
    data = response.url
    print(f'Статус ответа: OK [код 200] по URL = {data}')
    response.encoding = 'utf-8'
    content = response.content
    print(f'Содержание : {content}')
    headers = response.headers
    print(f'Заголовки : {headers}')

else:
    print('Ошибка при выполнении запроса')

print('-----------------------------------------------------------------------')


x = [31, 32, 33, 34, 35, 36]
y = [2019, 2020, 2021, 2022, 2023, 2024]
plt.plot(x, y)
plt.xlabel('Ocь х')
plt.ylabel('Ось  у')
plt.title('Количество человек в классе по годам')
plt.plot(x, y, color = 'orange', marker = '.', markersize = 9)
plt.show


def circle_area(radius):
    return np.pi * radius ** 2


# Create a vectorized version of the function
circle_ufunc = np.vectorize(circle_area)

# Test the ufunc with a single value
radius_values = np.array([1, 2, 3, 4])
areas = circle_ufunc(radius_values)
print(areas)




