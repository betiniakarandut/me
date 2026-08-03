import { renderContactSection } from "../components/contactForm";
import { renderReadabilityToolbar } from "../components/readabilityToolbar";
import {
  renderAboutSection,
  renderArticlesSection,
  renderChallengesSection,
  renderCtaSection,
  renderExperienceSection,
  renderGithubSection,
  renderHeroSection,
  renderJourneySection,
  renderNavbar,
  renderProjectsSection,
  renderScholarshipsSection,
  renderSiteFooter,
  renderPersonalLifeSection,
  renderTopAlert,
} from "../components/sections";
import {
  renderArchitectureSection,
  renderHighlightsSection,
  renderPerformanceCaseStudySection,
  renderPhilosophySection,
  renderProductionEngineeringSection,
  renderSkillsSection,
  renderStatsStrip,
} from "../components/engineeringSections";

export function renderHomePage(container, state) {
  const { data, errors } = state;
  const profile = data.profile;
  const journey = data.journey || [];
  const experience = data.experience || [];
  const scholarships = data.scholarships || [];
  const projects = data.projects || [];
  const skills = data.skills || [];
  const articles = data.articles || [];
  const githubRepos = data.githubRepos || [];

  container.innerHTML = `
    <main class="site-shell">
      <div class="app-layout">
        ${renderNavbar(profile)}
        <div class="content-column">
          ${renderTopAlert(errors)}
          ${renderReadabilityToolbar()}
          <section id="home">
            ${renderHeroSection(profile, skills)}
          </section>
          ${renderStatsStrip()}
          ${renderHighlightsSection()}
          ${renderAboutSection(profile)}
          ${renderProjectsSection(projects)}
          ${renderArchitectureSection()}
          ${renderProductionEngineeringSection()}
          ${renderPerformanceCaseStudySection()}
          <section id="journey-experience" class="stacked-section">
            ${renderJourneySection(journey)}
            ${renderExperienceSection(experience)}
          </section>
          ${renderPhilosophySection()}
          ${renderSkillsSection(skills)}
          ${renderChallengesSection()}
          ${renderPersonalLifeSection()}
          ${renderScholarshipsSection(scholarships)}
          ${renderArticlesSection(articles)}
          ${renderGithubSection(githubRepos)}
          ${renderCtaSection(profile)}
          <section id="contact">
            ${renderContactSection()}
          </section>
          ${renderSiteFooter(profile)}
        </div>
      </div>
    </main>
  `;
}
