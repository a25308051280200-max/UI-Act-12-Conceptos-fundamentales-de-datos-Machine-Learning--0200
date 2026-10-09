# Alejandra Rivera Valenzuela NC 0200
# Número de lista 49 = 19 
import pandas as pd

# Definición del diccionario de datos (Lista 19)
datos19 = {
    'distancia_km': [1.9, 6.0, 2.7, 4.1, 3.4],
    'trafico_nivel': [2, 3, 1, 2, 1],
    'edad_repartidor': [23, 44, 30, 36, 27],
    'tiempo_entrega_min': [16, 56, 18, 34, 23]
}

# Crear DataFrame
df = pd.DataFrame(datos19)

print("DATOS DEL REPARTIDOR - NÚMERO DE LISTA 19")
print(df)
print("-" * 40)

# Seleccionar variables de entrada (X) y variable objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']]
y = df['tiempo_entrega_min']


# Datos de un nuevo pedido para predecir
nuevo_pedido = pd.DataFrame({
    'distancia_km': [3.0],
    'trafico_nivel': [2],
    'edad_repartidor': [30]
})


print("PREDICCIÓN DEL TIEMPO DE ENTREGA")
print("Distancia: 3.0 km")
print("Nivel de tráfico: medio")
print("Edad del repartidor: 30 años")
print("Alejandra Rivera Valenzuela NC 0200")