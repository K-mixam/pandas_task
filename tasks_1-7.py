import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('works.csv')
# ___task-1___
# print(data.info())
# print(data.shape[0])
# print(len(data.index))
# ___task-1___

# ___task-2___
# male = (data['gender'] == 'Мужской').sum
# female = (data['gender'] == 'Женский').sum
# print(male, female)
#
# print(data.gender.value_counts())
# ___task-2___

# ___task-3___
# print(data.info())
# print(data.skills.notna().sum())
# print(data.skills.count())
# ___task-3___

# ___task-4___
# print(data.skills[data.skills.notna()])
# print(data.skills.dropna())
# ___task-4___

# ___task-5___
# new_data = data[data.skills.notna()]
# print(new_data[new_data.skills.str.lower().str.contains('python|питон')].salary)
#
# index = data.skills.str.lower().str.contains('python|питон')
# mask = index.notna()
# print(data[mask & index].salary)
# ___task-5___

# ___task-6___
# percentiles = np.linspace(.1, 1, 10)
# men_salary = data.query("gender == 'Мужской'").quantile(percentiles)
# women_salary = data.query("gender == 'Женский'").quantile(percentiles)
#
# data11 = 'Среднее'
# data12 = 20000
# new_request = data.query("educationType == @data11 and salary <= @data12")
#
# print(new_request)
# ___task-6___

# ___task-7___
gender = 'Мужской'
educationType = 'Высшее'
salary_data = data.query("gender == @gender and educationType == @educationType").salary
plt.title(' с ')
plt.xlabel('Зарплата')
plt.ylabel('Количество ')
plt.grid()
plt.hist(salary_data, bins=50)
plt.show()
# ___task-7___

