import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_csv("Students_Performance.csv")

print(students.head())

print(students.tail(3))

print(students[10:13])

print(students[students["test preparation course"] == "completed"]["math score"].head())

students["total score"] = students["math score"] + students["reading score"] + students["writing score"]
print(students.sort_values(["total score"], ascending=False).head())

scores = students.assign(total_score=lambda x: x["math score"] + x["reading score"] + x["writing score"])
print(scores.sort_values(["total_score"], ascending=False).head())

print(students.groupby(["gender", "test preparation course"])["writing score"].count())

agg_functions = {"math score": ["mean", "median"]}
print(students.groupby(["gender", "test preparation course"]).agg(agg_functions))

plt.hist(students["math score"], label="Тест по математике")
plt.xlabel("Баллы за тест")
plt.ylabel("Количество студентов")
plt.legend()
plt.show()