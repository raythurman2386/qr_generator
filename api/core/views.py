from flask import Blueprint, render_template, request
from flask_login import login_required
from io import BytesIO
from base64 import b64encode
import qrcode

core_bp = Blueprint("core", __name__)


@core_bp.route("/")
@login_required
def home():
    return render_template("core/index.html")


@core_bp.route('/api/generated', methods=['POST'])
@login_required
def generate():
    memory = BytesIO()
    text = request.form.get('text')
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(memory)
    memory.seek(0)

    base64_img = "data:image/png;base64," + \
        b64encode(memory.getvalue()).decode('ascii')

    return render_template('core/index.html', data=base64_img)