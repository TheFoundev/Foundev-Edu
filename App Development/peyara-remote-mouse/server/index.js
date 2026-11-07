// The WebSocket relay of the Peyara remote-mouse app.
//
// It receives the JSON events of the phone and drives the local cursor when
// robotjs is installed. Without robotjs the events are only logged, so the
// protocol can still be seen working.
//
// The logic lives in relay.js, which has no dependency on ws or robotjs and
// is covered by the tests in server/test.
const { WebSocketServer } = require('ws');

const { createRelay } = require('./relay');
const { readConfig } = require('./config');

const config = readConfig();

let robot = null;
if (config.enableRealInput) {
  try {
    robot = require('robotjs');
    console.log('ENABLE_REAL_INPUT is on: relay events can control host input.');
  } catch {
    console.log('robotjs is unavailable: events will only be logged.');
  }
} else {
  console.log('Safe mode: events are logged; set ENABLE_REAL_INPUT=true to allow host input.');
}

const relay = createRelay({ robot, sensitivity: config.sensitivity });

const wss = new WebSocketServer({ port: config.port, host: config.host });

wss.on('connection', (socket) => {
  relay.onConnection();
  socket.send(JSON.stringify({ type: 'welcome', message: 'relay ready' }));

  socket.on('message', (raw) => {
    relay.handleMessage(raw);
  });

  socket.on('close', () => relay.onDisconnection());
});

console.log(`Peyara relay listening on ws://${config.host}:${config.port}`);
if (config.networkListener) {
  console.warn('Network binding is enabled without TLS or client authentication. Use an isolated trusted LAN only.');
}
