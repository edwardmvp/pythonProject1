from flask import Flask, render_template, request, escape, session

def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))

app = Flask(__name__)
@app.route('/test')
def test() -> 'html':
    return render_template('test.html',
                           the_title="Тест отправки")
@app.route('/test-results', methods=['POST'])
def testPost() -> 'html':
    your_name = request.form['your_name']
    return render_template('test-results.html',
                           your_name = your_name,
                           the_title = "Результат")
@app.route('/')
def hello() -> str:
    return 'Hello world from Flask'

@app.route('/viewlog')
def view_the_log()->'html':
    contents = []
    with open('venv/log.txt') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Result')
    return render_template('viewlog.html',
                            the_title='View Log',
                            the_row_titles = titles,
                            the_data=contents,)


def log_request(req: 'flask_request', res: str)-> None:
    log_request = open('venv/log.txt', 'a')
    print(req, file=log_request)
    print(res, file=log_request)
    log_request.close()


@app.route('/search4', methods=['POST'])
def do_search()-> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results: '
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase = phrase,
                           the_letters = letters,
                           the_title = title,
                           the_results = results)
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Welcome")
app.run()

