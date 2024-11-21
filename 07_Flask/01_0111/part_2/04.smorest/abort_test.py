from flask import Flask, abort

app = Flask(__name__)

@app.route('/example')
def example():
    # 어떠한 조건에서 오류를 발생시키고 처리하는 코드
    error_condition = True

    if error_condition:
        abort(500, description="An error occurred while processing the request.")

    # 에러가 발생하지 않았다면 정상적으로 응답
    return "Success!"

if __name__ == "__main__":
    app.run()