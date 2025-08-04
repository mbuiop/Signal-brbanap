from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from database import init_db, get_db, save_ad, get_all_ads

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'static/images'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize database
init_db()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signals')
def signals():
    # نمونه سیگنال‌ها (در واقعیت از دیتابیس می‌آید)
    signals = [
        {"id": 1, "pair": "BTC/USDT", "direction": "BUY", "price": "42000", "target": "45000", "stop_loss": "40000"},
        {"id": 2, "pair": "ETH/USDT", "direction": "SELL", "price": "2800", "target": "2600", "stop_loss": "2900"},
        {"id": 3, "pair": "SOL/USDT", "direction": "BUY", "price": "120", "target": "140", "stop_loss": "110"}
    ]
    return render_template('signal.html', signals=signals)

@app.route('/analysis')
def analysis():
    # نمونه تحلیل‌ها (در واقعیت از دیتابیس می‌آید)
    analyses = [
        {"indicator": "RSI", "value": "65", "analysis": "در حال نزدیک شدن به منطقه اشباع خرید"},
        {"indicator": "MACD", "value": "مثبت", "analysis": "سیگنال خرید در تایم فریم روزانه"},
        {"indicator": "میانگین متحرک 50 روزه", "value": "41500", "analysis": "حمایت قوی در این ناحیه"}
    ]
    return render_template('analysis.html', analyses=analyses)

@app.route('/ads/new', methods=['GET', 'POST'])
def new_ad():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        contact = request.form['contact']
        
        # Handle file upload
        if 'image' not in request.files:
            flash('No file uploaded')
            return redirect(request.url)
        
        file = request.files['image']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Save to database
            save_ad(title, description, price, contact, filename)
            
            flash('آگهی با موفقیت ثبت شد!')
            return redirect(url_for('ads_list'))
        
    return render_template('ad_form.html')

@app.route('/ads')
def ads_list():
    ads = get_all_ads()
    return render_template('ads_list.html', ads=ads)

if __name__ == '__main__':
    app.run(debug=True)
