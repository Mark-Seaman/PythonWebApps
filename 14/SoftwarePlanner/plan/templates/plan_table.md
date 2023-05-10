# PLAN PROJECT

|{% for m in milestones %}
    * {{ m.0 }}
    {% for r in m.1 %}     
        * {{ r.0 }}
        {% for d in r.1 %}* {{ d }}{% endfor %}
    {% endfor %}
{% endfor %}