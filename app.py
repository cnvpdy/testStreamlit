import streamlit as st
import pandas as pd
view = [[100,150],[30]]

st.write('# Youtube View')
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)

st.write('#Pandas')
sview = pd.DataFrame(view)
sview