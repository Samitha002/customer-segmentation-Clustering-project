import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


file_path = r'C:\Users\SIVAJI\Downloads\customer segmentation\Mall_Customer_Segmentation.csv'
df = pd.read_csv(file_path)

print("Available columns in your file:", df.columns)

try:
    X = df[['Annual_Income_k$', 'Spending_Score_1_100']]
except KeyError:

    X = df[['Annual_Income', 'Spending_Score']]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
df['New_Cluster_ID'] = kmeans.fit_predict(X_scaled)


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df,
                x=X.columns[0],
                y=X.columns[1],
                hue='New_Cluster_ID',
                palette='bright')

plt.title('Customer Segments')
plt.show()

print("Success! Chart display")
df.to_csv(r'C:\Users\SIVAJI\Downloads\customer segmentation\final_segmented_data.csv', index=False)
print("File saved successfully ")