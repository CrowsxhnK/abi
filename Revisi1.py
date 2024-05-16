import streamlit as st

def nama_senyawa(anion, kation):
    nama_anion = {
        "Cl": "Klorida",
        "Br": "Bromida",
        "I": "Iodida",
        "O": "Oksida",
        "S": "Sulfida",
        "PO4": "Fosfat",
        "NO3": "Nitrat",
        "NO2": "Nitrit",
        "CH3COO": "Asetat",
        "ClO": "Hipoklorit",
        "ClO2": "Klorit",
        "ClO3": "Klorat",
        "CN": "Sianida",
        "OH": "Hidroksida",
        "SO3": "Sulfit",
        "SO4": "Sulfat",
        "CO3": "Karbonat",
        "SiO3": "Silikat",
        "CrO4": "Kromat",
        "Cr2O7": "Dikromat",
        "BrO": "Hipobromit",
        "BrO3": "Bromat",
        "C2O4": "Oksalat",
        "PO3": "Fosfit",
        "AsO3": "Arsenit",
        "AsO4": "Arsenat",
        "SbO3": "Antimonit",
        "SbO4": "Antimonat",
        "S2O3": "Tiosulfat",
        "MnO4": "Permanganat",
        "F": "Fluorida"
    }

    nama_kation = {
        "Na": "Natrium",
        "K": "Kalium",
        "Ca": "Kalsium",
        "Mg": "Magnesium",
        "Fe": "Besi",
        "Ag": "Perak",
        "NH4": "Amonium",
        "H": "Asam",
        "Sr": "Stronsium",
        "Ba": "Barium",
        "Al": "Aluminium",
        "Zn": "Seng",
        "Ni": "Nikel",
        "Sn": "Timah",
        "Pb": "Timbal",
        "Hg": "Raksa",
        "Cu": "Tembaga",
        "Au": "Emas",
        "Pt": "Platina"
    }

    if anion in nama_anion and kation in nama_kation:
        nama_senyawa = nama_kation[kation] + " " + nama_anion[anion]
        return nama_senyawa

# Buat di Streamlit
st.title("Mengubah Simbol Anion dan Kation menjadi Nama Senyawa")

# mengubah background
st.markdown(""" <style>.stApp {background-color: #ADD8E6;");
        background-size: cover;}</style>""", unsafe_allow_html=True)

# Sidebar menu
menu = st.sidebar.selectbox("Pilih Menu", ("Mengubah Simbol", "Pengertian Anion dan Kation", "Anggota"))

if menu == "Mengubah Simbol":
    st.write("Pilih simbol anion dan kation untuk mendapatkan nama senyawa yang sesuai.")
    
    nama_anion = {
        "Cl": "Klorida",
        "Br": "Bromida",
        "I": "Iodida",
        "O": "Oksida",
        "S": "Sulfida",
        "PO4": "Fosfat",
        "NO3": "Nitrat",
        "NO2": "Nitrit",
        "CH3COO": "Asetat",
        "ClO": "Hipoklorit",
        "ClO2": "Klorit",
        "ClO3": "Klorat",
        "CN": "Sianida",
        "OH": "Hidroksida",
        "SO3": "Sulfit",
        "SO4": "Sulfat",
        "CO3": "Karbonat",
        "SiO3": "Silikat",
        "CrO4": "Kromat",
        "Cr2O7": "Dikromat",
        "BrO": "Hipobromit",
        "BrO3": "Bromat",
        "C2O4": "Oksalat",
        "PO3": "Fosfit",
        "AsO3": "Arsenit",
        "AsO4": "Arsenat",
        "SbO3": "Antimonit",
        "SbO4": "Antimonat",
        "S2O3": "Tiosulfat",
        "MnO4": "Permanganat",
        "F": "Fluorida"
    }

    nama_kation = {
        "Na": "Natrium",
        "K": "Kalium",
        "Ca": "Kalsium",
        "Mg": "Magnesium",
        "Fe": "Besi",
        "Ag": "Perak",
        "NH4": "Amonium",
        "H": "Asam",
        "Sr": "Stronsium",
        "Ba": "Barium",
        "Al": "Aluminium",
        "Zn": "Seng",
        "Ni": "Nikel",
        "Sn": "Timah",
        "Pb": "Timbal",
        "Hg": "Raksa",
        "Cu": "Tembaga",
        "Au": "Emas",
        "Pt": "Platina"
    }

    kation = st.selectbox("Pilih simbol kation:", list(nama_kation.keys()))
    anion = st.selectbox("Pilih simbol anion:", list(nama_anion.keys()))
    
    if st.button("Hasil"):
        result = nama_senyawa(anion, kation)
        st.success("Nama senyawa: {}".format(result))

elif menu == "Pengertian Anion dan Kation":
    st.subheader("Pengertian Anion dan Kation")
    st.write("""Pengertian Anion  :""","Nama anion sendiri merupakan asalnya dari bahasa Yunani yaitu “ano”. Artinya naik.Pembentukan anion terjadi saat atom yang bukan logam mendapatkan satu atau lebih elektron. Pertambahan adanya elektron valensi dengan muatan negatif yang merubah atom tersebut.Atom dengan muatan awal netral kemudian menjadi bermuatan negatif. Oleh karena itu, tanda yang dimiliki oleh anion yaitu negatif (-) di bagian samping dari nama atom.Sementara angka yang ada di samping tanda negatif tersebut menunjukkan jumlah elektron yang sudah diterima oleh atom.")
    st.write("""Pengertian Kation  :""","Istilah kation sendiri asalnya dari bahasa Yunani yaitu “kata” yang memiliki arti turun.Pada atom terdapat elektron yang terletak di bagian lapisan sub kulit terluar atau disebut juga sebagai elektron valensi. Kation merupakan atom yang kehilangan satu maupun lebih dari elektron yang ada. Elektron yang hilang tersebut merupakan muatan negatif.Hal tersebut membuat atom yang awalnya memiliki muatan netral menjadi bermuatan positif. Atom dengan muatan positif tersebut yang dinamakan sebagai kation.Kation biasa ditandai dengan simbol positif (+) di bagian samping dari nama atomnya.")
    

elif menu == "Anggota":
    st.subheader("Disusun Oleh Kelompok 2")
    st.write("""
1. ADINDA NAZWA         (2360058)
2. DANNISA ALZULLA      (2360093)
3. DITYA ABIMANYU       (2360111)
4. M. NAZRIL NASWAN     (2360189)
5. TRISTARANI AZIZAH    (2360279)
    """)
    st.image("https://upload.wikimedia.org/wikipedia/id/thumb/8/82/Logo_Politeknik_AKA_Bogor.png/300px-Logo_Politeknik_AKA_Bogor.png", width=300)
