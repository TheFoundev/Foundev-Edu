'use strict';

const DEFAULT_HOST = '127.0.0.1';
const DEFAULT_PORT = 8765;

function readConfig(env = process.env) {
  const host = String(env.HOST || DEFAULT_HOST).trim();
  const port = Number(env.PORT || DEFAULT_PORT);
  const sensitivity = Number(env.SENSITIVITY || 1.5);
  const networkListener = !['127.0.0.1', 'localhost', '::1'].includes(host);

  if (!Number.isInteger(port) || port < 1 || port > 65535) {
    throw new Error('PORT must be an integer from 1 to 65535.');
  }
  if (!Number.isFinite(sensitivity) || sensitivity <= 0 || sensitivity > 10) {
    throw new Error('SENSITIVITY must be greater than 0 and no more than 10.');
  }
  if (networkListener && env.ALLOW_NETWORK_LISTEN !== 'true') {
    throw new Error('Binding beyond loopback requires ALLOW_NETWORK_LISTEN=true.');
  }

  return {
    host,
    port,
    sensitivity,
    networkListener,
    enableRealInput: env.ENABLE_REAL_INPUT === 'true',
  };
}

module.exports = { DEFAULT_HOST, DEFAULT_PORT, readConfig };
