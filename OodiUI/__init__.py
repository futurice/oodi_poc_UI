import os
#importtaa sierra

from flask import(
    Flask, flash, g, redirect, render_template, request, session, url_for)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path) #ensure the instance folder exists
    except OSError:
        pass

    @app.route('/', methods=['POST', 'GET'])
    def search_screen():
        if request.method == 'POST':
            searchterm = request.form['searchfield']
            error = None
            print("jee")
            #send searchterm forward to the sierra api?
            #if result == "":
            #    error = 'Kirjoita hakukenttään avainsana.'

            #if error is None:
            ##else:
                #insert method to fetch information from sierra api HERE!!
            ##    print('ei virheitä hienoa!!!')
            ##    return render_template('search/results.html', haku_result = result ) #render to the template with the results
                #return redirect(url_for('search.term_results')) #render temp
            flash(error)
        return render_template('base.html')

    @app.route('/term_result', methods=['POST', 'GET'])
    def start():
        #searchterm = request.form['searchfield']
        #print(searchterm)
        books = { 1469241: {'title': 'Frantsilan yrttitilan kasviskeittokirja', 'author': 'Raipala-Cormier, Virpi'},
        2251846: {'title': 'Uusimaa kuvissa : tarinoita ja tunnelmia Karkkilasta, Loviisasta, Porvoosta ja Vihdistä', 'author': 'Joku tyyppi'}}
        #ask sierra for the results
        return render_template('search/term_result.html', books = books)

        #return render_template('search/term_result.html', searchterm = searchterm)

    @app.route('/term_result/guidance_term', methods=['POST', 'GET'])
    def guidance_term():
        bookname = request.args.get('title')
        book_id = request.args.get('id')
        print(bookname)
        print(book_id)

        return render_template('/search/guidance_term.html', bookname = bookname, book_id = book_id)

    @app.route('/guidance_category', methods=['POST', 'GET'])
    def guidance_category():
        #categoryname = request.form['categoryname']
        #print(categoryname)
        categoryname = request.args.get('category')
        print("category", categoryname)

        return render_template('/search/guidance_category.html', categoryname = categoryname)

    #from . import search
    #app.register_blueprint(search.bp)

    @app.route('create_arrow', methods=['GET'])
    def create_arrow():
        #msg = request.form['foo'] UNCOMMENT THIS
        with open("direction.txt", "w+") as the_file:
            the_file.write('{}'.format(msg))
        #close file
        return 200

    @app.route('get_arrow', )
    def read_arrow():
        with open("direction.txt", "r") as the_file:
            arrow = the_file.read()

        return redirect(url_for('/guidance'), arrow = arrow)

    @app.route('/guidance', methods=['POST', 'GET'])
    def guide():
        direction = ''
        book_id = request.args.get('id')
        category = request.args.get('category')
        print(book_id)
        print(category)
        if book_id != None:
            print("we have an ID!")
            #send a signal to pick up a book from its location
        else:
            print("we have a category!")
            #send a signal to go to a category

        #if direction == 'left':
        #    return redirect(url_for('/guidance', direction = direction))
        #elif direction == 'right':
    #        return redirect(url_for('/guidance', direction = direction))
    #    elif direction == 'forward':
    #        return redirect(url_for('/guidance', direction = direction))
    #    else:
        #initiate the guiding scenario
        #if signal comes back, go to feedback section
        return render_template('/search/guidance.html', direction = direction)
    return app
