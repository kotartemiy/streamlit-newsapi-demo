from newscatcherapi import NewsCatcherApiClient
import streamlit as st

st.set_page_config(
   page_title="News API Demo",
   page_icon="🛠",
   layout="centered",
   initial_sidebar_state="expanded",
   menu_items={
         'About': 'How bla bla bla',
            }
)




newscatcherapi = NewsCatcherApiClient(x_api_key=st.secrets.api_key)

if 'calls' not in st.session_state:
    st.session_state['calls'] = 0



st.title('NewsCatcher Live Demo')
# st.subheader('No code live demo for News API. This is just a small part of entire functionality,\
# sign up to unock the full potential')
search_query = st.text_input('Search Query', 'Joe Biden', max_chars = 50, 
                    help = 'keyword(s) you want to search for',
                    placeholder = 'keyword(s) you want to search for')

language = st.selectbox('''article's language''', ['all','en', 'fr'],
                    help = 'the language of the article written')

# pub_date = st.selectbox('''Search articles within:''', ['last 7 days','last 24 hours', 'last hour'],
#                     help = 'time frame when the article is published')


api_search_query = search_query
# api_date = pub_date
api_serch_in = 'title'

if st.session_state['calls'] < 5:
    with st.spinner('Wait for it...'):
        if language == 'all':
            all_articles = newscatcherapi.get_search(q=api_search_query,
                                                    # from_=api_date,
                                                    search_in=api_serch_in,
                                                    page_size=20)
        else:
            api_lang = language
            all_articles = newscatcherapi.get_search(q=api_search_query,
                                                    lang=api_lang,
                                                    search_in=api_serch_in,
                                                    # from_=api_date,
                                                    page_size=20)
        st.session_state['calls'] += 1
        st.json(all_articles)
else:
    st.write('too many calls')