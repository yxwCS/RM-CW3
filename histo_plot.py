import matplotlib.pyplot as plt
import numpy as np

years = [2017, 2018, 2019, 2020, 2021, 2022, 2023]

case_study = [0, 0, 1, 1, 0, 0, 0]
controlled_user_study = [0, 1, 2, 0, 0, 1, 0]
literature_review = [0, 0, 1, 0, 0, 0, 0]
crowdsourcing = [0, 0, 0, 1, 0, 0, 0]
classroom_settings = [0, 0, 0, 0, 0, 0, 1]


plt.figure(figsize=(16, 8))

bar1 = plt.bar(years, case_study, 0.5, label='Case Study', color='orange') # orange at bnottom
bar2 = plt.bar(years, controlled_user_study, 0.5, bottom=np.array(case_study), label='Controlled User Study', color='skyblue')
bar3 = plt.bar(years, literature_review, 0.5, bottom=np.array(case_study) + np.array(controlled_user_study), label='Literature Review', color='green')
bar4 = plt.bar(years, crowdsourcing, 0.5, bottom=np.array(case_study) + np.array(controlled_user_study) + np.array(literature_review), label='Crowdsourcing', color='red')
bar5 = plt.bar(years, classroom_settings, 0.5, bottom=np.array(case_study) + np.array(controlled_user_study) + np.array(literature_review) + np.array(crowdsourcing), label='Classroom Settings', color='orange')

plt.xlabel('Publication Year')
plt.ylabel('Number of Publications')
plt.title('Number of Papers by Evaluation Methods')
plt.xticks(years)
plt.legend()

plt.show()
