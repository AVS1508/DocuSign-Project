import pdfkit

options = {
    'encoding': "UTF-8",
    'custom-header' : [
        ('Accept-Encoding', 'zip')
    ],
    'no-outline': None,
}

pdfkit.from_url('','out.pdf', options=options)