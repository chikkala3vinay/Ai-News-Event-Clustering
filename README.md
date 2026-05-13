# Ai-News-Event-Clustering

## project Overview
In today’s digital world, the same real-world event is reported by hundreds of news articles across multiple platforms and over different time periods. Because of the large volume of news data, it becomes difficult for users to clearly understand:

* What the actual event is

* How the event evolved over time

* What the important developments or milestones were

This project presents an AI-based News Event Detection and Timeline Generation system that automatically:

* Group the news articles into real world events

* Builds a chronological timeline for each event

* Generates a short summary explainning the event evolution

This project mainly focuses on:

* Natural Language Processing (NLP)
* Sentence Embeddings and Semantic Understanding
* Unsupervised Machine Learning
* Event Detection and Clustering
* Timeline Analysis and Visualization

## Dataset Details
This project uses the **News Category Dataset**

The Dataset containing over 209,000 news articles in Json format

Columns Used: 
  - Headlines
  - short_description
  - date

## Architecture

 ↓  **News Dataset**
      
 ↓  **Data Preprocessing**
    (Text Cleaning)
       
 ↓  **Text Preparation**
    (Combine Headline + Description)

 ↓  **Sentence Embedding**
   (Sentence Transformer)

 ↓  **Event Labelling**
   (Assign Event Names/Labels)

 ↓  **Event Clustering**
   (Kmeans Clustering)

 ↓  **Event Timeline Construction**
   (Build Chronological Event Timeline)

 ↓  **Event Summary Generation**
   (Generate Summary for Each Cluster)

 ↓  **Visualization & Dashboard**
   (Streamlit Web Application)
  
## Design Decisions

- Used Sentence Transformers for better semantic understanding
- Selected K-Means for efficient clustering of large datasets
- Combined headline and short description for richer text representation
- Used publication dates for event timeline construction
- Built the dashboard using Streamlit for interactive visualization
- Applied preprocessing techniques to improve clustering quality

## Challenges Faced

- Handling a large news dataset with thousands of articles
- Choosing the optimal number of clusters for K-Means
- Improving semantic similarity between news articles
- Removing noisy and irrelevant text data
- Generating meaningful event labels and summaries
- Managing processing time for sentence embeddings 

## Possible Improvements

- Implement real-time news data streaming
- Add advanced transformer-based summarization models
- Improve event labeling accuracy using NLP techniques
- Support multilingual news articles
- Add interactive timeline and cluster visualizations
- Experiment with advanced clustering algorithms like DBSCAN or HDBSCAN
- Deploy the application on cloud platforms for public access

## Conclusion

This project successfully clusters similar news articles into meaningful events using NLP and Machine Learning techniques. By applying sentence embeddings and K-Means clustering, the system identifies related news topics, generates event summaries, and constructs event timelines. The Streamlit dashboard provides an interactive way to visualize clustered events and analyze news trends effectively.
