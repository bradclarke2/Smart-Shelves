testthepythonintegration = """
{% extends "personal/header.html" %}

{% block content %}
    {% for c in content %}
        <p>{{c}}</p>
    {% endfor%}

{% endblock %}    
"""

Html_file= open("mysite/personal/templates/personal/basic.html","w")
Html_file.write(testthepythonintegration)
Html_file.close()