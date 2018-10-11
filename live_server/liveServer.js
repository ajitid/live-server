var ws = new WebSocket( // eslint-disable-line
  'ws://' + window.location.host +
  '/ws/live-server')

ws.onopen = e => {
  // console.log('connected')
}

ws.onmessage = function (msg) {
  // console.log(msg.data)
  window.location.reload()
}

ws.onclose = function (e) {
  console.error('Connection to Live Server got closed.')
  console.warn('Please restart Live Server and reload this page.')
}
