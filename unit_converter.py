import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        # Length units
        'meters': 1,
        'kilometers': 0.001,
        'miles': 0.000621371,
        'centimeters': 100,
        'millimeters': 1000,
        'inches': 39.3701,
        'feet': 3.28084,
        'yards': 1.09361,
        # Area units
        'square meters': 1,
        'square kilometers': 0.000001,
        'square miles': 3.861e-7,
        'acres': 0.000247105,
        'hectares': 0.0001,
        'square feet': 10.7639,
        'square yards': 1.19599,
    }
    
    if from_unit in conversion_factors and to_unit in conversion_factors:
        return value * conversion_factors[to_unit] / conversion_factors[from_unit]
    else:
        return None

# Title and Description
st.markdown("<h1 style='text-align: center; color: #1F618D;'>🔄 Unit Converter App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #626567;'>Convert different units easily using this app.</p>", unsafe_allow_html=True)

# User Inputs
unit_types = ["📏 Length", "🟦 Area"]
selected_type = st.selectbox("Select Unit Type:", unit_types)

if selected_type == "📏 Length":
    units = ["meters", "kilometers", "miles", "centimeters", "millimeters", "inches", "feet", "yards"]
elif selected_type == "🟦 Area":
    units = ["square meters", "square kilometers", "square miles", "acres", "hectares", "square feet", "square yards"]
else:
    units = []

value = st.number_input("Enter the value to be converted:", min_value=0.0, format="%.4f")

cols = st.columns(2)
with cols[0]:
    from_unit = st.selectbox("From Unit:", units)
with cols[1]:
    to_unit = st.selectbox("To Unit:", units)

# Convert Button
center_button_style = """
    <style>
    .stButton button {
        display: block;
        margin: 20px auto;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 1em;
        background-color: #f5f5f5
    }
    </style>
"""
st.markdown(center_button_style, unsafe_allow_html=True)

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    if result is not None:
        st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
    else:
        st.error("Conversion not possible with the selected units.")

# Adding a footer
st.markdown("""
    <style>
    .footer {
        bottom: 0;
        width: 100%;
        background-color: #1F618D;
        color: white;
        text-align: center;
        padding: 0 0;
        font-size: 0.8em;
        margin-top: 20px;
    }
    .footer p {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 8px 0;
    }
    </style>
    <div class="footer">
        <p>© 2025 Unit Converter App. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)
