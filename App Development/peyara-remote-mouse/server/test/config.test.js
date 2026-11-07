'use strict';

const assert = require('node:assert/strict');
const test = require('node:test');
const { readConfig } = require('../config');

test('defaults to loopback with real input disabled', () => {
  assert.deepEqual(readConfig({}), {
    host: '127.0.0.1', port: 8765, sensitivity: 1.5,
    networkListener: false, enableRealInput: false,
  });
});

test('requires explicit acknowledgement before binding to the network', () => {
  assert.throws(() => readConfig({ HOST: '0.0.0.0' }), /ALLOW_NETWORK_LISTEN/);
  assert.equal(readConfig({ HOST: '0.0.0.0', ALLOW_NETWORK_LISTEN: 'true' }).networkListener, true);
});

test('validates the listening port and movement sensitivity', () => {
  assert.throws(() => readConfig({ PORT: '70000' }), /PORT/);
  assert.throws(() => readConfig({ SENSITIVITY: 'NaN' }), /SENSITIVITY/);
  assert.equal(readConfig({ PORT: '9000', SENSITIVITY: '2' }).port, 9000);
});

test('real desktop input requires a separate explicit opt-in', () => {
  assert.equal(readConfig({ ENABLE_REAL_INPUT: 'true' }).enableRealInput, true);
  assert.equal(readConfig({ ENABLE_REAL_INPUT: 'false' }).enableRealInput, false);
});
