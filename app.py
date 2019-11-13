from flask import Flask, url_for, redirect, render_template, request, Markup, send_from_directory
from flask_restful import Api, Resource
from data.strings import band_full_name
import modules.subpage_choir as subpage_choir
import modules.subpage_contact as subpage_contact

app = Flask(__name__)
api = Api(app)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)

@app.route('/favicon.ico')
def send_favicon():
    return send_from_directory('static', 'favicon.ico')

def render_navlinks(is_main_page):
    return render_template('navlinks.html', main_page=is_main_page, links=[
            subpage_choir.get_navigation_details(),
            subpage_contact.get_navigation_details(),
    ])

def render_fullpage(is_main_page, title, content, styles=[]):
    styles = render_template('style_links.html', style_files=['static/main.css', 'static/colors.css', *styles])
    navlinks = render_navlinks(is_main_page)

    return render_template('fullpage.html',
        styles=Markup(styles),
        title=title,
        navlinks=Markup(navlinks),
        content=Markup(content))

@app.route('/')
@app.route('/home')
def index():
    sections = '\n'.join([
        subpage_choir.get_summary(),
        subpage_contact.get_summary()
    ])
    content = render_template('home_sections.html', sections=Markup(sections))
    return render_fullpage(True, band_full_name, content, styles = [
        'static/contact.css',
    ])

@app.route('/choir')
def render_choir():
    content = subpage_choir.get_fullcontent()
    return render_fullpage(False, subpage_choir.get_title(), content)

@app.route('/get_mail')
def get_mail():
    return 'chorpiumosso@gmail.com'

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 1234)
