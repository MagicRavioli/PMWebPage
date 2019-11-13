from flask import render_template
# from data.strings import band_full_name


def get_navigation_details():
    return {
        'name': 'Kontakt',
        'section': 'Contact'
    }

# def get_title():
#     return '{} - Kontakt'.format(band_full_name)


def get_summary():
    return render_template('contact_section_summary.html')

# def get_fullcontent():
#     return render_template('', host=get_host())
