import os

# Plan detallado por bloques (puedes ajustar los textos y recursos según tus necesidades)
plan = [
    # (inicio, fin, fase, objetivo, temas, recursos, quiz, lab, mini_proyecto)
    (1, 6, "Fundamentos Linux & Networking", "Profundizar en Fundamentos Linux & Networking",
     "Comandos básicos, estructura de archivos, permisos, usuarios, navegación CLI",
     [
         ("Linux Essentials - KodeKloud", "https://kodekloud.com/courses/linux-essentials/"),
         ("Linux Command Line - FreeCodeCamp", "https://www.freecodecamp.org/news/linux-command-line-beginners/"),
         ("GNU Bash Manual", "https://www.gnu.org/software/bash/manual/bash.html"),
     ],
     "https://www.freecodecamp.org/news/linux-command-line-quiz/",
     [
         "Ejecuta y documenta los comandos: pwd, ls -l, cd, mkdir, touch, cp, mv, rm, cat, less, head, tail",
         "Crea un usuario: sudo useradd devopsuser",
         "Cambia permisos: chmod 744 archivo.txt",
         "Cambia propietario: sudo chown devopsuser archivo.txt"
     ],
     [
         "Crea un script bash que automatice la creación de una estructura de carpetas y archivos para un proyecto ficticio."
     ]
    ),
    (7, 9, "Git, GitHub, Versionamiento", "Profundizar en Git, GitHub, Versionamiento",
     "Flujo Git, ramas, pull requests, colaboración, GitHub Actions básico",
     [
         ("Git Handbook - GitHub Docs", "https://docs.github.com/en/get-started/using-git"),
         ("Git & GitHub - FreeCodeCamp", "https://www.freecodecamp.org/news/git-and-github-for-beginners/"),
         ("GitHub Actions - Docs", "https://docs.github.com/en/actions"),
     ],
     "https://www.freecodecamp.org/news/git-quiz/",
     [
         "Clona un repositorio, crea ramas, realiza commits y pull requests.",
         "Configura un workflow básico de GitHub Actions."
     ],
     [
         "Crea un repositorio de portafolio y sube tus scripts y prácticas semanales."
     ]
    ),
    (10, 18, "Cloud - AWS (IAM, EC2, VPC, S3)", "Profundizar en Cloud - AWS (IAM, EC2, VPC, S3)",
     "IAM, EC2, VPC, S3, AWS CLI, automatización",
     [
         ("AWS Cloud Practitioner - FreeCodeCamp", "https://www.freecodecamp.org/news/aws-certified-cloud-practitioner/"),
         ("AWS CLI Docs", "https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html"),
         ("AWS Workshops", "https://workshops.aws/"),
     ],
     "https://kodekloud.com/courses/aws-cli/",
     [
         "Configura AWS CLI con un usuario IAM de práctica.",
         "Crea un bucket S3 y una instancia EC2 usando CLI.",
         "Crea un usuario IAM y asigna permisos mínimos."
     ],
     [
         "Automatiza la creación de una VPC, subred y EC2 usando Terraform."
     ]
    ),
    (19, 25, "Cloud - Azure (RBAC, VM, VNet, ACR)", "Profundizar en Cloud - Azure (RBAC, VM, VNet, ACR)",
     "Control de acceso, máquinas virtuales, redes, contenedores",
     [
         ("Microsoft Learn AZ-104", "https://learn.microsoft.com/en-us/certifications/exams/az-104/"),
         ("Azure CLI Docs", "https://learn.microsoft.com/en-us/cli/azure/"),
         ("Azure Quickstart Templates", "https://azure.microsoft.com/en-us/resources/templates/"),
     ],
     "https://www.freecodecamp.org/news/azure-quiz/",
     [
         "Crea un grupo de recursos y una VM usando Azure CLI.",
         "Configura RBAC para un usuario.",
         "Crea un contenedor en Azure Container Registry."
     ],
     [
         "Automatiza el despliegue de una VM y red usando Terraform en Azure."
     ]
    ),
    (26, 30, "Cloud - OCI (Tenancy, Compartments, Compute)", "Profundizar en Cloud - OCI (Tenancy, Compartments, Compute)",
     "Organización, compartimentos, cómputo, redes básicas",
     [
         ("OCI Getting Started", "https://docs.oracle.com/en-us/iaas/Content/GSG/Concepts/baremetalintro.htm"),
         ("OCI CLI Docs", "https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm"),
     ],
     "https://www.proprofs.com/quiz-school/story.php?title=oci-foundations",
     [
         "Crea un compartimento y una instancia de cómputo usando OCI CLI.",
         "Configura una red virtual cloud (VCN)."
     ],
     [
         "Automatiza el despliegue de una instancia y red en OCI usando Terraform."
     ]
    ),
    (31, 40, "Terraform - Fundamentos y Módulos", "Profundizar en Terraform - Fundamentos y Módulos",
     "Infraestructura como código, módulos, variables, estados, despliegue multicloud",
     [
         ("Terraform Getting Started", "https://developer.hashicorp.com/terraform/tutorials/aws-get-started"),
         ("Terraform Registry", "https://registry.terraform.io/"),
         ("Terraform for Beginners - KodeKloud", "https://kodekloud.com/courses/terraform-for-beginners/"),
     ],
     "https://kodekloud.com/courses/terraform-for-beginners/",
     [
         "Instala Terraform y configura tu primer archivo main.tf para crear un recurso cloud.",
         "Aplica y destruye la infraestructura con terraform init/plan/apply/destroy.",
         "Usa variables y outputs en tu configuración."
     ],
     [
         "Crea un módulo Terraform reutilizable para lanzar una instancia EC2 (o VM en Azure/OCI)."
     ]
    ),
    (41, 45, "CI/CD - GitHub Actions", "Profundizar en CI/CD - GitHub Actions",
     "Workflows, matrices, secrets, despliegue automatizado",
     [
         ("GitHub Actions Docs", "https://docs.github.com/en/actions"),
         ("GitHub Actions - FreeCodeCamp", "https://www.freecodecamp.org/news/github-actions-ci-cd-pipeline/"),
     ],
     "https://www.freecodecamp.org/news/github-actions-quiz/",
     [
         "Crea un workflow de CI/CD para compilar y testear un proyecto.",
         "Agrega secrets y variables de entorno.",
         "Despliega automáticamente a un entorno de pruebas."
     ],
     [
         "Automatiza el despliegue de una app simple usando GitHub Actions y Docker Hub."
     ]
    ),
    (46, 50, "CI/CD - Jenkins", "Profundizar en CI/CD - Jenkins",
     "Pipelines declarativos, integración con Docker y Git",
     [
         ("Jenkins User Documentation", "https://www.jenkins.io/doc/"),
         ("Jenkins Pipeline Tutorial", "https://www.jenkins.io/doc/book/pipeline/"),
         ("Jenkins + Docker - KodeKloud", "https://kodekloud.com/courses/jenkins/"),
     ],
     "https://www.proprofs.com/quiz-school/story.php?title=jenkins-quiz",
     [
         "Instala Jenkins en Docker.",
         "Crea un pipeline declarativo para compilar y testear un proyecto.",
         "Integra Jenkins con GitHub y Docker."
     ],
     [
         "Automatiza el build y push de una imagen Docker desde Jenkins."
     ]
    ),
    (51, 58, "Docker y Contenerización", "Profundizar en Docker y Contenerización",
     "Imágenes, Dockerfile, Compose, registro, buenas prácticas",
     [
         ("Docker Curriculum", "https://docker-curriculum.com/"),
         ("Docker Docs", "https://docs.docker.com/get-started/"),
         ("Docker for Beginners - KodeKloud", "https://kodekloud.com/courses/docker-for-beginners/"),
     ],
     "https://www.freecodecamp.org/news/docker-quiz/",
     [
         "Crea y ejecuta contenedores con Docker CLI.",
         "Construye una imagen personalizada con Dockerfile.",
         "Orquesta varios contenedores con Docker Compose."
     ],
     [
         "Publica una imagen en Docker Hub y documenta el proceso."
     ]
    ),
    (59, 70, "Kubernetes Core + Helm", "Profundizar en Kubernetes Core + Helm",
     "Pods, servicios, despliegues, ingress, Helm charts, upgrades",
     [
         ("Kubernetes by Example", "https://kubernetesbyexample.com/"),
         ("Kubernetes Docs", "https://kubernetes.io/docs/home/"),
         ("Helm Docs", "https://helm.sh/docs/"),
     ],
     "https://www.freecodecamp.org/news/kubernetes-quiz/",
     [
         "Despliega un pod y un deployment en Kubernetes usando YAML.",
         "Expón un servicio y configura un ingress.",
         "Instala y usa Helm para desplegar una app."
     ],
     [
         "Crea tu propio Helm chart y publícalo en un repositorio Git."
     ]
    ),
    (71, 78, "Observabilidad: Prometheus, Grafana, Loki", "Profundizar en Observabilidad: Prometheus, Grafana, Loki",
     "Métricas, logs, dashboards, alertas, monitoreo de clusters",
     [
         ("Prometheus Docs", "https://prometheus.io/docs/introduction/overview/"),
         ("Grafana Docs", "https://grafana.com/docs/"),
         ("Loki Docs", "https://grafana.com/docs/loki/latest/"),
     ],
     "https://www.proprofs.com/quiz-school/story.php?title=prometheus-quiz",
     [
         "Despliega Prometheus y Grafana en Kubernetes.",
         "Crea dashboards personalizados.",
         "Configura alertas básicas."
     ],
     [
         "Integra Loki para logs centralizados y crea un dashboard de logs."
     ]
    ),
    (79, 84, "Seguridad Cloud y CI/CD", "Profundizar en Seguridad Cloud y CI/CD",
     "IAM avanzado, escaneo de imágenes, secretos, políticas de seguridad",
     [
         ("AWS Security Best Practices", "https://aws.amazon.com/architecture/security-best-practices/"),
         ("Azure Security Documentation", "https://learn.microsoft.com/en-us/azure/security/"),
         ("Docker Security Cheat Sheet", "https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html"),
     ],
     "https://www.proprofs.com/quiz-school/story.php?title=cloud-security-quiz",
     [
         "Configura roles y políticas avanzadas en AWS/Azure.",
         "Escanea imágenes Docker con Trivy.",
         "Gestiona secretos con AWS Secrets Manager o Azure Key Vault."
     ],
     [
         "Implementa un pipeline CI/CD seguro con escaneo y control de secretos."
     ]
    ),
    (85, 88, "Testing Automatizado (unit, int, e2e)", "Profundizar en Testing Automatizado (unit, int, e2e)",
     "Pruebas unitarias, integración, extremo a extremo, pipelines de calidad",
     [
         ("Testing JavaScript - FreeCodeCamp", "https://www.freecodecamp.org/news/how-to-test-javascript-with-jest/"),
         ("Pytest Docs", "https://docs.pytest.org/en/7.1.x/"),
         ("Cypress Docs", "https://docs.cypress.io/guides/overview/why-cypress"),
     ],
     "https://www.proprofs.com/quiz-school/story.php?title=software-testing-quiz",
     [
         "Implementa pruebas unitarias y de integración en un proyecto.",
         "Integra pruebas en el pipeline CI/CD.",
         "Ejecuta pruebas e2e con Cypress o Selenium."
     ],
     [
         "Automatiza reportes de pruebas y cobertura en tu portafolio."
     ]
    ),
    (89, 104, "Proyecto Final + Publicación GitHub", "Profundizar en Proyecto Final + Publicación GitHub",
     "Diseño, despliegue, documentación, presentación, retroalimentación",
     [
         ("GitHub Docs", "https://docs.github.com/"),
         ("Markdown Guide", "https://www.markdownguide.org/"),
         ("Presentaciones Técnicas", "https://www.freecodecamp.org/news/how-to-give-technical-presentations/"),
     ],
     "https://www.proprofs.com/quiz-school/story.php?title=devops-final-quiz",
     [
         "Define el alcance y arquitectura de tu proyecto final.",
         "Despliega la solución usando IaC, CI/CD y contenedores.",
         "Documenta todo el proceso en tu portafolio GitHub."
     ],
     [
         "Presenta tu proyecto, recibe retroalimentación y publica el entregable final."
     ]
    ),
]

def get_block(week):
    for start, end, *rest in plan:
        if start <= week <= end:
            return (start, end, *rest)
    return None

def crear_archivos_semana(base_path, semana, bloque):
    start, end, fase, objetivo, temas, recursos, quiz, lab, mini_proyecto = bloque
    semana_path = os.path.join(base_path, f"semana-{semana:02d}")
    os.makedirs(semana_path, exist_ok=True)

    # resumen.md
    with open(os.path.join(semana_path, "resumen.md"), "w", encoding="utf-8") as f:
        f.write(f"# Semana {semana:02d} - Resumen\n\n")
        f.write(f"## Fase\n{fase}\n\n")
        f.write(f"## Objetivo\n{objetivo}\n\n")
        f.write(f"## Temas\n- {temas}\n\n")
        f.write("## Recursos recomendados\n")
        for nombre, url in recursos:
            f.write(f"- [{nombre}]({url})\n")

    # practicas.md
    with open(os.path.join(semana_path, "practicas.md"), "w", encoding="utf-8") as f:
        f.write("# Actividades prácticas\n\n")
        f.write("## Laboratorio\n\n")
        for l in lab:
            f.write(f"- [ ] {l}\n")
        f.write("\n## Mini-proyecto\n\n")
        for mp in mini_proyecto:
            f.write(f"- [ ] {mp}\n")
        f.write("\n## Checkpoint\n\n- [ ] ¿Dominas los conceptos y prácticas de esta semana?\n")
        f.write(f"\n## Quiz sugerido\n\n- [{quiz}]({quiz})\n")
        f.write("\n## Entregables\n\n- Evidencia en GitHub: scripts, capturas, README con reflexiones.\n")

    # retro.md
    with open(os.path.join(semana_path, "retro.md"), "w", encoding="utf-8") as f:
        f.write("# Retroalimentación y evaluación\n\n")
        f.write("## ✅ Checkpoint de progreso\n- ¿Dominas los comandos, prácticas y conceptos clave de esta semana?\n\n")
        f.write("## 📝 Quiz de repaso sugerido\n- [ ] Realiza el quiz sugerido y repasa conceptos clave.\n\n")
        f.write("## 🔁 Retrospectiva\n- ¿Qué funcionó bien?\n- ¿Qué mejorarías para la próxima semana?\n- ¿Qué dudas persisten?\n- ¿Cómo aplicarías lo aprendido en un entorno real?\n")

if __name__ == "__main__":
    base_path = os.path.join(os.getcwd(), "semanas")
    os.makedirs(base_path, exist_ok=True)
    for semana in range(1, 105):
        bloque = get_block(semana)
        if bloque:
            crear_archivos_semana(base_path, semana, bloque)
        else:
            # Si alguna semana no está cubierta, puedes personalizar aquí
            pass
    print("¡Carpetas y archivos generados!")