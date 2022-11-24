import datetime


def check_judet(cnp):
    judet = cnp[7] + cnp[8]
    judet = int(judet)
    if judet in range(1, 47) or judet in range(51, 53):
        return True
    return False


def check_luna(cnp):
    local = int(cnp[3]) * 10 + int(cnp[4])
    if 0 < local < 13:
        return True
    return False


def check_sex(cnp):
    sex = int(cnp[0])
    if sex > 10:
        return False
    else:
        return True


def check_date(cnp):
    def check_an(cnp):
        local = int(cnp[1] + cnp[2])
        return local

    def check_luna(cnp):
        local = int(cnp[3] + cnp[4])
        return local

    def check_zi(cnp):
        local = int(cnp[5] + cnp[6])
        return local

    an = check_an(cnp)
    luna = check_luna(cnp)
    zi = check_zi(cnp)
    try:
        x = datetime.datetime(an, luna, zi)
        return True
    except Exception:
        return False


def cifra_control(cnp):
    cod = '279146358279'
    suma = 0
    for index, value in enumerate(cnp):
        if (index <= 11):
            suma += int(value) * int(cod[index])
    rezultat = suma % 11
    if rezultat == 10:
        rezultat = 1
    else:
        rezultat = suma % 11

    return rezultat == int(cnp[12])


def check_cifre(cnp):
    if len(cnp) == 13:
        try:
            a = int(cnp)
            if a > 0:
                return True
            return False
        except ValueError:
            return False
    else:
        return False


def check_000(cnp):
    if cnp[9] == 0 and cnp[10] == 0 and cnp[11] == 0:
        return False
    return True
    # pentru singura exceptia la NNN


def validare_buletin(cnp):
    conditii_1 = check_judet(cnp) and check_luna(cnp) and check_sex(cnp) and check_000(cnp)
    conditii_2 = check_date(cnp) and cifra_control(cnp) and check_cifre(cnp)

    return conditii_1 and conditii_2


cod_buletin = input("Introduceti cnp ul")


print(validare_buletin(cod_buletin))