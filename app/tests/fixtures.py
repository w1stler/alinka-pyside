from datetime import date, datetime

child_data = {
    "full_name": "Wiktor Rzeźniczak",
    "full_name_gen": "Wiktora Rzeźniczaka",
    "pesel": "12121244441",
    "birth_date": "2012-12-24",
    "birth_place": "Pachy Wielkie",
    "town": "Poznań",
    "postal_code": "61-854",
    "address": "Mostowa 38",
    "klass": "3b",
    "profession": "murarz",
    "student": True,
}

school_data = {
    "school_type": "Szkoła podstawowa",
    "school_name": "Szkoła Podstawowa nr 4 w Grodzisku Wlkp.",
    "postal_code": "62-222",
    "town": "Grodzisk Wlkp.",
    "address": "ul. Jasna 33",
}

applicants_data = [
    {
        "full_name": "Tomasz Rzeźniczak",
        "full_name_gen": "Tomasza Rzeźniczaka",
        "town": "Studnia",
        "postal_code": "55-789",
        "address": "Wielka 4/6",
    },
    {
        "full_name": "Adelajda Słoneczko",
        "full_name_gen": "Adelajdy Słoneczko",
        "town": "Sadowisko",
        "postal_code": "15-671",
        "address": "Odnowy Stare, ul. Zamkowa 15/6a",
    },
]

meeting_data = {
    "date": "2019-07-15",
    "time": "16:00",
    "members": [
        {"name": "Antoni Stąsz-Lebieź", "function": "przewodniczący zespołu"},
        {"name": "mgr Leonia Witek-Konuś", "function": "psycholog, tyflopedagog"},
        {"name": "mgr Eleonora Roseveelt", "function": "socjoterapeuta, tyflopedagog"},
    ],
}

support_center_data = {
    "name_nominative": "Poradnia Psychologiczno - Pedagogiczna w Poznaniu",
    "name_genetive": "Poradni Psychologiczno - Pedagogicznej w Poznaniu",
    "institute_name": "Zespół Orzekający przy Poradni Psychologiczno-Pedagogicznej w Poznaniu",
    "town": "Poznań",
    "postal_code": "12-345",
    "address": "ul. Zbąszyńska 11",
    "kurator": "Poznaniu, ul Kościuszki 38, 64-400 Poznań",
}

common_data = {
    "address_child_checkbox": False,
    "addres_first_parent_checkbox": False,
    "issue": "specjalne",
    "period": "nauki w klasach I - III",
    "reasons": ["umiarkowane"],
    "activity_form": "indywidualne",
    "decision_no": "42",
    "child": child_data,
    "school": school_data,
    "applicants": applicants_data,
    "meeting_data": meeting_data,
    "support_center": support_center_data,
    "application_date": "2019-07-01",
    "file_no": "4455",
}


decision_data = {
    "id": 1,
    "created_at": datetime(2023, 4, 19, 19, 21, 9),
    "modified_at": datetime(2023, 4, 19, 19, 21, 9),
    "child_full_name": "Oliwier Gierach",
    "child_full_name_gen": "Oliwiera Gierach",
    "child_address": "ul. Słowianska 10",
    "child_town": "Marki",
    "child_postal_code": "48-315",
    "child_post": "Chomencice",
    "child_pesel": "21302081908",
    "child_birth_date": date(2020, 3, 5),
    "child_birth_place": "Stargard Szczeciński",
    "child_student": False,
    "klass": "7",
    "profession": "rzeźnik",
    "school_parent_organisation": "Zespół Liceów Medycznych",
    "school_type": "szkoła ponadpodstawowa",
    "school_name": "Technikum Mechaniczne ",
    "school_address": "aleja Fiołkowa 25",
    "school_town": "Grudziądz",
    "school_postal_code": "40-999",
    "school_post": "Grudziądz",
    "address_child_checkbox": False,
    "address_first_parent_checkbox": True,
    "first_parent_full_name": "Emilia Uroda",
    "first_parent_full_name_gen": "Emilii Urody",
    "first_parent_address": "plac Floriana 83/87",
    "first_parent_town": "Żary",
    "first_parent_postal_code": "14-867",
    "first_parent_post": "Lulki",
    "second_parent_full_name": "Mateusz Bacia",
    "second_parent_full_name_gen": "Mateusza Bacia",
    "second_parent_address": "pl. Jarzębinowa 84/32",
    "second_parent_town": "Ostrów Mazowiecka",
    "second_parent_postal_code": "30-602",
    "second_parent_post": "Ziemsko",
    "support_center_name_nominative": "Miejska Poradnia Psychologiczno - Pedagogiczna w Wejherowo",
    "support_center_name_genetive": "Powiatowej Poradni Psychologiczno - Pedagogicznej w Ząbki",
    "support_center_institute_name": "Zespół Orzekający przy Powiatowej Poradni Psychologiczno - Pedagogicznej w Ząbki",
    "support_center_kurator": "Gdańsku, plac Wiśniowa 65/54, 66-804 Bielsko-Biała",
    "support_center_address": "pl. Słoneczna 620",
    "support_center_town": "Żywiec",
    "support_center_postal_code": "82-637",
    "support_center_post": "Kremowo",
    "issue": "indywidualne",
    "period": "04/19/2023 - 09/10/2023",
    "reasons": ["znacznie_utrudniajacy"],
    "activity_form": "indywidualne",
    "decision_no": "PPP.2023.AC.224",
    "application_date": date(2023, 4, 5),
    "file_no": "4455",
    "meeting_date": date(2023, 4, 19),
    "meeting_time": "8:15",
    "meeting_members": [
        {"name": "Julian Oleksa", "function": "logopeda, pedagog"},
        {"name": "Natan Kulisz", "function": "tyflopedagog, logopeda"},
        {"name": "Kaja Nesterowicz", "function": "tyflopedagog, psycholog"},
    ],
}


schools = [
    {
        "school_parent_organisation": "Zespół Liceów Medycznych",
        "school_type": "szkoła ponadpodstawowa",
        "school_name": "Technikum Mechaniczne",
        "school_address": "aleja Fiołkowa 25",
        "school_town": "Grudziądz",
        "school_postal_code": "40-999",
        "school_post": "Grudziądz",
    },
    {
        "school_parent_organisation": None,
        "school_type": "szkoła ponadpodstawowa",
        "school_name": "Liceum Ogólnokształcące",
        "school_address": "ul. Janusza Korczaka 15",
        "school_town": "Sierpc",
        "school_postal_code": "22-111",
        "school_post": "Grudziądz",
    },
    {
        "school_parent_organisation": "Zespół Szkół Integracyjnych nr 3.",
        "school_type": "szkoła podstawowa",
        "school_name": "Szkoła Podstawowa nr 32",
        "school_address": "ul. Astrid Lindgren 2",
        "school_town": "Sieradz",
        "school_postal_code": "33-444",
        "school_post": "Grudziądz",
    },
    {
        "school_parent_organisation": None,
        "school_type": "szkoła podstawowa",
        "school_name": "Szkoła Podstawowa w Turku",
        "school_address": "ul. Paszy al Achmala 9",
        "school_town": "Turek",
        "school_postal_code": "44-123",
        "school_post": "Grudziądz",
    },
    {
        "school_parent_organisation": "Zespół Szkół z Oddziałami Przedszkolnymi",
        "school_type": "przedszkole",
        "school_name": "Przedszkole Samorządowe nr 1",
        "school_address": "ul. Pieska Lulka 44",
        "school_town": "Kostrzyn",
        "school_postal_code": "67-098",
        "school_post": "Grudziądz",
    },
]
