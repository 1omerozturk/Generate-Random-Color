import streamlit as st
import random

def generate_random_colors(num):
    colors = []
    for _ in range(num):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        colors.append((red, green, blue))
    return colors

def rgb_to_hex(rgb):
    # Her bir renk kanalını hexadecimal forma çevir
    hex_color = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
    return hex_color
# Başlık
st.title("Generate Random Color")


# Kullanıcıdan renk sayısı girişi
num_of_colors = st.number_input("How much generate random color?", min_value=1, value=5, step=1)

# Rastgele renkleri çizen fonksiyon
random_colors = generate_random_colors(num_of_colors)

# Renkleri ekrana yazdır
for i, color in enumerate(random_colors, start=1):
    st.markdown(f"<div style='text-align:center; margin-top:25px; color:rgb({color[0]}, {color[1]}, {color[2]})'>Renk {i}</div>",unsafe_allow_html=True)
    st.code(f"RGB{color}") 
    st.markdown(f"<div style='margin-left:50%;'> <div style='text-align:center;width: 75px; height: 45px;margin:8px;background-color: rgb({color[0]}, {color[1]}, {color[2]})'></div></div>",unsafe_allow_html=True)
    color = st.color_picker(f'Pick A Color',rgb_to_hex(color))
    st.divider()