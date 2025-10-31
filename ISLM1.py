import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Interactive ISLM", page_icon="📈", layout="wide", initial_sidebar_state="expanded")

st.title("Interactive IS-LM Dashboard")
st.write("This demo uses simple linear Keynesian IS and LM relations. Fiscal = ΔG; Monetary = Δ(M/P). Axis tick values are hidden; axis labels remain visible.")

a = 2.0
c = 0.5
T = 2.0
I0 = 4.0
b = 1.5
G0 = 3.0
k = 0.8
h = 1.2
M_over_P_base = 6.0

with st.sidebar:
    st.header("Policy")
    fiscal_shock = st.slider("Fiscal policy (ΔG) — negative = contractionary, positive = expansionary", min_value=-9.0, max_value=9.0, value=0.0, step=0.25)
    monetary_shock = st.slider("Monetary policy (ΔM/P) — negative = contractionary, positive = expansionary", min_value=-9.0, max_value=9.0, value=0.0, step=0.25)

G = G0 + fiscal_shock
M_over_P = M_over_P_base + monetary_shock
A = a - c * T + I0 + G
den = b * k + h * (1 - c)

Y_eq_current = float((h * A + b * M_over_P) / den)
r_eq_current = float((A - (1 - c) * Y_eq_current) / b)

G_base = G0
M_base = float(M_over_P_base)
A_base = a - c * T + I0 + G_base
Y_eq_base = float((h * A_base + b * M_base) / den)
r_eq_base = float((A_base - (1 - c) * Y_eq_base) / b)

Y_MIN, Y_MAX = 0.0, 30.0
r_MIN, r_MAX = -1.0, 6.0
M_MIN, M_MAX = max(0.0, M_base - 8.0), M_base + 8.0

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Keynesian Cross")
    Ys = np.linspace(Y_MIN, Y_MAX, 300)
    r_for_goods_current = r_eq_current
    r_for_goods_base = r_eq_base
    C = a + c * (Ys - T)
    I_base = I0 - b * r_for_goods_base
    E_base = C + I_base + G_base
    I_cur = I0 - b * r_for_goods_current
    E_cur = C + I_cur + G
    fig_kc = go.Figure()
    fig_kc.add_trace(go.Scatter(x=Ys, y=E_base, mode="lines", name="Planned Expenditure (baseline)", line=dict(color="gray", dash="dash")))
    fig_kc.add_trace(go.Scatter(x=Ys, y=E_cur, mode="lines", name="Planned Expenditure (current)", line=dict(color="#1f77b4")))
    fig_kc.add_trace(go.Scatter(x=Ys, y=Ys, mode="lines", name="45° (Y = E)", line=dict(color="#bfbfbf")))
    Y_goods_eq_base = (a - c * T + I0 - b * r_for_goods_base + G_base) / (1 - c)
    Y_goods_eq_cur = (a - c * T + I0 - b * r_for_goods_current + G) / (1 - c)
    fig_kc.add_trace(go.Scatter(x=[Y_goods_eq_base], y=[Y_goods_eq_base], mode="markers", marker=dict(color="gray", size=9), name="Base Equilibrium"))
    fig_kc.add_trace(go.Scatter(x=[Y_goods_eq_cur], y=[Y_goods_eq_cur], mode="markers", marker=dict(color="#1f77b4", size=9), name="Current Equilibrium"))
    fig_kc.update_layout(title="Keynesian Cross (Goods Market)", xaxis_title="Output / Income (Y)", yaxis_title="Expenditure (E)", xaxis=dict(range=[Y_MIN, Y_MAX], showticklabels=False), yaxis=dict(range=[Y_MIN, Y_MAX], showticklabels=False), margin=dict(l=30, r=10, t=50, b=30), height=420)
    st.plotly_chart(fig_kc, use_container_width=True)

with col2:
    st.subheader("Money Market")
    Y_for_money_base = Y_goods_eq_base
    Y_for_money_cur = Y_goods_eq_cur
    Ms = np.linspace(M_MIN, M_MAX, 300)
    r_from_M_base = (k * Y_for_money_base - Ms) / h
    r_from_M_cur = (k * Y_for_money_cur - Ms) / h
    fig_mm = go.Figure()
    fig_mm.add_trace(go.Scatter(x=Ms, y=r_from_M_base, mode="lines", name="Money demand (baseline)", line=dict(color="gray", dash="dash")))
    fig_mm.add_trace(go.Scatter(x=Ms, y=r_from_M_cur, mode="lines", name="Money demand (current)", line=dict(color="#1f77b4")))
    fig_mm.add_trace(go.Scatter(x=[M_base, M_base], y=[r_MIN, r_MAX], mode="lines", name="Money supply (baseline)", line=dict(color="gray", dash="dash")))
    fig_mm.add_trace(go.Scatter(x=[M_over_P, M_over_P], y=[r_MIN, r_MAX], mode="lines", name="Money supply (current)", line=dict(color="#1f77b4")))
    fig_mm.add_trace(go.Scatter(x=[M_base], y=[r_eq_base], mode="markers", marker=dict(color="gray", size=9), name="Base Equilibrium"))
    r_money_cur = r_eq_current
    fig_mm.add_trace(go.Scatter(x=[M_over_P], y=[r_money_cur], mode="markers", marker=dict(color="#1f77b4", size=9), name="Current Equilibrium"))
    fig_mm.update_layout(title="Money Market", xaxis_title="Real money (M/P)", yaxis_title="Interest rate (r)", xaxis=dict(range=[M_MIN, M_MAX], showticklabels=False), yaxis=dict(range=[r_MIN, r_MAX], showticklabels=False), margin=dict(l=30, r=10, t=40, b=30), height=420)
    st.plotly_chart(fig_mm, use_container_width=True)

st.subheader("IS-LM")
Ys = np.linspace(Y_MIN, Y_MAX, 300)
r_IS_base = (A_base - (1 - c) * Ys) / b
r_IS_cur = (A - (1 - c) * Ys) / b
r_LM_base = (k * Ys - M_base) / h
r_LM_cur = (k * Ys - M_over_P) / h
fig_islm = go.Figure()
fig_islm.add_trace(go.Scatter(x=Ys, y=r_IS_base, mode="lines", name="IS (baseline)", line=dict(color="gray", dash="dash")))
fig_islm.add_trace(go.Scatter(x=Ys, y=r_LM_base, mode="lines", name="LM (baseline)", line=dict(color="gray", dash="dash")))
fig_islm.add_trace(go.Scatter(x=Ys, y=r_IS_cur, mode="lines", name="IS (current)", line=dict(color="#1f77b4")))
fig_islm.add_trace(go.Scatter(x=Ys, y=r_LM_cur, mode="lines", name="LM (current)", line=dict(color="#1f77b4")))
fig_islm.add_trace(go.Scatter(x=[Y_eq_base], y=[r_eq_base], mode="markers", marker=dict(color="gray", size=11, symbol="x"), name="Base Equilibrium"))
fig_islm.add_trace(go.Scatter(x=[Y_eq_current], y=[r_eq_current], mode="markers", marker=dict(color="#1f77b4", size=11, symbol="x"), name="Current Equilibrium"))
fig_islm.update_layout(title="IS-LM", xaxis_title="Output / Income (Y)", yaxis_title="Interest rate (r)", xaxis=dict(range=[Y_MIN, Y_MAX], showticklabels=False), yaxis=dict(range=[r_MIN, r_MAX], showticklabels=False), margin=dict(l=30, r=10, t=50, b=30), height=520)
st.plotly_chart(fig_islm, use_container_width=True)

st.subheader("Alternative cases")

colA, colB = st.columns(2)

with colA:
    st.markdown("Steep IS (IS resistant to monetary policy)")
    b_steep = 0.05
    A_base_steep = a - c * T + I0 + G0
    den_steep = b_steep * k + h * (1 - c)
    Y_eq_base_steep = float((h * A_base_steep + b_steep * M_base) / den_steep)
    r_eq_base_steep = float((A_base_steep - (1 - c) * Y_eq_base_steep) / b_steep)
    G_cur_steep = G0 + fiscal_shock
    M_cur_steep = M_over_P_base + monetary_shock
    A_cur_steep = a - c * T + I0 + G_cur_steep
    Y_eq_cur_steep = float((h * A_cur_steep + b_steep * M_cur_steep) / den_steep)
    r_eq_cur_steep = float((A_cur_steep - (1 - c) * Y_eq_cur_steep) / b_steep)
    Ys_alt = np.linspace(0.0, 60.0, 400)
    r_IS_base_steep = (A_base_steep - (1 - c) * Ys_alt) / b_steep
    r_LM_base_steep = (k * Ys_alt - M_base) / h
    r_IS_cur_steep = (A_cur_steep - (1 - c) * Ys_alt) / b_steep
    r_LM_cur_steep = (k * Ys_alt - M_cur_steep) / h
    fig_steep = go.Figure()
    fig_steep.add_trace(go.Scatter(x=Ys_alt, y=r_IS_base_steep, mode="lines", name="IS (baseline, steep)", line=dict(color="gray", dash="dash")))
    fig_steep.add_trace(go.Scatter(x=Ys_alt, y=r_LM_base_steep, mode="lines", name="LM (baseline)", line=dict(color="gray", dash="dash")))
    fig_steep.add_trace(go.Scatter(x=Ys_alt, y=r_IS_cur_steep, mode="lines", name="IS (current, steep)", line=dict(color="#1f77b4")))
    fig_steep.add_trace(go.Scatter(x=Ys_alt, y=r_LM_cur_steep, mode="lines", name="LM (current)", line=dict(color="#1f77b4")))
    fig_steep.add_trace(go.Scatter(x=[Y_eq_base_steep], y=[r_eq_base_steep], mode="markers",name = "Base Equilibrium", marker=dict(color="gray", size=11, symbol="x")))
    fig_steep.add_trace(go.Scatter(x=[Y_eq_cur_steep], y=[r_eq_cur_steep], mode="markers", name = "Current Equilibrium", marker=dict(color="#1f77b4", size=11, symbol="x")))
    fig_steep.update_layout(title="Steep IS (resistant to monetary policy)", xaxis_title="Output / Income (Y)", yaxis_title="Interest rate (r)", xaxis=dict(range=[0.0, 60.0], showticklabels=False), yaxis=dict(range=[-1.0, 12.0], showticklabels=False), margin=dict(l=30, r=10, t=30, b=30), height=460)
    st.plotly_chart(fig_steep, use_container_width=True)

with colB:
    st.markdown("Flat IS (IS highly responsive to r)")
    b_flat = 100.0
    A_base_flat = a - c * T + I0 + G0
    den_flat = b_flat * k + h * (1 - c)
    Y_eq_base_flat = float((h * A_base_flat + b_flat * M_base) / den_flat)
    r_eq_base_flat = float((A_base_flat - (1 - c) * Y_eq_base_flat) / b_flat)
    G_cur_flat = G0 + fiscal_shock
    M_cur_flat = M_over_P_base + monetary_shock
    A_cur_flat = a - c * T + I0 + G_cur_flat
    Y_eq_cur_flat = float((h * A_cur_flat + b_flat * M_cur_flat) / den_flat)
    r_eq_cur_flat = float((A_cur_flat - (1 - c) * Y_eq_cur_flat) / b_flat)
    Ys_alt2 = np.linspace(0.0, 60.0, 400)
    r_IS_base_flat = (A_base_flat - (1 - c) * Ys_alt2) / b_flat
    r_LM_base_flat = (k * Ys_alt2 - M_base) / h
    r_IS_cur_flat = (A_cur_flat - (1 - c) * Ys_alt2) / b_flat
    r_LM_cur_flat = (k * Ys_alt2 - M_cur_flat) / h
    fig_flat = go.Figure()
    fig_flat.add_trace(go.Scatter(x=Ys_alt2, y=r_IS_base_flat, mode="lines", name="IS (baseline, flat)", line=dict(color="gray", dash="dash")))
    fig_flat.add_trace(go.Scatter(x=Ys_alt2, y=r_LM_base_flat, mode="lines", name="LM (baseline)", line=dict(color="gray", dash="dash")))
    fig_flat.add_trace(go.Scatter(x=Ys_alt2, y=r_IS_cur_flat, mode="lines", name="IS (current, flat)", line=dict(color="#1f77b4")))
    fig_flat.add_trace(go.Scatter(x=Ys_alt2, y=r_LM_cur_flat, mode="lines", name="LM (current)", line=dict(color="#1f77b4")))
    fig_flat.add_trace(go.Scatter(x=[Y_eq_base_flat], y=[r_eq_base_flat], mode="markers", name = "Base Equilibrium", marker=dict(color="gray", size=11, symbol="x")))
    fig_flat.add_trace(go.Scatter(x=[Y_eq_cur_flat], y=[r_eq_cur_flat], mode="markers", name = "Current Equilibrium", marker=dict(color="#1f77b4", size=11, symbol="x")))
    fig_flat.update_layout(title="Flat IS (highly responsive to r)", xaxis_title="Output / Income (Y)", yaxis_title="Interest rate (r)", xaxis=dict(range=[0.0, 60.0], showticklabels=False), yaxis=dict(range=[-1.0, 12.0], showticklabels=False), margin=dict(l=30, r=10, t=30, b=30), height=460)
    st.plotly_chart(fig_flat, use_container_width=True)

st.markdown("---")

colC, colD = st.columns(2)

with colC:
    st.markdown("LM very steep (fiscal largely ineffective)")
    h_steep = 0.05
    A_base_hs = a - c * T + I0 + G0
    den_hs = b * k + h_steep * (1 - c)
    Y_eq_base_hs = float((h_steep * A_base_hs + b * M_base) / den_hs)
    r_eq_base_hs = float((A_base_hs - (1 - c) * Y_eq_base_hs) / b)
    G_cur_hs = G0 + fiscal_shock
    M_cur_hs = M_over_P_base + monetary_shock
    A_cur_hs = a - c * T + I0 + G_cur_hs
    Y_eq_cur_hs = float((h_steep * A_cur_hs + b * M_cur_hs) / den_hs)
    r_eq_cur_hs = float((A_cur_hs - (1 - c) * Y_eq_cur_hs) / b)
    Ys_alt3 = np.linspace(0.0, 60.0, 400)
    r_IS_base_hs = (A_base_hs - (1 - c) * Ys_alt3) / b
    r_LM_base_hs = (k * Ys_alt3 - M_base) / h_steep
    r_IS_cur_hs = (A_cur_hs - (1 - c) * Ys_alt3) / b
    r_LM_cur_hs = (k * Ys_alt3 - M_cur_hs) / h_steep
    fig_hs = go.Figure()
    fig_hs.add_trace(go.Scatter(x=Ys_alt3, y=r_IS_base_hs, mode="lines",name = "IS (baseline)", line=dict(color="gray", dash="dash")))
    fig_hs.add_trace(go.Scatter(x=Ys_alt3, y=r_LM_base_hs, mode="lines", name = "LM (baseline, steep)", line=dict(color="gray", dash="dash")))
    fig_hs.add_trace(go.Scatter(x=Ys_alt3, y=r_IS_cur_hs, mode="lines",name = "IS (current)", line=dict(color="#1f77b4")))
    fig_hs.add_trace(go.Scatter(x=Ys_alt3, y=r_LM_cur_hs, mode="lines", name = "LM (current, steep)", line=dict(color="#1f77b4")))
    fig_hs.add_trace(go.Scatter(x=[Y_eq_base_hs], y=[r_eq_base_hs], mode="markers", name = "Base Equilibrium" , marker=dict(color="gray", size=11, symbol="x")))
    fig_hs.add_trace(go.Scatter(x=[Y_eq_cur_hs], y=[r_eq_cur_hs], mode="markers", name = "Current Equilibrium", marker=dict(color="#1f77b4", size=11, symbol="x")))
    fig_hs.update_layout(title="LM Very Steep (fiscal largely ineffective)", xaxis_title="Output / Income (Y)", yaxis_title="Interest rate (r)", xaxis=dict(range=[0.0, 60.0], showticklabels=False), yaxis=dict(range=[-1.0, 12.0], showticklabels=False), margin=dict(l=30, r=10, t=30, b=30), height=460)
    st.plotly_chart(fig_hs, use_container_width=True)

with colD:
    st.markdown("LM Flat (liquidity trap)")
    h_flat = 50.0
    A_base_hf = a - c * T + I0 + G0
    den_hf = b * k + h_flat * (1 - c)
    Y_eq_base_hf = float((h_flat * A_base_hf + b * M_base) / den_hf)
    r_eq_base_hf = float((A_base_hf - (1 - c) * Y_eq_base_hf) / b)
    G_cur_hf = G0 + fiscal_shock
    M_cur_hf = M_over_P_base + monetary_shock
    A_cur_hf = a - c * T + I0 + G_cur_hf
    Y_eq_cur_hf = float((h_flat * A_cur_hf + b * M_cur_hf) / den_hf)
    r_eq_cur_hf = float((A_cur_hf - (1 - c) * Y_eq_cur_hf) / b)
    Ys_alt4 = np.linspace(0.0, 60.0, 400)
    r_IS_base_hf = (A_base_hf - (1 - c) * Ys_alt4) / b
    r_LM_base_hf = (k * Ys_alt4 - M_base) / h_flat
    r_IS_cur_hf = (A_cur_hf - (1 - c) * Ys_alt4) / b
    r_LM_cur_hf = (k * Ys_alt4 - M_cur_hf) / h_flat
    fig_hf = go.Figure()
    fig_hf.add_trace(go.Scatter(x=Ys_alt4, y=r_IS_base_hf, mode="lines",name = "IS (baseline)", line=dict(color="gray", dash="dash")))
    fig_hf.add_trace(go.Scatter(x=Ys_alt4, y=r_LM_base_hf, mode="lines", name = "IM (baseline, flat)", line=dict(color="gray", dash="dash")))
    fig_hf.add_trace(go.Scatter(x=Ys_alt4, y=r_IS_cur_hf, mode="lines",name = "(current)", line=dict(color="#1f77b4")))
    fig_hf.add_trace(go.Scatter(x=Ys_alt4, y=r_LM_cur_hf, mode="lines", name = "LM (current, flat)",line=dict(color="#1f77b4")))
    fig_hf.add_trace(go.Scatter(x=[Y_eq_base_hf], y=[r_eq_base_hf], mode="markers", name = "Base Equilibrium", marker=dict(color="gray", size=11, symbol="x")))
    fig_hf.add_trace(go.Scatter(x=[Y_eq_cur_hf], y=[r_eq_cur_hf], mode="markers",name = "Current Equilibrium", marker=dict(color="#1f77b4", size=11, symbol="x")))
    fig_hf.update_layout(title="LM Flat (liquidity trap)", xaxis_title="Output / Income (Y)", yaxis_title="Interest rate (r)", xaxis=dict(range=[0.0, 60.0], showticklabels=False), yaxis=dict(range=[-1.0, 12.0], showticklabels=False), margin=dict(l=30, r=10, t=30, b=30), height=460)
    st.plotly_chart(fig_hf, use_container_width=True)

st.markdown("---")

st.subheader("Theoretical Basis and Explanation")
st.markdown("---")
st.write("In order to understand the intricacies of these graphs intuitively, we must define the equations and derivations definitively. " \
"We start with the goods market Equilibrium condition; the essential equation for the Keynesian Cross. Y = C(Y-T) + I(r) + G" \
"Where:\n Y: output / income \nC(Y-T): Consimption which depends positively on disposable income\n" 
"I(r): investment, which depends negatively on the interest rate\n" \
"G: government spending\n\n The vertical axis of the keynesian cross shows planned expenditure\n The " \
"horizontal axis shows the income/output(Y)\n the 45 degree line represents the points where E = Y\n" \
"The expenditure line shifts depending on the interest rate because I(r) affects the total expenditure" \
"When the interest rate falls, investment increases and thus planned expenditure line shifts upwards and the equilibrium output Y rises" \
"From this we trace out the IS curve by plotting each equilibrium Y that corresponds to a given r." \
"Thus the IS curve is downward sloping in (r,Y) space\n\n" \
"Now we explore the derivation of the LM curve. Start with the money market equilibrium condition in real terms: \n" \
"M/P = L(r,Y)\n" \
"where:\n M/P: real money supply\nL(r,Y): real money demand dependant on the interest rates and income\n" \
"The money supply is vertical as it is fixed by the central bank.\n" \
"The money demand curve is downward sloping because as interest rates fall, people want to hold more money.\n" \
"Now we take each equilibrium we take the equilibrium interest rate that balances the money market and using these points we can plot the LM curve. " \
"The LM curve slopes upwards because higher income increases the demand for money and with a fixed supply, the interest rate must also rise to restore equilibrium" \
"\n\n Now we explore the effects of fiscal and monetary policy on the IS-LM. \n" \
"Expansionary fiscal policy: This consists of an increase in G or a decrease in T.Results in a boost in aggregate demand, thus for any given interest rate, equilibrium output in the goods market is higher. Thus the IS curve shifts right. Contractionary fiscal policy does the opposite and shifts the IS curve to the left.\n" \
"Monetary policy: Implemented through changes in the money supply (M) by the central bank. Expansionary policy increases M, and results that for any level of income, interest rates fall due to more liquidity. Thus the LM curve shifts to the right or downward. The oppositite is true for contrationary policy." \
"\n\n Slope Sensitivity:\n Flat IS → Monetary policy very effective, Fiscal less effective.\nSteep IS → Fiscal policy more effective, Monetary less effective.\nFlat LM → Fiscal policy very effective (interest doesn’t rise much).\nSteep LM → Fiscal policy less effective (crowding out dominates)."

)