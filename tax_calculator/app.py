from flask import Flask, render_template, request
import math

app = Flask(__name__)


class Calculate:
    def __init__(self, name, pan, dob, number, institute, designation, year,
                 gross, pTax, hra, hli, ao1,
                 sbi, ifi, tds, pension, ao2,
                 gpf, gsli, lic, hlp, tuition, ao3,
                 self80d, parents80d, sbi80tta, nps, ao4):
        self.name = name
        self.pan = pan
        self.dob = dob
        self.number = number
        self.institute = institute
        self.designation = designation
        self.year = year
        self.gross = gross
        self.pTax = pTax if pTax != "" else "0"
        self.hra = hra if hra != "" else "0"
        self.hli = hli if hli != "" else "0"
        self.ao1 = ao1 if ao1 != "" else "0"
        self.sbi = sbi if sbi != "" else "0"
        self.ifi = ifi if ifi != "" else "0"
        self.tds = tds if tds != "" else "0"
        self.pension = pension if pension != "" else "0"
        self.ao2 = ao2 if ao2 != "" else "0"
        self.gpf = gpf if gpf != "" else "0"
        self.gsli = gsli if gsli != "" else "0"
        self.lic = lic if lic != "" else "0"
        self.hlp = hlp if hlp != "" else "0"
        self.tuition = tuition if tuition != "" else "0"
        self.ao3 = ao3 if ao3 != "" else "0"
        self.self80d = self80d if self80d != "" else "0"
        self.parents80d = parents80d if parents80d != "" else "0"
        self.sbi80tta = sbi80tta if sbi80tta != "" else "0"
        self.nps = nps if nps != "" else "0"
        self.ao4 = ao4 if ao4 != "" else "0"
        self.std_deduction = str(
            int(self.gross) - 50000) if int(self.gross) - 50000 > 0 else self.gross
        self.head = str(int(self.std_deduction) -
                        (int(self.hra) + int(self.pTax) + int(self.ao1)))
        self.total_in = str(int(self.head) + int(self.sbi) + int(self.ifi) + int(self.pension) + int(self.tds) +
                            int(self.ao2))
        self.gross_total = str(int(self.total_in) - int(self.hli))
        self.total_a_f = str(int(self.gpf) + int(self.gsli) + int(self.lic) + int(self.hlp) + int(self.tuition) +
                             int(self.ao3))
        self.total_a_f_max = self.total_a_f if int(
            self.total_a_f) <= 150000 else "150000"
        self.self80d_max = self.self80d if int(
            self.self80d) <= 25000 else "25000"
        self.parents80d_max = self.parents80d if int(
            self.parents80d) <= 25000 else "25000"
        self.sbi80tta_max = self.sbi80tta if int(
            self.sbi80tta) <= 10000 else "10000"
        self.nps_max = self.nps if int(self.nps) <= 50000 else "50000"
        self.total_i_iv = str(int(self.self80d) + int(self.parents80d) + int(self.sbi80tta) + int(self.nps) +
                              int(self.ao4))
        self.total_i_iv_max = str(int(self.self80d_max) + int(self.parents80d_max) + int(self.sbi80tta_max) +
                                  int(self.nps_max) + int(self.ao4))
        self.taxable_income = str(
            int(self.gross_total) - int(self.total_a_f_max) - int(self.total_i_iv_max))
        self.round_off = str(int(self.taxable_income) -
                             int(math.remainder(int(self.taxable_income), 10)))
        temp1 = int(self.round_off) - 250000
        temp2 = 12500 if temp1 >= 250000 else (temp1*5)/100
        self.tax1 = str(max(0, temp2))
        temp3 = int(self.round_off) - 500000
        temp4 = 100000 if temp3 >= 500000 else (temp3*20)/100
        self.tax2 = str(max(0, temp4))
        temp5 = int(self.round_off) - 1000000
        self.tax3 = str(max((temp5*30)/100, 0))
        self.tax_payable = str(
            float(self.tax1) + float(self.tax2) + float(self.tax3))
        self.less = self.tax_payable if float(
            self.tax_payable) - 12500 >= 0 else "0"
        self.hec = str(round((float(self.less) * 4) / 100))
        self.net_income_tax = str(float(self.less) + float(self.hec))
        temp6 = self.year.split('-')
        self.f_year = str(int(temp6[0]) - 1) + '-' + temp6[0]
        self.date = temp6[0][2:]


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route("/download", methods=['GET', 'POST'])
def downloads():
    if request.method == 'POST':
        name = request.form['name']
        pan = request.form['pan']
        dob = request.form['dob']
        number = request.form['number']
        institute = request.form['institute']
        designation = request.form['designation']
        year = request.form['year']
        gross = request.form['gross']
        pTax = request.form['pTax']
        hra = request.form['hra']
        hli = request.form['hli']
        ao1 = request.form['ao1']
        sbi = request.form['sbi']
        ifi = request.form['ifi']
        tds = request.form['tds']
        pension = request.form['pension']
        ao2 = request.form['ao2']
        gpf = request.form['gpf']
        gsli = request.form['gsli']
        lic = request.form['lic']
        hlp = request.form['hlp']
        tuition = request.form['tuition']
        ao3 = request.form['ao3']
        self80d = request.form['self80d']
        parents80d = request.form['parents80d']
        sbi80tta = request.form['sbi80tta']
        nps = request.form['nps']
        ao4 = request.form['ao4']
        data = Calculate(name, pan, dob, number, institute, designation, year, gross, pTax, hra, hli, ao1, sbi, ifi,
                         tds, pension, ao2, gpf, gsli, lic, hlp, tuition, ao3, self80d, parents80d, sbi80tta, nps, ao4)
        return render_template('compute.html', data=data)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
