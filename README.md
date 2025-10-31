IS-LM Model Interactive Dashboard
=================================

Overview
--------
This repository contains a small interactive dashboard (built with Streamlit) that demonstrates the Keynesian Cross, the Money Market, and the IS–LM model. The goal is educational: to let you change simple macroeconomic parameters (autonomous consumption, marginal propensity to consume, government spending, money supply, etc.) and immediately see how the equilibrium output and interest rate respond.

What you'll find
----------------
- `ISLM.py` — the Streamlit app. Run it to launch an interactive dashboard with three panels:
  - Keynesian Cross (Planned Expenditure vs Output)
  - Money Market (Nominal money supply and interest rate)
  - IS–LM Diagram (Interest rate r vs Output Y) with computed equilibrium point

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
streamlit run ISLM.py
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
streamlit run ISLM.py
```

- If sliders appear to freeze or not update, make sure you have a modern Streamlit version (see `requirements.txt`) and that the app is not blocked by background errors printed to the terminal.

- If plotted lines appear off-scale (e.g., very large y-intercept), try shrinking autonomous parameter values (a, I0, G) or expand the Y-axis range in the app.

Development notes
-----------------
- The code uses simple closed-form solutions for the Keynesian cross and IS–LM equilibrium where algebra permits. These are computed inside `ISLM.py` and plotted as markers.

- The model is intentionally simple and deterministic for pedagogical purposes; it omits taxes, expectations, and other extensions.

Contributing
------------
If you'd like to extend the dashboard, consider:
- Adding tax policy (a proportional tax rate) and showing the multiplier effects.
- Making investment an explicit function of r with a non-linear form.
- Adding a short explanation panel that walks the viewer through how fiscal and monetary policy shift the curves.

License & credits
-----------------
This project is provided as-is for educational use. If you include third-party code or packages, follow their licenses (most used packages here are permissively licensed). If you'd like, I can add a specific license file (MIT, Apache 2.0, etc.).

Contact
-------
If you want help expanding the dashboard (more parameters, nicer layout, or a deployment-ready Dockerfile), tell me which direction you prefer and I can add the code and tests.
