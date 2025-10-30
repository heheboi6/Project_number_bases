"""
Acest modul din program este folosit pentru a gestiona toată interfața aplicației, care este făcută din mesaje în consolă.

Modulul include funcții pentru a citi diferite tipuri de date în program, și funcții care afișează diverse mesaje care apar în meniu,
la introducerea datelor pentru o anumită funcționalitate sau atunci când programul returnează rezultatul unei operații alese de
utilizator.
"""
def afiseaza_mesaj_intrare_in_aplicatie():
    """
    Această funcție afișează un mesaj de bun-venit în consolă cu ajutorul unei instrucțiuni print(), și nu returnează nimic.
    """
    print("Bine ați venit în aplicație!\n")
def afiseaza_autor_aplicatie():
    """
    Această funcție afișează autorul aplicației în consolă cu ajutorul unei instrucțiuni print(), și nu returnează nimic.
    """
    print("Autorul acestei aplicații este studentul Budiul Alexandru Vasile.\n")
def afiseaza_meniu_principal():
    """
    Această funcție afișează meniul principal în consolă cu ajutorul unor instrucțiuni print(), și nu returnează nimic.
    """
    print("Vă rugăm alegeți o opțiune din meniu:")
    print("1. Efectuează operații aritmetice între numere dintr-o bază introdusă de la tastatură;")
    print("2. Transformă un număr dintr-o bază în alta cu ajutorul a mai multor metode de conversie;")
    print("3. Ieșire din aplicație;")
def afiseaza_mesaj_iesire_din_aplicatie():
    """
    Această funcție afișează un mesaj de rămas-bun în consolă cu ajutorul unei instrucțiuni print(), și nu returnează nimic.
    """
    print("Vă mulțumim că ați folosit aplicația, la revedere!")
def run():
    """
    Această funcție a programului a fost făcută pentru a rula meniul principal al programului, pentru a afișa meniul, și pentru a apela funcțiile referitoare celorlalte meniuri.
    De asemenea, această funcție nu returnează nimic, doar afișează mesaje în consolă.
    """
    try:
        aplicatie_pornita = True
        afiseaza_mesaj_intrare_in_aplicatie()
        afiseaza_autor_aplicatie()
        while aplicatie_pornita:
            afiseaza_meniu_principal()
    except KeyboardInterrupt:
        afiseaza_mesaj_iesire_din_aplicatie()