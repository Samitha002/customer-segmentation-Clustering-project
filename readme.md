&nbsp;Customer Segmentation Analysis 



 **Project Overview**



This project aims to segment a mall's customer base into distinct groups based on their \*\*Annual Income\*\* and \*\*Spending Score\*\*. By identifying these segments, a business can create highly targeted marketing strategies to improve sales and customer retention.



&nbsp;**Tech Stack Used**



* SQL (MySQL): Used for secure data storage, management, and querying.
* Python: Performed data cleaning and implemented the K-Means Clustering machine learning algorithm using the Scikit-learn library.
* Power BI: Developed an interactive dashboard to visualize the clusters and extract business insights.



 **Customer Segments (Analysis by Color)**



Based on the machine learning results, the customers were divided into 5 distinct groups:



* Purple (Cluster 1) - VIP Customers: High Annual Income and High Spending Score. These are the most valuable customers.
* Light Blue (Cluster 3) - Impulse Buyers: Low Annual Income but High Spending Score. These customers respond well to frequent offers.
* Dark Blue (Cluster 2) - Careful Spenders: High Annual Income but Low Spending Score. They have the potential to spend more with targeted premium ads.
* Orange (Cluster 0) - Sensible Group: Low Annual Income and Low Spending Score. These customers are budget-conscious.
* Pink (Cluster 4) - Standard Group: Average Income and Average Spending Score. These represent the core "middle-class" customer base.



 **Key Dashboard Insights**



* Total Customer Base: 500 records successfully processed.
* Average Spending Score: 51.36 out of 100.
* Interactivity: Integrated Slicers for Gender, Age, and Income to allow for dynamic filtering and deep-dive analysis.
* Market Distribution: The Donut Chart visualizes the percentage of customers belonging to each cluster.



&nbsp;**Repository Structure**



* customers.py: Python script containing the K-Means clustering logic.
* Mall\_Customer\_Segmentation.csv: The dataset used for analysis.
* Segmentation\_Dashboard.pbix: The Power BI dashboard file.





