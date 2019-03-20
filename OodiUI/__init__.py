import os
from flask import(
    Flask, flash, g, redirect, render_template, request, session, url_for, jsonify)
import sierra
import time
from pathlib import Path
import sqlite3

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
    def start_screen():

        return render_template('start.html')

    @app.route('/main', methods=['POST', 'GET'])
    def search_screen():
        #config = Path("/Users/nulm/Desktop/OodiMir/OodiUI/static/direction.txt")
        #if config.is_file():
        #    os.remove("/Users/nulm/Desktop/OodiMir/OodiUI/static/direction.txt")
        #config2 = Path("/Users/nulm/Desktop/OodiMir/OodiUI/static/home.txt")
        #if config2.is_file():
        #    os.remove("/Users/nulm/Desktop/OodiMir/OodiUI/static/home.txt")
        #if request.method == 'POST':
            #searchterm = request.form['searchfield']
            #error = None
            #send searchterm forward to the sierra api?
            #if result == "":
            #    error = 'Kirjoita hakukenttään avainsana.'
        #flash(error)
        return render_template('base.html')

    @app.route('/term_result', methods=['POST', 'GET'])
    def start():
        searchterm = request.form['searchfield']
        print(searchterm)
        books = sierra.search_shelved_books(searchterm)

        return render_template('search/term_result.html', books = books)
        #return render_template('search/term_result.html', searchterm = searchterm)

    @app.route('/term_result/guidance_term', methods=['POST', 'GET'])
    def guidance_term():
        bookname = request.args.get('title')
        book_id = request.args.get('id')
        #book_id = sierra.add_new_book_mission(id)
        print(bookname)
        print(book_id)

        return render_template('/search/guidance_term.html', bookname = bookname, book_id = book_id)

    @app.route('/guidance_category', methods=['POST', 'GET'])
    def guidance_category():
        #categoryname = request.form['categoryname']
        #print(categoryname)
        categoryname = request.args.get('category')
        section = request.args.get('id')
        print("section", section)
        print("category", categoryname)
        #sierra.insert_into_mission_table(section)

        return render_template('/search/guidance_category.html', categoryname = categoryname, section = section)

    @app.route('/create_arrow', methods=['GET'])
    def create_arrow():
        msg = request.form['foo']
        with open("direction.txt", "w+") as the_file:
            the_file.write('{}'.format(msg))
        return 200

    @app.route('/get_arrow', methods=['GET','POST'])
    def read_arrow():
        arrow = "-"
        config = Path("/Users/nulm/Desktop/OodiMir/OodiUI/static/direction.txt")
        if config.is_file():
            print("file exists")
            f = open("/Users/nulm/Desktop/OodiMir/OodiUI/static/direction.txt", "r")
            #os.remove("/Users/nulm/Desktop/OodiMir/OodiUI/static/direction.txt")
            arrow = f.read()
            arrow = arrow.rstrip('\n')
            return arrow
            #f.close()
        else:
            print("return some arrow")
            return arrow

    @app.route('/guidance', methods=['POST', 'GET'])
    def guide():
        #direction = ''
        book_id = request.args.get('id')
        category = request.args.get('category')
        section_id = request.args.get('category_id')
        print(book_id)
        print(category)
        if book_id != None:
            print("we have an ID!")
            sierra.add_new_book_mission(book_id)
            #send a signal to pick up a book from its location
        else:
            print("we have a category!")
            sierra.insert_into_mission_table(section_id)
            #send a signal to go to a category

        return render_template('/search/guidance.html')


    @app.route('/going_home', methods=['POST', 'GET'])
    def mission_finished():

        return render_template('/search/going_home.html')

    @app.route('/back_home', methods=['POST', 'GET'])
    def go_home():
        msg = "-"
        #look for a file and if the file contains "home" then redirect to the start page
        config = Path("/Users/nulm/Desktop/OodiMir/OodiUI/static/direction.txt")
        if config.is_file():
            print("file exists")
            f = open("/Users/nulm/Desktop/OodiMir/OodiUI/static/direction.txt", "r")
            msg = f.read()
            msg = msg.rstrip('\n')
            return msg
        else:
            print("not home yet")
            return msg

    return app
