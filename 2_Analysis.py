"""
Page 2 — Analysis Answers: 10 KAYEF questions
"""
import streamlit as st

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }
#MainMenu, footer { visibility: hidden; }
.main .block-container { padding: 1rem 2rem 2rem 2rem; max-width: 1100px; }

.page-header {
    border-left: 5px solid #2196F3;
    padding: 18px 24px;
    margin-bottom: 32px;
    border-radius: 0 12px 12px 0;
    background: rgba(33,150,243,0.06);
}
.page-header h1 { font-family:'Cairo',sans-serif; font-size:1.8rem; font-weight:900; margin:0; }
.page-header p  { font-size:0.9rem; color:#78909C; margin:4px 0 0 0; }

.section-label {
    display: inline-flex; align-items: center; gap: 8px;
    font-size: 11px; font-weight: 700; letter-spacing: 2px;
    text-transform: uppercase; padding: 5px 14px;
    border-radius: 20px; margin-bottom: 20px;
}
.easy   { background: rgba(76,175,80,0.12);  color: #2E7D32; border: 1px solid rgba(76,175,80,0.3); }
.medium { background: rgba(255,152,0,0.12);  color: #E65100; border: 1px solid rgba(255,152,0,0.3); }
.hard   { background: rgba(239,83,80,0.12);  color: #C62828; border: 1px solid rgba(239,83,80,0.3); }

.q-card {
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 16px;
    padding: 28px 32px;
    margin-bottom: 20px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.05);
}
.q-header { display:flex; align-items:center; gap:14px; margin-bottom:16px; }
.q-badge {
    font-family:'Cairo',sans-serif;
    font-size:1.3rem; font-weight:900;
    min-width:48px; height:48px;
    border-radius:12px;
    display:flex; align-items:center; justify-content:center;
    flex-shrink:0;
}
.q-badge.easy   { background:rgba(76,175,80,0.15);  color:#2E7D32; }
.q-badge.medium { background:rgba(255,152,0,0.15);  color:#E65100; }
.q-badge.hard   { background:rgba(239,83,80,0.15);  color:#C62828; }
.q-title { font-family:'Cairo',sans-serif; font-size:1.15rem; font-weight:700; margin:0; }
.q-pts   { font-size:11px; color:#90A4AE; font-weight:600; letter-spacing:1px; }

.q-body  { font-size:14px; line-height:1.85; color:#455A64; }
.q-body strong { font-weight:700; color:#263238; }
.q-body h4 { font-family:'Cairo',sans-serif; font-size:1rem; font-weight:700;
             color:#1976D2; margin:18px 0 6px 0; }

.so-what {
    margin-top: 16px;
    padding: 14px 18px;
    border-left: 4px solid #2196F3;
    border-radius: 0 10px 10px 0;
    background: rgba(33,150,243,0.07);
    font-size: 13.5px; line-height: 1.7;
}
.so-what strong { color: #1565C0; }

.stat-table { width:100%; border-collapse:collapse; margin:12px 0; font-size:13px; }
.stat-table th {
    background:rgba(33,150,243,0.1); color:#1565C0;
    padding:8px 12px; text-align:left; font-weight:700;
    border-bottom:2px solid rgba(33,150,243,0.2);
}
.stat-table td { padding:8px 12px; border-bottom:1px solid rgba(0,0,0,0.06); }
.stat-table tr:last-child td { border-bottom:none; }
.highlight-red   { color:#D32F2F; font-weight:700; }
.highlight-green { color:#2E7D32; font-weight:700; }
.highlight-amber { color:#E65100; font-weight:700; }
.highlight-blue  { color:#1565C0; font-weight:700; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
  <h1>🔍 Analysis Answers</h1>
  <p>Week #1 Task — 10 Business Questions · 100 Points Total · Employee Attrition Dataset</p>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# EASY SECTION
# ═══════════════════════════════════════════════════════════════
st.markdown('<div class="section-label easy">🟢 Easy · Foundations · 18 pts</div>', unsafe_allow_html=True)

# Q1
st.markdown("""
<div class="q-card">
  <div class="q-header">
    <div class="q-badge easy">Q1</div>
    <div>
      <div class="q-title">The Headline</div>
      <div class="q-pts">6 POINTS</div>
    </div>
  </div>
  <div class="q-body">
    <h4>📌 Overall Attrition</h4>
    <p><strong>47.5%</strong> of employees left — that's <strong>35,386 out of 74,498</strong>.
    This is <strong>3× the global benchmark</strong> of 10–15%, signaling a deep structural crisis.</p>

    <h4>📌 Which Job Role Is Losing the Most?</h4>
    <p>Surprisingly, <strong>all job roles sit within a 2% attrition band (~46–48%)</strong>.
    There is no single "leaky" role. This is more alarming than having one bad role —
    it means the problem cuts across every function equally.</p>
    <p><strong>Where to look first:</strong> Not at the job descriptions — at the organization itself.
    Culture, management quality, and working conditions are failing every team at the same rate.</p>
  </div>
  <div class="so-what">
    <strong>➡ So what:</strong> Don't waste resources on role-specific fixes. Launch a company-wide
    retention audit covering onboarding quality, manager effectiveness, and working conditions —
    because every department is bleeding equally.
  </div>
</div>
""", unsafe_allow_html=True)

# Q2
st.markdown("""
<div class="q-card">
  <div class="q-header">
    <div class="q-badge easy">Q2</div>
    <div>
      <div class="q-title">Overtime</div>
      <div class="q-pts">6 POINTS</div>
    </div>
  </div>
  <div class="q-body">
    <p>Yes — overtime employees leave at <strong class="highlight-red">51.5%</strong> vs
    <strong class="highlight-green">45.5%</strong> for those who don't — a <strong>6-point gap</strong>.</p>
    <p>The deeper problem: <strong class="highlight-amber">24,341 employees (≈33% of the workforce)</strong>
    currently work overtime. One in three people is under chronic overload.</p>
    <table class="stat-table">
      <tr><th>Group</th><th>Attrition Rate</th><th>Delta vs Baseline</th></tr>
      <tr><td>No Overtime</td><td class="highlight-green">45.5%</td><td>−2 pts</td></tr>
      <tr><td>With Overtime</td><td class="highlight-red">51.5%</td><td>+4 pts</td></tr>
      <tr><td>Company Average</td><td>47.5%</td><td>—</td></tr>
    </table>
  </div>
  <div class="so-what">
    <strong>➡ So what:</strong> HR must treat overtime as a retention risk flag, not just a scheduling issue.
    (1) Cap overtime for roles exceeding a set weekly threshold.
    (2) Audit the highest-OT teams — they are pre-attrition zones.
    (3) Redistribute workload or hire relief before this third of the workforce burns out.
  </div>
</div>
""", unsafe_allow_html=True)

# Q3
st.markdown("""
<div class="q-card">
  <div class="q-header">
    <div class="q-badge easy">Q3</div>
    <div>
      <div class="q-title">Remote Work</div>
      <div class="q-pts">6 POINTS</div>
    </div>
  </div>
  <div class="q-body">
    <p>Remote work is the <strong>single most powerful lever</strong> in this dataset:</p>
    <table class="stat-table">
      <tr><th>Work Mode</th><th>Attrition Rate</th></tr>
      <tr><td>On-Site</td><td class="highlight-red">~53%</td></tr>
      <tr><td>Remote</td><td class="highlight-green">~24%</td></tr>
      <tr><td><strong>Difference</strong></td><td><strong>29 percentage points</strong></td></tr>
    </table>
    <p>This effect holds consistently across <strong>all company sizes</strong>.</p>
    <p><strong>⚠️ Honest caveat:</strong> Only a minority of staff currently work remotely.
    We cannot fully rule out selection bias — remote-eligible roles may be inherently more senior
    or satisfying. We can conclude that <em>where remote is offered, retention dramatically improves</em>,
    but cannot guarantee identical results if applied universally overnight.</p>
  </div>
  <div class="so-what">
    <strong>➡ So what:</strong> Begin a structured hybrid/remote pilot for high-attrition segments
    (Entry-level, on-site, long-commute employees). The data strongly supports expanding
    remote eligibility as a direct retention investment.
  </div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# MEDIUM SECTION
# ═══════════════════════════════════════════════════════════════
st.markdown('<div class="section-label medium">🟡 Medium · Comparison & Segmentation · 42 pts</div>', unsafe_allow_html=True)

# Q4
st.markdown("""
<div class="q-card">
  <div class="q-header">
    <div class="q-badge medium">Q4</div>
    <div>
      <div class="q-title">Pay Fairness</div>
      <div class="q-pts">10 POINTS</div>
    </div>
  </div>
  <div class="q-body">
    <p>The data delivers a striking verdict: the mean monthly income difference between employees
    who left and those who stayed is <strong class="highlight-amber">only $46</strong>.
    The correlation between income and attrition is <strong>r = 0.011</strong> — statistically near zero.</p>
    <p>Within the same job level, higher pay does <strong>not</strong> meaningfully predict whether
    someone stays. Box plots for "Stayed" vs "Left" show nearly identical income distributions.</p>
    <p><strong>At what point does higher pay stop reducing attrition?</strong><br>
    Based on this data — it never started. Pay appears already above the threshold of dissatisfaction.</p>
  </div>
  <div class="so-what">
    <strong>➡ So what:</strong> Redirect retention budget away from blanket salary increases —
    the ROI is near zero. Invest instead in work-life balance programs, remote work infrastructure,
    and career development paths, which are the factors that actually correlate with staying.
  </div>
</div>
""", unsafe_allow_html=True)

# Q5
st.markdown("""
<div class="q-card">
  <div class="q-header">
    <div class="q-badge medium">Q5</div>
    <div>
      <div class="q-title">The Retention Timeline</div>
      <div class="q-pts">11 POINTS</div>
    </div>
  </div>
  <div class="q-body">
    <table class="stat-table">
      <tr><th>Tenure Window</th><th>Attrition Rate</th><th>Risk Level</th></tr>
      <tr><td>0–4 years</td><td class="highlight-red">51–53%</td><td>🔴 Critical</td></tr>
      <tr><td>5–9 years</td><td>~42–45%</td><td>🟡 Elevated</td></tr>
      <tr><td>10+ years</td><td class="highlight-green">Significantly lower</td><td>🟢 Stable</td></tr>
    </table>
    <p>The first five years are the <strong>single highest-risk window.</strong>
    After 10 years, employees cross a loyalty threshold and are far less likely to leave.</p>
    <h4>Where retention effort should be aimed:</h4>
    <ul>
      <li><strong>0–1 year:</strong> Onboarding quality, manager assignment, 30/60/90-day check-ins</li>
      <li><strong>1–4 years:</strong> Career pathing, first promotion timing, engagement programs</li>
      <li><strong>5–9 years:</strong> Mid-career development, leadership opportunity access</li>
      <li><strong>10+ years:</strong> Maintain & reward loyalty — low intervention needed</li>
    </ul>
  </div>
  <div class="so-what">
    <strong>➡ So what:</strong> The company is losing employees before recovering hiring and training costs.
    Build a <strong>"First 5 Years" retention program</strong> with structured milestones, mentorship,
    and clear promotion timelines — that's where the financial loss is concentrated.
  </div>
</div>
""", unsafe_allow_html=True)

# Q6
st.markdown("""
<div class="q-card">
  <div class="q-header">
    <div class="q-badge medium">Q6</div>
    <div>
      <div class="q-title">Engagement Warning Signs</div>
      <div class="q-pts">10 POINTS</div>
    </div>
  </div>
  <div class="q-body">
    <h4>Strongest early-warning combination:</h4>
    <p><strong class="highlight-red">High Performance + Low Job Satisfaction</strong> — this is the most
    dangerous segment. These employees are capable enough to be hired elsewhere quickly,
    and they're already unhappy. They don't complain; they quietly leave.</p>
    <p>Work-Life Balance adds a compounding layer:</p>
    <table class="stat-table">
      <tr><th>Work-Life Balance</th><th>Attrition Rate</th></tr>
      <tr><td>Poor</td><td class="highlight-red">60.2%</td></tr>
      <tr><td>Excellent</td><td class="highlight-green">35.7%</td></tr>
      <tr><td><strong>Gap</strong></td><td><strong>24.5 points</strong> — largest single-variable gap in dataset</td></tr>
    </table>
    <h4>What a manager should watch for:</h4>
    <ul>
      <li>High performer who stops volunteering for stretch projects</li>
      <li>Employee with Poor WLB rating who hasn't been offered any flexibility</li>
      <li>Low Job Satisfaction for 2+ consecutive review cycles</li>
      <li>Entry-level employee with no promotion path discussion after 12 months</li>
    </ul>
  </div>
  <div class="so-what">
    <strong>➡ So what:</strong> Build an early-warning flag in the HRIS that triggers a mandatory
    manager conversation when an employee scores both Low Job Satisfaction AND Poor Work-Life Balance.
    These two signals together are the strongest departure predictor in this dataset.
  </div>
</div>
""", unsafe_allow_html=True)

# Q7
st.markdown("""
<div class="q-card">
  <div class="q-header">
    <div class="q-badge medium">Q7</div>
    <div>
      <div class="q-title">Life Stage</div>
      <div class="q-pts">11 POINTS</div>
    </div>
  </div>
  <div class="q-body">
    <p>Yes — life stage is a powerful predictor across three dimensions:</p>
    <h4>Age:</h4>
    <p>Age 18–25: <strong class="highlight-red">53.1%</strong> — highest age group.
    Every older bracket shows progressively lower attrition. Younger employees have lower financial
    obligations, higher market demand, and more career mobility.</p>
    <h4>Marital Status × Gender:</h4>
    <table class="stat-table">
      <tr><th>Group</th><th>Attrition Rate</th></tr>
      <tr><td>Single Female</td><td class="highlight-red">72.2% ← highest in dataset</td></tr>
      <tr><td>Single Male</td><td class="highlight-red">62.3%</td></tr>
      <tr><td>Married (both)</td><td class="highlight-green">Significantly lower</td></tr>
    </table>
    <h4>Dependents:</h4>
    <p>Employees with dependents show lower attrition — family obligations create "staying forces".</p>
    <p><strong>Highest-risk life-stage profile:</strong> Single · Age 18–25 · No dependents</p>
    <h4>What would actually retain them:</h4>
    <ul>
      <li>Fast career progression and visible promotion paths (they're ambitious, not disloyal)</li>
      <li>Remote/hybrid options (flexibility matters more at this life stage than salary)</li>
      <li>Community & belonging programs (social anchoring replaces family anchoring)</li>
      <li>Mentorship from senior employees (they want to grow, not just collect a paycheck)</li>
    </ul>
  </div>
  <div class="so-what">
    <strong>➡ So what:</strong> Design a dedicated retention track for employees under 30, single,
    with no dependents. Standard tools (pay raises, stability messaging) don't work for this group —
    growth, flexibility, and community do.
  </div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# HARD SECTION
# ═══════════════════════════════════════════════════════════════
st.markdown('<div class="section-label hard">🔴 Hard · Synthesis & Decision-Making · 40 pts</div>', unsafe_allow_html=True)

# Q8
st.markdown("""
<div class="q-card">
  <div class="q-header">
    <div class="q-badge hard">Q8</div>
    <div>
      <div class="q-title">Career Stagnation</div>
      <div class="q-pts">13 POINTS</div>
    </div>
  </div>
  <div class="q-body">
    <p>The data builds an overwhelming case across <strong>four independent variables</strong>
    that all point to the same conclusion:</p>
    <h4>Evidence 1 — Promotions (strongest signal):</h4>
    <p>Number of Promotions has the <strong class="highlight-green">strongest negative correlation
    with attrition: r = −0.081</strong>. More promotions = significantly lower likelihood of leaving.
    This is the #1 retention predictor in the correlation matrix.</p>
    <h4>Evidence 2 — Leadership Opportunities:</h4>
    <p><strong class="highlight-red">95% of employees have zero leadership opportunities.</strong>
    When 19 out of 20 employees see no path to leadership, they find that path elsewhere.</p>
    <h4>Evidence 3 — Innovation Opportunities:</h4>
    <p><strong class="highlight-red">83% of employees have no innovation opportunities.</strong>
    Employees doing repetitive work with no creative challenge disengage silently before leaving.
    Boredom is an attrition driver that never appears on exit interviews.</p>
    <h4>Evidence 4 — Job Level Gap:</h4>
    <table class="stat-table">
      <tr><th>Job Level</th><th>Attrition Rate</th></tr>
      <tr><td>Entry</td><td class="highlight-red">63.3%</td></tr>
      <tr><td>Mid</td><td>~45%</td></tr>
      <tr><td>Senior</td><td class="highlight-green">20.3%</td></tr>
      <tr><td><strong>Gap Entry → Senior</strong></td><td><strong>43 percentage points</strong></td></tr>
    </table>
    <p>The path from Entry to Senior is too slow, unclear, or blocked for most employees.</p>
  </div>
  <div class="so-what">
    <strong>➡ Growth/Mobility Recommendation:</strong><br>
    (1) Create transparent Individual Development Plans (IDPs) for every Entry and Mid-level employee within 30 days of joining.<br>
    (2) Target at least one promotion per 18 months for Entry-level employees who meet performance standards.<br>
    (3) Launch an internal mobility program — let employees rotate before they look outside.<br>
    (4) Open 10% of leadership projects to Entry and Mid-level volunteers.
  </div>
</div>
""", unsafe_allow_html=True)

# Q9
st.markdown("""
<div class="q-card">
  <div class="q-header">
    <div class="q-badge hard">Q9</div>
    <div>
      <div class="q-title">The Highest-Risk Profile</div>
      <div class="q-pts">13 POINTS</div>
    </div>
  </div>
  <div class="q-body">
    <p>After combining the most predictive factors, the highest-risk profile is:</p>
    <p style="font-size:1.1rem; font-weight:700; color:#C62828; text-align:center; padding:12px;
       background:rgba(239,83,80,0.08); border-radius:10px; margin:12px 0;">
      Entry-Level · On-Site · Single · Age 18–25
    </p>
    <table class="stat-table">
      <tr><th>Factor</th><th>Attrition</th><th>Delta vs 47.5% avg</th></tr>
      <tr><td>Entry Level</td><td class="highlight-red">63.3%</td><td>+15.8 pts</td></tr>
      <tr><td>Entry + No Remote</td><td class="highlight-red">69.3%</td><td>+21.8 pts</td></tr>
      <tr><td>Single Female</td><td class="highlight-red">72.2%</td><td>+24.7 pts</td></tr>
      <tr><td>Age 18–25</td><td class="highlight-red">53.1%</td><td>+5.6 pts</td></tr>
      <tr><td><strong>Combined profile (est.)</strong></td><td class="highlight-red"><strong>~75–80%</strong></td><td><strong>+27–32 pts</strong></td></tr>
    </table>
    <h4>How many employees match this profile?</h4>
    <ul>
      <li>Entry Level (~33% of 74,498): <strong>~24,584</strong></li>
      <li>Of those, on-site (~67%): <strong>~16,471</strong></li>
      <li>Of those, single (~35%): <strong>~5,765</strong></li>
      <li>Of those, age 18–25 (~40%): <strong>~2,300 employees</strong></li>
    </ul>
    <p><strong>Is it worth acting on?</strong> Yes — 2,300 employees at ~77% attrition =
    <strong class="highlight-red">~1,770 expected to leave</strong>. At a conservative $5,000
    replacement cost: <strong class="highlight-red">~$8.85M in avoidable turnover cost</strong>
    from this profile alone.</p>
  </div>
  <div class="so-what">
    <strong>➡ So what:</strong> Flag every employee matching this profile in the HRIS and assign
    a dedicated retention action: remote-work eligibility review, fast-track promotion assessment,
    and a manager check-in within 30 days.
  </div>
</div>
""", unsafe_allow_html=True)

# Q10
st.markdown("""
<div class="q-card">
  <div class="q-header">
    <div class="q-badge hard">Q10</div>
    <div>
      <div class="q-title">What Moves the Needle</div>
      <div class="q-pts">14 POINTS</div>
    </div>
  </div>
  <div class="q-body">
    <h4>Top 3 drivers ranked by attrition delta above baseline (47.5%):</h4>
    <table class="stat-table">
      <tr><th>Rank</th><th>Driver</th><th>Attrition When Present</th><th>Delta</th><th>Scale</th></tr>
      <tr><td>🥇 1</td><td><strong>No Remote Work</strong></td><td class="highlight-red">~53%</td><td>+5.5 pts</td><td>~50,000+ employees</td></tr>
      <tr><td>🥈 2</td><td><strong>Poor Work-Life Balance</strong></td><td class="highlight-red">60.2%</td><td>+12.7 pts</td><td>~25% of workforce</td></tr>
      <tr><td>🥉 3</td><td><strong>Entry Level + No Career Path</strong></td><td class="highlight-red">63–69%</td><td>+15–21 pts</td><td>~24,500 employees</td></tr>
    </table>
    <h4>🥇 #1 Pick: Expand Remote Work for Entry-Level Employees</h4>
    <p>Remote work reduces attrition from ~53% on-site to ~24% remote — a
    <strong class="highlight-green">29-point reduction</strong>. For Entry-level specifically,
    it drops from 69.3% to an estimated ~35%, cutting attrition nearly in half.</p>
    <p><strong>Why this beats the alternatives:</strong></p>
    <ul>
      <li>Work-Life Balance is slower to fix (requires culture change, management training)</li>
      <li>Career paths require structural changes (new HR systems, promotion budget)</li>
      <li>Remote work is a <strong>policy decision</strong> — implementable in weeks, low operational cost,
      biggest measurable return in the dataset</li>
    </ul>
    <h4>Rough impact estimate:</h4>
    <table class="stat-table">
      <tr><th>Metric</th><th>Value</th></tr>
      <tr><td>Entry-level on-site employees</td><td>~16,500</td></tr>
      <tr><td>Current attrition (69.3%)</td><td class="highlight-red">~11,433 leaving</td></tr>
      <tr><td>Post-remote attrition (est. 35%)</td><td class="highlight-green">~5,775 leaving</td></tr>
      <tr><td><strong>Employees retained</strong></td><td class="highlight-green"><strong>~5,658</strong></td></tr>
      <tr><td><strong>Cost saved (@ $5k/hire)</strong></td><td class="highlight-green"><strong>~$28.3M per cycle</strong></td></tr>
    </table>
  </div>
  <div class="so-what">
    <strong>➡ Recommendation:</strong> Next quarter, extend remote-work eligibility to all Entry-level
    employees whose roles permit it (est. 60–70% of Entry roles). Run a 90-day pilot.
    Measure 30-day and 90-day retention rates against the current baseline.<br><br>
    <strong>The data is clear — remote work is not a perk. For this workforce, it is a retention
    strategy with a measurable 29-point return.</strong>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.caption("Analysis by Mostafa Nabil · KAYEF AI Engineering Program · Week #1 Task")
