import { sendContactMessage } from "../api/portfolioService";
import { EMAIL, RESUME_URL, SOCIAL_LINKS } from "../content/links";
import { escapeHtml } from "../utils/format";
import { renderSection } from "./ui";

const DIRECT_LINKS = SOCIAL_LINKS.filter((link) => ["linkedin", "github"].includes(link.key));

export function renderContactSection() {
  const body = `
    <div class="contact-grid">
      <div>
        <p class="muted">
          Open to backend, cloud and platform engineering roles, and to conversations about systems that
          have to work in the field.
        </p>
        <ul class="contact-links">
          <li><span class="label">Email</span><a href="mailto:${EMAIL}">${EMAIL}</a></li>
          ${DIRECT_LINKS.map(
            (link) =>
              `<li><span class="label">${escapeHtml(link.label)}</span><a href="${escapeHtml(link.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(link.url.replace(/^https:\/\/(www\.)?/, "").replace(/\/$/, ""))}</a></li>`
          ).join("")}
          <li><span class="label">Resume</span><a href="${RESUME_URL}" target="_blank" rel="noopener">resume.pdf</a></li>
        </ul>
      </div>
      <form id="contact-form" class="contact-form" novalidate>
        <label>
          Name
          <input type="text" name="name" required minlength="2" maxlength="80" autocomplete="name" />
        </label>
        <label>
          Email
          <input type="email" name="email" required autocomplete="email" />
        </label>
        <label>
          Subject
          <input type="text" name="subject" required minlength="3" maxlength="150" />
        </label>
        <label>
          Message
          <textarea name="message" required minlength="10" maxlength="2000" rows="5"></textarea>
        </label>
        <div class="hp-field" aria-hidden="true">
          <label>Website <input type="text" name="website" tabindex="-1" autocomplete="off" /></label>
        </div>
        <button class="button button-primary submit-btn" type="submit">Send message</button>
        <p id="contact-feedback" class="form-feedback" role="status" aria-live="polite"></p>
      </form>
    </div>
  `;
  return renderSection({ id: "contact", eyebrow: "Contact", title: "Get in touch", body });
}

function messageForError(error) {
  if (error?.status === 429) return "Too many messages from this connection. Please try again later, or email me directly.";
  if (error?.status === 422) return "Please check the fields: a valid email and a message of at least 10 characters.";
  return `Could not send right now. Please try again shortly, or email ${EMAIL}.`;
}

export function setupContactForm() {
  const form = document.querySelector("#contact-form");
  const feedback = document.querySelector("#contact-feedback");
  if (!form || !feedback) return;

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    const button = form.querySelector("button[type=submit]");
    const formData = new FormData(form);
    const payload = {
      name: String(formData.get("name") || "").trim(),
      email: String(formData.get("email") || "").trim(),
      subject: String(formData.get("subject") || "").trim(),
      message: String(formData.get("message") || "").trim(),
    };
    const honeypot = String(formData.get("website") || "");
    if (honeypot) payload.website = honeypot;

    button.disabled = true;
    feedback.textContent = "Sending…";
    try {
      await sendContactMessage(payload);
      feedback.textContent = "Message sent. Thank you, I'll reply by email.";
      form.reset();
    } catch (error) {
      feedback.textContent = messageForError(error);
    } finally {
      button.disabled = false;
    }
  });
}
