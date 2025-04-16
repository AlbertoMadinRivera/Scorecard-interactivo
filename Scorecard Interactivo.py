import dash
from dash import dcc, html, Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# ===============================
# 🎲 Simular datos con tendencias realistas
# ===============================
clientes = ['Cliente A', 'Cliente B', 'Cliente C']
periodos = pd.date_range('2020-01-01', '2024-12-01', freq='MS')

data = []
np.random.seed(42)  # Para reproducibilidad

for cliente in clientes:
    for i, periodo in enumerate(periodos):
        # Score general random
        score = np.random.uniform(60, 100)
        tendencia = np.random.uniform(65, 90)

        # Cobertura con patrón definido
        if cliente == 'Cliente A':
            cobertura = 70 + (i / len(periodos)) * (133 - 70)  # crece
        elif cliente == 'Cliente B':
            cobertura = 130 - (i / len(periodos)) * (130 - 70)  # decrece
        else:  # Cliente C
            cobertura = np.random.uniform(60, 140)  # estocástico

        data.append({
            'Cliente': cliente,
            'Fecha': periodo,
            'Score': score,
            'Tendencia': tendencia,
            'Cobertura': cobertura
        })

df = pd.DataFrame(data)

# ===============================
# 🚀 App Dash
# ===============================
app = dash.Dash(__name__)
app.title = "Scorecard Interactivo"

app.layout = html.Div(style={
    'fontFamily': 'Segoe UI, sans-serif',
    'backgroundColor': '#f5f7fa',
    'padding': '30px'
}, children=[

    html.H1("📊 Scorecard Interactivo", style={
        'textAlign': 'center',
        'color': '#2c3e50',
        'marginBottom': '40px'
    }),

    html.Div([
        html.Label("Selecciona un cliente:", style={
            'fontSize': '18px',
            'color': '#2c3e50'
        }),
        dcc.Dropdown(
            id='cliente-dropdown',
            options=[{'label': c, 'value': c} for c in df['Cliente'].unique()],
            value='Cliente A',
            style={
                'width': '300px',
                'marginTop': '10px',
                'marginBottom': '30px'
            }
        ),
    ], style={'textAlign': 'center'}),

    dcc.Graph(id='scorecard-grafico')
])

# ===============================
# 📈 Callback del gráfico
# ===============================
@app.callback(
    Output('scorecard-grafico', 'figure'),
    Input('cliente-dropdown', 'value')
)
def actualizar_grafico(cliente_seleccionado):
    df_cliente = df[df['Cliente'] == cliente_seleccionado]

    fig = go.Figure()

    # 🔵 Línea Score del cliente
    fig.add_trace(go.Scatter(
        x=df_cliente['Fecha'],
        y=df_cliente['Score'],
        mode='lines+markers',
        name='Score del Cliente',
        line=dict(color='royalblue', width=2),
        marker=dict(size=6)
    ))

    # 🔴 Línea Tendencia general
    fig.add_trace(go.Scatter(
        x=df_cliente['Fecha'],
        y=df_cliente['Tendencia'],
        mode='lines+markers',
        name='Tendencia Auditada',
        line=dict(color='firebrick', dash='dot', width=2),
        marker=dict(size=6)
    ))

    # ⚫ Barras de cobertura con alpha 50%
    fig.add_trace(go.Bar(
        x=df_cliente['Fecha'],
        y=df_cliente['Cobertura'],
        name='Cobertura (%)',
        marker_color='rgba(0,0,0,0.3)',
        yaxis='y2'
    ))

    fig.update_layout(
        title=f"Scorecard de {cliente_seleccionado}",
        title_font=dict(size=22, color='#2c3e50'),
        plot_bgcolor='#ffffff',
        paper_bgcolor='#f5f7fa',
        xaxis=dict(title='Fecha', showgrid=True, gridcolor='#e1e8ed'),
        yaxis=dict(title='Score', showgrid=True, gridcolor='#e1e8ed'),
        yaxis2=dict(
            title='Cobertura (%)',
            overlaying='y',
            side='right',
            range=[0, 150],
            showgrid=False
        ),
        legend=dict(
            x=0.01, y=0.99,
            bgcolor='rgba(255,255,255,0)',
            bordercolor='rgba(0,0,0,0)'
        ),
        height=550,
        margin=dict(l=50, r=50, t=80, b=50),
        font=dict(color='#2c3e50')
    )

    return fig

# ===============================
# ▶️ Ejecutar
# ===============================
if __name__ == '__main__':
    app.run_server(debug=True)