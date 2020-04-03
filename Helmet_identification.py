# coding:utf-8

from flask import Flask,render_template,request,Response,redirect,url_for
from werkzeug.utils import secure_filename
import os
from functions import single_image_test

app = Flask(__name__)
#主页为上传
@app.route('/')
def index():
    return redirect(url_for('upload'))
#上传图片的页面
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, 'static/uploads/beforeimg',secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        
        return redirect('/imgcontrast/'+secure_filename(f.filename))
    return render_template('upload.html')
#比较图片的页面
@app.route('/imgcontrast/<imgname>')
def imgcontrast(imgname):
    doc=single_image_test(imgname)
    return render_template('imgcontrast.html',imgname=imgname,doc=doc)

if __name__ == '__main__':
    app.run(debug=True)
