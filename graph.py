from collections import Counter
# import matplotlib_inline
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-notebook')
# %matplotlib inline

raw_text = str(input("enter the text to be summarized:"))
#raw_text = "The city of Kobe in Japan witnessed a devastating earthquake on January  17, 1995, killing more than 6,000 and making more than 45,000 people homeless.  The magnitude of the quake was 6.9 at the moment which caused damage of around 100 million dollars.  The governor of Kobe spent years on reconstruction and made efforts to bring back fifty thousand people who had left home.  Japan geologically is a highly active country. It lies upon four major tectonic plates namely, Eurasian, Philippine, Pacific, and North American which frequently meet and interact."


def plot_number_words(raw_text: str):
    n_words = len(raw_text.split())
    n_unique_words = len(set(raw_text.split()))
    print('Number of words: {}\nNumber of unique words: {}'.format(
        n_words, n_unique_words))
    height = [n_words, n_unique_words]
    bars = ("Words", "Unique words")
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height, color=['black', 'orange'])
    plt.xticks(y_pos, bars)
    plt.plot()
    plt.show()


plot_number_words(raw_text)

word_list = raw_text.split()
counts = dict(Counter(word_list).most_common(50))

labels, values = zip(*counts.items())
indSort = np.argsort(values)[::-1]
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]
indexes = np.arange(len(labels))

cmap = plt.cm.get_cmap('jet')
colors = cmap(np.arange(cmap.N))[::-5]
plt.figure(figsize=(20, 10))
plt.bar(indexes, values, color=colors)
plt.xticks(indexes, labels, fontsize=13, rotation=90)
plt.title("Top 50 (Uncleaned) Word frequencies")
plt.plot()
plt.show()