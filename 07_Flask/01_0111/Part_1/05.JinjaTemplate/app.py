from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 템플릿에 전달할 데이터
    data = {
        'title': 'Flask Jinja Template',
        'user': 'KEINZ',
        'is_admin': True,
        'item_list': ['Item 1', 'Item 2', 'Item 3']
    }
    
    # (1) rendring할 html 파일명 입력
    # (2) html로 넘겨줄 데이터 입력
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
