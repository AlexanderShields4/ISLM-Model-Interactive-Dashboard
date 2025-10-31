IS-LM Model Interactive Dashboard
=================================

Overview
--------
This repository contains a small interactive dashboard (built with Streamlit) that demonstrates the Keynesian Cross, the Money Market, and the IS–LM model. The goal is educational: to let you change simple macroeconomic parameters and immediately see how the equilibrium output and interest rate respond.
link: https://alexandershields4-islm-model-interactive-dashboard-islm1-abobt5.streamlit.app/

What you'll find
----------------
- `ISLM1.py` — the Streamlit app. Run it to launch an interactive dashboard with three panels:
  - Keynesian Cross (Planned Expenditure vs Output)
  - Money Market (Nominal money supply and interest rate)
  - IS–LM Diagrams (Interest rate r vs Output Y) with computed equilibrium point

Quick start
-----------
1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run ISLM1.py
```

This will open a browser window (or show a local URL you can open) with the interactive dashboard.

Key UI elements and parameters
------------------------------
All model parameters are available in the sidebar. Briefly:

- Autonomous consumption (a): the intercept of the consumption function.
- MPC (b): marginal propensity to consume (0 ≤ b < 1 in normal cases).
- Autonomous investment (I0): fixed part of planned investment.
- Government spending (G): fiscal policy lever.
- di: sensitivity of investment to the interest rate (shifts the slope of the IS curve).

Money market parameters:

- Nominal money supply (M): vertical line in the money market panel.
- Price level (P): converts nominal to real money supply (M/P).
- k: sensitivity of money demand to income (Y).
- h: sensitivity of money demand to the interest rate (r).

What the charts show
--------------------
- Keynesian Cross: the 45° line (Y = Planned Expenditure) and the Aggregate Demand curve (AD = C + I + G). The intersection is the Keynesian equilibrium Y*.
- Money Market: the relationship between money (horizontal axis) and the interest rate r (vertical axis) implied by money demand; the vertical money supply line shows the equilibrium interest rate for the chosen money supply.
- IS–LM: IS (goods market) and LM (money market) curves plotted as r vs Y. The intersection gives the simultaneous equilibrium (Y*, r*).

Troubleshooting
---------------
- If the app opens with an empty page or crashes, try running the Streamlit command from a terminal so you can see Python/Streamlit error output:

```bash
streamlit run ISLM1.py
```

- If sliders appear to freeze or not update, make sure you have a modern Streamlit version (see `requirements.txt`) and that the app is not blocked by background errors printed to the terminal.

- If plotted lines appear off-scale (e.g., very large y-intercept), try shrinking autonomous parameter values (a, I0, G) or expand the Y-axis range in the app.

Development notes
-----------------
- The code uses simple closed-form solutions for the Keynesian cross and IS–LM equilibrium where algebra permits. These are computed inside `ISLM1.py` and plotted as markers.

- The model is intentionally simple and deterministic for pedagogical purposes; it omits taxes, expectations, and other extensions.

License
-------
This project is released under the MIT License. See the `LICENSE` file in the repository root for the full text.

Short summary: you may use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, provided that the copyright notice and this license notice are included in all copies or substantial portions of the Software. The software is provided "as is", without warranty of any kind.

Contact
-------
If you want help expanding the dashboard (more parameters, nicer layout, or a deployment-ready Dockerfile), tell me which direction you prefer and I can add the code and tests.
