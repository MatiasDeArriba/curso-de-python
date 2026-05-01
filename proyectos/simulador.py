import streamlit as st

def calcular_probabilidad(viviendas, total_personas):
    """Calcula el porcentaje de probabilidad evitando la división por cero."""
    if total_personas == 0:
        return 0.0
    return (viviendas / total_personas) * 100

def main():
    st.title("Simulador de Probabilidad de Vivienda")
    
    # Configuración de los Sliders (Entradas)
    padron_original = st.slider("Padrón original", 0, 1000, 560)
    nuevos_anexados = st.slider("Nuevos anexados", 0, 500, 36)
    viviendas_disponibles = 25 # Dato fijo según la imagen
    
    # Lógica de cálculo
    total_inscriptos = padron_original + nuevos_anexados
    probabilidad = calcular_probabilidad(viviendas_disponibles, total_inscriptos)
    
    # Interfaz de resultados (Visualización)
    st.subheader(f"Total de participantes: {total_inscriptos}")
    
    # El "Card" de resultado con estilo destacado
    st.markdown(
        f"""
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center;">
            <h2 style="color: white; margin-bottom: 0;">Tu probabilidad es del:</h2>
            <h1 style="color: #4A90E2; font-size: 50px;">{probabilidad:.2f}%</h1>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()