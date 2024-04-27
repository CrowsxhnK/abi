import streamlit as st

def nama_senyawa(anion, kation):
    # Dictionary untuk pasangan anion dan kation
    nama_anion = {
        "Cl": "Klorida",
        "Br": "Bromida",
        "I": "Iodida",
        "O": "Oksida",
        "S": "Sulfida"
        # Tambahkan anion lainnya sesuai kebutuhan
    }

    nama_kation = {
        "Na": "Natrium",
        "K": "Kalium",
        "Ca": "Kalsium",
        "Mg": "Magnesium",
        "Fe": "Besi"
        # Tambahkan kation lainnya sesuai kebutuhan
    }

    # Cek apakah anion dan kation terdapat dalam kamus
    if anion in nama_anion and kation in nama_kation:
        nama_senyawa = nama_kation[kation] + " " + nama_anion[anion]
        return nama_senyawa
    else:
        return "Anion atau kation tidak dikenali."

# Tampilan menggunakan Streamlit
st.title("Konversi Simbol Anion dan Kation menjadi Nama Senyawa")
anion = st.text_input("Masukkan simbol anion (misalnya Cl, Br, I, O, S):")
kation = st.text_input("Masukkan simbol kation (misalnya Na, K, Ca, Mg, Fe):")

if st.button("Konversi"):
    if anion.strip() and kation.strip():
        result = nama_senyawa(anion.strip(), kation.strip())
        st.success("Nama senyawa: {}".format(result))
    else:
        st.warning("Masukkan simbol anion dan kation terlebih dahulu.")
