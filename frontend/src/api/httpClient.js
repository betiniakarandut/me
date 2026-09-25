import { API_BASE_URL } from "../config";

const REQUEST_TIMEOUT_MS = 10000;

export class HttpError extends Error {
  constructor(message, status) {
    super(message);
    this.status = status;
  }
}

async function request(path, options = {}) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);
  try {
    const response = await fetch(`${API_BASE_URL}${path}`, { ...options, signal: controller.signal });
    if (!response.ok) {
      throw new HttpError(`Request failed: ${response.status}`, response.status);
    }
    return await response.json();
  } catch (error) {
    if (error.name === "AbortError") {
      throw new HttpError("Request timed out", 0);
    }
    throw error;
  } finally {
    clearTimeout(timer);
  }
}

export function get(path) {
  return request(path);
}

export function post(path, payload) {
  const options = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
  };
  if (payload !== undefined) {
    options.body = JSON.stringify(payload);
  }
  return request(path, options);
}
