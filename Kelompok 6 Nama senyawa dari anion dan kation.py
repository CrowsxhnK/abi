import streamlit as st

def nama_senyawa(anion, kation):
    # Kamus untuk pasangan anion dan kation
    nama_anion = {
        "Cl": "Klorida",
        "Br": "Bromida",
        "I": "Iodida",
        "O": "Oksida",
        "S": "Sulfida",
        "PO4":"Fosfat",
        "NO3":"Nitrat",
        "NO2":"Nitrit",
        "CH3COO":"Asetat",
        "ClO":"Hipoklorit",
        "ClO2":"Klorit",
        "ClO3":"Klorat",
        "CN":"Sianida",
        "OH":"Hidroksida",
        "SO3":"Sulfit",
        "SO4":"Sulfat",
        "CO3":"Karbonat",
        "SiO3":"Silikat",
        "CrO4":"Kromat",
        "CrO7":"dikromat",
        "BrO":"Hipobromit",
        "BrO3":"Bromat",
        "C2O4":"Oksalat",
        "PO3":"Fosfit",
        "AsO3":"Arrneit",
        "AsO4":"Arsenit",
        "SbO3":"Antimonit",
        "SbO4":"Antimonat",
        "S2O3":"Tia sulfat",
        "MnO4":"Permanganat",
        "F":"Fluorida"
        # Belom semua
    }

    nama_kation = {
        "Na": "Natrium",
        "K": "Kalium",
        "Ca": "Kalsium",
        "Mg": "Magnesium",
        "Fe": "Besi",
        "Ag":"Perak",
        "NH4":"Amonium",
        "H":"Asam",
        "Sr":"Stronsium",
        "Ba":"Barium",
        "Al":"Aluminium",
        "Zn":"Zink",
        "Ni":"Nikel",
        "Sn":"Timah",
        "Pb":"Timbal",
        "Hg":"Raksa",
        "Cu":"Tembaga",
        "Au":"Emas",
        "Pt":"Platina"
        # Belom semua
    }

    # Cek ada nggak anion dan kation didalam kamus
    if anion in nama_anion and kation in nama_kation:
        nama_senyawa = nama_kation[kation] + " " + nama_anion[anion]
        return nama_senyawa
    else:
        return "Anion atau kation tidak dikenali."

# Buat di strimlit
st.title("Konversi Simbol Anion dan Kation menjadi Nama Senyawa")
anion = st.text_input("Masukkan simbol anion (misalnya Cl, Br, I, O):")
kation = st.text_input("Masukkan simbol kation (misalnya Na, K, Ca, Mg,):")

if st.button("Konversi"):
    if anion.strip() and kation.strip():
        result = nama_senyawa(anion.strip(), kation.strip())
        st.success("Nama senyawa: {}".format(result))
    else:
        st.warning("Masukkan simbol anion dan kation terlebih dahulu.")
