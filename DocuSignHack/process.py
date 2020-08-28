import pdfkit
import cgi
import cgitb 
cgitb.enable() 

data = cgi.FieldStorage()
first_name = data.getvalue('firstName')
last_name  = data.getvalue('lastName')

print("Content-Type: text/html\n")
print("<html><head><title>Hello - Second CGI Program</title></head><body><h2>Hello %s %s</h2>" % (first_name, last_name))
print("</body></html>")

# options = {
#     'encoding': "UTF-8",
#     'custom-header' : [
#         ('Accept-Encoding', 'zip')
#     ],
#     'no-outline': None,
# }

# pdfkit.from_url('','out.pdf', options=options)