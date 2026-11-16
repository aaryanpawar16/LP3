import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

cols = ["QUANTITYORDERED", "PRICEEACH", "SALES", "MSRP"]
df = pd.read_csv("sales_data_sample.csv", encoding="latin1").dropna(subset=cols)
X = StandardScaler().fit_transform(df[cols])

# Elbow method: plot inertia for k = 1..10, pick k where the curve bends
inertia = [KMeans(n_clusters=k, n_init=10, random_state=42).fit(X).inertia_ for k in range(1, 11)]
plt.plot(range(1, 11), inertia, marker="o")
plt.xlabel("k"); plt.ylabel("Inertia"); plt.title("Elbow method")
plt.show()

K = 3  # set from the elbow plot
df["Cluster"] = KMeans(n_clusters=K, n_init=10, random_state=42).fit_predict(X)
print(df.groupby("Cluster")[cols].mean())


# ======================= VIVA QUESTIONS =======================
# Q: What is clustering? Supervised or unsupervised?
# A: Grouping similar data points without labels - unsupervised learning.
# Q: What is customer segmentation?
# A: Dividing customers into groups with similar behaviour (spend, quantity) for targeted marketing.
# Q: Explain the K-Means algorithm.
# A: 1) Choose k and initialize k centroids. 2) Assign each point to the nearest centroid.
#    3) Recompute each centroid as the mean of its points. 4) Repeat 2-3 until centroids stop changing.
# Q: What is inertia / WCSS?
# A: Sum of squared distances of points to their cluster centroid; measures cluster compactness.
# Q: What is the elbow method?
# A: Plot inertia against k; choose the k where the curve bends (adding more clusters gives little improvement).
# Q: Other ways to choose k?
# A: Silhouette score, gap statistic, domain knowledge.
# Q: Why scale the data?
# A: K-Means uses Euclidean distance, so features with large ranges (SALES) would dominate.
# Q: Limitations of K-Means?
# A: Need to specify k, sensitive to initialization and outliers, assumes spherical equal-sized clusters,
#    only for numeric data, may converge to a local optimum.
# Q: What is k-means++?
# A: Smarter initialization that spreads the initial centroids apart (default in sklearn).
# Q: What are n_init and random_state?
# A: n_init = number of runs with different initial centroids (best kept); random_state = reproducibility.
# Q: Explain hierarchical clustering.
# A: Agglomerative (bottom-up: merge the closest clusters) or divisive (top-down). Result is shown as a dendrogram;
#    cut it at a height to get the clusters.
# Q: Linkage types?
# A: Single (min distance), complete (max), average, ward (minimizes variance increase).
# Q: K-Means vs hierarchical?
# A: K-Means: needs k, fast on large data, flat clusters. Hierarchical: no k needed upfront, dendrogram, slower O(n^2) or worse.
# Q: Time complexity of K-Means?
# A: O(n * k * d * iterations).
# Q: What is the silhouette score?
# A: Measures how close a point is to its own cluster vs the nearest other cluster, from -1 to 1 (higher is better).
# Q: Why encoding="latin1" when reading the CSV?
# A: The file contains non-UTF-8 characters (e.g. in names/addresses); latin1 reads them without errors.
# Q: Why dropna / only numeric columns?
# A: K-Means needs numeric, complete data; categorical columns need encoding first.
# Q: How do you interpret clusters?
# A: Look at the mean of each feature per cluster (groupby) and name them (e.g. high-value, bulk buyers, low spenders).
# Q: Other clustering algorithms?
# A: DBSCAN (density-based, finds outliers), K-Medoids, Gaussian Mixture Models.
# Q: Related technique for customer data?
# A: RFM analysis (Recency, Frequency, Monetary).
