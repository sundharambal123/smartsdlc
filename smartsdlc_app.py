# Smart SDLC AI Project

# Language: Python

import random

class SmartSDLC_AI:
    def __init__(self, project_name, requirements):
        self.project_name = project_name
        self.requirements = requirements

    def requirement_analysis(self):
        return f"Requirements for {self.project_name}: {self.requirements}"

    def design_phase(self):
        designs = [
            "Use MVC architecture",
            "Adopt Microservices design",
            "Apply Layered Architecture",
            "Use Client-Server model"
        ]
        return f"Suggested Design: {random.choice(designs)}"

    def development_phase(self):
        tech_stacks = [
            "Python + Django + MySQL",
            "Java + Spring Boot + PostgreSQL",
            "Node.js + Express + MongoDB",
            "React + Flask + SQLite"
        ]
        return f"Suggested Tech Stack: {random.choice(tech_stacks)}"

    def testing_phase(self):
        tests = [
            "Unit Testing, Integration Testing, System Testing",
            "Automated Testing using Selenium or PyTest",
            "Performance & Security Testing"
        ]
        return f"Testing Plan: {random.choice(tests)}"

    def deployment_phase(self):
        deployments = [
            "Deploy on AWS Cloud",
            "Deploy on Google Cloud",
            "Deploy on Microsoft Azure",
            "Deploy on On-Premise Server"
        ]
        return f"Deployment Plan: {random.choice(deployments)}"

    def maintenance_phase(self):
        maintenance = [
            "Regular Bug Fixes & Updates",
            "System Monitoring with Prometheus",
            "User Feedback Collection",
            "Security Patching"
        ]
        return f"Maintenance Plan: {random.choice(maintenance)}"

    def run_sdlc(self):
        print("------ Smart SDLC AI Assistant ------")
        print(self.requirement_analysis())
        print(self.design_phase())
        print(self.development_phase())
        print(self.testing_phase())
        print(self.deployment_phase())
        print(self.maintenance_phase())


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    project = SmartSDLC_AI(
        project_name="EduTutor AI",
        requirements="An AI-based e-learning tutor that answers student questions and provides study materials."
    )
    project.run_sdlc()