{% extends "partials/layout.html.tpl" %}
{% block content %}
    <div class="menu">
        <h1>Menu</h1>
        <h2>14 de Novembro de 2005</h2>
        <ul>
            {% for dish in menu.dishes %}
                <li>{{ dish }}</li>
            {% endfor %}
        </ul>
    </div>
{% endblock %}
