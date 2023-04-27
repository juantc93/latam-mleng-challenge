# README    

Este repositorio contiene el reto de código para Latam Airlines.

# Descripción del proyecto

```
.
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   └── model_v0.pkl
│   └── src
│       ├── __init__.py
│       └── models
│           ├── __init__.py
│           ├── predict.py
│           └── predict_v0.json
├── dataset_SCL.csv
├── requirements.txt
├── stress-test-results.txt
├── stress.sh
├── stress_config.lua
├── synthetic_features.csv
└── to-expose.ipynb


```

El proyecto consiste en un contenedor de docker que despliega una API programa en **FASTApi** (python). El código de la api se encuentra dentro de la carpeta app.

El modelo de predicción es entrenado y persistido a partir de la ejecución del notebook. Este será serializado en formato pkl y debe ser guardado en la carpeta **/app/models**.

**app/src/models** contiene los modelos de petición esperados por la Api de fast Api. Dicho modelo se genera a partir del **Dataframe** de entrenamiento del notebook. De manera que se añaden o remueven caracteristicas, se generara un nuevo JSONSchema (predict_v{}.json). Este archivo json es procesado dentro del notebook para crear un objeto de Pydantic. Con el cual FASTApi realiza verificación de que la petición recibida en el endpoint **/predict** contenga en formato esperado (1-hot enconding). 

Para este ejercicio se asumirá que la única responsabilidad de la API es entregar la predicción, y que el microservicio o usuario que realiza la petición debe entregar los datos en formato json one hot. Como se muestra a continuación.


```
{
  "OPERA_Aerolineas Argentinas": 0,
  "OPERA_Aeromexico": 0,
  "OPERA_Air Canada": 0,
  "OPERA_Air France": 0,
  "OPERA_Alitalia": 0,
  "OPERA_American Airlines": 0,
  "OPERA_Austral": 0,
  "OPERA_Avianca": 0,
  "OPERA_British Airways": 0,
  "OPERA_Copa Air": 0,
  "OPERA_Delta Air": 0,
  "OPERA_Gol Trans": 0,
  "OPERA_Grupo LATAM": 1,
  "OPERA_Iberia": 0,
  "OPERA_JetSmart SPA": 0,
  "OPERA_K.L.M.": 0,
  "OPERA_Lacsa": 0,
  "OPERA_Latin American Wings": 0,
  "OPERA_Oceanair Linhas Aereas": 0,
  "OPERA_Plus Ultra Lineas Aereas": 0,
  "OPERA_Qantas Airways": 0,
  "OPERA_Sky Airline": 0,
  "OPERA_United Airlines": 0,
  "TIPOVUELO_I": 1,
  "TIPOVUELO_N": 0,
  "MES_1": 0,
  "MES_2": 0,
  "MES_3": 0,
  "MES_4": 0,
  "MES_5": 0,
  "MES_6": 0,
  "MES_7": 0,
  "MES_8": 0,
  "MES_9": 0,
  "MES_10": 0,
  "MES_11": 0,
  "MES_12": 1,
  "PERIODO_mañana": 0,
  "PERIODO_noche": 0,
  "PERIODO_tarde": 1,
  "DIA_Domingo": 0,
  "DIA_Jueves": 0,
  "DIA_Lunes": 0,
  "DIA_Martes": 0,
  "DIA_Miercoles": 0,
  "DIA_Sabado": 0,
  "DIA_Viernes": 1,
  "DESTINO_Antofagasta": 0,
  "DESTINO_Arica": 0,
  "DESTINO_Asuncion": 1,
  "DESTINO_Atlanta": 0,
  "DESTINO_Auckland N.Z.": 0,
  "DESTINO_Balmaceda": 0,
  "DESTINO_Bariloche": 0,
  "DESTINO_Bogota": 0,
  "DESTINO_Buenos Aires": 0,
  "DESTINO_Calama": 0,
  "DESTINO_Cancun": 0,
  "DESTINO_Castro (Chiloe)": 0,
  "DESTINO_Cataratas Iguacu": 0,
  "DESTINO_Ciudad de Mexico": 0,
  "DESTINO_Ciudad de Panama": 0,
  "DESTINO_Concepcion": 0,
  "DESTINO_Copiapo": 0,
  "DESTINO_Cordoba": 0,
  "DESTINO_Dallas": 0,
  "DESTINO_Florianapolis": 0,
  "DESTINO_Guayaquil": 0,
  "DESTINO_Houston": 0,
  "DESTINO_Iquique": 0,
  "DESTINO_Isla de Pascua": 0,
  "DESTINO_La Paz": 0,
  "DESTINO_La Serena": 0,
  "DESTINO_Lima": 0,
  "DESTINO_Londres": 0,
  "DESTINO_Los Angeles": 0,
  "DESTINO_Madrid": 0,
  "DESTINO_Melbourne": 0,
  "DESTINO_Mendoza": 0,
  "DESTINO_Miami": 0,
  "DESTINO_Montevideo": 0,
  "DESTINO_Neuquen": 0,
  "DESTINO_Nueva York": 0,
  "DESTINO_Orlando": 0,
  "DESTINO_Osorno": 0,
  "DESTINO_Paris": 0,
  "DESTINO_Puerto Montt": 0,
  "DESTINO_Puerto Natales": 0,
  "DESTINO_Puerto Stanley": 0,
  "DESTINO_Punta Arenas": 0,
  "DESTINO_Punta Cana": 0,
  "DESTINO_Punta del Este": 0,
  "DESTINO_Rio de Janeiro": 0,
  "DESTINO_Roma": 0,
  "DESTINO_Rosario": 0,
  "DESTINO_San Juan, Arg.": 0,
  "DESTINO_Santa Cruz": 0,
  "DESTINO_Sao Paulo": 0,
  "DESTINO_Sydney": 0,
  "DESTINO_Temuco": 0,
  "DESTINO_Toronto": 0,
  "DESTINO_Tucuman": 0,
  "DESTINO_Ushuia": 0,
  "DESTINO_Valdivia": 0,
  "temporada_alta": 0,
  "hora": 13,
  "VUELOS-PROGRAMADOS-DIA": 214,
  "RANKING_DIA": 110,
  "FRACCION_RANKING_DIA": 0.514018691588785
}

```

el archivo stress.sh contiene un sencillo script que puede ejecutar en una shell de linux con wrk en su PATH. toma el archivo stress_confi.lua para enviar la petición almacenada al endpoint desplegado, y finalmente escribe el resultado en el archivo **stress-test-results**

Para probar el endpoint de predicción, puede compilar la imagen de docker y correr el contenedor, el servicio quedará expuesto en el puerto *80*. Alternativamente puede construir el entorno virtual de python (3.9.5) especificado en el archivo **requirements.txt**, ingresar al folder app y ejecutar el siguiente comando:


```
 uvicorn main:app --reload

```

La api quedará expuesta en el puerto 8000. Fastapi permite probar interactivamente los endpoints configurados ingresando a: http://127.0.0.1:8000/docs#. 

Seleccione el endpoint /predict y presione try it out. El notebook le permite generar peticiones a partir del dataset de entrenamiento que puede ingresar en el cuadro de texto y enviarlas presionando el botón execute.


## Mejora del resultado de la prueba de estrés.

Para obtener un mejor desempeño de la api en un caso real, se podría plantear el despliegue de la aplicación en un cluster de Kubernetes como servicio, asegurando tener cierto numero de réplicas que permitan responder al flujo de las peticiones entrantes. 

También se podría plantear la posibilidad de formular un modelo de menor complejidad con la posibilidad de comprometer parcialmente la precisión y la sensibilidad del modelo. 