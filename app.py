from django.db import models
from nanodjango import Django

app = Django()
@app.admin
class Order(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

@app.route("/")
def order_form(request):
    return f"<p>This is the order form :)</p>"

# TODO Order API

# TODO Part API

# TODO Preview API
