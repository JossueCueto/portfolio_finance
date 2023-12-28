import streamlit as st
import requests
from io import BytesIO

def run_perfil_profesional():
  
  st.header('Resumen Profesional')
  st.write('Bachiller en Ciencias Administrativas con dominio intermedio de inglés y sólidas habilidades analíticas y comunicativas. Seleccionado para el exclusivo programa Go to Market, destacando en gestión de portafolios y análisis de mercado de capitales. Proficiente en herramientas de ofimática avanzadas, con un enfoque práctico en la mejora de procesos. Comprometido con la excelencia, me preparo para obtener la certificación CFA y destacar en el CEFA en 2024.')
  
  st.header('Educación y Formación Académica')
  st.subheader('Ciencias Administrativas - UNJBG (2018-2022)')
  st.write('Bachiller en Ciencias Administrativas con distinción, alcanzando el segundo lugar entre 78 estudiantes.')
  st.markdown(""" **Cursos relevantes:** Teoría Económica I y II, Formulación y evaluación de proyectos, Finanzas I, II y III""")
  
  col1, col2,col3= st.columns([1,1,2])
  with col1:
      # Contenido columna 1
      st.markdown("<div style='text-align: center;'><strong>Certificado Bachiller</strong></div>", unsafe_allow_html=True)

      response_bachiller = requests.get('https://raw.github.com/JossueCueto/portfolio_finance/c9be76bf1429f6b81d541ff8316c21a5b0e9e186/PDF/Certificado_bachiller.pdf')
      pdf_bachiller = BytesIO(response_bachiller.content)
      st.download_button('Descargar', pdf_bachiller, 'Certificado_bachiller.pdf','application/pdf')
  with col2:
      # Contenido columna 2
      st.markdown("<div style='text-align: center;'><strong>Órden de Mérito</strong></div>", unsafe_allow_html=True)
      
      response_orden_merito = requests.get('https://raw.github.com/JossueCueto/portfolio_finance/c9be76bf1429f6b81d541ff8316c21a5b0e9e186/PDF/Constancia_Orden_Merito_Jossue.pdf')
      pdf_orden_merito = BytesIO(response_orden_merito.content)
      st.download_button('Descargar', pdf_orden_merito, 'Jossue_Constancia_Orden_Merito.pdf','application/pdf')
  with col3:
      st.write("")
    
  st.subheader('Ofimática - ITEL (2021)')
  st.write('Técnico en Ofimática con énfasis en Excel y Access, incluyendo programación en VBA para la creación de macros personalizadas que mejoran la eficiencia operativa.')
  st.markdown(""" **Cursos Relevantes:** Base de datos I y II, Hoja electrónica I y II (Excel y VBA)""")

  col1, col2,col3= st.columns([1,1,2])
  with col1:
      # Contenido columna 1
      st.markdown("<div style='text-align: center;'><strong>Certificado</strong></div>", unsafe_allow_html=True)

      response_itel = requests.get('https://raw.github.com/JossueCueto/portfolio_finance/c9be76bf1429f6b81d541ff8316c21a5b0e9e186/PDF/Certificado_itel.pdf')
      pdf_itel = BytesIO(response_itel.content)
      st.download_button('Descargar', pdf_itel, 'Jossue_Itel.pdf','application/pdf')
  with col2:
      st.write("")
  with col3:
      st.write("")

  st.header('Cursos de Especialización')
  st.subheader('Go to Market - NetValU (2023)')
  st.write('Seleccionado para un programa altamente competitivo de finanzas corporativas, inversiones, riesgos y empleabilidad, seleccionado entre más de 170 candidatos a nivel nacional para ser uno de los 20 participantes.')
  st.markdown("""
  - **Propuesta de Portafolio de inversión de renta fija**: Elaboración de un portafolio de inversión compuesto por 100% bonos corporativos en base a un análisis macroeconómico, sectorial y de ratios financieros de las empresas.
  - **Medición de Riesgos de Portafolio de Inversión**: Análisis del riesgo de mercado y su impacto en el portafolio, considerando variables macroeconómicas y sensibilidad a factores de riesgo.
  - **Evaluación del Riesgo Crediticio**: Evaluación de la calidad crediticia para la compra de un bono corporativo de la empresa H2Olmos usando métricas de riesgo de crédito.
  - **Budget de Flujo de Caja y P&L**: Estimación de los resultados financieros de la compañía Netflix en los últimos 2 trimestres del 2023.
  """)
  
  col1, col2, col3, col4 = st.columns(4)
  with col1:
      # Contenido columna 1
      st.markdown("<div style='text-align: center;'><strong>Renta Fija</strong></div>", unsafe_allow_html=True)
      
      response_fixed_income = requests.get('https://raw.github.com/JossueCueto/portfolio_finance/c9be76bf1429f6b81d541ff8316c21a5b0e9e186/PDF/Fixed_income.pdf')
      pdf_fixed_income = BytesIO(response_fixed_income.content)
      st.download_button('Descargar', pdf_fixed_income, 'Jossue_Fixed_Income.pdf','application/pdf')
  with col2:
      # Contenido columna 2
      st.markdown("<div style='text-align: center;'><strong>Riesgo de Mercado</strong></div>", unsafe_allow_html=True)
    
      response_market_risk = requests.get('https://raw.github.com/JossueCueto/portfolio_finance/c9be76bf1429f6b81d541ff8316c21a5b0e9e186/PDF/Market_Risk.pdf')
      pdf_market_risk = BytesIO(response_market_risk.content)
      st.download_button('Descargar', pdf_fixed_income, 'Jossue_Market_Risk.pdf','application/pdf')
  with col3:
      # Contenido columna 3
      st.markdown("<div style='text-align: center;'><strong>Riesgo de Crédito</strong></div>", unsafe_allow_html=True)
      
      response_credit_risk = requests.get('https://raw.github.com/JossueCueto/portfolio_finance/c9be76bf1429f6b81d541ff8316c21a5b0e9e186/PDF/Credit_Risk.pdf')
      pdf_credit_risk = BytesIO(response_credit_risk.content)
      st.download_button('Descargar', pdf_credit_risk, 'Jossue_Credit_Risk.pdf','application/pdf')
  with col4:
      # Contenido columna 4
      st.markdown("<div style='text-align: center;'><strong>Fincorp</strong></div>", unsafe_allow_html=True)

      response_fincorp = requests.get('https://raw.github.com/JossueCueto/portfolio_finance/c9be76bf1429f6b81d541ff8316c21a5b0e9e186/PDF/Fincorp.pdf')
      pdf_fincorp = BytesIO(response_fincorp.content)
      st.download_button('Descargar', pdf_fincorp, 'Jossue_Fincorp.pdf','application/pdf')
  
  st.header('Objetivos Profesionales para el 2024')
  st.subheader('CEFA - BCRP')
  st.write('Al haber sido seleccionado para participar en el Curso de Extensión de Finanzas Avanzadas ' + 
            '(CEFA) organizado por el BCRP a realizarse de Enero a Marzo del 2024, me he planteado como ' +
             'objetivo finalizar entre los primeros puestos. Esta meta refleja mi determinación de demostrar ' +
             'y profundizar mi capacidad y conocimiento en el área financiera, así como mi compromiso con el ' +
             'logro de la excelencia en un entorno competitivo.')

  st.subheader('CFA')
  st.write('Además, para el año 2024, me he propuesto aprobar el primer nivel del Chartered Financial ' +
             'Analyst (CFA). Este objetivo es crucial para acreditar y consolidar mi conocimiento en finanzas, ' +
             'representando un paso significativo hacia el reconocimiento profesional y la expansión de mis ' +
             'competencias en el sector financiero global.')
  st.header('Experiencia adicional')
  st.subheader('Auxiliar Administrativo - SAEC EIRL (2021-2022)')
  st.markdown("""
  Apoyo administrativo en la ejecución y mejora de los planes y proyectos de la empresa.
  - Ejecución y mejora de los procesos administrativos relacionados a gestión de activos fijos, prestación del servicio contable, gestión de RRHH y gestión de las redes sociales.
  - Apoyo en trámites relacionados a constitución de empresas, aumento de capital y otras modificaciones de estatutos.
  """)
  st.write('**Logro:** Mejora del sistema de gestión de activos fijo e implementación del SSST')
  st.subheader('Asistente Administrativo - Secoemp EIRL (2020-2021)')
  st.markdown("""
  Apoyo administrativo en la ejecución de los planes y proyectos de la empresa.
  - Ejecución y mejora de los procesos administrativos relacionados a gestión de activos fijos, prestación del servicio contable, gestión de RRHH y gestión de las redes sociales.
  - Redacción y respuesta a solicitudes de los colaboradores de la empresa.
  """)
