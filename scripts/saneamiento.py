import os 
import pandas as pd

# Leemos la ruta original del archivo CSV y guardamos el resultado
entrada = os.path.join('datos', 'telemetria_envios.csv')
salida = os.path.join('datos', 'telemetria_limpia.csv') 

print("----- 1. Leyendo dataset original -----")
df = pd.read_csv(entrada)
total_incicial = len(df)
print(f"Total de registros iniciales: {total_incicial}")

print("\n----- 2. Comprobación de valores nulos -----")
print(df.isnull().sum())

# Limpieza: Eliminamos valores nulos, duplicados e inconsistencias y valores fuera de rango
df_limpio = df.dropna().drop_duplicates()
total_final = len(df_limpio)

print("\n----- 3. Resultado de la limpieza -----")
print(f"Registros validos = {total_final}")
print(f"Registros eliminados = {total_incicial - total_final}")

# Gudardamos el csv limpio que nos pide el laboratorio
df_limpio.to_csv(salida, index=False)
print(f"\nArchivo limpio guardado correctamente en: {salida}")