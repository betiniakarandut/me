import { get, post } from "./httpClient";

export async function fetchPortfolioData() {
  try {
    await post("/articles/sync-hashnode");
  } catch {
    // Best effort sync; app should still render existing content.
  }

  const keys = [
    "profile",
    "journey",
    "experience",
    "scholarships",
    "projects",
    "skills",
    "articles",
    "githubRepos",
  ];

  const requests = [
    get("/profile"),
    get("/profile/journey"),
    get("/experience"),
    get("/scholarships"),
    get("/projects?featured=true"),
    get("/skills"),
    get("/articles"),
    get("/github/repositories?limit=6"),
  ];

  const settled = await Promise.allSettled(requests);
  const data = {};
  const errors = [];

  settled.forEach((result, index) => {
    const key = keys[index];
    if (result.status === "fulfilled") {
      data[key] = result.value;
      return;
    }
    data[key] = ["profile"].includes(key) ? null : [];
    errors.push(key);
  });

  return { data, errors };
}

export function sendContactMessage(payload) {
  return post("/contact", payload);
}
