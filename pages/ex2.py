import streamlit as st
from utilities.ai_inference import gpt4o_mini_inference_yes_no, gpt4o_mini_inference

# 初始化会话状态
if "scenario" not in st.session_state:
    st.session_state.scenario = None

# 每个要件的响应结果初始化
if "sub_response_offer_acceptance" not in st.session_state:
    st.session_state.sub_response_offer_acceptance = None

if "sub_response_intention" not in st.session_state:
    st.session_state.sub_response_intention = None

if "sub_response_consideration" not in st.session_state:
    st.session_state.sub_response_consideration = None

if "sub_response_capacity" not in st.session_state:
    st.session_state.sub_response_capacity = None

if "sub_response_consent" not in st.session_state:
    st.session_state.sub_response_consent = None

if "sub_response_legality" not in st.session_state:
    st.session_state.sub_response_legality = None

# 输入情境（合同信息）
st.session_state.scenario = st.text_area("请输入合同信息或相关描述：")

# Offer and Acceptance 要件
st.subheader("1. Offer and Acceptance")
if st.button("Answer Offer and Acceptance"):
    st.session_state.sub_response_offer_acceptance = gpt4o_mini_inference(
        "You are an experienced Australian contract lawyer.",
        f"""
        Your task is to evaluate whether a valid Offer and Acceptance exist in the following scenario:
        {st.session_state.scenario}
        Based on your legal expertise, provide a clear 'yes' or 'no' conclusion on whether there is a valid offer and acceptance.
        You must also provide an explanation based on Australian contract law.
        """
    )
if st.session_state.sub_response_offer_acceptance:
    st.write(f"AI 对 Offer and Acceptance 的判断是: {st.session_state.sub_response_offer_acceptance}")

# Intention to Create Legal Relations 要件
st.subheader("2. Intention to Create Legal Relations")
if st.button("Answer Intention to Create Legal Relations"):
    st.session_state.sub_response_intention = gpt4o_mini_inference(
        "You are an experienced Australian contract lawyer.",
        f"""
        Your task is to evaluate whether there was an intention to create legal relations in the following scenario:
        {st.session_state.scenario}
        Provide a clear 'yes' or 'no' conclusion on whether there was an intention to create legal relations, 
        along with an explanation based on Australian contract law.
        """
    )
if st.session_state.sub_response_intention:
    st.write(f"AI 对 Intention to Create Legal Relations 的判断是: {st.session_state.sub_response_intention}")

# Consideration 要件
st.subheader("3. Consideration")
if st.button("Answer Consideration"):
    st.session_state.sub_response_consideration = gpt4o_mini_inference(
        "You are an experienced Australian contract lawyer.",
        f"""
        Your task is to evaluate whether valid Consideration exists in the following scenario:
        {st.session_state.scenario}
        Provide a clear 'yes' or 'no' conclusion on whether there is valid consideration for the contract,
        along with an explanation based on Australian contract law.
        """
    )
if st.session_state.sub_response_consideration:
    st.write(f"AI 对 Consideration 的判断是: {st.session_state.sub_response_consideration}")

# Legal Capacity 要件
st.subheader("4. Legal Capacity")
if st.button("Answer Legal Capacity"):
    st.session_state.sub_response_capacity = gpt4o_mini_inference(
        "You are an experienced Australian contract lawyer.",
        f"""
        Your task is to evaluate whether both parties have the Legal Capacity to enter into a contract in the following scenario:
        {st.session_state.scenario}
        Provide a clear 'yes' or 'no' conclusion on whether both parties have the legal capacity to form a contract,
        along with an explanation based on Australian contract law.
        """
    )
if st.session_state.sub_response_capacity:
    st.write(f"AI 对 Legal Capacity 的判断是: {st.session_state.sub_response_capacity}")

# Consent 要件
st.subheader("5. Consent")
if st.button("Answer Consent"):
    st.session_state.sub_response_consent = gpt4o_mini_inference(
        "You are an experienced Australian contract lawyer.",
        f"""
        Your task is to evaluate whether both parties' Consent was valid in the following scenario:
        {st.session_state.scenario}
        Provide a clear 'yes' or 'no' conclusion on whether consent was valid,
        along with an explanation based on Australian contract law.
        """
    )
if st.session_state.sub_response_consent:
    st.write(f"AI 对 Consent 的判断是: {st.session_state.sub_response_consent}")

# Legality 要件
st.subheader("6. Legality")
if st.button("Answer Legality"):
    st.session_state.sub_response_legality = gpt4o_mini_inference(
        "You are an experienced Australian contract lawyer.",
        f"""
        Your task is to evaluate whether the contract is legal in the following scenario:
        {st.session_state.scenario}
        Provide a clear 'yes' or 'no' conclusion on whether the contract involves any illegal activity or violates public policy,
        along with an explanation based on Australian contract law and provide reasons.
        """
    )
if st.session_state.sub_response_legality:
    st.write(f"AI 对 Legality 的判断是: {st.session_state.sub_response_legality}")

# 综合结论判断
st.subheader("综合判断")
if st.button("Solve"):
    all_responses = [
        st.session_state.sub_response_offer_acceptance,
        st.session_state.sub_response_intention,
        st.session_state.sub_response_consideration,
        st.session_state.sub_response_capacity,
        st.session_state.sub_response_consent,
        st.session_state.sub_response_legality,
    ]

    # 如果所有要件都满足“yes”，则合同有效，否则无效
    if all(response == "yes" for response in all_responses):
        st.session_state.response = "合同有效"
    elif any(response == "no" for response in all_responses):
        st.session_state.response = "合同无效"
    else:
        st.session_state.response = "合同状态不确定"

    if st.session_state.response:
        st.write(f"综合判断结果: {st.session_state.response}")
