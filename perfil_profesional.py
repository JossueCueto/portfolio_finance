import streamlit as st

def run_perfil_profesional():
  
  st.header('Resumen Profesional')
  st.write('Aquí puedes escribir un resumen de tu introducción a la ciencia de datos o cualquier otro contenido.')
  
  st.header('Educación y Formación Académica')
  st.subheader('Ciencias Administrativas - UNJBG')
  st.write('Bachiller en Ciencias Administrativas, segundo lugar de mi promoción')
  st.markdown(""" Cursos Relevantes: Teoría Económica I y II, Formulación y evaluación de proyectos, Finanzas I, II y III""")
  st.subheader('Go to Market - NetValU')
  st.write('Seleccionado para un programa altamente competitivo de finanzas corporativas, inversiones, riesgos y empleabilidad, seleccionado entre más de 170 candidatos a nivel nacional para ser uno de los 20 participantes')
  # Your markdown content before the download button
  st.markdown("""
  - **Propuesta de Portafolio de inversión de renta fija**: Elaboración de un portafolio de inversión compuesto por 100% bonos corporativos en base a un análisis macroeconómico, sectorial y de ratios financieros de las empresas.
  - **Medición de Riesgos de Portafolio de Inversión**: Análisis del riesgo de mercado y su impacto en el portafolio, considerando variables macroeconómicas y sensibilidad a factores de riesgo.
  - **Evaluación del Riesgo Crediticio**: Evaluación de la calidad crediticia para la compra de un bono corporativo de la empresa H2Olmos usando métricas de riesgo de crédito.
  - **Budget de Flujo de Caja y P&L**: Estimación de los resultados financieros de la compañía Netflix en los últimos 2 trimestres del 2023.
  """)

  # Crear 4 columnas del mismo tamaño
  col1, col2, col3, col4 = st.columns(4)

  with col1:
      # Contenido para la columna 1
      st.markdown("<div style='text-align: center;'><strong>Renta Fija</strong></div>", unsafe_allow_html=True)
      st.download_button('Download Resume', 'path_to_resume.pdf', 'Tu Resumen.pdf',key='proyecto_1')
  
  with col2:
      # Contenido para la columna 2
      st.markdown("<div style='text-align: center;'><strong>Riesgo de Mercado</strong></div>", unsafe_allow_html=True)
      st.download_button('Download Resume', 'path_to_resume.pdf', 'Tu Resumen.pdf',key='proyecto_2')
  
  with col3:
      # Contenido para la columna 3
      st.markdown("<div style='text-align: center;'><strong>Riesgo de Crédito</strong></div>", unsafe_allow_html=True)
      st.download_button('Download Resume', 'path_to_resume.pdf', 'Tu Resumen.pdf',key='proyecto_3')
  
  with col4:
      # Contenido para la columna 4
      st.markdown("<div style='text-align: center;'><strong>Fincorp</strong></div>", unsafe_allow_html=True)
      st.download_button('Download Resume', 'path_to_resume.pdf', 'Tu Resumen.pdf',key='proyecto_4')
  
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
  st.markdown("""
  - **Propuesta de Portafolio de inversión de renta fija**: Elaboración de un portafolio de inversión compuesto por 100% bonos corporativos en base a un análisis macroeconómico, sectorial y de ratios financieros de las empresas.
  - **Medición de Riesgos de Portafolio de Inversión**: Análisis del riesgo de mercado y su impacto en el portafolio, considerando variables macroeconómicas y sensibilidad a factores de riesgo.
  - **Evaluación del Riesgo Crediticio**: Evaluación de la calidad crediticia para la compra de un bono corporativo de la empresa H2Olmos usando métricas de riesgo de crédito.
  - **Budget de Flujo de Caja y P&L**: Estimación de los resultados financieros de la compañía Netflix en los últimos 2 trimestres del 2023.
  """)
