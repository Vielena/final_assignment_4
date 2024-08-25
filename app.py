import pandas as pd

# Загружаем данные из data.csv
data = pd.read_csv('data.csv')

# Вычисляем среднюю зарплату
average_salary = data['salary'].mean()
print(f'Средняя зарплата всех сотрудников: {average_salary:.2f}')

# Отбираем сотрудников старше 30 лет
older_than_30 = data[data['age'] > 30]
print('Сотрудники старше 30 лет:')
print(older_than_30[['name', 'age', 'salary']])
