def read_data_company(company_data: list) -> None:
    for c in company_data:
        print(f'Firma ochroniarska {c[0]} z miejscowości {c[1]}.')
companies = [
    ["Securitas", "Warszawa"],
    ["Solid Security", "Kraków"],
    ["Konsalnet", "Poznań"],
    ["Juwentus", "Gdańsk"]]
read_data_company(companies)

def add_company(company_data: list) -> None:
    name = input('Podaj nazwę firmy: ')
    location = input('Podaj lokalizację: ')
    company_data.append([name, location])