import { renderContactSection } from "../components/contactForm";
import { renderReadabilityToolbar } from "../components/readabilityToolbar";
import {
  renderAboutSection,
  renderArticlesSection,
  renderCommunityServiceSection,
  renderCtaSection,
  renderExperienceSection,
  renderGithubSection,
  renderHeroSection,
  renderJourneySection,
  renderNavbar,
  renderProjectsSection,
  renderScholarshipsSection,
  renderSiteFooter,
  renderTopAlert,
} from "../components/sections";
import {
  renderArchitectureSection,
  renderDataSystemsSection,
  renderHighlightsSection,
  renderPhilosophySection,
  renderProductionEngineeringSection,
  renderSkillsSection,
  renderStatsStrip,
  renderTracTracCaseStudiesSection,
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
          ${renderTracTracCaseStudiesSection()}
          ${renderArchitectureSection()}
          ${renderProductionEngineeringSection()}
          <section id="journey-experience">
            ${renderExperienceSection(experience)}
          </section>
          ${renderDataSystemsSection()}
          ${renderArticlesSection(articles)}
          ${renderGithubSection(githubRepos)}
          ${renderPhilosophySection()}
          ${renderSkillsSection(skills)}
          ${renderJourneySection(journey)}
          ${renderCommunityServiceSection()}
          ${renderScholarshipsSection(scholarships)}
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
