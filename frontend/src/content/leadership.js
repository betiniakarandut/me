// Technical leadership and programme delivery beyond writing code.

export const LEADERSHIP_INTRO =
  "My engineering work sits inside real operational environments. Increasingly I take responsibility beyond implementation: for how systems perform, how they are explained, and how the programmes around them are delivered.";

export const LEADERSHIP_ITEMS = [
  {
    kind: "Engineering leadership",
    title: "Offline-first field architecture",
    body: "Led the offline-first workflow for tractor and labour-saving-device requests at TracTrac, which replaced a paid third-party data-collection tool.",
    link: { href: "#tractrac-offline", label: "Read the case study" },
  },
  {
    kind: "Production engineering",
    title: "Dashboard performance investigation",
    body: "Diagnosed a dashboard screen issuing 60+ backend requests, redesigned it around caching, page-scoped fetching and server-side summaries, and documented the decision as an ADR.",
    link: { href: "#tractrac-incident", label: "Read the investigation" },
  },
  {
    kind: "Field enablement",
    title: "Training mechanisation service providers",
    body: "Provided field and technical support and trained MSPs in Nasarawa and Kaduna on the technology they use to serve smallholder farmers.",
  },
];

export const LEARNING_EVENT = {
  kind: "Technical communication",
  title: "“ISSAM: Two Years In” — Year 2 Learning Event explainer",
  body: "Contributed to the development and production of an approximately 14-minute documentary-style doodle explainer for the ISSAM Year 2 Learning Event. It translates the architecture, operating model and two years of evidence of a technology-enabled agricultural programme into a narrative for stakeholders who don't work with the systems day to day.",
  structure: ["Problem", "Programme", "Impact", "Horizon"],
  covered: [
    "The agricultural mechanisation problem",
    "ISSAM and the TracTrac + Mastercard Foundation partnership",
    "Mechanisation-as-a-service and the cooperative structure",
    "The technology and how it supports field operations",
    "Programme objectives and theory of change",
    "Field implementation and programme results",
    "Policy engagement and investment",
    "The 2029 horizon",
  ],
  format:
    "Whiteboard/doodle visuals, documentary narration, structured and timed scenes, and data visualisation of programme results.",
};

export const PITCH_CHALLENGE = {
  kind: "Programme leadership",
  title: "Young Innovators in Agricultural Mechanisation — ₦1 Million Pitch Challenge",
  role: "Lead, Young Innovators in Agricultural Mechanisation Pitch Challenge Team",
  context: "Part of the TracTrac Mechanization Investment Promotion Roadshow 2026.",
  summary:
    "Led the team responsible for designing and coordinating a youth-focused agricultural mechanisation pitch challenge.",
  theme: "Powering the Future of Agricultural Mechanisation in Nigeria through Young People.",
  question:
    "How can your business, idea or solution accelerate agricultural mechanisation for Nigerian smallholder farmers?",
  eligibility: [
    "Young Nigerians aged 18–35, as individuals or teams",
    "Early-stage ideas as well as existing businesses and MSPs",
    "Submission: a 1-minute video pitch and a pitch deck",
  ],
  process: [
    "Application",
    "Screening",
    "Shortlisting",
    "Finalist communication",
    "Pitch preparation",
    "Pitch deck",
    "Live pitch",
    "Judging",
    "Awards",
  ],
  scope: [
    "Challenge structure, application design, eligibility and requirements",
    "Finalist communications, briefings and event reminders",
    "Pitch-preparation webinar and pitch-deck guidance",
    "Judging structure and live-pitch preparation",
  ],
  prizes: [
    { value: "₦500,000", label: "1st place" },
    { value: "₦300,000", label: "2nd place" },
    { value: "₦200,000", label: "3rd place" },
  ],
  prizeNote: "₦1,000,000 prize pool for participants, shown as the programme's structure. It is not a personal award.",
};
