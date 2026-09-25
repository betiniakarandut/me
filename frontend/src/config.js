const DEFAULT_API_BASE_URL = import.meta.env.PROD
  ? "https://api.betiniakarandut.com/api/v1"
  : "http://127.0.0.1:8000/api/v1";

export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || DEFAULT_API_BASE_URL;
export const READABILITY_STORAGE_KEY = "betini-readability-mode";
export const SITE_URL = "https://betiniakarandut.com";
