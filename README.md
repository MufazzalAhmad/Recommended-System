# Book Recommendation System

## Data Description

We've three dataset -
• Book data – (ISBN, Book-Title, Book-Author, Year-Of-Publication, Publisher, Image-URL-S, Image-URL-M, Image-URL-L)
• Users data - (User-ID, Location, Age)
• Ratings data - (User-ID, ISBN, Book-Rating)

Dataset: You can download the dataset from this repo

## Summary of Project

We started with data cleaning, feature engineering, and EDA on the book dataset.

Then, we built a popularity-based recommendation system by merging book and rating data, selecting only books with more than 250 ratings. We displayed the Top 50 highest-rated books.

Next, we implemented Collaborative Filtering using a memory-based approach:

Selected users who rated more than 200 books and books rated by over 50 users.
Applied cosine similarity to find similar items (item-based filtering).
Generated predictions based on similarity scores.
Finally, we created a recommend() function that takes a book name as input and returns 4 similar books with authors.

## Reference Images
<img width="1855" height="880" alt="Screenshot 2025-08-04 154756" src="https://github.com/user-attachments/assets/d73a16bb-654a-4a63-9fc1-5d8d9d686518" />



<img width="1848" height="883" alt="Screenshot 2025-08-04 154829" src="https://github.com/user-attachments/assets/46da77e2-5401-4132-984d-798797c2bd07" />

