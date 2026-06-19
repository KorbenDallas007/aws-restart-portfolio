# ­ƒøá´©Å Laboratorio: Gesti├│n Centralizada con AWS Systems Manager

*   **Dificultad:** Intermedia
*   **Tiempo Estimado:** 30 minutos
*   **Servicios Principales:** AWS Systems Manager (Fleet Manager, Run Command, Parameter Store, Session Manager), Amazon EC2.

---

## ­ƒôØ Resumen y Objetivos
AWS Systems Manager (SSM) es el centro de operaciones para la infraestructura en la nube y on-premises. Este laboratorio se enfoca en eliminar la dependencia de tareas manuales y conexiones inseguras (como SSH), permitiendo la automatizaci├│n de configuraciones y la gesti├│n de flotas a escala.

**Los objetivos de este laboratorio son:**
1.  **Recolectar metadatos** e inventario de software de forma autom├ítica.
2.  **Ejecutar scripts y despliegues** de aplicaciones sin acceso remoto directo mediante Run Command.
3.  **Gestionar configuraciones din├ímicas** de aplicaciones usando Parameter Store.
4.  **Establecer t├║neles de administraci├│n seguros** mediante Session Manager (sustituyendo SSH).

---

## ­ƒöì An├ílisis del Escenario
**Diagn├│stico:** El departamento de operaciones requiere una estrategia para gestionar servidores Red Hat y Amazon Linux sin necesidad de abrir el puerto 22 en los Grupos de Seguridad, ni distribuir llaves `.pem`. Adem├ís, necesitan una forma de activar caracter├¡sticas en "caliente" (hot-swapping) en sus aplicaciones web. Como ingeniero de SysOps, implementar├ís los m├│dulos de Node Management y Application Management de SSM para garantizar una administraci├│n auditable y eficiente.

---

## ­ƒÅù´©Å Arquitectura
1.  **Agente SSM:** Preinstalado en la instancia, act├║a como puente entre la API de SSM y el SO.
2.  **IAM Role:** La instancia posee un perfil de instancia que le otorga permisos para comunicarse con el servicio SSM.
3.  **Control Plane:** El usuario interact├║a con la consola de SSM, la cual env├¡a instrucciones cifradas a la instancia a trav├®s del agente.

<p align="center">
<img src="images/1.png" width="450"
</p>
<p align="center">
<img src="images/2.png" width="450">
</p>

---

## ­ƒÜÇ Desarrollo

### Tarea 1: Generaci├│n de Listas de Inventario con Fleet Manager
Esta funcionalidad permite auditar qu├® software y versiones est├ín instaladas en tu flota.

1.  **Navega** a la consola de **Systems Manager** desde la barra de b├║squeda.
2.  **Selecciona** **Fleet Manager** en el panel de navegaci├│n izquierdo (secci├│n *Node Management*).
3.  **Haz clic** en el men├║ desplegable **Account management** y selecciona **Set up inventory**.

<p align="center">
<img src="images/3.png" width="750">
</p>

1.  **Configura** los detalles del inventario:
    *   **Name:** `Inventory-Association`.
    *   **Targets:** Selecciona **Manually selecting instances**.
    *   **Instancias:** Marca la casilla de la instancia llamada `Managed Instance`.
2.  **Finaliza** haciendo clic en **Setup Inventory**.

<p align="center">
<img src="images/4.png" width="750">
</p>

1.  **Espera** un minuto, selecciona el **Node ID** de la instancia y navega a la pesta├▒a **Inventory** para explorar las aplicaciones y servicios detectados por el agente.

<p align="center">
<img src="images/5.png" width="750">
</p>

### Tarea 2: Instalaci├│n de Aplicaci├│n mediante Run Command
Run Command permite ejecutar comandos de shell o scripts de PowerShell de forma masiva y segura.

1.  **Selecciona** **Run Command** en el panel izquierdo (secci├│n *Node Management*).
2.  **Haz clic** en el bot├│n naranja **Run command**.
3.  **Busca el documento:** Haz clic en la barra de b├║squeda, selecciona el filtro **Owner** y elige **Owned by me**.
4.  **Selecciona** el documento que aparece (dise├▒ado para instalar la Dashboard App).
5.  **Define el Target:** Selecciona **Choose instances manually** y marca la casilla de `Managed Instance`.

<p align="center">
<img src="images/6.png" width="750">
</p>

6.  **Desactiva** la opci├│n **Enable an S3 bucket** en la secci├│n *Output options* (para simplificar este ejercicio).
7.  **Haz clic** en **Run**.

<p align="center">
<img src="images/7.png" width="750">
</p>

8.  **Verificaci├│n:** Una vez el estado sea "Success", **copia** la `ServerIP` desde el panel de detalles del laboratorio y **p├®gala** en tu navegador. Deber├¡as ver el "Widget Manufacturing Dashboard".

<p align="center">
<img src="images/8.png" width="750">
</p>
<p align="center">
<img src="images/9.png" width="750">
</p>

### Tarea 3: Gesti├│n de Configuraci├│n con Parameter Store
Utilizar├ís un almac├®n de par├ímetros para cambiar el comportamiento de la aplicaci├│n sin modificar el c├│digo.

1.  **Navega** a **Parameter Store** en el panel izquierdo (secci├│n *Application Management*).
2.  **Haz clic** en **Create parameter**.
3.  **Escribe** los siguientes valores:
    *   **Name:** `/dashboard/show-beta-features`
    *   **Description:** `Display beta features`
    *   **Value:** `True`
4.  **Haz clic** en **Create parameter**.

<p align="center">
<img src="images/10.png" width="750">
</p>

5.  **Actualiza** la pesta├▒a del navegador donde tienes abierta la Dashboard App.
6.  **Observa** que ahora aparece un tercer gr├ífico (Beta). La aplicaci├│n est├í programada para consultar la API de SSM y reaccionar seg├║n este par├ímetro.

<p align="center">
<img src="images/11.png" width="750">
</p>

### Tarea 4: Acceso Remoto Seguro con Session Manager
Session Manager permite el acceso a la terminal sin llaves SSH y sin necesidad de abrir puertos de entrada en el Firewall.

1.  **Selecciona** **Session Manager** en el panel izquierdo.
2.  **Haz clic** en **Start session**.
3.  **Selecciona** la `Managed Instance` y haz clic en **Start session**.

<p align="center">
<img src="images/12.png" width="750">
</p>

4.  **Interact├║a con el sistema:** Se abrir├í una terminal en el navegador. Ejecuta:
    ```bash
    ls /var/www/html
    ```
5.  **Consulta metadatos y CLI:** Ejecuta el siguiente bloque para obtener informaci├│n de la regi├│n e instancias:
    ```bash
    # Obtener regi├│n desde el servicio de metadatos
    AZ=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
    export AWS_DEFAULT_REGION=${AZ::-1}

    # Listar informaci├│n mediante AWS CLI (ya configurada por el rol de IAM)
    aws ec2 describe-instances
    ```
<p align="center">
<img src="images/13.png" width="750">
</p>
<p align="center">
<img src="images/14.png" width="750">
</p>
---

## ­ƒºá Respuestas Anal├¡ticas

*   **┬┐Cu├íl es la ventaja de Run Command sobre el acceso SSH tradicional?**
    *   **Respuesta:** Run Command permite la ejecuci├│n paralela en cientos de instancias, registra autom├íticamente el historial de comandos en CloudTrail (auditor├¡a) y no requiere que el puerto 22 est├® expuesto a Internet, reduciendo dr├ísticamente la superficie de ataque.

*   **┬┐C├│mo sabe la aplicaci├│n web que debe mostrar el gr├ífico Beta?**
    *   **Respuesta:** La aplicaci├│n utiliza el AWS SDK para realizar una llamada a la API `ssm:GetParameter`. Al cambiar el valor en Parameter Store de `False` a `True`, la l├│gica interna de la app detecta el cambio en su siguiente consulta y renderiza el contenido adicional.

*   **┬┐Por qu├® Session Manager es preferible en entornos corporativos?**
    *   **Respuesta:** Porque centraliza el control de acceso mediante pol├¡ticas de IAM en lugar de archivos de llaves `.pem` que pueden perderse o ser robados. Adem├ís, proporciona logs completos de cada sesi├│n, cumpliendo con est├índares de cumplimiento (Compliance).

---
**Conclusi├│n:** Has implementado un ecosistema de gesti├│n moderno donde la infraestructura es tratada como c├│digo y el acceso es estrictamente controlado y auditado.
