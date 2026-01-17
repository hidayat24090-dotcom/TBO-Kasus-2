import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

y_true = [1] * 50 + [0] * 20

verbs_transitive = [
    "pinaka", "kaucap", "ngelaksanayang", "nyarengin", "mungkah", "pengalgal", 
    "nyontoang", "nangiang", "negesan", "maweweh", "katambanin", "urati", 
    "ngerauhan", "nyanggra", "ngambil", "nuturang", "nyumbungan", "kaaptiyang", 
    "nyaga", "kaaptiang", "ngicen", "katangarin", "ngaturang", "nangian", 
    "nincapan", "kalaksanayang", "ngemastikayang", "ngaryanin", "maosang", 
    "makarya", "katureksain", "nganggen", "ngamargiang", "mapangapti", 
    "mapinunas", "ngaptiang", "nedungin", "mecikang", "nguripan", "nyihnayang", 
    "medue", "ngadep", "ngadepang", "meliang", "mamula", "mamaca", "meli", 
    "ngajeng", "manting", "nulis", "ngarit", "memacul", "ngidih", "memace", 
    "ngempu", "nyakan", "megandong" 
]

verbs_intransitive = [
    "memargi", "kauningin", "mapikayun", "kaloktah", "mawesana", "keni", 
    "embas", "uning", "kantun", "melaib", "mapatung", "negak", "luas", 
    "sirep", "megending", "metanding", "melali", "megedi", "ngeling", 
    "medagang", "majeng", "manjus", "dados"
]

pronoun = [
    "dane", "ipun", "ia", "ragane", "ida", "bli", 
    "meme", "bapa", "pekak", "ibapa", "memene", "adine", "tiang", "titiang"
]

nouns = [
    "anak", "lanang", "kalih", "diri", "krama", "kramane", "makasami", 
    "alit-alit", "para", "yowana", "pemedek", "pembeli", "perajin", "pamikarya", 
    "rare", "angon", "sekretaris", "daerah", "provinsi", "bali", "gubernur", 
    "wayan", "koster", "wakil", "tjokorda", "oka", "artha", "ardhana", 
    "sukawati", "kadek", "suprapta", "meranggi", "guru", "besar", "isi", 
    "denpasar", "dosen", "bahasa", "lan", "sastra", "unud", "putri", "astawa", 
    "gede", "putra", "ariawan", "ibu", "jero", "dewa", "indra", "luh", "sari", 
    "pemerintah", "desa", "beraban", "menteri", "pariwisata", "pmi", "pulah", 
    "palihne", "palih", "genah", "sesuduk", "pacentokan", "layangan", "virtual", 
    "acara", "swadharma", "baga", "usaha", "bengkel", "pemilet", "utsaha", 
    "masan", "pandemi", "pbmb", "pidarta", "pasien", "covid-19", "respati", 
    "rumah", "sakit", "kabencana", "gunung", "batur", "bencana", "benjang", 
    "pungkur", "parikrama", "konferens", "pemargi", "industri", "cerpen", 
    "palemahan", "pura", "dura", "negara", "seseleh", "budayane", "aksi", 
    "terorisme", "suksmaning", "manah", "fraksi-fraksi", "dprd", "hatinya", 
    "pkk", "pasar", "gotong", "royong", "pangan", "hari", "kerja", "angga", 
    "karya", "kayu", "ekonomi", "parindikane", "phk", "kuliner", "jeronnyane", 
    "porsi", "abon", "pindang", "galungan", "wisatawan", "geguat", "dina", 
    "mabasa", "campuran", "bulan", "warsa", "tenaga", "penyuluh", "bendera", 
    "merah", "putih", "yayasan", "satuan", "pendidikan", "kerjasama", "sistem", 
    "ajah-ajah", "umkm", "perekonomian", "iraga", "kauratiang", "jiwa", "seni", 
    "jukut", "jaja", "buku", "toko", "gramedia", "padi", "uma", "ituni", 
    "semengan", "umah", "kaluwihan", "inggih", "klambi", "celeng", "timpal", 
    "timpalne", "nasi", "peken", "kursi", "paon", "tegal", "bale", "baju", 
    "tukad", "surat", "pulpen", "made", "padang", "abian", "pasarean", "tabia", 
    "i", "carik", "tvne", "canang", "carike", "pis", "perpustakaane", "umahne", 
    "art", "center", "ibi", "sanje", "sanja", "banten", "klungkung", "arya", 
    "sekda", "titi", "tiang",
    "ayu", "iluh", "montor", "dealer", "honda", "dadong", "bubuh", "tuni", 
    "semengane", "tundu", "cerita", "nusa", "dua", "jumah", "kayehan",
    "luh_sari", "ibi_sanja", "peken_klungkung", "toko_gramedia", "desa_beraban",
    "putu", "jayanti", "bapane", "perpustakaan"
]

adjectives = ["becik", "lantang", "satia", "negatif", "positif", "kenak", "ageng", "kentel", "suci", "karesikan", "tebel", "anyar", "patut"]
adverb = ["sampun", "dados", "mangda", "sumeken", "pastika", "durung", "patut", "dahat", "banget", "setata", "tan", "surud-surud", "majanten", "nenten", "wantah", "tetep", "sesai"]
prepositions = ["ring", "majeng", "olih", "kantos", "sangkaning", "antuk", "sareng", "di", "ka", "jak", "ke", "uli", "nganggo"]
det = ["punika", "puniki", "ento", "ne", "niki", "sane"]

R = {
    "K": [
        ["VPt", "NP"], ["VPt", "C1"], ["VPt", "C2"], ["VPt", "C3"], 
        ["VPt", "C5"], ["VPt", "C7"], ["VPi", "NP"], ["VPi", "C2"],
        ["VPi", "C1"]
    ],

    "VPt": [
        ["Vt", "NP"], ["Vt", "Vt"], ["Adverb", "Vt"]
    ],

    "VPi": [
        ["Vi", "Vi"], ["Adverb", "Vi"]
    ],

    "C1": [["NP", "NP"], ["NP", "AP"]], 
    "C2": [["NP", "PP"]],
    "C3": [["NP", "C4"]],
    "C4": [["NP", "PP"]],
    "C5": [["NP", "C6"]],
    "C6": [["NP", "NP"], ["NP", "AP"]],
    "C7": [["NP", "C8"]],
    "C8": [["NP", "C9"]],
    "C9": [["NP", "PP"], ["AP", "PP"]],

    "NP": [
        ["N", "Det"], ["N", "AP"], ["Det", "N"], ["N", "N"],
        ["NP", "Det"], ["NP", "NP"], ["NP", "Pron"]
    ],
    
    "AP": [["Det", "A"], ["A", "Det"]],
    "PP": [["Prep", "NP"]],
    
    "Vt": [[x] for x in verbs_transitive],
    "Vi": [[x] for x in verbs_intransitive],
    "Prep": [[x] for x in prepositions],
    "Det": [[x] for x in det],
    "N": [[x] for x in nouns],
    "A": [[x] for x in adjectives],
    "Adverb": [[x] for x in adverb],
    "Pron": [[x] for x in pronoun]
}

for vt_word in verbs_transitive:
    R["VPt"].append([vt_word])

for vi_word in verbs_intransitive:
    R["VPi"].append([vi_word])

for n_word in nouns:
    R["NP"].append([n_word])

for p_word in pronoun:
    R["NP"].append([p_word])

for a_word in adjectives:
    R["AP"].append([a_word])

def cykParse(w):
    n = len(w)
    w_clean = [word.lower() for word in w]
    print(f"\nAnalisis: {w}")
    T = [[set([]) for j in range(n)] for i in range(n)]

    for j in range(0, n):
        current_word = w_clean[j]
        found = False
        for lhs, rules in R.items():
            for rhs in rules:
                if len(rhs) == 1 and rhs[0].lower() == current_word:
                    T[j][j].add(lhs)
                    found = True
        if not found:
            print(f"ERROR: Kata '{current_word}' tidak ada di kamus!")
            return False

    for l in range(2, n + 1): 
        for i in range(0, n - l + 1): 
            j = i + l - 1 
            for k in range(i, j):   
                for lhs, rules in R.items():
                    for rhs in rules:
                        if len(rhs) == 2:
                            B = rhs[0]
                            C = rhs[1]
                            if B in T[i][k] and C in T[k + 1][j]:
                                T[i][j].add(lhs)

    final_cell = T[0][n-1]
    if "K" in final_cell:
        print(f"[VALID] Kalimat Diterima.")
        return True
    else:
        print("[INVALID] Struktur Gagal.")
        return False

if __name__ == "__main__":
    kalimat_positif = [
        "Melaib tiang.", "Medagang Luh Sari.", "Mamaca ia buku.", "Meli tiang jaja.",
        "Dados ia pamikarya.", "Memargi dane ring desa beraban.", "Makarya tiang jaja ring pasar.",
        "Mamaca ia buku ring toko.", "Ngicen tiang adine buku.", "Ngicen ia adine buku ring toko",
        "Meli nasi tiang ring peken.", "Negak ia di kursi.", "Ngajeng Meme jaja di paon.",
        "Luas Bapa ka tegal.", "Mamaca ia buku di bale.", "Manting Luh baju ring tukad.",
        "Nulis ia surat nganggo pulpen.", "Ngarit Made padang di abian.", "Sirep ia ring pasarean.",
        "Mapatung ia celeng jak timpalne.", "Pinaka Sekda Bali anak lanang punika.",
        "Ngelaksanayang pulah palih ne para PMI punika.", "Nyarengin sesuduk sane patut dane makasami.",
        "Mungkah pacentokan layangan Wakil Gubernur.", "Dados pacentokan puniki titi majeng rare angon.",
        "Pinaka pengalgal Kadek Suprapta acara punika.", "Ngelaksanayang dane pacentokan baga kalih.",
        "Ngelaksanayang titiang swadharma.", "Nyontoang dane usaha bengkel.",
        "Dados guru Putu Jayanti ring klungkung.", "Ngaptiang titiang.", "Ngadep jukut Luh Sari.",
        "Medagang Luh Sari banten.", "Ngadep jukut memene Luh Sari.", "Mamaca ia buku ibi sanja.",
        "Medagang ayu banten di peken Klungkung.", "Medagang jaja arya di peken Klungkung.",
        "Ngadep jukut memene Luh Sari di peken Klungkung.", "Meliang adine buku ia di Toko Gramedia.",
        "Mamula padi i Bapa.", "Meli ia montor di dealer honda", "memacul pekak di carike",
        "Ngadep iluh nasi di peken", "melali made ka nusa dua", "Medagang i dadong bubuh tuni semengane",
        "megandong adine ring tundu bapane", "memace ia buku ring perpustakaan",
        "Nyakan meme nasi di jumah.", "manjus ia ke kayehan.", "Memace ia buku cerita ring perpustakaane"
    ]
    kalimat_negatif = [
        "Guru bapanne niki", "Pedagang memenne ento", "Nelayan pekakne nika",
        "Balian dadongne punika", "Dokter tunanganne niki", "Sopir bli ento",
        "Penari luh ne", "Mahasiswa Wayan punika", "Juru masak panakne makejang",
        "Petani Komang ne", "Seniman Nyoman niki", "Montir Putu punika",
        "Wartawan tiang niki", "Guru matematika bapanne niki", "Balian usada tiang punika",
        "Montir motor Gede ento", "Juru masak lawar memenne ne", "Tukang mebel Wayan niki",
        "Penjahit kebaya Luh punika", "Pedagang banten dadongne niki" 
    ]
    
    semua_kalimat = kalimat_positif + kalimat_negatif
    y_pred = [] 
    for teks in semua_kalimat:
        clean_teks = teks.replace(".", "").replace(",", "").split()
        is_valid = cykParse(clean_teks)
        y_pred.append(1 if is_valid else 0)
            
    akurasi = accuracy_score(y_true, y_pred)
    cm = confusion_matrix(y_true, y_pred)
    df_cm = pd.DataFrame(
        cm, 
        index=['Aktual: NEGATIF (0)', 'Aktual: POSITIF (1)'],
        columns=['Prediksi: INVALID (0)', 'Prediksi: VALID (1)']
    )

    print("\n" + "="*64)
    print("                   HASIL EVALUASI MODEL CFG")
    print("="*64)
    print(f"Nilai Akurasi: {akurasi * 100:.2f}%")
    print("-"*64)
    print("TABEL CONFUSION MATRIX:")
    print(df_cm)
    print("-"*64)
    print("LAPORAN KLASIFIKASI:")
    print(classification_report(y_true, y_pred, target_names=['Invalid', 'Valid']))
    print("="*64)