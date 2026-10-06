from pathlib import Path
import streamlit as st

st.set_page_config(page_title='Process Mining | Moative', page_icon='▶', layout='wide')
st.markdown('''<style>
.stApp { background: #f6f5f1; }
.block-container { max-width: 1120px; padding-top: 4rem; }
h1 { font-family: Georgia, serif; color: #16201f; }
a { color: #b95421 !important; }
</style>''', unsafe_allow_html=True)
st.caption('MOATIVE / HEALTHCARE IP')
st.title('Find where cash waits and labor repeats.')
st.write('Process Mining reconstructs claim journeys to reveal bottlenecks, delays and rework. Watch the team move from the process overview into the events behind an individual claim.')
st.video(str(Path(__file__).parent / 'media' / 'process-mining-demo.mp4'))
st.caption('Process Mining demonstration · 4 min 47 sec · Generated demonstration data')
st.markdown('[Explore Moative](https://www.moative.com/)')
