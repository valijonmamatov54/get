from flask import Flask, request, render_template_string, redirect, url_for, session, send_file
import os

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "change-this-secret-key")

PIN_FILES = {
    "1390": "0940-d7fc-1ebd1.pdf",
    "1590": "0940-d7fc-1ebd12doniyor.pdf",
    "1795": "0940-d7fc-1ebd-12es-zohid.pdf",
    "1591": "0940-d7fc-1ebd12sattor.pdf",
    "5191": "0940-d7fc-1ebd12diyorbek.pdf",    
   "9795": "0940-d7fc-1ebd-12es-zohidd.pdf", 
    "5591": "0940-d7fc-1ebd12ruslan.pdf",
    "3482": "0940-d7fc-1ebd-12esz.pdf",
    "8491": "g8he-09a9-d7fc-1ebd12xolbek.pdf",
    "9894": "javohirbaxtiyorov.pdf",
    "5483": "akobirabdumajidov.pdf",
    "6083": "zuhraajurayeva.pdf",
    "7893": "akobir.pdf",
    "4589": "shaxzod.pdf",
    "7579": "ulugbek.pdf",
    "7679": "azimov.pdf",
    "4699": "elomon.pdf",
    "8093": "samandarr.pdf",
    "7079": "rasulbekt.pdf",
    "1079": "firdavss.pdf",
    "6499": "madinabonu.pdf",
    "6090": "diyorbek11.pdf",
    "4195": "diyorbek1112.pdf",
    "9045": "VAFOQULOV11111.pdf",
    "9849": "rirdavssss04.pdf",
    "5095": "davroon07.pdf",
    "8994": "esirgapovsamandar05.pdf",
    "1379": "firdavssss04.pdf",
    "6679": "jahongiir07.pdf",
    "2526": "jasurbeka142aa125.pdf",
    "2022": "diyora99.pdf",
    "6777": "XOLQULOV0101.pdf",
    "6897": "jasurr2004.pdf",
    "6887": "Robiyabonuuu.pdf",
     "6807": "0940-d7fc-1ebdIBROHIM.pdf",
     "6907": "AKOBIRbd12.pdf",
    "3026": "saamandaar.pdf",
    "1023": "kalmanovnaibs.pdf",
     "5678": "ABDUMUTAL.pdf",
    "9876": "jinonnjsgahjs5140.pdf",
    "8967": "QILICHBEKQILICHBEK.pdf",
    "3926": "NARGIZA20.02.2026.pdf",
    "5906": "a-ss1245-121aa-hga.pdf",
    "4226": "0940-d7fc-1fazlidinakbaraliyev.pdf",
    "8534": "asqarnurmamatov.8456.153.pdf",
    "8834": "abdumannobov8745-8574-5847.pdf",
    "6190": "samandaresin0940-d7fc-1ebd12.pdf",
    "5806": "5478_56542-5ads-5647.pdf",
    "2234": "sultanovzafarjoonna02070156.pdf",
    "9118": "XASANBOYEVSANJARBEKRUSTAMJO .pdf",
    "9599": "turdibekovakamolaxon90.pdf",
    "9138": "2a45sa4d4d72a4s.pdf",
    "4998": "2a45sa4d4d72a21534s.pdf",
    "8579": "sherzod2a45sa4d4d72a4s.pdf",
    "8578": "AS22a45sa4d4d72a4s.pdf",
    "1918": "484ASAGGDJ.pdf",
    "4456": "ashhk44656ahsfdaj.pdf",
    "2032": "425115asd1d4fewa2nurbek.pdf",
    "8447": "radshbdgsggasbhgynd2135.pdf",
    "9248": "20415512lazo.pdf",
    "0219": "2a45sa4d4d72a214s.pdf",
    "9955": "275a45sa4d4d72a47214s.pdf",
    "8855": "gdvs545dbf454f7ds514s.pdf",
    "1894": "tesn4555s4d55dds14s.pdf",
    "0199": "0940-d7fc-1ebd1245781.pdf",
    "1994": "2a45sa541289as65ds.pdf",
    "8787": "AFS545D2D45F8F45.pdf",
    


}


LOGO_FILENAME = "dmed.jpg"

TEXTS = {
    'uz': {
        'title': "DMED Hujjatlar",
        'subtitle': "Hujjatni ko‘rish uchun PIN kodni kiriting",
        'btn': "Ochish",
        'err': "PIN kodi noto‘g‘ri! Qayta urinib ko‘ring.",
    },
    'ru': {
        'title': "DMED Документы",
        'subtitle': "Для просмотра документа введите PIN-код",
        'btn': "Открыть",
        'err': "PIN-код неверен! Попробуйте еще раз.",
    },
    'en': {
        'title': "DMED Documents",
        'subtitle': "Enter PIN code to view the document",
        'btn': "Open",
        'err': "Incorrect PIN! Please try again.",
    }
}

FLAGS = {
    'ru': {
        'flag': "https://upload.wikimedia.org/wikipedia/commons/f/f3/Flag_of_Russia.svg",
        'label': "Русский"
    },
    'uz': {
        'flag': "https://upload.wikimedia.org/wikipedia/commons/8/84/Flag_of_Uzbekistan.svg",
        'label': "O'zbekcha"
    },
    'en': {
        'flag': "https://upload.wikimedia.org/wikipedia/commons/a/a5/Flag_of_the_United_Kingdom_%281-2%29.svg",
        'label': "English"
    }
}

HTML_FORM = """
<!DOCTYPE html>
<html lang="{{ lang }}">
<head>
    <meta charset="UTF-8">
    <title>{{ texts['title'] }}</title>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    {% raw %}
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 80px; background: #fcfcfc; }
        .box { display:inline-block; padding:24px 32px;border-radius:12px; background:#fcfcfc;
                }
        .header-logo-row { display:flex; align-items:center; justify-content:space-between;
                          margin-bottom:22px; width:100%; }
        .header-logo-row img { height:44px; width:auto; }

        .lang-menu { position: relative; display: flex; align-items: center; }
        .lang-main-btn { border:none; background:transparent; cursor:pointer; padding:4px;
                         border-radius:50%; transition:box-shadow .2s; }
        .lang-main-btn img { width:26px; height:26px; border-radius:50%;
                            border:1.5px solid #d0d0d0; }
        .lang-main-btn:hover img { border-color:#0596e3; }
        .lang-list { position:absolute; right:0; top:38px; background:#fff; border-radius:14px;
                     box-shadow:0 4px 14px rgba(0,0,0,0.1); padding:6px 0; display:none;
                     z-index:100; min-width:140px; }
        .lang-list.open { display:block; }
        .lang-opt-btn { border:none; background:transparent; display:flex; align-items:center;
                        width:100%; padding:6px 10px; cursor:pointer; transition:background .2s; }
        .lang-opt-btn:hover { background:#f0f7ff; }
        .lang-opt-btn img { width:23px; height:15px; border-radius:15%;
                            margin-right:8px; border:1px solid #eee; }
        .lang-opt-btn span { font-size:15px; color:#333; }
        .lang-opt-btn.selected span { font-weight:bold; color:#0596e3; }

        .pin-row { display:flex; justify-content:center; margin-bottom:25px; gap:16px; }
        .pin-input {
            width:56px;height:56px;font-size:32px;text-align:center;
            border-radius:12px; border:2px solid #99bee2; background:#fff;
            box-shadow:0 2px 8px #0596e322; transition:border-color .2s;
        }
        .pin-input:focus { border-color:#0596e3; outline:none; }

        .btn { margin-top:30px; font-size:20px; padding:10px 70px; background:#0596e3;
              color:#fff;border:none;border-radius:8px; cursor:pointer; }
        .btn:disabled { background:#bbb; color:#fff; cursor:not-allowed; }

        h2 { font-size:26px;}

        .below-img {
            margin-top:25px;
            border-radius:10px;
            box-shadow:0 2px 10px rgba(0,0,0,0.1);
            max-width:320px;
            width:100%;
        }
    </style>
    {% endraw %}
</head>
<body>
    <div class="box">
      <div class="header-logo-row">
        <img src="{{ logo_url }}" alt="DMED Logo">
        <div class="lang-menu">
            <button type="button" class="lang-main-btn" onclick="toggleLangMenu()">
                <img src="{{ flags[lang]['flag'] }}" alt="{{ lang }}">
            </button>
            <div class="lang-list" id="langList">
                {% for code, info in flags.items() %}
                <form method="get">
                  <input type="hidden" name="lang" value="{{ code }}">
                  <button type="submit" class="lang-opt-btn {% if lang == code %}selected{% endif %}">
                    <img src="{{ info['flag'] }}" alt="{{ code }}">
                    <span>{{ info['label'] }}</span>
                  </button>
                </form>
                {% endfor %}
            </div>
        </div>
      </div>

      <h2>{{ texts['subtitle'] }}</h2>

      {% if message %}
        <p style="color:red; margin-top:10px;">{{ message }}</p>
      {% endif %}

      <form method="post" style="display:flex;flex-direction:column;align-items:center;">
        <div class="pin-row">
          <input type="text" maxlength="1" name="pin1" class="pin-input" required autofocus inputmode="numeric" pattern="[0-9]">
          <input type="text" maxlength="1" name="pin2" class="pin-input" required inputmode="numeric" pattern="[0-9]">
          <input type="text" maxlength="1" name="pin3" class="pin-input" required inputmode="numeric" pattern="[0-9]">
          <input type="text" maxlength="1" name="pin4" class="pin-input" required inputmode="numeric" pattern="[0-9]">
        </div>
        <button class="btn" type="submit" id="openBtn" disabled>{{ texts['btn'] }}</button>
      </form>

      <img src="{{ url_for('static', filename='dme.jpg') }}" alt="PIN code location" class="below-img">
    </div>

    {% raw %}
    <script>
    const pins = document.querySelectorAll('.pin-input');
    const openBtn = document.getElementById('openBtn');
    pins.forEach((input,idx) => {
        input.addEventListener('input',function(){
            if (this.value && idx < pins.length-1) pins[idx+1].focus();
            openBtn.disabled = ![...pins].every(inp=>inp.value);
            if ([...pins].every(inp=>inp.value)) {
                setTimeout(()=> this.closest('form').submit(), 120);
            }
        });
        input.addEventListener('keydown',function(e){
            if(e.key==='Backspace' && !this.value && idx>0)pins[idx-1].focus();
        });
    });

    function toggleLangMenu() {
        const list = document.getElementById('langList');
        list.classList.toggle('open');
        if(list.classList.contains('open')){
            setTimeout(() => document.addEventListener('click', closeLangList, { once:true }), 100);
        }
    }
    function closeLangList(e){
        const list = document.getElementById('langList');
        if(!list.contains(e.target)){
            list.classList.remove('open');
        }
    }
    </script>
    {% endraw %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    lang = request.values.get('lang', 'uz')
    if lang not in TEXTS:
        lang = 'uz'
    texts = TEXTS[lang]
    message = ""
    logo_url = url_for('static', filename=LOGO_FILENAME)

    if request.method == "POST":
        pin = request.form['pin1'] + request.form['pin2'] + request.form['pin3'] + request.form['pin4']
        if pin in PIN_FILES:
            session['authenticated'] = pin
            return redirect(url_for('pdf_full'))
        else:
            message = texts['err']

    return render_template_string(HTML_FORM, texts=texts, lang=lang,
                                  message=message, flags=FLAGS, logo_url=logo_url)

@app.route("/pdf_full")
def pdf_full():
    pin = session.get('authenticated')
    if not pin or pin not in PIN_FILES:
        return redirect(url_for('index'))

    pdf_url = url_for('serve_pdf', pin=pin)
    HTML_PDF = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      <title>DMED Documents</title>
      <style>
        html, body {{ height: 95%; margin: 0; padding: 0; background: #000; }}
        .viewer {{ position: fixed; inset: 0; width: 95%; height: 95%; border: none; }}
      </style>
    </head>
    <body>
      <iframe class="viewer" src="{pdf_url}" frameborder="0" allowfullscreen></iframe>
    </body>
    </html>
    """
    return HTML_PDF

@app.route("/view/<pin>")
def serve_pdf(pin):
    if pin not in PIN_FILES or session.get("authenticated") != pin:
        return redirect(url_for('index'))

    pdf_path = os.path.join("static", PIN_FILES[pin])
    if not os.path.exists(pdf_path):
        return "PDF topilmadi", 404

    return send_file(
        pdf_path,
        mimetype="application/pdf",
        as_attachment=False,
        download_name="document.pdf",
        conditional=True
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
