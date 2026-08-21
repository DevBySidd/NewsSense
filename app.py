import streamlit as st
import pandas as pd
import plotly.express as px
import time

from Sentiment import analyze_sentiment
import database


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="NewsSense",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

database.create_table()


# ============================================================
# PREMIUM ANIMATED CSS
# ============================================================

st.html("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
);


/* ==========================================================
   GLOBAL
========================================================== */

* {
    font-family: 'Inter', sans-serif;
}

.stApp {

    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(99,102,241,0.11),
            transparent 25%
        ),
        radial-gradient(
            circle at 90% 15%,
            rgba(168,85,247,0.10),
            transparent 25%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(59,130,246,0.07),
            transparent 30%
        ),
        #f7f8fc;

    overflow-x: hidden;
}


/* ==========================================================
   REMOVE STREAMLIT DEFAULT
========================================================== */

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.block-container {
    max-width: 1450px;
    padding-top: 35px;
    padding-bottom: 60px;
}


/* ==========================================================
   SIDEBAR
========================================================== */

section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            rgba(255,255,255,0.98),
            rgba(248,247,255,0.98)
        );

    border-right: 1px solid #e7e8ef;
}


/* ==========================================================
   BRAND
========================================================== */

.brand {

    padding: 10px 5px 30px 5px;

    animation:
        slideDown 0.8s ease;
}

.brand-row {

    display: flex;
    align-items: center;

    gap: 12px;
}

.logo {

    width: 46px;
    height: 46px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 14px;

    font-size: 22px;

    background:
        linear-gradient(
            135deg,
            #6366f1,
            #8b5cf6,
            #a855f7
        );

    background-size: 200% 200%;

    box-shadow:
        0 10px 25px rgba(99,102,241,.25);

    animation:
        gradientMove 4s ease infinite,
        logoFloat 3s ease-in-out infinite;
}

.brand-name {

    font-size: 22px;

    font-weight: 800;

    color: #111827;
}

.brand-name span {

    background:
        linear-gradient(
            90deg,
            #6366f1,
            #8b5cf6
        );

    -webkit-background-clip: text;

    color: transparent;
}

.brand-sub {

    font-size: 9px;

    color: #9ca3af;

    letter-spacing: 1.3px;

    margin-top: 3px;
}


/* ==========================================================
   HERO
========================================================== */

.hero {

    position: relative;

    overflow: hidden;

    padding: 55px 55px;

    min-height: 350px;

    border-radius: 30px;

    border: 1px solid rgba(99,102,241,.14);

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,.96),
            rgba(245,243,255,.96)
        );

    box-shadow:
        0 25px 70px rgba(79,70,229,.09);

    animation:
        fadeUp .8s ease;
}


/* floating blobs */

.blob {

    position: absolute;

    border-radius: 50%;

    filter: blur(2px);

    pointer-events: none;
}

.blob-one {

    width: 300px;
    height: 300px;

    right: -100px;
    top: -140px;

    background:
        radial-gradient(
            circle,
            rgba(99,102,241,.23),
            rgba(139,92,246,.03)
        );

    animation:
        blobFloat 8s ease-in-out infinite;
}

.blob-two {

    width: 180px;
    height: 180px;

    right: 240px;
    bottom: -110px;

    background:
        radial-gradient(
            circle,
            rgba(59,130,246,.13),
            transparent
        );

    animation:
        blobFloatReverse 10s ease-in-out infinite;
}

.blob-three {

    width: 90px;
    height: 90px;

    left: 40%;
    top: 20px;

    background:
        rgba(168,85,247,.08);

    animation:
        blobFloat 6s ease-in-out infinite;
}


/* hero content */

.hero-content {

    position: relative;

    z-index: 5;
}

.badge {

    display: inline-flex;

    align-items: center;

    gap: 8px;

    padding: 8px 14px;

    border-radius: 50px;

    background: #efedff;

    color: #5b5bd6;

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 1.2px;

    animation:
        fadeUp 1s ease;
}

.badge-dot {

    width: 7px;
    height: 7px;

    border-radius: 50%;

    background: #6366f1;

    box-shadow:
        0 0 0 5px rgba(99,102,241,.12);

    animation:
        pulse 2s infinite;
}

.hero-title {

    margin-top: 22px;

    font-size: 50px;

    line-height: 1.08;

    letter-spacing: -2px;

    font-weight: 800;

    color: #111827;

    max-width: 780px;

    animation:
        fadeUp 1.1s ease;
}

.gradient-text {

    background:
        linear-gradient(
            90deg,
            #6366f1,
            #8b5cf6,
            #a855f7,
            #6366f1
        );

    background-size: 300% auto;

    -webkit-background-clip: text;

    color: transparent;

    animation:
        gradientText 5s linear infinite;
}

.hero-description {

    max-width: 690px;

    margin-top: 18px;

    color: #6b7280;

    font-size: 14px;

    line-height: 1.8;

    animation:
        fadeUp 1.3s ease;
}

.hero-button {

    display: inline-block;

    margin-top: 25px;

    padding: 11px 17px;

    border-radius: 12px;

    color: white;

    font-size: 12px;

    font-weight: 700;

    background:
        linear-gradient(
            135deg,
            #6366f1,
            #7c3aed
        );

    box-shadow:
        0 10px 25px rgba(99,102,241,.23);

    animation:
        fadeUp 1.5s ease,
        buttonGlow 3s ease-in-out infinite;
}


/* ==========================================================
   SECTION
========================================================== */

.section-title {

    margin-top: 34px;

    font-size: 20px;

    font-weight: 800;

    color: #111827;

    animation:
        fadeUp .6s ease;
}

.section-sub {

    color: #9ca3af;

    font-size: 12px;

    margin-top: 4px;

    margin-bottom: 18px;
}


/* ==========================================================
   STAT CARDS
========================================================== */

.stat-card {

    position: relative;

    overflow: hidden;

    min-height: 145px;

    padding: 22px;

    border-radius: 20px;

    background:
        rgba(255,255,255,.92);

    border: 1px solid #e7e8ef;

    box-shadow:
        0 10px 30px rgba(15,23,42,.045);

    transition:
        transform .35s cubic-bezier(.2,.8,.2,1),
        box-shadow .35s ease;

    animation:
        cardAppear .7s ease both;
}

.stat-card:hover {

    transform:
        translateY(-8px)
        scale(1.015);

    box-shadow:
        0 22px 45px rgba(15,23,42,.10);
}

.stat-glow {

    position: absolute;

    width: 120px;
    height: 120px;

    right: -50px;
    bottom: -50px;

    border-radius: 50%;

    background:
        rgba(99,102,241,.07);

    transition:
        transform .4s ease;
}

.stat-card:hover .stat-glow {

    transform:
        scale(1.6);
}

.stat-icon {

    width: 42px;
    height: 42px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 12px;

    background:
        linear-gradient(
            135deg,
            #efedff,
            #f7f3ff
        );

    font-size: 18px;
}

.stat-label {

    margin-top: 13px;

    color: #9ca3af;

    font-size: 11px;

    font-weight: 600;
}

.stat-number {

    margin-top: 2px;

    font-size: 29px;

    font-weight: 800;

    color: #111827;
}


/* ==========================================================
   ANALYZER CARD
========================================================== */

.analyzer {

    padding: 30px;

    border-radius: 24px;

    background:
        rgba(255,255,255,.95);

    border: 1px solid #e6e7ef;

    box-shadow:
        0 18px 45px rgba(15,23,42,.055);

    animation:
        fadeUp .7s ease;
}

.analyzer-top {

    display: flex;

    align-items: center;

    gap: 12px;

    margin-bottom: 20px;
}

.analyzer-icon {

    width: 43px;
    height: 43px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 13px;

    background:
        linear-gradient(
            135deg,
            #6366f1,
            #8b5cf6
        );

    color: white;

    box-shadow:
        0 8px 20px rgba(99,102,241,.22);

    animation:
        logoFloat 3s ease-in-out infinite;
}

.analyzer-title {

    font-size: 18px;

    font-weight: 800;

    color: #111827;
}

.analyzer-sub {

    font-size: 11px;

    color: #9ca3af;

    margin-top: 3px;
}


/* ==========================================================
   RESULT
========================================================== */

.result {

    position: relative;

    overflow: hidden;

    margin-top: 25px;

    padding: 32px;

    border-radius: 24px;

    background:
        linear-gradient(
            135deg,
            #ffffff,
            #f6f4ff
        );

    border: 1px solid #e5e1ff;

    box-shadow:
        0 18px 45px rgba(99,102,241,.08);

    animation:
        resultReveal .8s cubic-bezier(.2,.8,.2,1);
}

.result::before {

    content: "";

    position: absolute;

    width: 240px;
    height: 240px;

    right: -90px;
    top: -100px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(99,102,241,.14),
            transparent 70%
        );

    animation:
        blobFloat 7s infinite;
}

.result-icon {

    position: relative;

    font-size: 52px;

    animation:
        emojiPop .7s cubic-bezier(.2,1.5,.4,1);
}

.result-label {

    position: relative;

    margin-top: 8px;

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 1.5px;

    color: #9ca3af;
}

.result-sentiment {

    position: relative;

    margin-top: 5px;

    font-size: 35px;

    font-weight: 800;

    color: #111827;

    animation:
        fadeUp .6s ease;
}

.result-description {

    position: relative;

    margin-top: 5px;

    font-size: 13px;

    color: #6b7280;
}


/* ==========================================================
   SCORE BOX
========================================================== */

.score {

    padding: 20px;

    border-radius: 17px;

    background: white;

    border: 1px solid #e7e8ef;

    transition: .3s ease;

    animation:
        cardAppear .7s ease both;
}

.score:hover {

    transform:
        translateY(-5px);

    box-shadow:
        0 14px 30px rgba(15,23,42,.07);
}

.score-label {

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 1px;

    color: #9ca3af;
}

.score-value {

    margin-top: 7px;

    font-size: 25px;

    font-weight: 800;

    color: #111827;
}


/* ==========================================================
   LOADER
========================================================== */

.loader {

    display: flex;

    flex-direction: column;

    align-items: center;

    justify-content: center;

    padding: 40px;

    border-radius: 22px;

    background: white;

    border: 1px solid #e8e9ef;

    animation:
        fadeUp .5s ease;
}

.loader-ring {

    width: 55px;
    height: 55px;

    border-radius: 50%;

    border: 4px solid #e9e7ff;

    border-top-color: #6366f1;

    animation:
        spin 1s linear infinite;
}

.loader-text {

    margin-top: 18px;

    color: #6366f1;

    font-size: 13px;

    font-weight: 700;

    animation:
        blink 1.5s infinite;
}


/* ==========================================================
   FOOTER
========================================================== */

.footer {

    margin-top: 60px;

    padding-top: 22px;

    border-top: 1px solid #e5e7eb;

    text-align: center;

    color: #9ca3af;

    font-size: 11px;
}


/* ==========================================================
   BUTTON
========================================================== */

.stButton > button {

    min-height: 47px;

    border: none !important;

    border-radius: 12px !important;

    background:
        linear-gradient(
            135deg,
            #6366f1,
            #7c3aed
        ) !important;

    color: white !important;

    font-weight: 700 !important;

    box-shadow:
        0 9px 22px rgba(99,102,241,.22);

    transition:
        transform .25s ease,
        box-shadow .25s ease;
}

.stButton > button:hover {

    transform:
        translateY(-3px);

    box-shadow:
        0 15px 30px rgba(99,102,241,.30);
}


/* ==========================================================
   ANIMATIONS
========================================================== */

@keyframes fadeUp {

    from {
        opacity: 0;
        transform: translateY(25px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideDown {

    from {
        opacity: 0;
        transform: translateY(-20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes cardAppear {

    from {
        opacity: 0;
        transform: translateY(20px) scale(.97);
    }

    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

@keyframes resultReveal {

    from {
        opacity: 0;
        transform: translateY(25px) scale(.96);
    }

    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

@keyframes emojiPop {

    0% {
        transform: scale(.3);
        opacity: 0;
    }

    70% {
        transform: scale(1.2);
    }

    100% {
        transform: scale(1);
        opacity: 1;
    }
}

@keyframes pulse {

    0%,100% {
        transform: scale(1);
        opacity: 1;
    }

    50% {
        transform: scale(1.25);
        opacity: .65;
    }
}

@keyframes spin {

    to {
        transform: rotate(360deg);
    }
}

@keyframes blink {

    0%,100% {
        opacity: .45;
    }

    50% {
        opacity: 1;
    }
}

@keyframes logoFloat {

    0%,100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-5px);
    }
}

@keyframes blobFloat {

    0%,100% {
        transform: translate(0,0);
    }

    50% {
        transform: translate(-20px,20px);
    }
}

@keyframes blobFloatReverse {

    0%,100% {
        transform: translate(0,0);
    }

    50% {
        transform: translate(20px,-15px);
    }
}

@keyframes gradientMove {

    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}

@keyframes gradientText {

    0% {
        background-position: 0% center;
    }

    100% {
        background-position: 300% center;
    }
}

@keyframes buttonGlow {

    0%,100% {
        box-shadow:
            0 10px 25px rgba(99,102,241,.20);
    }

    50% {
        box-shadow:
            0 14px 35px rgba(99,102,241,.34);
    }
}

</style>
""")


# ============================================================
# HELPERS
# ============================================================

def load_data():

    records = database.get_all_news()

    if not records:
        return pd.DataFrame(
            columns=[
                "ID",
                "Headline",
                "Article",
                "Sentiment",
                "Polarity",
                "Subjectivity",
                "Created At"
            ]
        )

    return pd.DataFrame(
        records,
        columns=[
            "ID",
            "Headline",
            "Article",
            "Sentiment",
            "Polarity",
            "Subjectivity",
            "Created At"
        ]
    )


def get_icon(sentiment):

    if sentiment == "Positive":
        return "😊"

    if sentiment == "Negative":
        return "😞"

    return "😐"


def get_description(sentiment):

    if sentiment == "Positive":
        return "The story expresses a positive emotional tone."

    if sentiment == "Negative":
        return "The story expresses a negative emotional tone."

    return "The story appears emotionally neutral."


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html("""
    <div class="brand">

        <div class="brand-row">

            <div class="logo">
                📰
            </div>

            <div>

                <div class="brand-name">
                    News<span>Sense</span>
                </div>

                <div class="brand-sub">
                    NEWS SENTIMENT INTELLIGENCE
                </div>

            </div>

        </div>

    </div>
    """)


    page = st.radio(
        "WORKSPACE",
        [
            "🏠 Dashboard",
            "🔎 Analyze News",
            "📚 News History"
        ]
    )


    st.divider()


    st.html("""
    <div style="
        padding:5px;
        color:#9ca3af;
        font-size:11px;
        line-height:2;
    ">

        <b style="
            letter-spacing:1px;
            color:#6b7280;
        ">
            TECHNOLOGY
        </b>

        <br>

        Python<br>
        TextBlob NLP<br>
        Pandas<br>
        SQLite<br>
        Plotly<br>
        Streamlit

    </div>
    """)


    st.divider()

    st.caption("NewsSense • v1.0")


# ============================================================
# LOAD DATA
# ============================================================

df = load_data()


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.html("""
    <div class="hero">

        <div class="blob blob-one"></div>
        <div class="blob blob-two"></div>
        <div class="blob blob-three"></div>

        <div class="hero-content">

            <div class="badge">

                <span class="badge-dot"></span>

                NEWS INTELLIGENCE PLATFORM

            </div>

            <div class="hero-title">

                Understand the
                <span class="gradient-text">
                    emotion
                </span>

                <br>

                behind every story.

            </div>

            <div class="hero-description">

                NewsSense analyzes news content using
                Natural Language Processing to identify
                sentiment, measure polarity and
                uncover emotional patterns.

            </div>

            <div class="hero-button">

                ✦ Intelligent Sentiment Analysis

            </div>

        </div>

    </div>
    """)


    total = len(df)

    positive = len(
        df[df["Sentiment"] == "Positive"]
    )

    negative = len(
        df[df["Sentiment"] == "Negative"]
    )

    neutral = len(
        df[df["Sentiment"] == "Neutral"]
    )


    st.html("""
    <div class="section-title">
        Overview
    </div>

    <div class="section-sub">
        Real-time summary of your analyzed news
    </div>
    """)


    columns = st.columns(4)


    cards = [
        ("📰", "Total Articles", total),
        ("😊", "Positive", positive),
        ("😞", "Negative", negative),
        ("😐", "Neutral", neutral)
    ]


    for i, (icon, label, value) in enumerate(cards):

        with columns[i]:

            st.html(
                f"""
                <div class="stat-card">

                    <div class="stat-glow"></div>

                    <div class="stat-icon">
                        {icon}
                    </div>

                    <div class="stat-label">
                        {label}
                    </div>

                    <div class="stat-number">
                        {value}
                    </div>

                </div>
                """
            )


    if df.empty:

        st.html("""
        <div style="
            margin-top:35px;
            padding:65px 30px;
            text-align:center;
            background:white;
            border:1px solid #e7e8ef;
            border-radius:24px;
            animation:fadeUp .7s ease;
        ">

            <div style="
                font-size:48px;
                animation:logoFloat 3s infinite;
            ">
                📰
            </div>

            <div style="
                margin-top:14px;
                font-size:21px;
                font-weight:800;
                color:#111827;
            ">
                Your dashboard is ready
            </div>

            <div style="
                margin-top:8px;
                font-size:13px;
                color:#9ca3af;
            ">
                Analyze your first article to unlock
                your sentiment analytics.
            </div>

        </div>
        """)

    else:

        st.html("""
        <div class="section-title">
            Sentiment Analytics
        </div>

        <div class="section-sub">
            Explore the emotional distribution of your news
        </div>
        """)


        col1, col2 = st.columns(2)


        with col1:

            counts = (
                df["Sentiment"]
                .value_counts()
                .reset_index()
            )

            counts.columns = [
                "Sentiment",
                "Count"
            ]


            fig = px.pie(
                counts,
                names="Sentiment",
                values="Count",
                hole=.70
            )


            fig.update_layout(
                title="Sentiment Distribution",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                margin=dict(
                    l=10,
                    r=10,
                    t=50,
                    b=10
                ),
                legend=dict(
                    orientation="h",
                    y=-0.08
                )
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


        with col2:

            fig = px.histogram(
                df,
                x="Polarity",
                nbins=12
            )


            fig.update_layout(
                title="Polarity Distribution",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                margin=dict(
                    l=10,
                    r=10,
                    t=50,
                    b=10
                )
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


# ============================================================
# ANALYZE NEWS
# ============================================================

elif page == "🔎 Analyze News":

    st.html("""
    <div class="hero">

        <div class="blob blob-one"></div>
        <div class="blob blob-three"></div>

        <div class="hero-content">

            <div class="badge">

                <span class="badge-dot"></span>

                SENTIMENT ENGINE

            </div>

            <div class="hero-title">

                Analyze a
                <span class="gradient-text">
                    news story.
                </span>

            </div>

            <div class="hero-description">

                Give NewsSense a headline and article.
                Our NLP engine will identify the emotional
                tone of the story.

            </div>

        </div>

    </div>
    """)


    st.html("""
    <div class="section-title">
        Analyze Content
    </div>

    <div class="section-sub">
        Enter the story you want NewsSense to understand
    </div>
    """)


    st.html("""
    <div class="analyzer">

        <div class="analyzer-top">

            <div class="analyzer-icon">
                ✦
            </div>

            <div>

                <div class="analyzer-title">
                    Sentiment Analysis
                </div>

                <div class="analyzer-sub">
                    Powered by TextBlob Natural Language Processing
                </div>

            </div>

        </div>

    """)


    headline = st.text_input(
        "Headline",
        placeholder="Example: India wins a historic cricket match"
    )


    article = st.text_area(
        "Article",
        placeholder="Paste the complete news article here...",
        height=240
    )


    analyze = st.button(
        "✦  Analyze Story",
        use_container_width=True
    )


    st.html("</div>")


    # --------------------------------------------------------
    # ANALYZE
    # --------------------------------------------------------

    if analyze:

        if not headline.strip() and not article.strip():

            st.warning(
                "Please enter a headline or article first."
            )

        else:

            if headline.strip() and article.strip():

                text = (
                    headline.strip()
                    + ". "
                    + article.strip()
                )

            elif headline.strip():

                text = headline.strip()

            else:

                text = article.strip()


            # Animated loading

            loader = st.empty()


            loader.html("""
            <div class="loader">

                <div class="loader-ring"></div>

                <div class="loader-text">
                    Analyzing emotional patterns...
                </div>

            </div>
            """)


            time.sleep(.8)


            result = analyze_sentiment(text)


            loader.empty()


            sentiment = result["sentiment"]

            polarity = float(
                result["polarity"]
            )

            subjectivity = float(
                result["subjectivity"]
            )


            # Save database

            database.save_news(
                headline.strip()
                if headline.strip()
                else "No headline",

                article.strip()
                if article.strip()
                else text,

                sentiment,
                polarity,
                subjectivity
            )


            # ------------------------------------------------
            # RESULT
            # ------------------------------------------------

            icon = get_icon(sentiment)

            description = get_description(
                sentiment
            )


            st.html(
                f"""
                <div class="section-title">
                    Analysis Complete
                </div>

                <div class="result">

                    <div class="result-icon">
                        {icon}
                    </div>

                    <div class="result-label">
                        DETECTED SENTIMENT
                    </div>

                    <div class="result-sentiment">
                        {sentiment}
                    </div>

                    <div class="result-description">
                        {description}
                    </div>

                </div>
                """
            )


            st.write("")


            c1, c2, c3 = st.columns(3)


            with c1:

                st.html(
                    f"""
                    <div class="score">

                        <div class="score-label">
                            SENTIMENT
                        </div>

                        <div class="score-value">
                            {sentiment}
                        </div>

                    </div>
                    """
                )


            with c2:

                st.html(
                    f"""
                    <div class="score">

                        <div class="score-label">
                            POLARITY
                        </div>

                        <div class="score-value">
                            {polarity:+.2f}
                        </div>

                    </div>
                    """
                )


            with c3:

                st.html(
                    f"""
                    <div class="score">

                        <div class="score-label">
                            SUBJECTIVITY
                        </div>

                        <div class="score-value">
                            {subjectivity:.2f}
                        </div>

                    </div>
                    """
                )


            # ------------------------------------------------
            # POLARITY
            # ------------------------------------------------

            st.html("""
            <div class="section-title">
                Emotional Score
            </div>

            <div class="section-sub">
                Where this story sits between negative and positive
            </div>
            """)


            progress = (
                polarity + 1
            ) / 2


            progress = max(
                0,
                min(1, progress)
            )


            st.progress(progress)


            st.caption(
                "−1.0  Negative     •     0.0  Neutral     •     +1.0  Positive"
            )


            st.html("""
            <div class="section-title">
                What does this mean?
            </div>
            """)


            if polarity > 0.05:

                st.success(
                    f"The article has a positive tone with a polarity score of {polarity:.2f}."
                )

            elif polarity < -0.05:

                st.error(
                    f"The article has a negative tone with a polarity score of {polarity:.2f}."
                )

            else:

                st.info(
                    f"The article has a neutral tone with a polarity score of {polarity:.2f}."
                )


# ============================================================
# HISTORY
# ============================================================

elif page == "📚 News History":

    st.html("""
    <div class="hero">

        <div class="blob blob-two"></div>

        <div class="hero-content">

            <div class="badge">

                <span class="badge-dot"></span>

                NEWS ARCHIVE

            </div>

            <div class="hero-title">

                Your
                <span class="gradient-text">
                    intelligence
                </span>

                history.

            </div>

            <div class="hero-description">

                Explore every story previously analyzed
                by NewsSense.

            </div>

        </div>

    </div>
    """)


    df = load_data()


    if df.empty:

        st.info(
            "No news has been analyzed yet."
        )

    else:

        st.html("""
        <div class="section-title">
            Search History
        </div>
        """)


        col1, col2 = st.columns([2, 1])


        with col1:

            search = st.text_input(
                "Search",
                placeholder="Search by headline..."
            )


        with col2:

            filter_sentiment = st.selectbox(
                "Filter",
                [
                    "All",
                    "Positive",
                    "Negative",
                    "Neutral"
                ]
            )


        filtered = df.copy()


        if search:

            filtered = filtered[
                filtered["Headline"]
                .astype(str)
                .str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]


        if filter_sentiment != "All":

            filtered = filtered[
                filtered["Sentiment"]
                == filter_sentiment
            ]


        st.caption(
            f"{len(filtered)} article(s)"
        )


        st.dataframe(
            filtered[
                [
                    "ID",
                    "Headline",
                    "Sentiment",
                    "Polarity",
                    "Subjectivity",
                    "Created At"
                ]
            ],
            use_container_width=True,
            hide_index=True
        )


        st.write("")


        with st.expander(
            "⚙️ Database Management"
        ):

            st.warning(
                "This will permanently remove all analyzed news."
            )


            if st.button(
                "Delete All History"
            ):

                database.delete_all_news()

                st.success(
                    "History deleted successfully."
                )

                st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="footer">

    <b style="color:#6366f1;">
        NewsSense
    </b>

    &nbsp;•&nbsp;

    News Sentiment Intelligence

    <br><br>

    Built with Python · TextBlob · Pandas · SQLite · Plotly · Streamlit

</div>
""")