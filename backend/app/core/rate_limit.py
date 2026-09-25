import threading
import time
from collections import deque


class SlidingWindowRateLimiter:
    """In-memory sliding-window limiter.

    Adequate for a single-process API (the portfolio runs one uvicorn worker).
    State resets on restart, which is acceptable for spam protection.
    """

    def __init__(self, per_client: int, global_limit: int, window_seconds: int) -> None:
        self.per_client = per_client
        self.global_limit = global_limit
        self.window_seconds = window_seconds
        self._clients: dict[str, deque[float]] = {}
        self._global: deque[float] = deque()
        self._lock = threading.Lock()

    def _prune(self, bucket: deque[float], now: float) -> None:
        cutoff = now - self.window_seconds
        while bucket and bucket[0] <= cutoff:
            bucket.popleft()

    def allow(self, client_id: str) -> bool:
        now = time.monotonic()
        with self._lock:
            self._prune(self._global, now)
            bucket = self._clients.setdefault(client_id, deque())
            self._prune(bucket, now)
            if len(bucket) >= self.per_client or len(self._global) >= self.global_limit:
                return False
            bucket.append(now)
            self._global.append(now)
            # Drop idle clients so the map cannot grow without bound.
            if len(self._clients) > 5000:
                for key, entries in list(self._clients.items()):
                    self._prune(entries, now)
                    if not entries:
                        del self._clients[key]
            return True

    def reset(self) -> None:
        with self._lock:
            self._clients.clear()
            self._global.clear()
