import pandas as pd
import plotly.express as px
import json

class VisualizadorDatos:
    def __init__(self, csv_path):
        # Cargar el CSV
        self.df = pd.read_csv(csv_path)
        
        # las columnas tienen que ser iguales al csv

        columnas_esperadas = {'CAUSA_DEF','ANIO_REGIS','ENT_CVE','MUN_CVE','SEXO','RANGO_EDAD','CONTEO','POBLACION','TASA','TASA_TYPE','ENT_NAME','MUN_NAME','Descripcion','TASA_100K','TASA_10K','TASA_1K','TASA_100'}
        if not columnas_esperadas.issubset(self.df.columns): #issubset() devuelve True si todos los elementos de un conjunto están presentes
            raise ValueError(f"El CSV debe contener las columnas: {columnas_esperadas}") #raise se usa para lanzar una excepción esto detiene la ejecución del programa y muestra un mensaje de error.

    #Generar grafico boxplot
    def generar_grafico_boxplot(self, columna_x, columna_y,color, titulo, output_html, output_json):

        # Crear el gráfico de barras
        fig = px.box(self.df, x=columna_x, y=columna_y, color=color, title=titulo)
        fig.write_html(output_html)
        
        # Guardar metadata del gráfico
        metadata = {
            'tipo': 'boxplot',
            'columnas': {'x': columna_x, 'y': columna_y},
            'color': color,
            'titulo': titulo,
            'archivo_html': output_html
        }
        
        with open(output_json, 'w') as json_file:
            json.dump(metadata, json_file, indent=4)   


    #Generar grafico barras
    def generar_grafico_barras(self, columna_x, columna_y, color, titulo, output_html, output_json):

        # Crear el gráfico de barras
        fig = px.bar(self.df, x=columna_x, y=columna_y, color=color, title=titulo)
        fig.write_html(output_html)
        
        # Guardar metadata del gráfico
        metadata = {
            'tipo': 'barras',
            'columnas': {'x': columna_x, 'y': columna_y},
            'color': color,
            'titulo': titulo,
            'archivo_html': output_html
        }
        
        with open(output_json, 'w') as json_file:
            json.dump(metadata, json_file, indent=4)

    #Generar grafico line
    def generar_grafico_line(self, columna_x, columna_y, color, titulo, output_html, output_json):
        # Crear el gráfico de barras
        fig = px.line(self.df, x=columna_x, y=columna_y, color=color ,title=titulo)
        """fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.df[columna_x], y=self.df[columna_y], mode='lines+markers', name='Data'))"""
        fig.write_html(output_html)
    # Guardar metadata del gráfico
        metadata = {
            'tipo': 'line',
            'columnas': {'x': columna_x, 'y': columna_y},
            'color':color,
            'titulo': titulo,
            'archivo_html': output_html
        }
            
        with open(output_json, 'w') as json_file:
            json.dump(metadata, json_file, indent=4)

    #Generar grafico sunburst
    def generar_grafico_sunburst(self, jerarquia, valores, titulo, output_html, output_json):
        
        # Crear el gráfico Sunburst
        fig = px.sunburst(self.df, path=jerarquia, values=valores, title=titulo)
        
        # Guardar el gráfico como un archivo HTML
        fig.write_html(output_html)
        
        # Guardar metadata del gráfico
        metadata = {
            'tipo': 'sunburst',
            'jerarquia': jerarquia,
            'valores': valores,
            'titulo': titulo,
            'archivo_html': output_html
        }
 
        # Guardar el archivo JSON
        with open(output_json, 'w') as json_file:
            json.dump(metadata, json_file, indent=4)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia del visualizador con la ruta al CSV
    visualizador = VisualizadorDatos('./generador_graficos/data/U_Rates.csv')

    # Generar un gráfico boxplot
    visualizador.generar_grafico_boxplot(
        columna_x='SEXO', 
        columna_y='POBLACION',    
        color = 'RANGO_EDAD',
        titulo='Boxplot',
        output_html='./generador_graficos/test/Boxplot/boxplot.html',
        output_json='./generador_graficos/test/Boxplot/boxplot.json'
    )
    
    # Generar un gráfico de barras
    visualizador.generar_grafico_barras(
        columna_x= 'SEXO',
        columna_y='POBLACION',    
        color = 'RANGO_EDAD',
        titulo='Distribución de edades por entidad',
        output_html='./generador_graficos/test/Barras/grafico_barras_entidad.html',
        output_json='./generador_graficos/test/Barras/grafico_barras_entidad.json'
    )

    # Generar un gráfico lineplot
    visualizador.generar_grafico_line(
        columna_x='SEXO', 
        columna_y='POBLACION',   
        color = 'RANGO_EDAD',  
        titulo='LINE PLOT',
        output_html='./generador_graficos/test/Lineplot/lineplot.html',
        output_json='./generador_graficos/test/Lineplot/lineplot.json'
    )

    # Generar un gráfico sunburst
    visualizador.generar_grafico_sunburst(
        jerarquia='MUN_NAME',
        valores='CONTEO',     
        titulo='Sunburst',
        output_html='./generador_graficos/test/Sunburst/sunburst.html',
        output_json='./generador_graficos/test/Sunburst/sunburst.json'
    )