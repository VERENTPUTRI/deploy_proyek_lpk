import streamlit as st

# judul aplikasi
st.title('Kalkulator Stoikiometri Gas')

# intro aplikasi
st.write('Aplikasi ini bertujuan untuk memudahkan dalam menghitung stoikiometri gas. Gas tersebut berupa gas Hidrogen, Oksigen, Nitrogen, dan Argon. Silakan ikuti perintah yang ditampilkan di layar.')
st.markdown('---')

# input untuk jumlah mol gas
mol_gas = st.number_input('Masukkan jumlah mol gas (mol)', min_value=0.0)

# input untuk suhu gas
suhu = st.number_input('Masukkan suhu gas (K)', min_value=0.0)

# input untuk tekanan gas
tekanan = st.number_input('Masukkan tekanan gas (atm)', min_value=0.0)

# input untuk volume gas
volume = st.number_input('Masukkan volume gas (L)', min_value=0.0)

# konstanta gas
R = 0.0821  # L.atm/mol.K

# pilihan untuk jenis gas
gas = st.selectbox('Pilih jenis gas', ('Hidrogen', 'Oksigen', 'Nitrogen', 'Argon'))

# output jumlah mol gas
st.write('### Jumlah Mol Gas')
st.write(f'{mol_gas:.4f} mol {gas}')

tombol = st.button('Hitung Nilai')

# menghitung massa molar gas
if gas == 'Hidrogen':
    massa_molar = 2.016
elif gas == 'Oksigen':
    massa_molar = 32.00
elif gas == 'Nitrogen':
    massa_molar = 28.02
elif gas == 'Argon':
    massa_molar = 39.95
    
# output massa gas
if tombol:
    massa_gas = mol_gas * massa_molar
    st.write('### Massa Gas')
    st.success(f'{massa_gas:.4f} g {gas}')

# menghitung volume gas pada kondisi STP
if tombol:
    st.write('### Volume Gas pada STP')
    st.write('Kondisi STP : Suhu 273 K dan Tekanan 1 atm')
    volume_stp = (mol_gas * R * 273.0) / tekanan
    st.success(f'{volume_stp:.4f} L {gas}')

# menghitung volume gas pada suhu dan tekanan tertentu
if tombol:
    st.write('### Volume Gas pada Suhu dan Tekanan Tertentu')
    volume_gas = (mol_gas * R * suhu) / tekanan
    st.success(f'{volume_gas:.4f} L {gas} pada suhu {suhu:.2f} K dan tekanan {tekanan:.2f} atm')
    st.balloons()