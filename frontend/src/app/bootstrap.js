import { fetchPortfolioData } from "../api/portfolioService";
import { setupContactForm } from "../components/contactForm";
import { setupReadabilityToggle } from "../components/readabilityToolbar";
import { renderHomePage } from "./renderHomePage";

export async function bootstrapApp(container) {
  container.innerHTML = `
    <main class="site-shell">
      <section class="card">
        <h2>Loading portfolio...</h2>
        <p class="muted">Fetching live data from backend APIs.</p>
      </section>
    </main>
  `;

  const state = await fetchPortfolioData();
  renderHomePage(container, state);
  setupReadabilityToggle();
  setupContactForm();
}
