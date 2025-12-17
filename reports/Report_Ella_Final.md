# FIELD TRIP REPORT TO KORLEBU TEACHING HOSPITAL.

FOR THE PROGRAMME OF STUDY OF BSc COMPUTER SCIENCE (CYBERSECURITY OPTION)
OF THE COMPUTER SCIENCE DEPARTMENT
OF GHANA COMMUNICATION TECHNOLOGY UNIVERSITY
BY
INDEX NO: 1704895585
NAME: EMMANNUELLA NANA AMA WEIR

LECTURER: DR. MARTIN MABEIFAM UJAKPA.
NOVEMBER 2025.

Abstract
This report documents a field trip to Korle‑Bu Teaching Hospital carried out as part of the BSc Computer Science (Cybersecurity option) programme. The primary objective was to observe and analyse the hospital's IT/Health Information Systems operations, identify operational and cybersecurity challenges, and propose a practicable, computerised procurement automation solution to reduce delays and improve auditability. The study used direct observation, interviews with IT personnel, and a brief review of operational workflows. Findings show that delays in procurement, manual approval bottlenecks, and limited interoperability with hospital systems reduce operational efficiency and can impact patient care. The proposed solution is a secure procurement automation platform (production design: Node.js + Vue + MongoDB with FHIR integration; classroom demo: Flask + SQLite) that prioritises role‑based access, audit trails, encryption, and staged deployment. The report includes system specifications, development and testing plans, and recommendations for pilot rollout and future enhancements.

Table Of Contents
1.1. INTRODUCTION	1
1.2 INDUSTRY: Health	1
1.3 COMPANY: Korle-bu Teaching Hospital	2
1.3.1 DEPARTMENT: It/Health Information Systems	2
1.4 Operations, Activities and Resources	2
1.5 Operational Effectiveness and Efficiencies of Korle-bu	3
1.5.1 CHALLENGES	3
1.5.2.  ANALYSIS	4
1.5.3 PROPOSED SOLUTION	4
1.5.4 EXPECTED BENEFITS.	4
1.6 Proposed Solution Specifications and Design	4
1.6.1 Agile Methodology	4
1.6.2 Requirement Analysis	5
1.6.2.1 Functional Requirements	5
1.6.2.2 Non-functional Requirements	5
1.6.2.3 Hardware Requirements	6
1.6.2.4 Software Requirements	6
1.6.2.5 Sprints and Iterations	6
1.6.2.6 User Stories	6
1.6.2.7 Continuous Integration and Testing	7
1.6.2.8 Adaptability to Change	7
1.6.3 System Design	7
1.6.3.1 System Architecture Diagram	7
1.6.3.2 Use Case Diagram	8
1.6.3.3 Sequence Diagram	9
1.6.3.4 User Interface Design	9
1.7. Proposed solution Development	12
1.7.1 Development Technology and Tools Specifications	12
1.7.1.1 Software including Programming Language, IDE and runtime	12
1.7.1.2 Hardware (development/runtime)	13
1.7.2 Implementation details, Network specs and developed code	13
1.7.2.1 Network specifications	13
1.7.2.2 Developed solution and associated code	14
1.8 SYSTEM TESTING	15
1.8.1 Unit Test	15
1.8.2 Integration Testing	15
1.8.3 System Testing	16
References	17

1.1. INTRODUCTION
Field trips form an essential component to experiential learning within computing and cyber security. They provide students with the opportunity to observe how organizations operate in the real world, how technological processes are implemented, and how cyber security principles are applied within practical work environments. For students pursuing a Bachelor of Science in Cyber security, these visits bridge the gap between theoretical course work and industry practices, fostering a deeper understanding of organizational systems, digital operations and security challenges.

The purpose of this field trip exercise is to explore the structure, operations, and technological frameworks of a selected firm in the Health Industry. By engaging directly with industry professionals and observing active technological systems, the exercise helps to highlight how organizations deploy, secure and maintain their digital infrastructure. More importantly, it enables the identification of operational challenges and cyber security vulnerabilities.

This report focuses on KORLE-BU TEACHING HOSPITAL and specifically examines its Information Security and Infrastructure / IT Department. The content presented is based on observations made during the field visit, interactions with technical personnel, and an assessment of the hospital's operational structure and security practices. The report provides an overview of the industry, the firm, and the department understudy, leading to a detailed analysis of challenges observed and proposed solutions aligned with cyber security best practices.

1.2 INDUSTRY: Health
The health industry in Ghana comprises public, private, and faith-based institutions that collectively deliver essential medical services to the population. This sector plays vital roles such as disease prevention, diagnosis, treatment, emergency response, maternal and child healthcare, and control of public health threats. In addition, health institutions are responsible for the management of patient information, including the accurate collection, storage, and protection of medical records and health data. Effective data handling supports clinical decision-making, improves service delivery, ensures continuity of care, and helps facilities meet regulatory standards for confidentiality and data security. Overall, the health industry remains central to safeguarding public health while maintaining reliable health information systems that support national development.

1.3 COMPANY: Korle-bu Teaching Hospital
Korle-bu Teaching Hospital is Ghana's largest and premier referral hospital, located in Accra. Established in 1923, it serves as the main teaching hospital for the University of Ghana Medical School and plays a central role in training doctors, nurses, and other health professionals. As a tertiary facility, it provides highly specialized services such as cardiothoracic surgery, renal dialysis, oncology, plastic surgery, and advanced diagnostic care. The hospital also manages a large volume of patient information, ensuring proper handling of medical records for accurate diagnosis, continuity of care, and compliance with data protection standards. Korle-Bu remains a key pillar in Ghana's health system, offering advanced medical care, supporting medical research, and contributing significantly to national healthcare development.

1.3.1 DEPARTMENT: IT/Health Information Systems
The IT/Health Information Systems Department is responsible for managing the hospital's technological infrastructure and ensuring the smooth flow of digital information across all units. Their core role is to support clinical and administrative operations by maintaining computer systems, networks, hospital software, and electronic health record platforms. This department ensures that patient data is accurately captured, securely stored, and readily accessible to authorized healthcare professionals. They also implement cyber security measures to protect sensitive health information from breaches, unauthorized access, and data loss. Additionally, the department supports digital services such as telemedicine, diagnostic imaging systems, data analytics, and internal communication platforms. Overall, the IT/Health Information Systems Department plays a vital role in improving efficiency, enhancing patient care, and ensuring compliance with data protection regulations.

1.4 Operations, Activities and Resources
Korle-bu Teaching Hospital operates as Ghana's premier tertiary referral and teaching facility, providing advanced clinical care, medical training, and research services to support the country's health system. Some operations include specialized diagnostics, surgical procedures, maternal and child healthcare, emergency services, and the treatment of complex medical conditions referred from across the nation. It undertakes key activities such as clinical service delivery, professional training for medical and allied health students, medical research, and comprehensive health information management, which involves the secure handling of patient data and the use of digital health systems to support accurate decision-making. Korle-bu's resources include a highly skilled workforce of medical specialists, nurses, pharmacists, laboratory professionals, and IT personnel, supported by modern physical and technological assets such as specialized centers, advanced diagnostic equipment, operating theatres, and electronic health record systems. These combined operations, activities, and resources enable the hospital to deliver high-quality healthcare while fulfilling its mandate as a national center of excellence.

1.5 Operational Effectiveness and Efficiencies of Korle-bu
During my field trip to Korle Bu Teaching Hospital, it became evident that the facility demonstrates strong operational effectiveness and efficiency through its well-coordinated clinical services, specialized units, and use of structured health management systems. The hospital's ability to provide advanced medical care is supported by skilled specialists, modern diagnostic equipment, and clearly defined clinical protocols that enhance the accuracy and quality of patient treatment. Efficiency is further improved by the integration of health information systems, which streamline the handling of patient records, reduce waiting times, and facilitate smooth communication across departments. Additionally, the hospital's commitment to continuous professional training, multidisciplinary teamwork, and the organized use of its physical and technological resources contributes to timely service delivery and improved patient outcomes.

1.5.1 CHALLENGES
Korle-bu Teaching Hospital faces several challenges that affect its ability to operate at full efficiency. One of the major issues is the delay in procurement of devices. Delays in procuring medical devices can disrupt hospital operations by slowing down diagnosis, treatment, and essential procedures. Without timely equipment, staff may be forced to use outdated tools, leading to longer waiting times, reduced efficiency, and potential risks to patient safety. These delays can also increase congestion in departments and negatively affect overall healthcare delivery.

1.5.2 ANALYSIS
Delays in the procurement of medical devices often stem from slow approval processes, limited budgets, supplier issues, and poor coordination between hospital departments. These delays disrupt hospital operations by slowing diagnosis and treatment, increasing patient waiting times, and forcing staff to rely on outdated or inadequate equipment. As a result, overall efficiency and quality of care decline, and the hospital may incur higher costs due to emergency purchases or frequent repairs.

1.5.3 PROPOSED SOLUTION
A system to automate the manual procurement workflow for items.

1.5.4 EXPECTED BENEFITS
Automating the manual procurement process for hospital devices offers several important benefits. It speeds up the approval and ordering stages, reduces human errors, and provides clear tracking of requests in real time. Automation also improves communication between departments, enhances record-keeping for audits, and supports better budgeting. By streamlining workflows and preventing delays in obtaining essential equipment, the system ultimately improves operational efficiency and supports better patient care.

1.6 Proposed Solution Specifications and Design
The proposed solution is a digital procurement system designed to automate and streamline the process of acquiring medical and IT devices at Korle-bu Teaching Hospital. This system will replace the inefficient manual workflow, providing a transparent, efficient, and accountable platform for all procurement activities, from request initiation to final delivery and approval.

1.6.1 Agile Methodology
To ensure the successful development of the procurement automation system, the Agile methodology is selected as the most appropriate approach (Fowler, 2004). Agile is an iterative and flexible project management framework well-suited for developing solutions where requirements may evolve. Its core principles align perfectly with the need to deliver value quickly and adapt to feedback from hospital staff. This approach allows for the system to be developed in small, incremental cycles (sprints), facilitating the rapid delivery of functional components. Agile emphasizes continuous collaboration between the development team and key stakeholders, and this feedback process will be managed using tools like GitHub Projects, which provides Kanban boards to visualize sprint progress and track tasks transparently. The hospital's dynamic environment means that requirements may change, and the Agile approach allows for these adjustments to be incorporated throughout the development process (Sommerville, 2016).

1.6.2 Requirement Analysis
A thorough requirement analysis defines what the system must do (functional requirements) and the quality standards it must meet (non-functional requirements).

1.6.2.1 Functional Requirements
- Role-based access: Requesters (staff), Dept Heads, Procurement Officers, Admins.
- Submit procurement request with item details, quantity, justification.
- Review and approve/reject by Dept Head with comments.
- Procurement officer workflow: generate PO, manage suppliers, mark delivered.
- Status tracking and notifications for all actors.
- Audit trail and reporting.

1.6.2.2 Non-functional Requirements
- Security: encryption in transit and at rest; compliance with Ghana Data Protection Act (Act 843).
- Reliability: target uptime &gt; 99.9%, automated backups.
- Performance: UI interactions under 2 seconds.
- Usability: clear UI, minimal training.
- Scalability and maintainability.

1.6.2.3 Hardware Requirements
- Server: modern multicore CPU, 16 GB RAM minimum, 500 GB SSD (or cloud equivalent).
- Client: standard desktop/laptop/tablet with modern browser.

1.6.2.4 Software Requirements
- Linux server (Ubuntu), Nginx, Django/React (or chosen stack).
- PostgreSQL (or planned DB), Git, Docker for deployments.

1.6.2.5 Sprints and Iterations
- Four two-week sprints: auth + request submission; approvals + PO management; reporting + integrations; UAT + deployment.

1.6.2.6 User Stories
- As a nurse, submit request quickly.
- As Dept Head, view pending approvals dashboard.
- As Procurement Officer, generate and track POs.

1.6.2.7 Continuous Integration and Testing
- GitHub Actions: lint, unit tests, build on PRs.

1.6.2.8 Adaptability to Change
- Agile backlog management on GitHub; modular architecture to allow enhancements.

1.6.3 System Design
A three-tier architecture (Client, Application, Data) with secure integrations to hospital systems and strong auditability.

1.6.3.1 System Architecture Diagram
(Refer to diagrams/ella_system_architecture.mmd in repo)

1.6.3.2 Use Case Diagram
(Refer to diagrams/ella_use_case.mmd in repo)

1.6.3.3 Sequence Diagram
(Refer to diagrams/ella_sequence.mmd in repo)

1.6.3.4 User Interface Design
Clean, responsive, dashboard-centric UI for staff and approvers with clear status states and notifications.

1.7 Proposed solution Development
This section describes how the procurement automation system for Korle‑Bu will be developed, the tools and environments to be used, and the delivered code/artefacts. Ella's development emphasizes a JSON-first stack for easier interoperability (FHIR) and quick prototyping.

1.7.1 Development Technology and Tools Specifications

1.7.1.1 Software (programming language, IDE and runtime)
- Backend: Node.js (Express), or Python/Django if preferred by the hospital; in Ella's prototype the production design is Node.js.
- Frontend: Vue.js (v3) for a responsive SPA.
- Database: MongoDB for flexible schema (production) but the classroom demo uses SQLite for simplicity.
- Dev tools: VS Code, Docker Compose, npm/yarn.
- Security libs: Helmet, rate limiting, JWT/OAuth2 for auth.

1.7.1.2 Hardware (development and runtime)
- Dev machines: 8–16 GB RAM, SSD, Docker.
- Production: app servers (2+ vCPU, 8–16 GB RAM), MongoDB replica set (3 nodes recommended), load balancer (Nginx), secure backup storage.

1.7.2 Implementation details and delivered code

1.7.2.1 Network specifications
- VLAN segmentation, TLS everywhere, minimal open ports, mutual TLS or OAuth2 for HIS FHIR integration.
- Nginx or HAProxy for load balancing + health checks.

1.7.2.2 Developed solution and associated code
- Repository layout: backend/, frontend/, docker-compose.yml, infra/.
- Core behaviour: submit request -&gt; audit log -&gt; dept head approval -&gt; procurement PO -&gt; delivery confirmation.
- Audit middleware to persist non-repudiable logs.

1.8 SYSTEM TESTING

1.8.1 Unit Test
- Use Jest or Mocha for backend; Vue Test Utils + Jest for frontend.
- Test validation, controllers, and services with in-memory DB where possible.

1.8.2 Integration Testing
- Test whole flows against staging: ingest -&gt; approval -&gt; PO -&gt; delivery.
- Use test doubles for HIS (FHIR sandbox) and SMTP.

1.8.3 System Testing
- UAT with pilot staff, performance/load testing (k6/JMeter), security testing (SAST/DAST), resilience and backup/restore exercises.

References
Fowler, M. (2004) UML Distilled: A Brief Guide to the Standard Object Modeling Language. 3rd edn. Boston: Addison-Wesley Professional.
Fowler, M. (2006) Continuous Integration. Available at: https://martinfowler.com/articles/continuousIntegration.html (Accessed: 5 December 2025).
Government of Ghana (2012) Data Protection Act, 2012 (Act 843). Accra: Ghana Publishing Company.
Nielsen, J. (1994) 10 Usability Heuristics for User Interface Design. Available at: https://www.nngroup.com/articles/ten-usability-heuristics/ (Accessed: 5 December 2025).
Sommerville, I. (2016) Software Engineering. 10th edn. Harlow: Pearson Education.

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
UI is clean, responsive, and role‑aware. Dashboard for Staff shows "Create New Request" and a table of recent requests with status badges. Department Head dashboard lists pending approvals with quick actions. Procurement dashboard shows approved requests, supplier search, PO generation, and delivery status updates. UI guidelines follow Nielsen's heuristics: visibility of system status, consistency, error prevention, and minimal cognitive load.

1.7. Proposed Solution Development

This section outlines development planning, repository strategy, deployment, and deliverables.

Project repository will be hosted on GitHub under a private organization/repo named korlebu/procurement-system. Branching strategy: main (protected), develop (integration), feature/* (feature branches), hotfix/*. Pull Requests will require at least one reviewer and passing CI checks.

1.7.1. Development Technology and Tools Specifications

1.7.1.1. Software including Programming Language, IDE and those that the solution would run on  
Programming languages: Python (backend), JavaScript/TypeScript (frontend). Frameworks: Django (REST APIs), Django REST Framework, React (frontend). Database: PostgreSQL. Containerization: Docker. CI/CD: GitHub Actions. Web server: Nginx. Development IDEs: Visual Studio Code, PyCharm. Tools: Postman for API testing, Git for version control, Node.js and npm/yarn for frontend builds. The application will run on Linux servers (Ubuntu Server LTS) and be accessible via modern browsers (Chrome, Edge, Firefox).

1.7.1.2. Hardware (for development and for system runtime)  
Development: Developer laptops with at least 8 cores, 16 GB RAM, 256+ GB SSD; local Docker for dev. Test/staging server: 4 vCPU, 8–16 GB RAM, 200 GB SSD. Production: App server(s) 8 vCPU, 32–64 GB RAM, 1–2 TB SSD; DB server: 4–8 vCPU, 16–32 GB RAM with fast disk I/O; optional load balancer and HA pair for DB, backup storage for nightly backups.

1.7.2. Network and Security Specifications

1.7.2.1. Network specifications  
The system will be deployed inside a secured hospital network. Recommended network specifications: separate VLAN for application servers, DMZ for public facing reverse proxy (if needed), firewall rules to allow only required ports (HTTPS 443 to Nginx, SSH 22 restricted to admin IP ranges, PostgreSQL port 5432 restricted to app servers). SSL/TLS must be enforced (Let's Encrypt or enterprise CA). Use a reverse proxy/load balancer (Nginx/HAProxy) for TLS termination and to permit rolling deployments. Implement a VPN (IPsec/OpenVPN) for administrative access from offsite. IDS/IPS integration is recommended and logs forwarded to the SIEM.

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
    
    def __str__(self):
        return f"{self.item_name} - {self.status}"
```

Django REST API view (views.py):
```python
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ProcurementRequest
from .serializers import ProcurementRequestSerializer

class ProcurementRequestViewSet(viewsets.ModelViewSet):
    queryset = ProcurementRequest.objects.all()
    serializer_class = ProcurementRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Procurement Officer').exists():
            return ProcurementRequest.objects.all()
        return ProcurementRequest.objects.filter(requester=user)
    
    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        procurement_request = self.get_object()
        if request.user.groups.filter(name='Department Head').exists():
            procurement_request.status = 'APPROVED'
            procurement_request.save()
            # Send notification to procurement officer
            return Response({'status': 'approved'})
        return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
```

1.7.3. Deployment Strategy

Deployment will follow a staged approach: Development → Staging → Production. GitHub Actions will automate builds, run tests, and create Docker images. Staging deployments occur automatically on merges to develop branch for integration testing. Production deployments require manual approval and are triggered from tagged releases on the main branch. Rolling deployments will be used to ensure zero downtime. Database migrations will be tested in staging before production execution.

1.8. Testing, Quality Assurance and Maintenance

1.8.1. Testing Strategy

Testing will be conducted at multiple levels to ensure quality and reliability:

**Unit Testing**: pytest will validate individual functions and methods. Target: >80% code coverage. Tests will be run automatically on every commit via GitHub Actions.

**Integration Testing**: Test interactions between components (API endpoints, database operations, authentication). Validate end-to-end workflows such as request submission, approval, and notification delivery.

**User Acceptance Testing (UAT)**: Conducted with actual hospital staff (department heads, procurement officers) in a staging environment. Feedback will be collected via structured forms and incorporated before production release.

**Security Testing**: Automated scans using tools like Bandit (Python security linter), OWASP ZAP for vulnerability scanning, and dependency checks via Dependabot. Penetration testing will be conducted by qualified cybersecurity professionals before production deployment.

**Performance Testing**: Load testing with tools like Locust to simulate concurrent users and ensure system meets performance requirements (<2s page load under normal load).

1.8.2. Quality Assurance

Code quality will be maintained through:
- **Code Reviews**: All pull requests require approval from at least one senior developer
- **Linting**: Automated checks using flake8 (Python) and ESLint (JavaScript)
- **Static Analysis**: SonarQube integration for code quality metrics and technical debt tracking
- **Documentation**: All functions, classes, and APIs must have docstrings/comments
- **Coding Standards**: Follow PEP 8 (Python) and Airbnb style guide (JavaScript)

1.8.3. Maintenance and Support

**Ongoing Maintenance**: Regular updates to dependencies, security patches, and bug fixes will be scheduled monthly. A maintenance window will be established for system updates with advance notification to users.

**Monitoring**: Production system will be monitored using Prometheus and Grafana for metrics (CPU, memory, response times) and ELK Stack for log aggregation and analysis. Alerts will be configured for critical issues.

**Backup and Recovery**: Daily automated backups of the database with retention for 30 days. Weekly full backups retained for 1 year. Disaster recovery plan includes procedures for system restoration, with target Recovery Time Objective (RTO) of 4 hours and Recovery Point Objective (RPO) of 1 hour.

**Support Model**: Tiered support structure:
- Level 1: Help desk for user queries and basic troubleshooting
- Level 2: IT department for system administration and configuration
- Level 3: Development team for bug fixes and enhancements

**Documentation**: Comprehensive documentation will be maintained including:
- User manuals for each role (staff, department heads, procurement officers)
- System administration guide for IT staff
- Developer documentation for code maintenance and extension
- API documentation using Swagger/OpenAPI specifications

1.8.4. Training and Change Management

Before system rollout, comprehensive training sessions will be conducted:
- Role-specific training workshops (2-3 hours per role)
- Hands-on practice sessions in staging environment
- Quick reference guides and video tutorials
- Train-the-trainer approach to ensure sustainability

Change management strategy includes:
- Phased rollout starting with pilot departments
- Parallel running of old and new systems for 2 weeks during transition
- Continuous feedback collection and rapid issue resolution
- Post-implementation review after 3 months

1.9. CONCLUSION

This field trip to Korle‑Bu Teaching Hospital provided valuable insights into the practical application of information technology and cybersecurity in a critical healthcare environment. The observed challenges—particularly in procurement workflow efficiency and security monitoring—highlight common issues faced by large institutions transitioning to digital operations.

The proposed procurement automation system addresses a significant operational pain point by reducing manual processes, improving transparency, and providing audit trails for compliance. By leveraging modern development practices including Agile methodology, GitHub-based version control and CI/CD, and containerized deployment, the solution demonstrates how contemporary software engineering principles can be applied to solve real-world healthcare administration challenges.

From a cybersecurity perspective, the analysis revealed the critical importance of centralized monitoring, proactive threat detection, and defense-in-depth strategies in healthcare settings where patient data confidentiality and system availability are paramount. The recommendations for SIEM integration, network segmentation, and security testing protocols align with industry best practices and regulatory requirements for healthcare information systems.

This experiential learning exercise successfully bridged academic coursework with industry practice, reinforcing key concepts in systems design, software development lifecycle, cybersecurity architecture, and project management. The skills and knowledge gained through direct observation and engagement with healthcare IT professionals will inform future academic work and professional practice in the field of cybersecurity.

The project demonstrates that effective digital transformation in healthcare requires not only technical solutions but also careful attention to user needs, change management, training, and ongoing support. Success depends on collaboration between IT professionals, clinical staff, and management to ensure systems are secure, reliable, and support the hospital's mission of delivering quality patient care.

REFERENCES

1. Ghana Ministry of Health. (2023). *National e-Health Strategy 2023-2027*. Accra: Ministry of Health.

2. Korle-Bu Teaching Hospital. (2024). *Annual Report 2023*. Retrieved from hospital administration.

3. Health Insurance Portability and Accountability Act (HIPAA). (1996). *45 CFR Parts 160, 162, and 164*. U.S. Department of Health & Human Services.

4. Fast Healthcare Interoperability Resources (FHIR). (2023). *FHIR R4 Specification*. HL7 International. https://www.hl7.org/fhir/

5. Django Software Foundation. (2024). *Django Documentation (v4.2)*. https://docs.djangoproject.com/

6. Open Web Application Security Project. (2021). *OWASP Top Ten Web Application Security Risks*. OWASP Foundation. https://owasp.org/www-project-top-ten/

7. National Institute of Standards and Technology. (2018). *Framework for Improving Critical Infrastructure Cybersecurity (Version 1.1)*. NIST. https://doi.org/10.6028/NIST.CSWP.04162018

8. International Organization for Standardization. (2013). *ISO/IEC 27001:2013 Information Security Management Systems*. ISO/IEC.

9. Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide*. Scrum.org.

10. Pressman, R. S., & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). McGraw-Hill Education.

11. Stallings, W., & Brown, L. (2018). *Computer Security: Principles and Practice* (4th ed.). Pearson Education.

12. Ghana Data Protection Commission. (2012). *Data Protection Act, 2012 (Act 843)*. Government of Ghana.

13. World Health Organization. (2021). *Global Strategy on Digital Health 2020-2025*. WHO Press.

14. GitHub, Inc. (2024). *GitHub Actions Documentation*. https://docs.github.com/en/actions

15. PostgreSQL Global Development Group. (2024). *PostgreSQL 13 Documentation*. https://www.postgresql.org/docs/13/

---
END OF REPORT
