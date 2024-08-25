from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.before_request
def redirect_all_requests():
    if request.path != '/' and not ("static" in request.path):
        return redirect('/')

@app.route('/')
def maintenance():
    return render_template('maintenance.html')

if __name__ == '__main__':
    app.run(debug=True)
