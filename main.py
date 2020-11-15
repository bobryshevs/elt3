from plot import buildPlot
from math import sqrt, pi, atan


def to_file(experiment_type: str, ach: list, fch: list, f_nu):
    answer = f'{experiment_type}\n' \
             f'f\tФЧХ\tАЧХ\n'
    for f in f_nu:
        tmp = f'{f}\t{round(fch[f], 3)}\t{round(ach[f], 3)}\n'
        answer += tmp

    with open(f'./Таблицы/{experiment_type}.txt', 'w') as file:
        file.write(answer)


def getACH_RC(f_ch: list, r: float, c: float):
    k = []
    for f in f_ch:
        tmp = 1 / sqrt(1 + (2 * pi * f * r * c) * (2 * pi * f * r * c))
        k.append(tmp)
    return k


def getFCH_RC(f_ch: list, r: float, c: float):
    fi = []
    for f in f_ch:
        tmp = 1 + (-atan(2 * pi * f * r * c)) / pi * 2
        fi.append(tmp)
    return fi


def getACH_CR(f_ch: list, r: float, c: float):
    k = []
    for f in f_ch:
        tmp = r * 2 * pi * f * c / sqrt(r * 2 * pi * f * c * r * 2 * pi * f * c + 1)
        k.append(tmp)
    return k


def getFCH_CR(f_ch: list, r: float, c: float):
    fi = []
    for f in f_ch:
        tmp = (pi / 2 - atan(2 * pi * f * r * c))/pi * 2
        fi.append(tmp)
    return fi


def getACH_RL(f_ch: list, r: float, l: float):
    k = []
    for f in f_ch:
        tmp = (2 * pi * f * l) / sqrt(r * r + 2 * pi * f * l * 2 * pi * f * l)
        k.append(tmp)
    return k


def getFCH_RL(f_ch: list, r: float, l: float):
    fi = []
    for f in f_ch:
        tmp = (pi / 2 - atan(2 * pi * f * l / r)) / pi * 2
        fi.append(tmp)
    return fi


def getACH_LR(f_ch: list, r: float, l: float):
    k = []
    for f in f_ch:
        tmp = r / sqrt(2 * pi * f * l * 2 * pi * f * l + r * r)
        k.append(tmp)
    return k


def getFCH_LR(f_ch: list, r: float, l: float):
    fi = []
    for f in f_ch:
        tmp = 1 + (-atan(2 * pi * f * l))/pi*2
        fi.append(tmp)
    return fi


def R_C():
    # R-C
    R = float(input("R_[Om] = "))
    C = float(input("C_[mkF] = ")) * 10 ** -6
    f = [int(i) for i in range(5000)]
    K = getACH_RC(f, R, C)
    fi = getFCH_RC(f, R, C)
    buildPlot(x=f, y=K, table_name='АЧХ R-C', x_lbl='f', y_lbl='K', label='АЧХ')
    buildPlot(x=f, y=fi, table_name="ФЧХ R-C", x_lbl='f', y_lbl='φ', label='ФЧХ')
    to_file('R-C', K, fi, f)


def C_R():
    # C-R
    R = float(input("R_[Om] = "))
    C = float(input("C_[mkF] = ")) * 10 ** -6
    f = [int(i) for i in range(5000)]
    K = getACH_CR(f, R, C)
    fi = getFCH_CR(f, R, C)
    buildPlot(x=f, y=K, table_name="АЧХ C-R", x_lbl='f', y_lbl='K', label='АЧХ')
    buildPlot(x=f, y=fi, table_name="ФЧХ C-R", x_lbl='f', y_lbl='φ', label='ФЧХ')
    to_file('C-R', K, fi, f)


def R_L():
    # R-L
    R = float(input("R_[Om] = "))
    L = float(input("L_[mGn] = ")) * 10 ** -3
    f = [int(i) for i in range(1000)]
    K = getACH_RL(f, R, L)
    fi = getFCH_RL(f, R, L)
    buildPlot(x=f, y=K, table_name='АЧХ R-L', x_lbl='f', y_lbl='K', label='АЧХ')
    buildPlot(x=f, y=fi, table_name='ФЧХ R-L', x_lbl='f', y_lbl='φ', label='ФЧХ')
    to_file('R-L', K, fi, f)


def L_R():
    # L-R
    R = float(input("R_[Om] = "))
    L = float(input("L_[mGn] = ")) * 10 ** -3
    f = [int(i) for i in range(1000)]
    K = getACH_LR(f, R, L)
    fi = getFCH_LR(f, R, L)
    buildPlot(x=f, y=K, table_name='АЧХ L-R', x_lbl='f', y_lbl='K', label='АЧХ')
    buildPlot(x=f, y=fi, table_name='ФЧХ L-R', x_lbl='f', y_lbl='φ', label='ФЧХ')
    to_file('L-R', K, fi, f)


def main():
    while True:
        functions = [R_C, C_R, R_L, L_R]
        try:
            us_change = int(input("R-C ->  [0]\n"
                                  "C-R ->  [1]\n"
                                  "R-L ->  [2]\n"
                                  "L-R ->  [3]\n"
                                  "exit -> [4]\n"
                                  "Your change --> "))
            if us_change == 4:
                return
            functions[us_change]()

        except:
            pass


if __name__ == '__main__':
    main()
