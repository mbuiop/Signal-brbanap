#!/bin/bash

# 1. ساخت پوشه‌ها
mkdir -p templates static/{css,js,images}

# 2. ایجاد فایل‌های اصلی
touch app.py database.py requirements.txt

# 3. ایجاد فایل‌های HTML
touch templates/{base.html,index.html,signal.html,analysis.html,ad_form.html,ads_list.html}

# 4. ایجاد فایل‌های استاتیک
touch static/css/style.css static/js/script.js

# 5. نوشتن محتوای پیش‌فرض برای فایل‌های کلیدی

## app.py
cat > app.py << 'EOF'
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
EOF

## templates/base.html
cat > templates/base.html << 'EOF'
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>پروژه Flask</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
EOF

## templates/index.html
cat > templates/index.html << 'EOF'
{% extends "base.html" %}
{% block content %}
<h1>خوش آمدید!</h1>
{% endblock %}
EOF

## static/css/style.css
cat > static/css/style.css << 'EOF'
body {
    font-family: 'Vazir', sans-serif;
    padding: 20px;
}
EOF

## requirements.txt
echo "Flask==2.3.2" > requirements.txt

echo "✅ ساختار پروژه با موفقیت ایجاد شد!"
