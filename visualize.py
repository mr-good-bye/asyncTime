import json
import matplotlib.pyplot as plt


with open('res.json', 'r') as file:
    res = dict(json.load(file))


_res = {}
for k, v in res.items():
    m, n = k.split()
    n = float(n)
    if m in _res:
        _res[m][n] = v
    else:
        _res[m] = {}
print(_res.keys())


def visual_low():
    colors = 'bgrcmyk'
    i = 0
    for mode in _res.keys():
        plt.plot(list(_res[mode].keys())[:4], list(_res[mode].values())[:4], colors[i], label=mode)
        i += 1
    plt.legend()
    plt.savefig('visual_low.png', format='png')
    plt.show()


def visual():
    colors = 'bgrcmyk'
    i = 0
    for mode in _res.keys():
        plt.plot(_res[mode].keys(), _res[mode].values(), colors[i], label=mode)
        i += 1
    plt.legend()
    plt.savefig('visual.png', format='png')
    plt.show()


def data():
    m = max(_res['one'].keys())
    for mode in _res.keys():
        print(f'\'{mode}\''.rjust(9) + f'faster than \'one\' by {_res["one"][m]/_res[mode][m]}')


visual()
visual_low()
data()
