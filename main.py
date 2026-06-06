'''import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
st.title("HOUSE PRICE PREDCITION")
data=pd.read_csv("LINEAR.csv")
# print(data.columns)

X=data[['Hours_Studied']]
y=data['Exam_Score']
X_train,X_test,y_train,y_test=train_test_split(X,y)
model=LinearRegression()
model.fit(X_train,y_train)
sq=st.number_input("Enter sqft")
bt=st.button("Submit")
bt1=st.button("evalution")
if bt:
    out=model.predict([[sq]])
    st.write(out)
if bt1:
    out=model.predict(X_test)
    mae=mean_absolute_error(y_test,out)
    mse=mean_squared_error(y_test,out)
    r2=r2_score(y_test,out)
    st.write(mae,mse,r2)'''

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

st.set_page_config(
    page_title="ScorePredictor",
    page_icon="📈",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background: #0a0a0f !important;
}

[data-testid="stAppViewContainer"] {
    background: radial-gradient(ellipse 80% 60% at 50% -10%, #1a1040 0%, #0a0a0f 60%) !important;
    min-height: 100vh;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stToolbar"] { display: none; }
.block-container { padding: 3rem 2rem 4rem !important; max-width: 760px !important; }

h1, h2, h3, p, label, div {
    font-family: 'Syne', sans-serif !important;
}

.hero {
    text-align: center;
    padding: 3rem 0 2rem;
}
.hero-tag {
    display: inline-block;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    color: #8b5cf6;
    background: rgba(139, 92, 246, 0.1);
    border: 1px solid rgba(139, 92, 246, 0.3);
    padding: 0.3rem 0.9rem;
    border-radius: 20px;
    margin-bottom: 1.2rem;
    text-transform: uppercase;
}
.hero-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 3.2rem !important;
    font-weight: 800 !important;
    color: #f0eeff !important;
    line-height: 1.1 !important;
    letter-spacing: -0.03em !important;
    margin-bottom: 0.8rem !important;
}
.hero-title span {
    background: linear-gradient(135deg, #a78bfa, #7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.85rem !important;
    color: #6b6880 !important;
    letter-spacing: 0.05em !important;
}
.divider {
    width: 60px;
    height: 2px;
    background: linear-gradient(90deg, #7c3aed, transparent);
    margin: 2rem auto;
}

.card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(139,92,246,0.5), transparent);
}
.card-label {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.65rem !important;
    letter-spacing: 0.2em !important;
    text-transform: uppercase !important;
    color: #8b5cf6 !important;
    margin-bottom: 1rem !important;
}
.card-title {
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    color: #e2deff !important;
    margin-bottom: 0.4rem !important;
}
.card-desc {
    font-size: 0.82rem !important;
    color: #6b6880 !important;
    font-family: 'DM Mono', monospace !important;
    line-height: 1.6 !important;
}

[data-testid="stNumberInput"] input {
    background: rgba(139, 92, 246, 0.06) !important;
    border: 1px solid rgba(139, 92, 246, 0.25) !important;
    border-radius: 10px !important;
    color: #e2deff !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 1.3rem !important;
    padding: 0.8rem 1rem !important;
}
[data-testid="stNumberInput"] label {
    color: #a89fc8 !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    font-family: 'DM Mono', monospace !important;
}

.stButton > button {
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.05em !important;
    border-radius: 10px !important;
    padding: 0.7rem 2rem !important;
    border: none !important;
    cursor: pointer !important;
    width: 100% !important;
    transition: all 0.2s ease !important;
}
[data-testid="column"]:first-child .stButton > button {
    background: linear-gradient(135deg, #7c3aed, #a78bfa) !important;
    color: white !important;
    box-shadow: 0 4px 20px rgba(124, 58, 237, 0.4) !important;
}
[data-testid="column"]:last-child .stButton > button {
    background: rgba(255,255,255,0.04) !important;
    color: #a89fc8 !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
}

.result-box {
    background: linear-gradient(135deg, rgba(124,58,237,0.15), rgba(167,139,250,0.08));
    border: 1px solid rgba(139, 92, 246, 0.4);
    border-radius: 14px;
    padding: 2.5rem;
    text-align: center;
    margin-top: 1.5rem;
}
.result-value {
    font-size: 4rem;
    font-weight: 800;
    color: #c4b5fd;
    letter-spacing: -0.04em;
    line-height: 1;
}
.result-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    color: #6b6880;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-top: 0.6rem;
}

.metrics-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 1rem;
    margin-top: 1.2rem;
}
.metric-item {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 1.4rem;
    text-align: center;
}
.metric-value {
    font-size: 1.6rem;
    font-weight: 800;
    color: #a78bfa;
    letter-spacing: -0.02em;
}
.metric-name {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    color: #524f6a;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-top: 0.3rem;
}
.metric-desc {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    color: #6b6880;
    margin-top: 0.2rem;
}

.footer {
    text-align: center;
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 1px solid rgba(255,255,255,0.05);
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    color: #3d3a52;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_model():
    data = pd.read_csv("LINEAR.csv")
    X = data[['Hours_Studied']]
    y = data['Exam_Score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model, X_test, y_test


model, X_test, y_test = load_model()

# ── Hero ──────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-tag">ML · Linear Regression</div>
  <div class="hero-title">Score<span>Predictor</span></div>
  <div class="hero-sub">Predict exam performance from study hours</div>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ── Input Card ────────────────────────────────────────────────
st.markdown("""
<div class="card">
  <div class="card-label">01 — Prediction Engine</div>
  <div class="card-title">Enter Study Hours</div>
  <div class="card-desc">Input the number of hours studied to generate an exam score prediction using a trained linear regression model.</div>
</div>
""", unsafe_allow_html=True)

hours = st.number_input("Hours Studied", min_value=0.0, max_value=200.0, value=40.0, step=0.5)

col1, col2 = st.columns([3, 1])
with col1:
    predict_btn = st.button("⚡  Predict Score")
with col2:
    eval_btn = st.button("📊  Evaluate")

if predict_btn:
    prediction = model.predict([[hours]])[0]
    st.markdown(f"""
    <div class="result-box">
      <div class="result-value">{prediction:.1f}</div>
      <div class="result-label">Predicted Exam Score &nbsp;·&nbsp; {hours:.1f} hours studied</div>
    </div>
    """, unsafe_allow_html=True)

if eval_btn:
    preds = model.predict(X_test)
    mae  = mean_absolute_error(y_test, preds)
    mse  = mean_squared_error(y_test, preds)
    r2   = r2_score(y_test, preds)
    rmse = np.sqrt(mse)

    st.markdown("""
    <div class="card" style="margin-top:1.5rem">
      <div class="card-label">02 — Model Evaluation</div>
      <div class="card-title">Performance Metrics</div>
      <div class="card-desc">Measured on held-out test data (25% split).</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="metrics-grid">
      <div class="metric-item">
        <div class="metric-value">{r2:.3f}</div>
        <div class="metric-name">R² Score</div>
        <div class="metric-desc">Variance explained</div>
      </div>
      <div class="metric-item">
        <div class="metric-value">{mae:.2f}</div>
        <div class="metric-name">MAE</div>
        <div class="metric-desc">Mean abs. error</div>
      </div>
      <div class="metric-item">
        <div class="metric-value">{rmse:.2f}</div>
        <div class="metric-name">RMSE</div>
        <div class="metric-desc">Root mean sq. err</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
  Linear Regression · ScorePredictor · sklearn · streamlit
</div>
""", unsafe_allow_html=True)
