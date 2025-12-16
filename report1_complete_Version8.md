FIELD TRIP REPORT TO KORLE-BU TEACHING HOSPITAL

FOR THE PROGRAMME OF STUDY OF BSc COMPUTER SCIENCE (CYBERSECURITY OPTION)  
OF THE COMPUTER SCIENCE DEPARTMENT  
OF GHANA COMMUNICATION TECHNOLOGY UNIVERSITY

BY  
INDEX NO: 1704895585  
NAME: EMMANUELLA NANA AMA WEIR

LECTURER: DR. MARTIN MABEIFAM UJAKPA.  
NOVEMBER 2025.

1.1. INTRODUCTION

Field trips form an essential component of experiential learning within computing and cybersecurity. They provide students with the opportunity to observe how organizations operate in the real world, how technological processes are implemented, and how cybersecurity principles are applied within practical work environments. For students pursuing a Bachelor of Science in Cybersecurity, these visits bridge the gap between theoretical coursework and industry practices, fostering a deeper understanding of organizational systems, digital operations, and security challenges.  
The purpose of this field trip is to explore the structure, operations, and technological frameworks of a selected firm in the Health Industry. By engaging directly with industry professionals and observing active technological systems, the exercise highlights how organizations deploy, secure, and maintain their digital infrastructure and enables identification of operational challenges and cybersecurity vulnerabilities.  
This report focuses on KORLE‑BU TEACHING HOSPITAL and specifically examines its IT/Health Information Systems Department. The content is based on observations during the field visit, interactions with technical personnel, and an assessment of the hospital's operational structure and security practices. It provides an overview of the industry, the firm, and the department under study, leading to a detailed analysis of observed challenges and proposed solutions aligned with cybersecurity best practices.

1.2. INDUSTRY: HEALTH

The health industry in Ghana comprises public, private, and faith‑based institutions that together deliver essential medical services. The sector is responsible for disease prevention, diagnosis, treatment, emergency response, maternal and child healthcare, and public health threat management. Health institutions manage patient information, ensuring accurate collection, storage, and protection of medical records and health data to support clinical decisions, continuity of care, and regulatory compliance.

1.3. COMPANY: KORLE‑BU TEACHING HOSPITAL

Korle‑Bu Teaching Hospital is Ghana’s largest referral hospital and principal teaching hospital for the University of Ghana Medical School. Established in 1923 and located in Accra, it provides highly specialized services including cardiothoracic surgery, dialysis, oncology, and advanced diagnostics. The hospital manages large volumes of patient data and supports research and training across multiple clinical disciplines.

1.3.1. DEPARTMENT: IT / HEALTH INFORMATION SYSTEMS DEPARTMENT

The IT/Health Information Systems Department manages the hospital’s technology infrastructure and ensures the secure flow of digital information. Its responsibilities include maintaining networks, servers, clinical applications, electronic health record platforms, and implementing cybersecurity measures to protect patient data and hospital systems. The department also supports telemedicine, diagnostic imaging integration, data analytics, and internal communication platforms.

1.4. Chosen Company Operations, Activities & Resources

Korle‑Bu operates as a tertiary referral and teaching facility delivering advanced clinical care, training and research. Core operations include specialized diagnostics, surgery, emergency services, maternal and child care, and complex case management. Activities include clinical service delivery, professional training, medical research, and health information management. Resources include skilled clinicians, nurses, lab professionals, IT staff, diagnostic equipment, operating theatres, and electronic health record systems.

1.5. Operational Effectiveness and Efficiencies of Korle‑Bu

Korle‑Bu demonstrates operational effectiveness through coordinated clinical services, specialized units, and structured health management systems. Integration of digital records reduces duplication and facilitates communication between departments. Continuous professional training and multidisciplinary teamwork contribute to timely service delivery and improved patient outcomes. Within the IT department, routine network management and system administration maintain critical services; however, gaps exist in proactive security monitoring and automation of some administrative workflows (notably procurement), which affect resilience and speed of response to incidents.

1.5.1. Challenges

The primary operational challenge observed is delays and inefficiencies in procurement workflows for medical and IT devices, which cause service disruptions when equipment is unavailable. In the IT/security context, a critical challenge is the lack of centralized, real‑time security monitoring (visibility) across network devices, servers, and clinical systems. This leads to a reactive security posture, slow incident detection and response, and increased risk of data breaches or ransomware impacts.

1.5.2. Analysis

Procurement delays stem from manual processes, paper approvals, and poor tracking; this increases downtime for critical equipment and slows clinical operations. The absence of a SIEM/centralized monitoring capability means logs are dispersed, staff rely on ad‑hoc checks, and correlation of events across systems is manual and slow. These weaknesses raise risk of undetected intrusions and non‑compliance with data protection requirements.

1.5.3. Proposed Solution

Implement a digital procurement automation system hosted on GitHub for development and workflow tracking, and implement a Security Information and Event Management (SIEM) solution for real‑time monitoring. This report focuses on completing the procurement system design (primary), with security monitoring integrated into operations planning and future work.

1.5.4. Expected Benefits

Automating procurement reduces approval lead times, eliminates manual errors, provides auditable trails for compliance, and improves asset availability. A SIEM improves security by enabling real‑time detection, faster incident response, centralized logging for audits, and improved operational resilience—together these solutions reduce downtime, improve patient care continuity, and strengthen regulatory compliance.

1.6. Proposed Solution Specifications and Design

This section defines the specifications and design for the procurement automation system (hosted and developed via GitHub) and outlines integration and development practices.

1.6.1. Agile Methodology

The project will follow Agile (Scrum) with two‑week sprints. GitHub Projects will manage sprints and backlog, GitHub Issues will capture user stories and tasks, and GitHub Actions will run CI pipelines. Frequent demos and stakeholder reviews will ensure the product meets hospital needs and adapts to feedback.

1.6.2. Requirement Analysis

1.6.2.1. Functional Requirements  
The system shall provide role‑based access (Staff, Department Head, Procurement Officer, Admin). Staff can create and submit procurement requests with item details, justification, and attachments. Department Heads can review, approve, or reject requests and provide comments. Procurement Officers can view approved requests, manage suppliers, generate purchase orders, and update delivery status. The system shall send automated notifications, provide request tracking, and produce audit/exportable reports.

1.6.2.2. Non‑functional Requirements  
Security: TLS for transport, encryption at rest, RBAC, and audit logging. Availability: >99.5% target with backups and recovery. Performance: page loads <2s under normal load. Usability: intuitive UI with minimal training. Maintainability: well‑documented code and version control. Scalability: support growth in users and requests.

1.6.2.3. Hardware Requirements  
Development: modern developer laptops (8+ cores recommended, 16+ GB RAM). Production: one or more servers (on‑premise or cloud): 8–16 vCPUs, 32–64 GB RAM, 1–2 TB SSD for app + logs; database server with 4–8 vCPUs, 16–32 GB RAM, fast I/O storage. Optionally use managed cloud DB for redundancy.

1.6.2.4. Software Requirements  
Backend: Python 3.10+, Django 4.x. Frontend: React 18+. Database: PostgreSQL 13+. Web server: Nginx. Containerization: Docker. CI/CD: GitHub Actions. Version control: Git hosted on GitHub (private repo). Testing: pytest, Jest, Cypress.

1.6.2.5. Sprints and Iterations  
Sprint 0: project setup, repo, environment, CI pipelines. Sprint 1: auth, user roles, DB models. Sprint 2: request submission UI & API. Sprint 3: approval workflows and notifications. Sprint 4: procurement dashboard and PO generation. Sprint 5: reporting, export, testing, and deployment. Further sprints: hardening, monitoring, feature enhancements.

1.6.2.6. User Stories  
"As a Staff member, I want to submit a procurement request so that I can request a device."  
"As a Department Head, I want to approve or reject requests so that I control departmental spending."  
"As a Procurement Officer, I want to generate purchase orders from approved requests so that procurement is fast and accurate."  
"As an Admin, I want to manage user accounts so that access is controlled."

1.6.2.7. Continuous Integration and Testing  
GitHub Actions will run unit tests, linting, and build checks on pull requests. Docker images will be built and pushed to a container registry on successful merges to main. Test coverage thresholds will be enforced and automatic notifications provided on failures.

1.6.2.8. Adaptability to Change  
Backlog items will be prioritized in GitHub Projects. New features or policy changes can be scheduled into upcoming sprints. The modular architecture (separated frontend, backend, and DB) supports incremental enhancements with limited disruption.

1.6.3. System Design

1.6.3.1. System Architecture  
Three‑tier architecture: Client (browser/desktop/tablet) → Web/Application (Nginx + Django app hosted on hospital server or cloud) → Data (PostgreSQL). Source code and CI/CD definitions are stored in a private GitHub repository. Deployment will use Docker containers orchestrated manually or via docker‑compose or Kubernetes for scale.

1.6.3.2. Use Case Diagram  
A system boundary contains use cases: Submit Request, View Request Status, Approve/Reject Request, Generate Purchase Order, Manage Suppliers, Manage Users, Generate Reports. Actors outside the boundary: Department Staff, Department Head, Procurement Officer, System Administrator.

1.6.3.3. Sequence Diagram  
Typical flow: Staff logs in → completes form → system validates → creates request in DB → system sends notification to Department Head → Head approves → system updates status and notifies Procurement Officer → Procurement Officer generates PO → procurement lifecycle continues (ordering, delivery, closing).

1.6.3.4. User Interface Design  
UI is clean, responsive, and role‑aware. Dashboard for Staff shows "Create New Request" and a table of recent requests with status badges. Department Head dashboard lists pending approvals with quick actions. Procurement dashboard shows approved requests, supplier search, PO generation, and delivery status updates. UI guidelines follow Nielsen’s heuristics: visibility of system status, consistency, error prevention, and minimal cognitive load.

1.7. Proposed Solution Development

This section outlines development planning, repository strategy, deployment, and deliverables.

Project repository will be hosted on GitHub under a private organization/repo named korlebu/procurement-system. Branching strategy: main (protected), develop (integration), feature/* (feature branches), hotfix/*. Pull Requests will require at least one reviewer and passing CI checks.

1.7.1. Development Technology and Tools Specifications

1.7.1.1. Software including Programming Language, IDE and those that the solution would run on  
Programming languages: Python (backend), JavaScript/TypeScript (frontend). Frameworks: Django (REST APIs), Django REST Framework, React (frontend). Database: PostgreSQL. Containerization: Docker. CI/CD: GitHub Actions. Web server: Nginx. Development IDEs: Visual Studio Code, PyCharm. Tools: Postman for API testing, Git for version control, Node.js and npm/yarn for frontend builds. The application will run on Linux servers (Ubuntu Server LTS) and be accessible via modern browsers (Chrome, Edge, Firefox).

1.7.1.2. Hardware (for development and for system runtime)  
Development: Developer laptops with at least 8 cores, 16 GB RAM, 256+ GB SSD; local Docker for dev. Test/staging server: 4 vCPU, 8–16 GB RAM, 200 GB SSD. Production: App server(s) 8 vCPU, 32–64 GB RAM, 1–2 TB SSD; DB server: 4–8 vCPU, 16–32 GB RAM with fast disk I/O; optional load balancer and HA pair for DB, backup storage for nightly backups.

1.7.2.1. Network specifications  
The system will be deployed inside a secured hospital network. Recommended network specifications: separate VLAN for application servers, DMZ for public facing reverse proxy (if needed), firewall rules to allow only required ports (HTTPS 443 to Nginx, SSH 22 restricted to admin IP ranges, PostgreSQL port 5432 restricted to app servers). SSL/TLS must be enforced (Let’s Encrypt or enterprise CA). Use a reverse proxy/load balancer (Nginx/HAProxy) for TLS termination and to permit rolling deployments. Implement a VPN (IPsec/OpenVPN) for administrative access from offsite. IDS/IPS integration is recommended and logs forwarded to the SIEM.

1.7.2.2. Developed solution and associated Code (examples)

Django model for procurement request (models.py):
```python
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ProcurementRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('ORDERED', 'Ordered'),
        ('DELIVERED', 'Delivered'),
    ]
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=128)
    item_name = models.CharField(max_length=256)
    quantity = models.PositiveIntegerField(default=1)
    justification = models.TextField()
    attachments = models.FileField(upload_to='attachments/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```