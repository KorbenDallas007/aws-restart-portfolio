# AWS SimuLearn: Creación de un Asistente Inteligente con IA (Amazon Bedrock)

| Parámetro | Detalle |
| :--- | :--- |
| **Dificultad** | Avanzada |
| **Tiempo Estimado** | 90 Minutos |
| **Servicios Principales** | Amazon Bedrock (Agents & Knowledge Bases), Amazon OpenSearch Serverless, AWS Lambda, Amazon S3, Amazon DynamoDB |

---

## 1. Resumen y Objetivos
Este laboratorio práctico se centra en la implementación de una solución de **IA Generativa** completa utilizando una arquitectura de **Generación Aumentada por Recuperación (RAG)**. Configurarás un asistente inteligente capaz de consultar documentos privados y ejecutar acciones transaccionales en tiempo real.

**Los objetivos principales son:**
*   Configurar una **Knowledge Base** en Amazon Bedrock vinculada a un almacén de vectores en OpenSearch Serverless.
*   Orquestar un **Amazon Bedrock Agent** utilizando modelos de lenguaje avanzados (LLM).
*   Implementar **Action Groups** mediante funciones AWS Lambda para persistir datos en Amazon DynamoDB.
*   Validar el flujo end-to-end: desde la consulta del usuario hasta la ejecución de la lógica de negocio.

---

## 2. Análisis del Escenario
El cliente requiere un asistente de Recursos Humanos (HR) que reduzca la carga operativa del departamento. El asistente debe cumplir dos funciones críticas:
1.  **Consulta de información:** Responder preguntas basadas en manuales de empleados y políticas de compensación (Datos no estructurados).
2.  **Ejecución de procesos:** Procesar solicitudes de vacaciones de empleados e insertarlas en la base de datos de la empresa (Acciones programáticas).

Como Ingeniero de AWS, implementarás Amazon Bedrock como el motor central de inferencia, asegurando que el modelo solo acceda a la información autorizada en el bucket de S3.

---

## 3. Arquitectura
La solución sigue un flujo de trabajo moderno de IA:
1.  **Almacenamiento:** Documentos en **S3** y registros en **DynamoDB**.
2.  **Indexación:** **OpenSearch Serverless** almacena los *embeddings* (vectores) de los documentos para búsquedas semánticas.
3.  **Capa de IA:** **Amazon Bedrock** gestiona la base de conocimientos y el agente.
4.  **Capa de Computación:** **Lambda** actúa como el puente entre el agente y la base de datos para ejecutar acciones.

<div align="center">
  <img src="./images/5.png" style="width:100%;" />
</div>

---

## 4. Desarrollo de las Tareas Paso a Paso

### Tarea 1: Recopilación de Recursos y Prompts
Antes de configurar la IA, debes obtener las instrucciones y los datos base.

1.  **Accede a Amazon S3:** Navega a la consola de S3 y localiza el bucket `lab-bucket-d3494210`.

<div align="center">
  <img src="./images/6.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/7.png" style="width:100%;" />
</div>

2.  **Obtén el Prompt del Agente:** Abre el archivo `agent-prompt.txt` y **copia** su contenido. Este archivo define la personalidad y responsabilidades del asistente de HR.

<div align="center">
  <img src="./images/8.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/9.png" style="width:100%;" />
</div>

3.  **Revisa los manuales:** En el bucket `knowledge-base-bucket-...`, confirma la existencia de los archivos `employee_handbook.txt` y `compensation_handbook.txt`. Estos alimentarán la Knowledge Base.

<div align="center">
  <img src="./images/10.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/11.png" style="width:100%;" />
</div>

### Tarea 2: Configuración del Motor de Búsqueda Vectorial
Amazon Bedrock requiere un lugar donde buscar información de forma semántica.

1.  **Navega a Amazon OpenSearch Service:** Ve a la sección **Serverless** > **Collections**.

<div align="center">
  <img src="./images/12.png" style="width:100%;" />
</div>

2.  **Identifica la Colección:** Selecciona `kb-collection` y **copia su ARN**. Lo necesitarás para vincular la Knowledge Base.

<div align="center">
  <img src="./images/13.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/14.png" style="width:100%;" />
</div>

3.  **Verifica el Índice:** Confirma que existe un índice llamado `bedrock-knowledge-base-index` con dimensiones configuradas para vectores (usualmente 1024 o 1536).

<div align="center">
  <img src="./images/15.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/16.png" style="width:100%;" />
</div>

### Tarea 3: Creación de la Knowledge Base (RAG)
Aquí conectarás el modelo de IA con tus documentos privados.

1.  **Navega a Amazon Bedrock:** Selecciona **Knowledge Bases** en el menú lateral y haz clic en **Create**.

<div align="center">
  <img src="./images/17.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/18.png" style="width:100%;" />
</div>

2.  **Configura los detalles:** Asigna el nombre `hr-knowledge-base` y selecciona el rol de IAM existente `Bedrock_KB_Role`.

<div align="center">
  <img src="./images/19.png" style="width:100%;" />
</div>

3.  **Conecta el Data Source:** Selecciona **Amazon S3** y apunta al bucket que contiene los manuales de HR.

<div align="center">
  <img src="./images/20.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/21.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/22.png" style="width:100%;" />
</div>

4.  **Selecciona el modelo de Embeddings:** Elige **Titan Text Embeddings V2**.

<div align="center">
  <img src="./images/23.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/24.png" style="width:100%;" />
</div>

5.  **Vincula el Vector Store:** Selecciona **OpenSearch Serverless**, pega el ARN de la colección y define los nombres de los campos de metadatos y vectores según las especificaciones del lab.

<div align="center">
  <img src="./images/25.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/26.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/27.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/28.png" style="width:100%;" />
</div>

6.  **Sincroniza:** Una vez creada, haz clic en **Sync** para que Bedrock procese los documentos y los convierta en vectores.

<div align="center">
  <img src="./images/29.png" style="width:100%;" />
</div>

### Tarea 4: Orquestación del Bedrock Agent
El Agente es el "cerebro" que decide si responder una pregunta o ejecutar una acción.

1.  **Crea el Agente:** En Bedrock, ve a **Agents** > **Create agent**. Nombre: `hr-assistant-agent`.

<div align="center">
  <img src="./images/30.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/31.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/32.png" style="width:100%;" />
</div>

2.  **Selecciona el Modelo:** Elige **Amazon Nova Pro 1.0** (optimizado para agentes inteligentes).

<div align="center">
  <img src="./images/33.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/34.png" style="width:100%;" />
</div>

3.  **Configura las Instrucciones:** Pega el contenido que copiaste del archivo `agent-prompt.txt`.

<div align="center">
  <img src="./images/35.png" style="width:100%;" />
</div>

4.  **Asocia la Knowledge Base:** En la sección de Knowledge Bases del agente, añade `hr-knowledge-base`. Esto le da acceso a los manuales de la empresa.

<div align="center">
  <img src="./images/36.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/37.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/38.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/39.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/40.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/41.png" style="width:100%;" />
</div>

### Tarea 5: Implementación de Action Groups (Lógica de Negocio)
Permitirás que el agente "haga cosas", no solo que "hable".

<div align="center">
  <img src="./images/42.png" style="width:100%;" />
</div>

1.  **Añade un Action Group:** Dale el nombre `submit_leave_action`.

<div align="center">
  <img src="./images/43.png" style="width:100%;" />
</div>

2.  **Vincula Lambda:** Selecciona la función Lambda existente `submit_leave`.

<div align="center">
  <img src="./images/44.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/45.png" style="width:100%;" />
</div>

3.  **Define Parámetros:** Configura los parámetros que el agente debe extraer de la conversación:
    *   `employee_name` (String, Required)
    *   `startDate` (String, Required)
    *   `endDate` (String, Required)

<div align="center">
  <img src="./images/46.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/47.png" style="width:100%;" />
</div>

4.  **Configura la Interacción:** Habilita el "User Input" para que el agente pueda preguntar detalles faltantes al usuario.

<div align="center">
  <img src="./images/48.png" style="width:100%;" />
</div>

### Tarea 6: Pruebas y Validación en DynamoDB
1.  **Prepara el Agente:** Haz clic en **Save** y luego en **Prepare**.
2.  **Prueba de Conocimiento:** En el chat de prueba, pregunta: *"What is the vacation policy?"*. El agente debe responder citando los manuales de S3.
3.  **Prueba de Acción:** Escribe: *"submit my vacation request"*. El agente te pedirá tu nombre y fechas. Proporciona los datos (ej: Jane Doe, Jan 1 to June 30).
4.  **Verificación Final:** Navega a **Amazon DynamoDB** > **Tables** > **VacationTable**. Haz clic en **Explore table items** y confirma que los datos de "Jane Doe" han sido insertados correctamente por el Agente.

<div align="center">
  <img src="./images/49.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/50.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/51.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/52.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/53.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/54.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/55.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/56.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/57.png" style="width:100%;" />
</div>
<div align="center">
  <img src="./images/58.png" style="width:100%;" />
</div>

---

## 5. Respuestas Analíticas

*   **¿Cuál es la ventaja de usar Nova Pro en lugar de un modelo estándar?**
    El modelo **Nova Pro** está específicamente optimizado para la orquestación de agentes. Posee una mayor capacidad de razonamiento para determinar cuándo debe consultar la base de conocimientos y cuándo debe invocar una función Lambda (Tool Use/Function Calling) con alta precisión en la extracción de parámetros.

*   **¿Por qué es necesario el proceso de "Sync" en la Knowledge Base?**
    El proceso de sincronización realiza el *chunking* (división del texto) y la vectorización de los documentos. Sin este paso, el modelo de lenguaje no podría realizar búsquedas semánticas sobre los datos de S3, ya que los LLM no leen archivos planos en tiempo de ejecución, sino que consultan representaciones matemáticas (vectores) en OpenSearch.

*   **¿Qué función cumple Lambda en este ecosistema?**
    Lambda actúa como el ejecutor de efectos secundarios. Mientras que el Agente procesa el lenguaje natural, Lambda traduce las intenciones del Agente en llamadas de API o consultas de base de datos (en este caso, un `PutItem` en DynamoDB), permitiendo que la IA interactúe con sistemas transaccionales legacy o modernos.

---
**Documentación generada por Alejandro Barrenechea.**

**April, 2026**

---