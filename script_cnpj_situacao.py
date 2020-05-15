from requests import get
import json
from time import sleep


def read_file(filename):
    info = []
    file = open(filename, 'r')
    for line in file:
        cnpj, valid = parse(line)
        info.append(cnpj if valid else None)
    file.close()
    return info


def save_file(filename, data):
    file = open(filename, 'w')
    for line in data:
        file.write(line + '\n')
    file.close()


def parse(raw_cnpj):
    cnpj = raw_cnpj.replace('-', '').replace('/', '').replace('.', '')[:-1]
    return cnpj, len(cnpj) == 14


if __name__ == "__main__":
    data = read_file('cnpj_list')
    results = []
    fail = []
    cont = 1
    for cnpj in data:
        try:
            if cnpj:
                response = get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')
                status = json.loads(response.text).get('situacao')
                results.append(status)
                print(f'CPNJ {cnpj} - {status}')
            else:
                results.append('Inválido')
        except:
            print(f'CNPJ {cnpj} pulado')
            fail.append(cnpj)
        if not cont % 3:
            cont = 1
            sleep(60)
        else:
            cont += 1
    save_file('cnpj_status', results)
    print('\n'.join(fail))
