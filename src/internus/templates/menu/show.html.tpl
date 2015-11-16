{% extends "partials/layout.html.tpl" %}
{% block content %}
    <div class="menu">
        <h1>Menu</h1>
        <h2>{{ menu.day_d.strftime('%B %d, %Y') }}</h2>
        <dl>
            {% for dish in menu.dishes %}
                <dt>{{ dish }}</dt><dd>-</dd>
            {% endfor %}
        </dl>
    </div>
{% endblock %}
