"""
Acest modul din program este folosit pentru validarea datelor introduse de utilizator la citire, și conține funcții care sunt folosite
pentru a verifica dacă utilizatorul a introdus tipul corect de date.

Modulul include funcții care validează datele introduse de utilizator când introduce de la tastatură o opțiune în meniu, un număr sau o bază de numerație.
"""
def validare_optiune_meniu(optiune : str, numar_optiuni_meniu : int) -> bool:
    """
    Această funcție primește un șir de caractere ca parametru și numărul de opțiuni dintr-un anumit meniu, și verifică dacă acel șir de caractere reprezintă o opțiune validă în meniu.
    optiune - un șir de caractere, reprezintă opțiunea introdusă de utilizator care trebuie validată
    numar_optiuni_meniu - un număr întreg, 
    """