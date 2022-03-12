# r4_functions.py - funkcje dodatkowe

def ok_module_info(names):
    print(f"Moduły: {', '.join(names)} – zainstalowano poprawnie!")
    print("Super! Możemy działać....")


def error_module_info(name):
    print(f"{name}")
    print("Instalacja poleceniem: pip install", name[16:].replace("'", ""))
    print("-----------------------")
    return False


def get_horizon_data(nasaids, names, colors, sizes, start_date="2018-01-01"):
    """nasaids = [1, 2, 3, 4]
    funkcja bazuje na projekcie https://github.com/chongchonghe/Python-solar-system"""

    from astropy.time import Time
    from astroquery.jplhorizons import Horizons
    from numpy import double

    data = {
        "info": "Baza danych o pozycjach i prędkości planet w określonym dniu",
        "date": start_date,
    }

    for i, nasaid in enumerate(nasaids):
        obj = Horizons(
            id=nasaid, location="@sun", epochs=Time(start_date).jd, id_type="id"
        ).vectors()

        print("----------------------------------------------------------------")
        print(f"Pobieramy dane dla {names[i]}:")
        print(obj)

        data[nasaid] = {
            "name": names[i],
            "size": sizes[i],
            "color": colors[i],
            "r": [double(obj[xi]) for xi in ["x", "y", "z"]],
            "v": [double(obj[vxi]) for vxi in ["vx", "vy", "vz"]],
        }
    return data


if __name__ == "__main__":
    print("To jest moduł dodatkowy dla rozdziału 4.")
