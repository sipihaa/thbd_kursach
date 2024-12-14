import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("Data_LIWC.csv")
data['date'] = pd.to_datetime(data['Date1'], dayfirst=True)


def categorize_period(date):
    if date < pd.to_datetime('2020-03-25'):
        return 'До COVID-19'
    elif date <= pd.to_datetime('2021-06-30'):
        return 'Локдаун'
    else:
        return 'После COVID-19'


data['period'] = data['date'].apply(categorize_period)

# Средние значения по периодам
features = ['certitude', 'Positive', 'Cognition']
averages = data.groupby('period')[features].mean()

# Построение графика
averages.plot(kind='bar')
plt.title('Лингвистические характеристики на разных этапах')
plt.xlabel('Периоды')
plt.ylabel('Средние значения')
plt.show()

sns.boxplot(x='Vividness', y='like_count', data=data)
plt.title('Влияние типа медиа на лайки')
plt.xlabel('Тип медиа')
plt.ylabel('Среднее кол-во лайков')
plt.show()

sns.boxplot(x='Vividness', y='retweet_count', data=data)
plt.title('Влияние типа медиа на ретвиты')
plt.xlabel('Тип медиа')
plt.ylabel('Среднее кол-во ретвитов')
plt.show()

# plt.figure(figsize=(12, 6))
# media_types = data['Vividness'].unique()
# colors = sns.color_palette('husl', len(media_types))
#
# for media, color in zip(media_types, colors):
#     media_data = data[data['Vividness'] == media]
#     plt.plot(media_data['date'], media_data['like_count'], label=media, color=color)
#
# plt.title('Динамика вовлечённости по типу медиа')
# plt.xlabel('Дата')
# plt.ylabel('Количество лайков')
# plt.legend(title='Тип медиа')
# plt.grid(True)
# plt.show()

tweet_length_metrics = data.groupby(pd.cut(data['WC'], bins=5))[['like_count', 'retweet_count']].mean()

fig, ax = plt.subplots(figsize=(10, 6))
tweet_length_metrics.plot(kind='line', ax=ax, marker='o', color=['blue', 'green'], linewidth=2)

ax.set_title('Влияние длины твита на лайки и ретвиты', fontsize=14)
ax.set_ylabel('Среднее количество взаимодействий', fontsize=12)
ax.set_xlabel('Длина твита (количество слов)', fontsize=12)
ax.legend(['Лайки', 'Ретвиты'], fontsize=10)
ax.grid(axis='both', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

hourly_engagement = data.groupby('OpnHours')['like_count'].mean()

plt.figure(figsize=(10, 6))
plt.bar(hourly_engagement.index, hourly_engagement.values, color=['blue', 'green'])
plt.title('Среднее количество лайков в зависимости от времени суток')
plt.ylabel('Среднее количество лайков')
plt.grid(axis='y')
plt.show()
