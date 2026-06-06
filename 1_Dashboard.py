"""
Page 1 — Dashboard: 19 interactive charts
"""
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

# ── CSS: light/dark compatible (no hardcoded dark backgrounds) ────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }
#MainMenu, footer { visibility: hidden; }

.main .block-container { padding: 1rem 2rem 2rem 2rem; max-width: 1400px; }

/* Header */
.dash-header {
    border: 1px solid rgba(33,150,243,0.3);
    border-radius: 20px;
    padding: 28px 36px;
    margin-bottom: 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
}
.dash-week-tag {
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #2196F3;
    margin-bottom: 6px;
}
.dash-title {
    font-family: 'Cairo', sans-serif;
    font-size: 1.9rem;
    font-weight: 900;
    margin: 0;
    line-height: 1.2;
}
.dash-subtitle {
    font-size: 0.88rem;
    color: #78909C;
    margin-top: 6px;
    font-weight: 300;
}

/* KPI Cards */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-bottom: 28px;
}
.kpi-card {
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 16px;
    padding: 24px 28px;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.kpi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    border-radius: 16px 16px 0 0;
}
.kpi-card.blue::before  { background: linear-gradient(90deg, #2196F3, #42A5F5); }
.kpi-card.red::before   { background: linear-gradient(90deg, #EF5350, #EF9A9A); }
.kpi-card.amber::before { background: linear-gradient(90deg, #FF8F00, #FFC107); }
.kpi-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #90CAF9;
    margin-bottom: 10px;
}
.kpi-value {
    font-family: 'Cairo', sans-serif;
    font-size: 2.4rem;
    font-weight: 900;
    line-height: 1;
    margin-bottom: 4px;
}
.kpi-value.blue  { color: #2196F3; }
.kpi-value.red   { color: #EF5350; }
.kpi-value.amber { color: #FF8F00; }
.kpi-sub { font-size: 12px; color: #90A4AE; }

/* Chart section */
.chart-section {
    border: 1px solid rgba(0,0,0,0.07);
    border-radius: 20px;
    padding: 28px;
    margin-bottom: 24px;
    box-shadow: 0 2px 16px rgba(0,0,0,0.05);
}
.chart-number {
    background: linear-gradient(135deg, #2196F3, #1565C0);
    color: white;
    font-size: 11px;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 20px;
    letter-spacing: 0.5px;
    display: inline-block;
}
.chart-name {
    font-family: 'Cairo', sans-serif;
    font-size: 1.2rem;
    font-weight: 700;
    margin: 8px 0 0 0;
}

/* Insight / Warning boxes */
.insight-box {
    border-left: 4px solid #2196F3;
    border-radius: 0 12px 12px 0;
    padding: 14px 18px;
    margin-top: 16px;
    background: rgba(33,150,243,0.07);
}
.insight-title {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #1976D2;
    margin-bottom: 6px;
}
.insight-text {
    font-size: 13.5px;
    line-height: 1.7;
    margin: 0;
}
.warning-box {
    border-left: 4px solid #EF5350;
    border-radius: 0 12px 12px 0;
    padding: 14px 18px;
    margin-top: 16px;
    background: rgba(239,83,80,0.07);
}
.warning-title {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #C62828;
    margin-bottom: 6px;
}
.warning-text { font-size: 13.5px; line-height: 1.7; margin: 0; }

/* Keyword highlights */
.kw-red   { background:rgba(239,83,80,0.15);  color:#D32F2F; font-weight:700; padding:1px 6px; border-radius:4px; }
.kw-green { background:rgba(76,175,80,0.15);  color:#2E7D32; font-weight:700; padding:1px 6px; border-radius:4px; }
.kw-blue  { background:rgba(33,150,243,0.15); color:#1565C0; font-weight:700; padding:1px 6px; border-radius:4px; }
.kw-amber { background:rgba(255,152,0,0.15);  color:#E65100; font-weight:700; padding:1px 6px; border-radius:4px; }

/* Divider */
.section-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(33,150,243,0.25), transparent);
    margin: 8px 0 24px 0;
}
</style>
""", unsafe_allow_html=True)

# ── Helpers ───────────────────────────────────────────────────────────────────
C = dict(stayed="#2196F3", left="#EF5350", line="#FF8F00", grid="rgba(0,0,0,0.06)",
         paper="rgba(0,0,0,0)", text="#37474F")
BLUE_SEQ  = [[0,"#BBDEFB"],[0.5,"#1E88E5"],[1,"#0D47A1"]]
DIVERGING = [[0,"#EF5350"],[0.5,"#ECEFF1"],[1,"#2196F3"]]

def layout(title, sub, h=480):
    return dict(
        title=dict(text=f"<b>{title}</b><br><sub>{sub}</sub>", x=0.5,
                   font=dict(size=16, color=C["text"])),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="IBM Plex Sans, sans-serif", color=C["text"]),
        height=h,
        margin=dict(t=80, b=50, l=50, r=30),
        legend=dict(orientation="h", y=-0.22, x=0.5, xanchor="center",
                    bgcolor="rgba(0,0,0,0)")
    )

def ax(**kw):
    return dict(gridcolor=C["grid"], linecolor="rgba(0,0,0,0.1)", zeroline=False,
                tickfont=dict(size=11, color="#546E7A"),
                title_font=dict(size=12, color="#546E7A"), **kw)

def show(fig): st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

@st.cache_data
def load_data(f=None):
    import os
    if f is not None:
        try:    return pd.read_excel(f)
        except: return pd.read_csv(f)
    for path in ["final_dataset.csv","final_dataset.xlsx"]:
        if os.path.exists(path):
            return pd.read_csv(path) if path.endswith(".csv") else pd.read_excel(path)
    return None

# ── Charts ────────────────────────────────────────────────────────────────────
def chart1(df):
    c = df["Attrition"].value_counts()
    fig = go.Figure(go.Pie(
        labels=c.index, values=c.values, hole=0.6,
        marker=dict(colors=[C["stayed"],C["left"]], line=dict(color="white",width=3)),
        textinfo="percent+label", textfont=dict(size=13),
        hovertemplate="<b>%{label}</b><br>Count: %{value:,}<br>Share: %{percent}<extra></extra>"
    ))
    fig.update_layout(**layout("Attrition Overview","Stayed vs. Left",420),
        annotations=[dict(text=f"<b>{len(df):,}</b><br>Total",
                          x=0.5,y=0.5,showarrow=False,font=dict(size=14,color=C["text"]))])
    show(fig)

def chart2(df):
    g  = df.groupby(["Gender","Attrition"]).size().unstack()
    gp = df.groupby("Gender")["Attrition"].value_counts(normalize=True).unstack()*100
    fig = go.Figure([
        go.Bar(name="Stayed",x=g.index,y=g["Stayed"],marker_color=C["stayed"],
               text=[f"{v:,}" for v in g["Stayed"]],textposition="outside"),
        go.Bar(name="Left",  x=g.index,y=g["Left"],  marker_color=C["left"],
               text=[f"{v:,}" for v in g["Left"]],  textposition="outside"),
    ])
    for gen in g.index:
        fig.add_annotation(x=gen,y=g.loc[gen].max()+2000,
                           text=f"<b>Rate: {gp.loc[gen,'Left']:.1f}%</b>",
                           showarrow=False,font=dict(size=11,color=C["left"]))
    fig.update_layout(**layout("Attrition by Gender","Comparing turnover between genders"),barmode="group")
    fig.update_xaxes(**ax(title_text="Gender")); fig.update_yaxes(**ax(title_text="Headcount"))
    show(fig)

def chart3(df):
    df=df.copy()
    df["AG"]=pd.cut(df["Age"],[17,25,35,45,55,65],labels=["18–25","26–35","36–45","46–55","56–65"])
    g =df.groupby(["AG","Attrition"],observed=False).size().unstack()
    gp=df.groupby("AG",observed=False)["Attrition"].value_counts(normalize=True).unstack()*100
    fig=go.Figure([
        go.Bar(name="Stayed",x=g.index.astype(str),y=g["Stayed"],marker_color=C["stayed"]),
        go.Bar(name="Left",  x=g.index.astype(str),y=g["Left"],  marker_color=C["left"]),
    ])
    fig.add_trace(go.Scatter(name="Attrition Rate %",x=g.index.astype(str),y=gp["Left"],yaxis="y2",
        mode="lines+markers",line=dict(color=C["line"],width=2.5),marker=dict(size=9,color=C["line"])))
    fig.update_layout(**layout("Attrition by Age Group","How attrition shifts across age brackets"),barmode="group",
        yaxis2=dict(overlaying="y",side="right",range=[0,100],showgrid=False,
                    title="Rate (%)",tickfont=dict(color=C["line"]),title_font=dict(color=C["line"])))
    fig.update_xaxes(**ax(title_text="Age Group")); fig.update_yaxes(**ax(title_text="Headcount"))
    show(fig)

def chart4(df):
    pct=df.groupby("Job Role")["Attrition"].apply(lambda x:(x=="Left").mean()*100).sort_values()
    fig=go.Figure(go.Bar(x=pct.values,y=pct.index,orientation="h",
        marker=dict(color=pct.values,colorscale=BLUE_SEQ,showscale=True,
                    colorbar=dict(title="Rate %")),
        text=[f"{v:.1f}%" for v in pct.values],textposition="outside"))
    fig.update_layout(**layout("Attrition by Job Role","Which roles have highest turnover?",420))
    fig.update_xaxes(**ax(title_text="Attrition Rate (%)"))
    show(fig)

def chart5(df):
    fig=go.Figure()
    for label,color in [("Stayed",C["stayed"]),("Left",C["left"])]:
        sub=df[df["Attrition"]==label]["Monthly Income"]
        fig.add_trace(go.Box(y=sub,name=label,marker_color=color,boxmean=True,line=dict(color=color)))
        fig.add_annotation(x=label,y=sub.mean()+800,text=f"<b>Mean: ${sub.mean():,.0f}</b>",
                           showarrow=False,font=dict(size=11,color=color))
    fig.update_layout(**layout("Monthly Income by Attrition","Do lower earners leave more?"))
    fig.update_yaxes(**ax(title_text="Monthly Income (USD)"))
    show(fig)

def chart6(df):
    order=["Poor","Fair","Good","Excellent"]
    g =df.groupby(["Work-Life Balance","Attrition"],observed=False).size().unstack().reindex(order)
    gp=df.groupby("Work-Life Balance",observed=False)["Attrition"].value_counts(normalize=True).unstack().reindex(order)*100
    fig=go.Figure([
        go.Bar(name="Stayed",x=g.index,y=g["Stayed"],marker_color=C["stayed"],
               text=[f"{v:,}" for v in g["Stayed"]],textposition="inside"),
        go.Bar(name="Left",  x=g.index,y=g["Left"],  marker_color=C["left"],
               text=[f"{v:,}" for v in g["Left"]],  textposition="inside"),
    ])
    for wl in order:
        fig.add_annotation(x=wl,y=g.loc[wl].sum()+800,
                           text=f"<b>Rate: {gp.loc[wl,'Left']:.1f}%</b>",
                           showarrow=False,font=dict(size=10,color=C["left"]))
    fig.update_layout(**layout("Attrition by Work-Life Balance","Does poor WLB drive attrition?"),barmode="stack")
    fig.update_xaxes(**ax(title_text="Work-Life Balance")); fig.update_yaxes(**ax(title_text="Headcount"))
    show(fig)

def chart7(df):
    ot=df.groupby("Overtime")["Attrition"].value_counts(normalize=True).unstack()*100
    oy=df[df["Overtime"]=="Yes"]["Attrition"].value_counts()
    fig=make_subplots(1,2,specs=[[{"type":"pie"},{"type":"bar"}]],
                      subplot_titles=("Among Overtime Workers","Attrition Rate: OT vs No OT"))
    fig.add_trace(go.Pie(labels=["Stayed","Left"],values=[oy.get("Stayed",0),oy.get("Left",0)],
        marker=dict(colors=[C["stayed"],C["left"]]),hole=0.5,textinfo="percent+label"),1,1)
    fig.add_trace(go.Bar(x=["No Overtime","With Overtime"],y=ot["Left"],
        marker=dict(color=[C["stayed"],C["left"]]),
        text=[f"{v:.1f}%" for v in ot["Left"]],textposition="outside"),1,2)
    fig.update_layout(**layout("Overtime Impact on Attrition","Overtime employees leave significantly more",450),showlegend=False)
    show(fig)

def chart8(df):
    df2=df.copy()
    df2["Education Level"]=df2["Education Level"].str.replace("'","'").str.replace("'","'")
    order=["High School","Associate Degree","Bachelor's Degree","Master's Degree","PhD"]
    short=["High\nSchool","Associate\nDegree","Bachelor's\nDegree","Master's\nDegree","PhD"]
    pct=df2.groupby("Education Level")["Attrition"].apply(lambda x:(x=="Left").mean()*100).reindex(order)
    counts=df2["Education Level"].value_counts().reindex(order)
    pct_vals=[v if not pd.isna(v) else 0 for v in pct.values]
    fig=go.Figure(go.Bar(x=short,y=pct_vals,
        marker=dict(color=pct_vals,colorscale=BLUE_SEQ,showscale=True),
        text=[f"{v:.1f}%" for v in pct_vals],textposition="outside"))
    for lbl,p,n in zip(short,pct_vals,[counts.get(k,0) for k in order]):
        if p>0: fig.add_annotation(x=lbl,y=p+3.5,text=f"n={n:,}",showarrow=False,font=dict(size=10,color="#90A4AE"))
    fig.update_layout(**layout("Attrition by Education Level","Does education correlate with turnover?",500))
    fig.update_xaxes(**ax(title_text="Education Level"))
    fig.update_yaxes(**ax(title_text="Attrition Rate (%)",range=[0,60]))
    show(fig)

def chart9(df):
    cols=["Age","Years at Company","Monthly Income","Number of Promotions",
          "Distance from Home","Number of Dependents","Company Tenure"]
    df2=df.copy(); df2["Attrition_Bin"]=(df2["Attrition"]=="Left").astype(int)
    corr=df2[cols+["Attrition_Bin"]].corr()
    labels=["Age","Years","Income","Promotions","Distance","Dependents","Tenure","Attrition"]
    fig=go.Figure(go.Heatmap(z=corr.values,x=labels,y=labels,colorscale=DIVERGING,zmin=-1,zmax=1,
        text=corr.round(2).values,texttemplate="%{text:.2f}",textfont=dict(size=10),
        colorbar=dict(title="r")))
    fig.update_layout(**layout("Correlation Heatmap","Which variables correlate with attrition?",500))
    show(fig)

def chart10(df):
    df=df.copy(); bins=list(range(0,55,5))
    df["YG"]=pd.cut(df["Years at Company"],bins=bins,
                    labels=[f"{i}–{i+4}" for i in bins[:-1]],include_lowest=True)
    g =df.groupby("YG",observed=True)["Attrition"].value_counts().unstack(fill_value=0)
    gp=df.groupby("YG",observed=True)["Attrition"].value_counts(normalize=True).unstack(fill_value=0)*100
    fig=go.Figure([
        go.Bar(name="Stayed",x=g.index.astype(str),y=g["Stayed"],marker_color=C["stayed"]),
        go.Bar(name="Left",  x=g.index.astype(str),y=g["Left"],  marker_color=C["left"]),
    ])
    fig.add_trace(go.Scatter(name="Attrition Rate %",x=g.index.astype(str),y=gp["Left"],yaxis="y2",
        mode="lines+markers",line=dict(color=C["line"],width=2.5),marker=dict(size=8,color=C["line"])))
    fig.update_layout(**layout("Attrition by Tenure","Early employees have higher turnover"),barmode="stack",
        yaxis2=dict(overlaying="y",side="right",range=[0,100],showgrid=False,
                    title="Rate (%)",tickfont=dict(color=C["line"]),title_font=dict(color=C["line"])))
    fig.update_xaxes(**ax(title_text="Years at Company")); fig.update_yaxes(**ax(title_text="Headcount"))
    show(fig)

def chart11(df):
    data=df.groupby(["Marital Status","Gender"])["Attrition"].apply(lambda x:(x=="Left").mean()*100).unstack()
    colors={"Male":C["stayed"],"Female":"#AB47BC"}
    fig=go.Figure([go.Bar(name=g,x=data.index,y=data[g],marker_color=colors.get(g,"#78909C"),
        text=[f"{v:.1f}%" for v in data[g]],textposition="outside") for g in data.columns])
    fig.update_layout(**layout("Attrition by Marital Status & Gender","Single employees show highest turnover"),barmode="group")
    fig.update_xaxes(**ax(title_text="Marital Status")); fig.update_yaxes(**ax(title_text="Attrition Rate (%)"))
    show(fig)

def chart12(df):
    data=df.groupby(["Company Size","Remote Work"])["Attrition"].apply(lambda x:(x=="Left").mean()*100).unstack()
    colors={"Yes":"#26A69A","No":C["left"]}; labels={"Yes":"Remote","No":"On-site"}
    fig=go.Figure([go.Bar(name=labels.get(k,k),x=data.index,y=data[k],marker_color=colors.get(k,"#78909C"),
        text=[f"{v:.1f}%" for v in data[k]],textposition="outside") for k in data.columns])
    fig.update_layout(**layout("Attrition by Company Size & Remote Work","How size and remote work affect turnover"),barmode="group")
    fig.update_xaxes(**ax(title_text="Company Size")); fig.update_yaxes(**ax(title_text="Attrition Rate (%)"))
    show(fig)

def chart13(df):
    pivot=df.groupby(["Performance Rating","Job Satisfaction"])["Attrition"].apply(
        lambda x:(x=="Left").mean()*100).unstack()
    fig=go.Figure(go.Heatmap(z=pivot.values,x=pivot.columns,y=pivot.index,colorscale=BLUE_SEQ,
        text=pivot.round(1).values,texttemplate="%{text:.1f}%",textfont=dict(size=11),
        colorbar=dict(title="Rate %")))
    fig.update_layout(**layout("Performance Rating × Job Satisfaction","Interaction effects on attrition",420))
    show(fig)

def chart14(df):
    df=df.copy()
    df["DG"]=pd.cut(df["Distance from Home"],[0,20,40,60,80,100],
                    labels=["0–20","21–40","41–60","61–80","81–100"])
    pct=df.groupby("DG",observed=True)["Attrition"].apply(lambda x:(x=="Left").mean()*100)
    fig=go.Figure(go.Bar(x=pct.index.astype(str),y=pct.values,
        marker=dict(color=pct.values,colorscale=BLUE_SEQ,showscale=True),
        text=[f"{v:.1f}%" for v in pct.values],textposition="outside"))
    fig.update_layout(**layout("Attrition by Commute Distance","Does longer commute drive attrition?"))
    fig.update_xaxes(**ax(title_text="Distance from Home (km)"))
    fig.update_yaxes(**ax(title_text="Attrition Rate (%)",range=[0,pct.max()*1.25]))
    show(fig)

def chart15(df):
    pct  =df.groupby("Leadership Opportunities")["Attrition"].apply(lambda x:(x=="Left").mean()*100)
    count=df["Leadership Opportunities"].value_counts()
    colors={"No":C["left"],"Yes":C["stayed"]}; labels={"No":"No Leadership Opps","Yes":"Has Leadership Opps"}
    fig=go.Figure()
    for val in ["No","Yes"]:
        fig.add_trace(go.Bar(x=[labels[val]],y=[pct[val]],name=labels[val],marker_color=colors[val],
            text=[f"{pct[val]:.1f}%"],textposition="outside",width=0.4))
        fig.add_annotation(x=labels[val],y=pct[val]+3,text=f"n={count[val]:,}",
                           showarrow=False,font=dict(size=11,color="#90A4AE"))
    fig.update_layout(**layout("Attrition by Leadership Opportunities",
        f"Only {count.get('Yes',0)/len(df)*100:.1f}% of employees have leadership opportunities",420),
        showlegend=False,yaxis=dict(**ax(title_text="Attrition Rate (%)",range=[0,60])))
    show(fig)

def chart16(df):
    pct  =df.groupby("Innovation Opportunities")["Attrition"].apply(lambda x:(x=="Left").mean()*100)
    count=df["Innovation Opportunities"].value_counts()
    colors={"No":C["left"],"Yes":C["stayed"]}; labels={"No":"No Innovation Opps","Yes":"Has Innovation Opps"}
    fig=go.Figure()
    for val in ["No","Yes"]:
        fig.add_trace(go.Bar(x=[labels[val]],y=[pct[val]],name=labels[val],marker_color=colors[val],
            text=[f"{pct[val]:.1f}%"],textposition="outside",width=0.4))
        fig.add_annotation(x=labels[val],y=pct[val]+3,text=f"n={count[val]:,}",
                           showarrow=False,font=dict(size=11,color="#90A4AE"))
    fig.update_layout(**layout("Attrition by Innovation Opportunities",
        f"{count.get('No',0)/len(df)*100:.1f}% of employees have no innovation opportunities",420),
        showlegend=False,yaxis=dict(**ax(title_text="Attrition Rate (%)",range=[0,60])))
    show(fig)

def chart17(df):
    order=["Poor","Fair","Good","Excellent"]
    pct  =df.groupby("Company Reputation")["Attrition"].apply(lambda x:(x=="Left").mean()*100).reindex(order)
    count=df["Company Reputation"].value_counts().reindex(order)
    fig=go.Figure(go.Bar(x=pct.values,y=pct.index,orientation="h",
        marker=dict(color=pct.values,colorscale=DIVERGING,cmin=35,cmax=60,showscale=True),
        text=[f"{v:.1f}%" for v in pct.values],textposition="outside"))
    for rep,p in zip(pct.index,pct.values):
        fig.add_annotation(x=p+2,y=rep,text=f"n={count[rep]:,}",
                           showarrow=False,font=dict(size=10,color="#90A4AE"),xanchor="left")
    fig.update_layout(**layout("Attrition by Company Reputation","Poor reputation drives significantly higher turnover",420),
        xaxis=dict(**ax(title_text="Attrition Rate (%)",range=[0,70])),
        yaxis=dict(**ax(title_text="Company Reputation")))
    show(fig)

def chart18(df):
    order=["Low","Medium","High","Very High"]
    pct  =df.groupby("Employee Recognition",observed=False)["Attrition"].apply(
              lambda x:(x=="Left").mean()*100).reindex(order)
    count=df["Employee Recognition"].value_counts().reindex(order)
    fig=go.Figure()
    fig.add_trace(go.Bar(x=pct.index,y=pct.values,
        marker=dict(color=pct.values,colorscale=BLUE_SEQ,showscale=True),
        text=[f"{v:.1f}%" for v in pct.values],textposition="outside",name="Attrition Rate"))
    fig.add_trace(go.Scatter(x=order,y=count.values,yaxis="y2",mode="lines+markers",
        line=dict(color=C["line"],width=2.5,dash="dot"),marker=dict(size=9,color=C["line"]),
        name="Employee Count"))
    fig.update_layout(**layout("Attrition by Employee Recognition",
        "Recognition level has minimal impact — only 1.8% difference across all levels",480),
        yaxis=dict(**ax(title_text="Attrition Rate (%)",range=[0,60])),
        yaxis2=dict(overlaying="y",side="right",showgrid=False,title="Employee Count",
                    tickfont=dict(color=C["line"]),title_font=dict(color=C["line"])))
    show(fig)

def chart19(df):
    order_jl=["Entry","Mid","Senior"]
    g  =df.groupby("Job Level")["Attrition"].value_counts().unstack().reindex(order_jl)
    gp =df.groupby("Job Level")["Attrition"].value_counts(normalize=True).unstack().reindex(order_jl)*100
    pivot=df.groupby(["Job Level","Remote Work"])["Attrition"].apply(
              lambda x:(x=="Left").mean()*100).unstack().reindex(order_jl)
    fig=make_subplots(rows=1,cols=2,column_widths=[0.6,0.4],
        subplot_titles=("Attrition Count & Rate by Job Level","Rate % by Job Level × Remote Work"),
        specs=[[{"type":"bar"},{"type":"heatmap"}]])
    fig.add_trace(go.Bar(name="Stayed",x=order_jl,y=g["Stayed"],marker_color=C["stayed"],
        text=[f"{v:,}" for v in g["Stayed"]],textposition="inside"),row=1,col=1)
    fig.add_trace(go.Bar(name="Left",x=order_jl,y=g["Left"],marker_color=C["left"],
        text=[f"{v:,}" for v in g["Left"]],textposition="inside"),row=1,col=1)
    fig.add_trace(go.Scatter(name="Attrition Rate %",x=order_jl,y=gp["Left"],yaxis="y2",
        mode="lines+markers",line=dict(color=C["line"],width=2.5),marker=dict(size=10,color=C["line"])),row=1,col=1)
    fig.add_trace(go.Heatmap(z=pivot.values,x=pivot.columns.tolist(),y=order_jl,
        colorscale=BLUE_SEQ,text=pivot.round(1).values,texttemplate="%{text:.1f}%",
        textfont=dict(size=13),colorbar=dict(title="Rate %",x=1.02),showscale=True),row=1,col=2)
    fig.update_layout(**layout("Job Level Impact on Attrition",
        "Entry-level employees leave at 63.3% — Senior at only 20.3%",500),
        barmode="group",
        yaxis2=dict(overlaying="y",side="right",range=[0,100],showgrid=False,
                    title="Rate (%)",tickfont=dict(color=C["line"]),title_font=dict(color=C["line"])))
    fig.update_xaxes(title_text="Job Level",row=1,col=1)
    fig.update_yaxes(title_text="Headcount",row=1,col=1)
    fig.update_xaxes(title_text="Remote Work",row=1,col=2)
    show(fig)

# ── Insights ──────────────────────────────────────────────────────────────────
INSIGHTS = {
    "1":  ("insight", 'نسبة الـ Attrition تبلغ <span class="kw-red">47.5%</span> — ضعف المعدل العالمي الطبيعي <span class="kw-blue">10-15%</span>. يعني تقريباً <span class="kw-red">موظف من كل 2 يغادر الشركة</span>، وهو ما يشير إلى <span class="kw-amber">مشكلة هيكلية عميقة</span> تستوجب تحقيقاً فورياً.'),
    "2":  ("warning", 'الإناث يغادرن بنسبة <span class="kw-red">53%</span> مقابل <span class="kw-blue">42.9%</span> للذكور — فارق <span class="kw-amber">10 نقاط كاملة</span>. هذا يوحي بوجود تحديات خاصة تواجه الموظفات، سواء في <span class="kw-red">التوازن الأسري</span> أو <span class="kw-red">فرص الترقي</span> أو بيئة العمل.'),
    "3":  ("insight", 'فئة <span class="kw-red">18-25 سنة</span> هي الأعلى في المغادرة بنسبة <span class="kw-red">53.1%</span>. كل ما زاد العمر انخفضت النسبة تدريجياً، مما يستوجب التركيز على <span class="kw-green">برامج الاحتفاظ بالموظفين الجدد</span>.'),
    "4":  ("insight", 'الفارق بين الوظائف لا يتجاوز <span class="kw-blue">2%</span> — وهذا يؤكد أن المشكلة <span class="kw-red">ليست في وظيفة بعينها</span>، بل هي <span class="kw-amber">مشكلة مؤسسية شاملة</span> تمس ثقافة الشركة وسياساتها.'),
    "5":  ("warning", 'الفارق في الراتب بين من غادروا ومن بقوا هو <span class="kw-amber">46 دولاراً فقط</span>! هذا يكشف أن <span class="kw-red">الراتب ليس السبب الرئيسي للمغادرة</span>، مما يعني أن <span class="kw-amber">رفع الرواتب وحده لن يحل المشكلة</span>.'),
    "6":  ("warning", 'موظفو الـ <span class="kw-red">Poor WLB</span> يغادرون بنسبة <span class="kw-red">60.2%</span> مقابل <span class="kw-green">35.7%</span> لأصحاب الـ Excellent — فارق <span class="kw-amber">24.5 نقطة</span>! <span class="kw-blue">التوازن بين العمل والحياة</span> هو أكثر العوامل تأثيراً على الاستبقاء.'),
    "7":  ("insight", 'الموظفون الذين يعملون <span class="kw-red">أوفر تايم</span> يغادرون بنسبة <span class="kw-red">51.5%</span> مقابل <span class="kw-green">45.5%</span>. والخطير أن <span class="kw-amber">ثلث الموظفين (24,341)</span> يعملون أوفر تايم، مما يشكل <span class="kw-red">ضغطاً مزمناً</span> على المؤسسة.'),
    "8":  ("insight", 'أصحاب <span class="kw-green">PhD</span> يغادرون بنسبة <span class="kw-green">24.4% فقط</span> مقارنة بـ <span class="kw-red">~48%</span> لباقي المستويات — فارق مذهل! في حين أن باقي المستويات التعليمية <span class="kw-blue">متقاربة جداً</span> في نسب المغادرة.'),
    "9":  ("insight", 'أقوى عامل للاستبقاء هو <span class="kw-green">الترقيات (-0.081)</span>، وأقوى عامل للمغادرة هو <span class="kw-red">بُعد المسافة (+0.094)</span>. أما الراتب فعلاقته بالمغادرة <span class="kw-amber">شبه معدومة (0.011)</span>.'),
    "10": ("warning", 'أول <span class="kw-red">5 سنوات</span> هي الأخطر بنسبة مغادرة <span class="kw-red">51-53%</span>. بعد <span class="kw-green">10 سنوات</span> تنخفض النسبة بشكل ملحوظ، مما يجعل <span class="kw-amber">الـ Onboarding والسنوات الأولى</span> أولوية قصوى.'),
    "11": ("warning", 'الأعزب/العزباء يغادرون بنسب صادمة: <span class="kw-red">72.2%</span> للإناث و<span class="kw-red">62.3%</span> للذكور. <span class="kw-green">المتزوجون</span> هم الأكثر استقراراً بفارق كبير بسبب <span class="kw-blue">الالتزامات الأسرية</span>.'),
    "12": ("insight", 'الـ <span class="kw-green">Remote Work</span> يخفض الـ Attrition بأكثر من <span class="kw-green">28 نقطة</span> في جميع أحجام الشركات! من <span class="kw-red">~53% On-site</span> إلى <span class="kw-green">~24% Remote</span> — هذا <span class="kw-amber">أقوى قرار</span> يمكن اتخاذه للاحتفاظ بالموظفين.'),
    "13": ("warning", 'الأخطر هو الموظف <span class="kw-red">High Performance + Low Satisfaction</span> — شاطر لكن غير راضٍ، وسيجد فرصة أخرى بسرعة. يجب <span class="kw-amber">تحديد هؤلاء والتحدث معهم</span> قبل مغادرتهم.'),
    "14": ("insight", 'كل ما زادت المسافة، زادت نسبة المغادرة من <span class="kw-green">41.7%</span> للأقرب إلى <span class="kw-red">52.9%</span> للأبعد. توفير خيار <span class="kw-green">Hybrid/Remote</span> للموظفين البعيدين سيقلل هذا الأثر بشكل كبير.'),
    "15": ("warning", '<span class="kw-red">95%</span> من الموظفين ليس لديهم أي <span class="kw-red">فرصة قيادية</span>! هذا يعني غياب <span class="kw-amber">مسار التطوير الوظيفي</span> لغالبية الموظفين، وهو من أهم أسباب الشعور بالركود والرغبة في المغادرة.'),
    "16": ("warning", '<span class="kw-red">83%</span> من الموظفين محرومون من <span class="kw-red">فرص الابتكار</span>. الموظف الذي يكرر نفس المهام يومياً بدون تحدٍّ <span class="kw-amber">سيبحث عن بيئة أكثر إثارة وتحفيزاً</span>.'),
    "17": ("insight", 'السمعة الضعيفة <span class="kw-red">(Poor)</span> ترفع نسبة المغادرة إلى <span class="kw-red">56%</span> مقارنة بـ <span class="kw-green">43%</span> للسمعة الجيدة — فارق <span class="kw-amber">13 نقطة</span>. الموظف يريد أن <span class="kw-blue">يفتخر بمكان عمله</span> أمام الآخرين.'),
    "18": ("insight", 'الفارق بين أعلى وأدنى مستوى من التقدير <span class="kw-amber">1.8% فقط</span>! مما يؤكد أن <span class="kw-red">التقدير اللفظي بدون مكافآت ملموسة</span> أو ترقيات <span class="kw-red">لا أثر له</span> على قرار البقاء.'),
    "19": ("warning", 'الأخطر في الداتا كلها: <span class="kw-red">Entry Level بدون Remote = 69.3%</span> مغادرة! بينما <span class="kw-green">Senior مع Remote = 5.2% فقط</span>. تركيز جهود الـ Remote على <span class="kw-amber">الـ Entry Level هو أولوية الأولويات</span>.'),
}

CHARTS = {
    "1":("Attrition Overview",chart1), "2":("Attrition by Gender",chart2),
    "3":("Attrition by Age Group",chart3), "4":("Attrition by Job Role",chart4),
    "5":("Monthly Income",chart5), "6":("Work-Life Balance",chart6),
    "7":("Overtime Impact",chart7), "8":("Education Level",chart8),
    "9":("Correlation Heatmap",chart9), "10":("Attrition by Tenure",chart10),
    "11":("Marital Status × Gender",chart11), "12":("Company Size × Remote Work",chart12),
    "13":("Performance × Satisfaction",chart13), "14":("Commute Distance",chart14),
    "15":("Leadership Opportunities",chart15), "16":("Innovation Opportunities",chart16),
    "17":("Company Reputation",chart17), "18":("Employee Recognition",chart18),
    "19":("Job Level × Remote Work",chart19),
}

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📊 Employee Attrition Dashboard")
    st.markdown("---")
    uploaded = st.file_uploader("📂 Upload dataset (optional)", type=["xlsx","csv"])
    st.info("✅ Default data loads automatically\n\n74,498 employees · 24 variables")
    st.markdown("---")
    show_all = st.checkbox("Show all charts", value=True)
    chart_options = [f"Chart {k} — {v[0]}" for k,v in CHARTS.items()]
    selected_labels = st.multiselect("Or pick specific charts:", chart_options, disabled=show_all)
    st.markdown("---")
    st.caption("📊 19 Interactive Charts\n🔍 Deep HR Analytics\n💡 Actionable Insights")

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="dash-header">
  <div>
    <div class="dash-week-tag">Week #1 Task</div>
    <h1 class="dash-title">📊 Employee Attrition Dashboard</h1>
    <p class="dash-subtitle">تحليل معمّق لأسباب مغادرة الموظفين · 19 Visualization · 74,498 Employee</p>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Load data & KPIs ──────────────────────────────────────────────────────────
df = load_data(uploaded) if uploaded is not None else load_data()

if df is None:
    st.error("❌ Dataset not found — make sure final_dataset.csv is in the repo root")
    st.stop()

total = len(df)
left  = (df["Attrition"]=="Left").sum()
rate  = left/total*100

st.markdown(f"""
<div class="kpi-grid">
  <div class="kpi-card blue">
    <div class="kpi-label">Total Employees</div>
    <div class="kpi-value blue">{total:,}</div>
    <div class="kpi-sub">Full Dataset</div>
  </div>
  <div class="kpi-card red">
    <div class="kpi-label">Employees Left</div>
    <div class="kpi-value red">{left:,}</div>
    <div class="kpi-sub">Attrition Count</div>
  </div>
  <div class="kpi-card amber">
    <div class="kpi-label">Attrition Rate</div>
    <div class="kpi-value amber">{rate:.1f}%</div>
    <div class="kpi-sub">Global avg: 10–15%</div>
  </div>
</div>
<div class="section-divider"></div>
""", unsafe_allow_html=True)

# ── Render charts ─────────────────────────────────────────────────────────────
keys_to_show = list(CHARTS.keys()) if show_all else \
    [lbl.split(" — ")[0].replace("Chart ","") for lbl in selected_labels]

if not keys_to_show:
    st.info("👈 Select at least one chart from the sidebar")
else:
    for k in keys_to_show:
        name, fn = CHARTS[k]
        itype, itext = INSIGHTS[k]
        box_cls   = "insight-box"  if itype=="insight" else "warning-box"
        title_cls = "insight-title" if itype=="insight" else "warning-title"
        p_cls     = "insight-text"  if itype=="insight" else "warning-text"
        icon      = "💡 KEY INSIGHT" if itype=="insight" else "⚠️ CRITICAL FINDING"

        st.markdown(f"""
        <div class="chart-section">
          <span class="chart-number">CHART {k} / 19</span>
          <h3 class="chart-name">{name}</h3>
        """, unsafe_allow_html=True)

        fn(df)

        st.markdown(f"""
          <div class="{box_cls}">
            <div class="{title_cls}">{icon}</div>
            <p class="{p_cls}" dir="auto" style="text-align:right;unicode-bidi:plaintext;">{itext}</p>
          </div>
        </div>
        """, unsafe_allow_html=True)
