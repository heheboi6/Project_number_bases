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
        print("Vă mulțumim că ați folosit aplicația, la revedere!")