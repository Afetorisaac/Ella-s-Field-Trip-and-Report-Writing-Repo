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

Korle‑Bu Teaching Hospital is Ghana's largest referral hospital and principal teaching hospital for the University of Ghana Medical School. Established in 1923 and located in Accra, it provides highly specialized services including cardiothoracic surgery, dialysis, oncology, and advanced diagnostics. The hospital manages large volumes of patient data and supports research and training across multiple clinical disciplines.

1.3.1. DEPARTMENT: IT / HEALTH INFORMATION SYSTEMS DEPARTMENT

The IT/Health Information Systems Department manages the hospital's technology infrastructure and ensures the secure flow of digital information. Its responsibilities include maintaining networks, servers, clinical applications, electronic health record platforms, and implementing cybersecurity measures to protect patient data and hospital systems. The department also supports telemedicine, diagnostic imaging integration, data analytics, and internal communication platforms.

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
