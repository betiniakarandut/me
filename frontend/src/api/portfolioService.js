import { get, post } from "./httpClient";

// One function per endpoint so each page section can load and fail independently.
export const fetchProfile = () => get("/profile");
export const fetchJourney = () => get("/profile/journey");
export const fetchExperience = () => get("/experience");
export const fetchProjects = () => get("/projects");
export const fetchCredentials = () => get("/scholarships");
export const fetchSkills = () => get("/skills");
export const fetchArticles = () => get("/articles");
export const fetchGithubRepos = () => get("/github/repositories?limit=6");

export function sendContactMessage(payload) {
  return post("/contact", payload);
}
