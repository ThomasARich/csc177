import pandas as pd
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

dataset = pd.read_csv('imdb_dataset.csv')
dataset = dataset.head(20)
dataset.replace(to_replace =['no'], value ='0', inplace = True)
dataset.replace(to_replace =['yes'], value ='1', inplace = True)

titles = dataset['title']
y = dataset['critics_rating']
x = dataset[['best_pic_nom', 'best_pic_win', 'best_actor_win', 'best_actress_win', 'best_dir_win', 'top200_box']]
z = hierarchy.linkage(x.values, 'single')
dn = hierarchy.dendrogram(z, labels = titles.tolist(), orientation = 'right')

plt.tight_layout()
plt.savefig('hierarchical_single.png')

z = hierarchy.linkage(x.values, 'complete')
dn = hierarchy.dendrogram(z,labels = titles.tolist(), orientation='right')

plt.tight_layout()
plt.savefig('hierarchical_complete.png')

z = hierarchy.linkage(x.values, 'average')
dn = hierarchy.dendrogram(z, labels = titles.tolist(), orientation='right')

plt.tight_layout()
plt.savefig('hierarchical_average.png')