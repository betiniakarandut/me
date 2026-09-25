import { renderContactSection } from "../components/contactForm";
import {
  renderAboutShell,
  renderCredentialsShell,
  renderExperienceShell,
  renderStackShell,
  renderSystemsShell,
  renderWritingShell,
} from "../components/dataSections";
import { renderNavbar, renderSiteFooter, renderStatusBanner } from "../components/layout";
import {
  renderArchitectureSection,
  renderHeroSection,
  renderImpactSection,
  renderLeadershipSection,
  renderPrinciplesSection,
  renderProductionEngineeringSection,
  renderTracTracCaseStudy,
} from "../components/narrativeSections";

/**
 * Renders the whole page shell synchronously. Static sections are complete;
 * API-backed sections contain `data-slot` placeholders filled by bootstrap.js.
 */
export function renderHomePage(container) {
  container.innerHTML = `
    <a class="skip-link" href="#main">Skip to content</a>
    <div class="site-shell">
      <div class="app-layout">
        ${renderNavbar()}
        <main id="main" class="content-column" tabindex="-1">
          ${renderStatusBanner()}
          ${renderHeroSection()}
          ${renderImpactSection()}
          ${renderSystemsShell()}
          ${renderTracTracCaseStudy()}
          ${renderArchitectureSection()}
          ${renderProductionEngineeringSection()}
          ${renderLeadershipSection()}
          ${renderExperienceShell()}
          ${renderStackShell()}
          ${renderWritingShell()}
          ${renderPrinciplesSection()}
          ${renderAboutShell()}
          ${renderCredentialsShell()}
          ${renderContactSection()}
          ${renderSiteFooter()}
        </main>
      </div>
    </div>
  `;
}
