from django.shortcuts import render
from react.render import render_component
import os

def index(request):
    rendered = render_component(os.path.join(os.getcwd()+'/hello_world/static/js/hello.jsx'),{},to_static_markup=True)
    return render(request,'hello_world/index.html', {'component': rendered })
