import { API_BASE_URL } from "../config";

async function request(path, options = {}) {
  const response = await fetch(`${API_BASE_URL}${path}`, options);
  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }
  return response.json();
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
  return request(path, {
    ...options,
  });
}
