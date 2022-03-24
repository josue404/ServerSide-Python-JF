from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/document', methods=['GET'])
def document():
    return render_template('person.html')


@app.route('/document_detail', methods=['POST'])
def document_detail():
    id_document = request.form['id_document']
    title = request.form['title']
    no_pages = request.form['no_pages']
    category = request.form['category']
    author = request.form['author']
    j = Document(id_document=id_document, title=title, no_pages=no_pages, category=category, authors=author)
    model.append(j)
    return render_template('person_detail.html', value=j)


@app.route('/document')
def document():
    data = [(i.id_document, i.title, i.no_pages, i.category, i.author) for i in model]
    print(data)
    return render_template('document.html', value=data)


if __name__ == '__main__':
    app.run(debug=True)
