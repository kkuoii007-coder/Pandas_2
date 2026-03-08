import pandas as pd

students = [
    {'name': 'Анна Иванова', 'math': 5, 'physics': 4, 'chemistry': 5, 'russian': 5, 'english': 4},
    {'name': 'Борис Петров', 'math': 4, 'physics': 5, 'chemistry': 4, 'russian': 4, 'english': 5},
    {'name': 'Виктория Сидорова', 'math': 5, 'physics': 5, 'chemistry': 5, 'russian': 5, 'english': 5},
    {'name': 'Глеб Кузнецов', 'math': 3, 'physics': 4, 'chemistry': 3, 'russian': 4, 'english': 3},
    {'name': 'Анна Иванова', 'math': 5, 'physics': 4, 'chemistry': 5, 'russian': 5, 'english': 4},
    {'name': 'Борис Петров', 'math': 4, 'physics': 5, 'chemistry': 4, 'russian': 4, 'english': 5},
    {'name': 'Глеб Кузнецов', 'math': 5, 'physics': 5, 'chemistry': 5, 'russian': 5, 'english': 5},
    {'name': 'Глеб Кузнецов', 'math': 3, 'physics': 4, 'chemistry': 3, 'russian': 4, 'english': 3},
    {'name': 'Арсений Петров', 'math': 3, 'physics': 3, 'chemistry': 3, 'russian': 5, 'english': 3},
    {'name': 'Юрий Юнусов', 'math': 4, 'physics': 4, 'chemistry': 4, 'russian': 4, 'english': 4},
    {'name': 'Маша Васнецова', 'math': 5, 'physics': 5, 'chemistry': 5, 'russian': 5, 'english': 5}
    ]

df = pd.DataFrame(students)
print(df.head())
print()
print(df[['math', 'physics', 'chemistry', 'russian', 'english']].mean())
print()
print(df[['math', 'physics', 'chemistry', 'russian', 'english']].median())
print()
Q1 = df['math'].quantile(0.25)
Q3 = df['math'].quantile(0.75)
IQR = Q3 - Q1
print(Q1, Q3, IQR)
print()
print(df[['math', 'physics', 'chemistry', 'russian', 'english']].std())

