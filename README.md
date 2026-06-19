# AWS Restart Portfolio 🚀
<!-- Badges -->
<p align="left">
  <img src="https://img.shields.io/github/license/KorbenDallas007/aws-restart-portfolio?style=flat-square" alt="License">
  <img src="https://img.shields.io/github/languages/top/KorbenDallas007/aws-restart-portfolio?style=flat-square" alt="Language">
  <img src="https://img.shields.io/github/last-commit/KorbenDallas007/aws-restart-portfolio?style=flat-square" alt="Last Commit">
  <img src="https://img.shields.io/github/v/release/KorbenDallas007/aws-restart-portfolio?style=flat-square&include_prereleases" alt="Latest Release">
</p>

## 📑 Tabla de Contenidos
- [Objetivo](#objetivo)
- [Ruta de Aprendizaje](#ruta-de-aprendizaje)
- [Laboratorios](#estructura-de-módulos)
- [Contribución](#contribuir)

Repositorio completo de laboratorios y ejercicios del programa **AWS Restart** - una iniciativa de capacitación en AWS para desarrolladores.

## 📚 Descripción General

Este portfolio contiene una colección integral de laboratorios prácticos, ejercicios y conceptos fundamentales de **Amazon Web Services (AWS)**, organizados en módulos temáticos. Cada módulo incluye documentación detallada, laboratorios paso a paso y mejores prácticas.

### 🎯 Objetivo del Repositorio

Proporcionar una ruta de aprendizaje estructurada desde conceptos fundamentales de cloud hasta aplicaciones avanzadas en AI/ML con AWS.

---

## 📁 Estructura de Módulos

### [00-Cloud-Fundamentals](./00-Cloud-Fundamentals/) ☁️
**Fundamentos de Cloud Computing**
- [Automatización con AWS Systems Manager](./00-Cloud-Fundamentals/Automatizacion_SSM/)
- [CLI y Operaciones de Sistemas](./00-Cloud-Fundamentals/CLI_y_SysOps/)
- [Infrastructure as Code con CloudFormation](./00-Cloud-Fundamentals/CloudFormation/)
- [Costos y Etiquetado de Recursos](./00-Cloud-Fundamentals/Costos_y_Etiquetas/)

**Conceptos clave:** IAM, CloudFormation, sistemas de costos, automatización

---

### [01-Networking-VPC](./01-Networking-VPC/) 🌐
**Redes y Virtual Private Cloud**
- [Conceptos de Redes Avanzados](./01-Networking-VPC/Conceptos_Redes/)
- [Configuración y Troubleshooting de VPC](./01-Networking-VPC/Configuracion_VPC/)

**Conceptos clave:** VPC, subredes, IP públicas/privadas, routing, seguridad de red

---

### [02-Compute-EC2](./02-Compute-EC2/) 💻
**Computación con Amazon EC2**
- [Escalado y Balanceo de Carga](./02-Compute-EC2/Escalado_y_Balanceo/)
- [Fundamentos de Linux y EC2](./02-Compute-EC2/Fundamentos_Linux_y_EC2/)
- [Serverless y Contenedores](./02-Compute-EC2/Serverless_y_Contenedores/)
- [Configuración Avanzada de Servidores](./02-Compute-EC2/Servidores/)

**Conceptos clave:** EC2 instances, Auto Scaling, Load Balancer, Lambda, ECS, EKS

---

### [03-Storage-S3](./03-Storage-S3/) 💾
**Almacenamiento y Objetos**
- [Almacenamiento y Archivado de Datos](./03-Storage-S3/Almacenamiento_y_Archivado/)

**Conceptos clave:** S3 buckets, storage tiers, lifecycle policies, data archival

---

### [04-Security-IAM](./04-Security-IAM/) 🔐
**Seguridad e Identity Access Management**
- [Seguridad e IAM](./04-Security-IAM/Seguridad_e_IAM/)
- [Monitoreo y CloudTrail](./04-Security-IAM/Monitoreo_y_CloudTrail/)

**Conceptos clave:** IAM users/roles, MFA, CloudTrail, CloudWatch, compliance

---

### [05-Databases-RDS](./05-Databases-RDS/) 🗄️
**Bases de Datos Relacionales**
- [Fundamentos de BD y RDS](./05-Databases-RDS/Fundamentos_DB_y_RDS/)
- [Migración y Servicios de Base de Datos](./05-Databases-RDS/Migracion_y_Servicios/)

**Conceptos clave:** RDS, MySQL, PostgreSQL, Multi-AZ, backups, DMS

---

### [06-Python-Fundamentals](./06-Python-Fundamentals/) 🐍
**Programación en Python**
- [Laboratorios Base](./06-Python-Fundamentals/Laboratorios_Base/)
- [Ejercicios Adicionales](./06-Python-Fundamentals/Ejercicios_Adicionales/)

**Conceptos clave:** Python basics, AWS SDK (Boto3), automation scripts

---

### [07-AI-Machine-Learning](./07-AI-Machine-Learning/) 🤖
**Machine Learning y IA**
- [SageMaker y AI](./07-AI-Machine-Learning/SageMaker_y_AI/)

**Conceptos clave:** SageMaker, model training, AutoML, deployment, inference

---

## 🎓 Ruta de Aprendizaje Recomendada

### Nivel Principiante
1. **00-Cloud-Fundamentals** - Entender conceptos básicos de AWS
2. **01-Networking-VPC** - Fundamentos de redes
3. **06-Python-Fundamentals** - Scripting y automatización

### Nivel Intermedio
4. **02-Compute-EC2** - Computación y escalado
5. **03-Storage-S3** - Almacenamiento de datos
6. **04-Security-IAM** - Seguridad y cumplimiento

### Nivel Avanzado
7. **05-Databases-RDS** - Bases de datos en producción
8. **07-AI-Machine-Learning** - Machine Learning con SageMaker

---

## 📊 Estadísticas del Repositorio

| Métrica | Valor |
|---------|-------|
| **Módulos Principales** | 8 |
| **Submódulos** | 16 |
| **Laboratorios Totales** | 60+ |
| **Líneas de Documentación** | 5000+ |
| **Temas Cubiertos** | 30+ |

---

## 🛠️ Requisitos Previos

### Software
- Git (para clonar el repositorio)
- Cuenta de AWS (gratuita o paga)
- Navegador web moderno (Chrome, Firefox, Safari, Edge)

### Conocimiento Recomendado
- Conceptos básicos de cloud computing
- Familiaridad con línea de comandos (bash/PowerShell)
- Nociones de redes básicas
- Python 3.7+ (para módulos avanzados)

### Configuración de AWS CLI
```bash
# Instalar AWS CLI
pip install awscli

# Configurar credenciales
aws configure
# Ingresar Access Key ID
# Ingresar Secret Access Key
# Ingresar región por defecto (ej: us-east-1)
# Ingresar formato de salida (json)
```

---

## 🚀 Empezar Rápido

### 1. Clonar el Repositorio
```bash
git clone https://github.com/KorbenDallas007/aws-restart-portfolio.git
cd aws-restart-portfolio
```

### 2. Elegir un Módulo
Navega a cualquier carpeta de módulo:
```bash
cd 00-Cloud-Fundamentals
cat README.md  # Lee la documentación
```

### 3. Seguir los Laboratorios
Cada submódulo tiene un `README.md` con:
- Objetivos de aprendizaje
- Laboratorios numerados
- Instrucciones paso a paso
- Mejores prácticas

---

## 💡 Mejores Prácticas Generales

### Seguridad
✅ Nunca commites credenciales AWS en Git  
✅ Usa AWS Secrets Manager para producción  
✅ Implementa MFA en tu cuenta AWS  
✅ Revisa regularmente CloudTrail logs  
✅ Usa principio de menor privilegio (IAM)  

### Costos
✅ Monitorea costos con AWS Cost Explorer  
✅ Usa presupuestos y alertas de costos  
✅ Detiene instancias EC2 cuando no las uses  
✅ Implementa políticas de retención para S3  
✅ Usa Reserved Instances para cargas predecibles  

### Operaciones
✅ Documenta tu infraestructura  
✅ Usa Infrastructure as Code (CloudFormation/Terraform)  
✅ Implementa logging y monitoreo  
✅ Automatiza tareas repetitivas  
✅ Realiza backups regulares  

### Desarrollo
✅ Usa diferentes ambientes (dev, test, prod)  
✅ Implementa CI/CD pipelines  
✅ Realiza testing exhaustivo  
✅ Versionea tu código  
✅ Documenta cambios en commits  

---

## 📖 Recursos Oficiales

- [AWS Documentation](https://docs.aws.amazon.com/)
- [AWS Tutorials](https://aws.amazon.com/tutorials/)
- [AWS Training and Certification](https://aws.amazon.com/training/)
- [AWS Restart Program](https://aws.amazon.com/restart/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)

---

## 🎯 Certificaciones Relacionadas

Este portfolio te prepara para:

- **AWS Certified Cloud Practitioner** ☁️
- **AWS Certified Solutions Architect - Associate**
- **AWS Certified Developer - Associate**
- **AWS Certified SysOps Administrator - Associate**
- **AWS Certified Machine Learning - Specialty**

---

## 📝 Cómo Usar Este Repositorio

### Para Aprender
1. Selecciona el módulo que quieres estudiar
2. Lee el README del módulo para contexto
3. Sigue los laboratorios paso a paso
4. Toma notas y experimenta
5. Completa los desafíos propuestos

### Para Compartir Conocimiento
1. Crea un fork del repositorio
2. Agrega tus laboratorios o mejoras
3. Envia un pull request con descripción clara
4. Participa en discusiones y code reviews

### Para Colaborar
- **Issues:** Reporta errores o sugiere mejoras
- **Discussions:** Comparte experiencias y preguntas
- **Pull Requests:** Contribuye con código y documentación

---

## 🔧 Estructura de Archivos

```
aws-restart-portfolio/
├── README.md                          # Este archivo
├── push_labs.ps1                      # Script para automatizar tareas
├── 00-Cloud-Fundamentals/             # Módulo 00
│   ├── README.md                      # Guía del módulo
│   ├── Automatizacion_SSM/
│   ├── CLI_y_SysOps/
│   ├── CloudFormation/
│   └── Costos_y_Etiquetas/
├── 01-Networking-VPC/                 # Módulo 01
│   ├── README.md
│   ├── Conceptos_Redes/
│   └── Configuracion_VPC/
├── 02-Compute-EC2/                    # Módulo 02
│   ├── README.md
│   ├── Escalado_y_Balanceo/
│   ├── Fundamentos_Linux_y_EC2/
│   ├── Serverless_y_Contenedores/
│   └── Servidores/
├── 03-Storage-S3/                     # Módulo 03
│   ├── README.md
│   └── Almacenamiento_y_Archivado/
├── 04-Security-IAM/                   # Módulo 04
│   ├── README.md
│   ├── Seguridad_e_IAM/
│   └── Monitoreo_y_CloudTrail/
├── 05-Databases-RDS/                  # Módulo 05
│   ├── README.md
│   ├── Fundamentos_DB_y_RDS/
│   └── Migracion_y_Servicios/
├── 06-Python-Fundamentals/            # Módulo 06
│   ├── README.md
│   ├── Laboratorios_Base/
│   └── Ejercicios_Adicionales/
└── 07-AI-Machine-Learning/            # Módulo 07
    ├── README.md
    └── SageMaker_y_AI/
```

---

## ⚠️ Notas Importantes

### Limpieza de Recursos
Después de completar cada laboratorio:
1. Elimina instancias EC2 innecesarias
2. Vacía y elimina buckets S3 de prueba
3. Detén bases de datos RDS
4. Limpia grupos de seguridad

Esto evita cargos inesperados en tu cuenta AWS.

### Costo Estimado
- Los laboratorios pueden generar cargos si no se usan recursos de capa gratuita
- AWS ofrece 12 meses de capa gratuita para nuevas cuentas
- Usa alertas de costos para monitorar gastos

---

## 🤝 Contribuir

### Reportar Errores
Si encuentras errores o información desactualizada:
1. Abre una **Issue** describiendo el problema
2. Incluye la versión o fecha del lab
3. Sugiere una solución si es posible

### Contribuciones
Las contribuciones son bienvenidas:
1. Fork el repositorio
2. Crea una rama feature (`git checkout -b feature/mejora`)
3. Commit tus cambios (`git commit -m 'Agrega mejora'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo licencia **MIT**. Siéntete libre de usar el contenido para aprender y enseñar.

---

## 👨‍💼 Autor

**Portfolio creado como parte del programa AWS Restart**

Repositorio mantenido y actualizado regularmente.

---

## 📞 Soporte y Contacto

- **Problemas técnicos:** Abre una Issue en el repositorio
- **Preguntas generales:** Inicia una Discussion
- **Sugerencias:** Contacta a través de Issues o Pull Requests

---

## 🎉 Agradecimientos

Gracias a:
- AWS Restart Program por la iniciativa educativa
- Comunidad AWS por el soporte y feedback
- Todos los contribuidores que mejoran este repositorio

---

## 📈 Progreso de Aprendizaje

Marca tu progreso conforme completes cada módulo:

- [ ] 00 - Cloud Fundamentals
- [ ] 01 - Networking VPC
- [ ] 02 - Compute EC2
- [ ] 03 - Storage S3
- [ ] 04 - Security IAM
- [ ] 05 - Databases RDS
- [ ] 06 - Python Fundamentals
- [ ] 07 - AI Machine Learning

---

**Última actualización:** Junio 2026

**Síguenos:** [GitHub](https://github.com/KorbenDallas007/aws-restart-portfolio) | [AWS Documentation](https://docs.aws.amazon.com/)

¡Happy Learning! 🚀
