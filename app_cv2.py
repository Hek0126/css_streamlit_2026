# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 14:45:26 2026

@author: hekes
"""



import streamlit as st

# Page configuration
st.set_page_config(
    page_title="CV of Buhlebenkosi Heketshe",
    page_icon="📄",
    layout="wide"
)

# ======================
# SIDEBAR
# ======================
st.sidebar.title("📄 Curriculum Vitae")
#st.sidebar.subheader("Buhlebenkosi Heketshe")

st.sidebar.write("📍 Achievers Way, Bellville, Cape Town, 7530")
st.sidebar.write("📧 221688366@mycput.ac.za")
st.sidebar.write("🔗 linkedin.com/in/buhlebenkosi-heketshe-7b781b231")
st.sidebar.write("💻 github.com/Hek0126")
st.sidebar.write("📞 +27 63 569 8897")

st.sidebar.markdown("---")
st.sidebar.write("""**Key Skills** 
                 - Data Analysis, Science & Engineering
                 - Python
                 - R
                 - SAS
                 - SQL
                 - Streamlit
                 - GitBash""")

st.sidebar.markdown("---")
st.sidebar.subheader("🌍 Languages")
st.sidebar.write("- IsiZulu (Native)")
st.sidebar.write("- IsiXhosa (Native)")
st.sidebar.write("- English (Fluent)")
st.sidebar.write("- Setswana (Fluent)")


# ======================
# MAIN CONTENT
# ======================
st.title("Buhlebenkosi Heketshe")
st.subheader("Mathematical Sciences Honours Student")

st.markdown("""
**Profile Summary**

Mathematical Sciences graduate with a strong interest in mathematical modelling, statistical analysis, data 
science, and machine learning. Possesses strong analytical, mathematical, and critical-thinking abilities, 
with an enthusiasm for investigating complex problems and applying quantitative methods to real-world contexts. 
Committed to developing rigorous research and analytical skills and further exploring the application of 
mathematical and statistical methods through Master's-level study.


""")

# ======================
# EDUCATION
# ======================
st.header("🎓 Education")

st.markdown("""
**Postgraduate Diploma in Mathematical Sciences | 
  Cape Peninsula University of Technology**  
*Year: 2026 - Present*  

**Relevant Modules**
- Advanced Programming for Data Science  
- Bayesian Statistics  
- Convex Optimisation  
- Computational Methods  
- Data Engineering & Visualisation  
- Machine Leraning 5A  
- Machine Leraning 5B
- Mathematical Modelling
- Research Project  
""")

st.markdown("""
**Advanced Diploma in Mathematical Sciences | 
  Cape Peninsula University of Technology**  
*Year: 2025 - 2025*  

**Relevant Modules**
- Principles of Mathematical Analysis  
- Biomathematics 4
- Biostatistics 4
- Non Linear & Partial Diff Equations
- Machine Learning & Data Science 4
- Matrix Theory & Linear Algebra
- Mathematical Sciences Project 4
- Mathematical Statistics
- Numerical Methods 4
- Programming & Database Development  
""")

st.markdown("""
**Diploma in Mathematical Sciences | 
Cape Peninsula University of Technology**  
*Year: 2021 - 2024*  

**Relevant Modules**
- Mathematics  
- Statistics  
- Biomathematics  
- Bioscience  
- Programming  
- Numerical Methods 
- Introduction to Projects
- Mathematical Sciences Project
- Operations Research
- Programming for Statistics  
""")

st.markdown("""
**National Senior Certificate (NSC) | 
Far North Secondary School**  
*Completed: 2020*
""")

# ======================
# TECHNICAL SKILLS
# ======================
st.header("🛠 Skills")

col1, col2 = st.columns(2)

with col1:
    st.write("""
    **Techical skills**
    - Programming
    - Machine Learning
    - Data Pipelines
    - Data Wrangling & Cleaning
    - Data Visualisation & Reporting
    - Power BI
    - Matlab

    **Tools**: Python, R, SAS, SQL, PowerBI, Matlab, Streamlit, GitBash""")

with col2:
    st.write("""
    **Soft Skills**
    - Communication & Data Storytelling
    - Intellectual Curiosity
    - Problem Solving & Critical Thinking
    - Cross-Functional Collaboration
    - Attention to Detail
    - Time Management
    """)

# ======================
# EXPERIENCE
# ======================
st.header("💼 Experience")

with st.expander("Risk Intern | RCS Group (2026 - Present)"):
    st.write("""
    - Apply statistical and quantitative methods to credit-risk analysis
    - Use SAS and Python for data analysis and risk monitoring
    """)

with st.expander("Peer Mentor | Cape Peninsula University of Technology (2023 - 2025)"):
    st.write("""
    - Provided socio-academic support to students in need  
    - Connected students to relevant professional services 
    """)

# ======================
# RESEARCH & PROJECTS
# ======================
st.header("🔬 Research & Projects")

with st.expander("Data Quality Governance & Risk Monitoring | RCS / CPUT (2026 - Present)"):
    st.write("""
    - Developing timeliness controls and early-warning alerts for data quality governance
    - Applying data analysis and risk-monitoring techniques to a real-world industry problem
    """)

with st.expander("Student Debt Analysis | CPUT Finance Department (2025)"):
    st.write("""
    - Analysed student debt in relation to academic and graduation factors
    - Developed a Power BI dashboard to visualise findings
    """)

with st.expander("QSAR Analysis | CPUT / UWC Bioinformatics (2024)"):
    st.write("""
    - Conducted QSAR analysis of the PI3K protein using Python
    - Investigated protein associations with colorectal cancer
    """)

with st.expander("Diabetes Risk Prediction | CPUT Maths & Physics (2024)"):
    st.write("""
    - Predicted diabetes risk using machine learning models
    - Analysed patient health parameters using R
    """)
    
# ======================
# CERTIFICATIONS
# ======================
st.header("📜 Certifications")

st.markdown("""
- **Coding Summer School** – CHPC & NITheCS (2026)  
- Python for Beginners - Alison (2026) 
- Power BI: Dashboards for Beginners (2025)
- SAS - Specialization in Undergraduate Applied Statistics (2025) 
  """)

# ======================
# HOBBIES & INTERESTS
# ======================
# st.header("⚽ Hobbies & Interests")

# st.write("""
# - Reading  
# - Writing  
# - Athletics    
# """)

st.markdown("---")
st.write("© 2026 Buhlebenkosi Heketshe")
