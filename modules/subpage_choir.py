from flask import render_template
from data.strings import band_full_name

def get_navigation_details():
    return {
        'name': 'Chór',
        'section': 'Choir',
        'subpage': 'choir',
        'submenu': {
            'About': 'O nas',
            'Conductor': 'Dyrygent',
            'ChoirMembers': 'Chórzyści'
        }
    }

def get_title():
    return '{} - O nas'.format(band_full_name)    

def get_summary():
    return render_template('choir_section_summary.html')

def get_fullcontent():
    return render_template('choir_sections.html')
