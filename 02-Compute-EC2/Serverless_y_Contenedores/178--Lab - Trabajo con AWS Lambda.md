# 🏗️ Lab: Trabajo con AWS Lambda y Computación Serverless
**Dificultad:** Intermedia | ⏱️ **Tiempo Estimado:** 60 minutos
**Servicios Principales:** ƛ AWS Lambda, 🖥️ Amazon EC2, 🔔 Amazon SNS, 🔑 Systems Manager, 📅 EventBridge.

## 📋 Resumen y Objetivos
En este laboratorio, desplegarás y configurarás una solución de computación **serverless** basada en **AWS Lambda**. La arquitectura automatiza la generación de reportes de ventas diarios extrayendo datos de una base de datos MySQL (alojada en EC2) y enviando los resultados por correo electrónico mediante SNS.

**Objetivos técnicos:**
*   🛡️ Verificar permisos de **IAM** para la ejecución de funciones.
*   📦 Crear una **Lambda Layer** para gestionar la librería externa `PyMySQL`.
*   🌐 Configurar funciones Lambda para acceder a recursos dentro de una **VPC**.
*   💻 Utilizar la **AWS CLI** para el despliegue de funciones.
*   🕒 Automatizar tareas mediante reglas de cron en **Amazon EventBridge**.

## 🔍 Análisis del Escenario
El cliente requiere un sistema de reportes que no consuma recursos de manera ociosa. La solución utiliza una función "Extractora" que interactúa directamente con la base de datos privada en EC2 y una función "Orquestadora" que gestiona la lógica del negocio y las notificaciones. Se utiliza **Systems Manager Parameter Store** para centralizar las credenciales, cumpliendo con el pilar de seguridad de AWS al evitar el "hardcoding" de datos sensibles.

## 🗺️ Arquitectura
<p align="center">
    <img src="images/1.png" width="550">
</p> 

---

## 🛠️ Desarrollo del Laboratorio

### 1️⃣ Tarea 1: Observación de permisos IAM 🛡️
1.  **Navega** a la consola de **IAM** y selecciona **Roles**.
2.  **Busca** la palabra `sales` en el cuadro de búsqueda para filtrar los roles necesarios.
<p align="center"><img src="images/3.png" width="750"></p>

3.  **Haz clic** en el rol `salesAnalysisReportRole`.
    *   **Verifica** en la pestaña **Trust relationships** que el servicio `lambda.amazonaws.com` aparezca como entidad de confianza.
<p align="center"><img src="images/4.png" width="750"></p>

3. **Analiza** las políticas adjuntas en la pestaña **Permissions**: `AmazonSNSFullAccess`, `AmazonSSMReadOnlyAccess`, `AWSLambdaBasicExecutionRole` y `AWSLambdaRole`.
<p align="center"><img src="images/7.png" width="750"></p>
<p align="center"><img src="images/8.png" width="750"></p>
<p align="center"><img src="images/9.png" width="750"></p>


4.  **Regresa** a la lista de roles y **selecciona** `salesAnalysisReportDERole`.
    *   **Confirma** que incluya la política `AWSLambdaVPCAccessExecutionRole`. Esta es indispensable para que la función genere interfaces de red (ENI) y acceda a la base de datos dentro de la VPC.
<p align="center"><img src="images/10.png" width="750"></p>
<p align="center"><img src="images/11.png" width="750"></p>
<p align="center"><img src="images/12.png" width="750"></p>
<p align="center"><img src="images/13.png" width="750"></p>

### 2️⃣ Tarea 2: Creación de Lambda Layer y Función Extractora 📦
1.  **Descarga** los archivos: `pymysql-v3.zip` y `salesAnalysisReportDataExtractor-v3.zip`.
2.  **Navega** a **AWS Lambda** > **Layers** > **Create layer**.
    *   **Nombre:** `pymysqlLibrary`.
    *   **Upload:** Sube el archivo `pymysql-v3.zip`.
    *   **Compatible runtimes:** Selecciona **Python 3.14**.
    *   **Haz clic** en **Create**.
<p align="center"><img src="images/14.png" width="750"></p>

3.  **Crea la función:** Ve a **Functions** > **Create function**.
    *   **Selecciona:** "Author from scratch".
    *   **Nombre:** `salesAnalysisReportDataExtractor`.
    *   **Runtime:** **Python 3.14**.
    *   **Role:** Selecciona **Use an existing role** y elige `salesAnalysisReportDERole`.
    *   **Haz clic** en **Create function**.
<p align="center"><img src="images/15.png" width="750"></p>

4.  **Añade el Layer:** En la sección **Layers** (al final de la página), haz clic en **Add a layer**.
<p align="center"><img src="images/16.png" width="750"></p>
<p align="center"><img src="images/17.png" width="750"></p>

**Selecciona:** "Custom layers" > `pymysqlLibrary` > Versión **1**.

<p align="center"><img src="images/18.png" width="750"></p>
<p align="center"><img src="images/19.png" width="750"></p>


5.  **Importa el código:** En la pestaña **Code**, haz clic en **Upload from** > **.zip file** y carga `salesAnalysisReportDataExtractor-v3.zip`.
<p align="center"><img src="images/20.png" width="750"></p>
<p align="center"><img src="images/21.png" width="750"></p>

6.  **Configura el Handler:** En **Runtime settings**, haz clic en **Edit** y escribe `salesAnalysisReportDataExtractor.lambda_handler`. **Guarda**.
7.  **Configura la red:** Ve a **Configuration** > **VPC** > **Edit**.
    *   **VPC:** Selecciona `Cafe VPC`.
    *   **Subnets:** Elige `Cafe Public Subnet 1`.
    *   **Security groups:** Selecciona `CafeSecurityGroup`. **Haz clic en Save**.
<p align="center"><img src="images/22.png" width="750"></p>

### 3️⃣ Tarea 3: Pruebas y Troubleshooting 🧪
1.  **Obtén parámetros:** Navega a **Systems Manager** > **Parameter Store**. **Copia** los valores de `/cafe/dbUrl`, `/cafe/dbName`, `/cafe/dbUser` y `/cafe/dbPassword`.
<p align="center"><img src="images/23.png" width="750"></p>

2.  **Crea el Test:** En la pestaña **Test** de tu Lambda.
    *   **Nombre:** `SARDETestEvent`.
    *   **JSON:** Reemplaza los valores con los datos reales obtenidos en el paso anterior. **Guarda**.
<p align="center"><img src="images/24.png" width="750"></p>

3.  **Ejecuta el Test:** Recibirás un error de **Timeout** (3s). Este es el comportamiento esperado inicial.
<p align="center"><img src="images/25.png" width="750"></p>

4.  **Ajuste del Firewall:** Ve a **EC2** > **Security Groups** > `CafeSecurityGroup`.
    *   **Edita las Inbound Rules**: Agrega una regla para **MySQL/Aurora (3306)** permitiendo el tráfico desde `0.0.0.0/0`.
<p align="center"><img src="images/26.png" width="750"></p>

5.  **Repite el Test:** Ahora el resultado debe ser **Succeeded**.
<p align="center"><img src="images/27.png" width="750"></p>

6.  **Simulación de Negocio:** Accede a la web del café (`http://<PublicIP>/cafe`), realiza pedidos y verifica que la Lambda extraiga los nuevos datos.
<p align="center"><img src="images/28.png" width="750"></p>
<p align="center"><img src="images/29.png" width="750"></p>

### 4️⃣ Tarea 4: Configuración de Notificaciones (SNS) 🔔
1.  **Navega** a **Amazon SNS** > **Topics** > **Create topic**.
    *   **Tipo:** Standard. **Nombre:** `salesAnalysisReportTopic`.
<p align="center"><img src="images/30.png" width="750"></p>

2.  **Copia el ARN** del tópico.
3.  **Crea la suscripción:** Haz clic en **Create subscription**.
    *   **Protocol:** Email. **Endpoint:** Tu correo electrónico.
<p align="center"><img src="images/31.png" width="750"></p>

4.  **Confirmación:** Revisa tu email y haz clic en el enlace de confirmación. Asegúrate de ver el mensaje "Subscription confirmed!".
<p align="center"><img src="images/32.png" width="350"></p>

### 5️⃣ Tarea 5: Despliegue con CLI 💻
1.  **Conéctate:** En EC2, selecciona `CLI Host` y utiliza **EC2 Instance Connect**.
<p align="center"><img src="images/33.png" width="750"></p>
<p align="center"><img src="images/34.png" width="750"></p>

2.  **Configura el CLI:** Ejecuta `aws configure` e ingresa tu **Access Key**, **Secret Key** y la región `us-west-2`.
<p align="center"><img src="images/35.png" width="750"></p>

3.  **Crea la función orquestadora:**
    ```bash
    aws lambda create-function \
    --function-name salesAnalysisReport \
    --runtime python3.14 \
    --zip-file fileb://salesAnalysisReport-v2.zip \
    --handler salesAnalysisReport.lambda_handler \
    --region us-west-2 \
    --role <ARN_DEL_ROL_IAM_SALES_ANALYSIS_REPORT>
    ```
<p align="center"><img src="images/36.png" width="750"></p>

4.  **Variables de entorno:** En la consola de Lambda > `salesAnalysisReport` > **Configuration** > **Environment variables**.
    *   **Añade:** Key: `topicARN` | Value: El ARN de tu tópico SNS.
<p align="center"><img src="images/37.png" width="750"></p>

5.  **Test Final:** Ejecuta `SARTestEvent`. Recibirás el reporte final en tu correo.
<p align="center"><img src="images/38.png" width="750"></p>

### 6️⃣ Tarea 6: Automatización (EventBridge) 📅
1.  En la función `salesAnalysisReport`, **añade un trigger** de **EventBridge**.
2.  **Crea una nueva regla**: `salesAnalysisReportDailyTrigger`.
3.  **Expresión Cron:** Para ejecutar el reporte, usa por ejemplo `cron(0 20 ? * MON-SAT *)` para las 8 PM.

---

## 🧠 Respuestas Analíticas

*   **¿Por qué usamos Python 3.14?** Al ser el runtime recomendado por la consola moderna, garantiza el acceso a las últimas optimizaciones de rendimiento y soporte extendido de AWS.
*   **¿Cuál es la función del Security Group en este lab?** Funciona como un firewall virtual que permite que el tráfico MySQL (puerto 3306) originado en la interfaz de red de la Lambda llegue al servidor EC2. Sin esta regla, la conexión se bloquea.
*   **¿Qué ventaja ofrece Parameter Store?** Permite que los datos de conexión sean variables. Si la base de datos se migra a otro servidor, solo actualizamos el parámetro en Systems Manager y la arquitectura Lambda se adapta instantáneamente sin tocar el código.