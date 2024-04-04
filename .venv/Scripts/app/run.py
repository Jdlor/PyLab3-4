from flask import Flask, render_template, request
from math import sqrt
import unittest
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("tmeplate.html")
class UravnSolver():
    def isfloat(x):
        try:
            a = float(x)
        except (TypeError, ValueError):
            return False
        else:
            return True

    def uravn(a,b,c):

        if (UravnSolver.isfloat(a) and UravnSolver.isfloat(b) and UravnSolver.isfloat(c)):
            a = float(a)
            b = float(b)
            c = float(c)
            D = b * b - 4 * a * c

            if D > 0:
                x1 = str((-b + sqrt(D)) / (2 * a))
                x2 = str((-b - sqrt(D)) / (2 * a))
                return '2 корня, х1 = ' + x1 + ' x2 = ' + x2
            elif D == 0:
                x1 = str(-b / (2 * a))
                return '1 корень, х= ' + x1

            elif D < 0:
                return 'дискриминант меньше нуля, корней нет'
        elif(a=='' or b=='' or c==''):
            return 'все поля должны быть заполнены'
        else:
            return 'введёные данные должны быть числами (дробные числа следует разделять точкой)'


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        a = request.form.get('a')
        b = request.form.get('b')
        c = request.form.get('c')
        return render_template('tmeplate.html', ans=UravnSolver.uravn(a,b,c))



if __name__ == '__main__':
    app.run()

