import streamlit as st
from utilities.ai_embedding import text_small_embedding
from utilities.ai_inference import gpt4o_mini_inference, gpt4o_mini_inference_yes_no
from utilities.chroma_db import get_or_create_persistent_chromadb_client_and_collection, add_document_chunk_to_chroma_collection, query_chromadb_collection, delete_chromadb_collection
from utilities.documents import upload_document, read_document, chunk_document, download_document, delete_document
from utilities.layout import page_config

if "problem" not in st.session_state:
    st.session_state.problem = None


if "response" not in st.session_state:
    st.session_state.response = None

#this is the main problem/response

if "sub_problem_1" not in st.session_state:
    st.session_state.sub_problem_1 = None

if "sub_response_1" not in st.session_state:
    st.session_state.sub_response_1 = None

#this is the first sub prpblem/response

if "sub_problem_2" not in st.session_state:
    st.session_state.sub_problem_2 = None

if "sub_response_2" not in st.session_state:
    st.session_state.sub_response_2 = None

#this is the second sub prpblem/response

if "sub_problem_3" not in st.session_state:
    st.session_state.sub_problem_3 = None

if "sub_response_3" not in st.session_state:
    st.session_state.sub_response_3 = None

st.subheader("Main Problem")

st.session_state.problem = "Should I get a coffee now?"

st.write(st.session_state.problem)



st.subheader("Sub Problems")

st.session_state.sub_problem_1 = "Did I have a coffee in last two hours?"

#st.write(st.session_state.sub_problem_1)

st.session_state.sub_response_1 = st.selectbox(
    st.session_state.sub_problem_1,
    ("yes","no","unsure"),
    index = 1
    
#这是一个可选参数，用于设置选择框中默认选中的项的索引。
#索引是从 0 开始的，因此 index=1 表示默认选中第二个选项，即“no”。
#如果没有指定 index，默认情况下会选择列表中的第一个选项（即索引为 0 的选项）
)

st.session_state.sub_problem_2 = "Did I get eight hours sleep?"

st.session_state.sub_response_2 = st.selectbox(
    st.session_state.sub_problem_2,
    ("yes","no","unsure"),
    index = 1
)

st.subheader("Solving Problem")