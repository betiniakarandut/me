import { sendContactMessage } from "../api/portfolioService";

export function renderContactSection() {
  return `
    <section class="card">
      <h2>Contact</h2>
      <form id="contact-form" class="contact-form">
        <label>
          Name
          <input type="text" name="name" required minlength="2" />
        </label>
        <label>
          Email
          <input type="email" name="email" required />
        </label>
        <label>
          Subject
          <input type="text" name="subject" required minlength="3" />
        </label>
        <label>
          Message
          <textarea name="message" required minlength="10" rows="4"></textarea>
        </label>
        <button class="radio-toggle submit-btn" type="submit">
          <span class="radio-icon" aria-hidden="true"></span>
          <span class="radio-text">Send Message</span>
        </button>
        <p id="contact-feedback" class="muted form-feedback"></p>
      </form>
    </section>
  `;
}

export function setupContactForm() {
  const form = document.querySelector("#contact-form");
  const feedback = document.querySelector("#contact-feedback");
  if (!form || !feedback) return;

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    feedback.textContent = "Sending...";

    const formData = new FormData(form);
    const payload = {
      name: String(formData.get("name") || "").trim(),
      email: String(formData.get("email") || "").trim(),
      subject: String(formData.get("subject") || "").trim(),
      message: String(formData.get("message") || "").trim(),
    };

    try {
      await sendContactMessage(payload);
      feedback.textContent = "Message sent successfully. Thank you!";
      form.reset();
    } catch {
      feedback.textContent = "Could not send message right now. Please try again shortly.";
    }
  });
}
