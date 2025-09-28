import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
  stages: [
    { duration: '15s', target: 10 },
    { duration: '30s', target: 50 },
    { duration: '30s', target: 100 },
    { duration: '30s', target: 200 },
    { duration: '30s', target: 0 },
  ],
  thresholds: {
    'http_req_duration': ['p(95)<1000'], // 95% < 1s
    'http_req_failed': ['rate<0.01'], // <1% errors
  },
};

const DEFAULT_TARGET = 'http://localhost:8000/';
const TARGET = __ENV.TARGET_URL || DEFAULT_TARGET;

export default function () {
  const res = http.get(TARGET);
  check(res, {
    'status is 200': (r) => r.status === 200,
  });
  sleep(1);
}
