# A modest application
This is a small Django app written for the 2017 Oli Fitness internship. I chose Django because I haven't used it before and I wanted to see how it works.

# A note about Django
I appreciate Django's waterfall approach to url routing. Instead of a monolithic urls document like node.js, the urls are parsed level by level, passing only the portion of the url not matched by previous regex, so the url routes in each app of the django project is bitesized and manageable.