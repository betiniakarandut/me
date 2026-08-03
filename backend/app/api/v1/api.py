from fastapi import APIRouter

from app.api.v1.endpoints import (
    articles,
    contact,
    experience,
    github,
    health,
    profile,
    projects,
    scholarships,
    skills,
)

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(profile.router, prefix="/profile", tags=["profile"])
api_router.include_router(experience.router, prefix="/experience", tags=["experience"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(articles.router, prefix="/articles", tags=["articles"])
api_router.include_router(scholarships.router, prefix="/scholarships", tags=["scholarships"])
api_router.include_router(skills.router, prefix="/skills", tags=["skills"])
api_router.include_router(contact.router, prefix="/contact", tags=["contact"])
api_router.include_router(github.router, prefix="/github", tags=["github"])

