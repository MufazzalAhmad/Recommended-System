from flask import Flask,render_template,request
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('table.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommended.html')

@app.route('/recommend_books', methods=['POST'])
def recommend_books():
    user_input = request.form.get('user_input')
    
    if not user_input:
        return render_template('recommended.html', data=[["No input provided."]])
    
    # Normalize user input
    book = user_input.strip().lower()

    # Create a mapping of lowercase titles to original titles
    title_map = {title.lower(): title for title in pt.index}

    if book not in title_map:
        return render_template('recommended.html', data=[["Book not found. Please check the title."]])

    matched_book = title_map[book]
    index = np.where(pt.index == matched_book)[0][0]

    # Get similar books
    similar_books = sorted(
        list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True
    )[1:6]

    data = []
    for i in similar_books:
        item = []
        temp = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)

    return render_template('recommended.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)