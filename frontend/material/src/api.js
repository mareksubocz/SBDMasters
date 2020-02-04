var API_TIMEOUT = 5;

var API_HOST = 'http://0.0.0.0:8000/';
var API_POOL = {};

export function api_test(response) {
  console.log("--- START");
  console.log(response);
  console.log("--- END");
}

export function api_add_to_pull(callback, request_token, session_data) {
    API_POOL[request_token] = [API_TIMEOUT, null]
    API_POOL[request_token][1] = setInterval(function(){
      api_pull(callback, session_data)
      API_POOL[request_token][0] -= 1
      if (API_POOL[request_token][0] <= 0)
        clearInterval(API_POOL[request_token][1])
    }, 1000);
}

export function api_pull(callback, session_data) {
  console.log("API_PULL", session_data)
  var xhr_pull = new XMLHttpRequest()

  // if result == -1 ----> not ready

  xhr_pull.addEventListener('load',
    () => {
      var response = JSON.parse(xhr_pull.responseText)
      if (response.result != -1) {
        clearInterval(API_POOL[session_data.token][1])
      }
      console.log("----------> RESULT", xhr_pull.responseText);
      callback(response); })

  xhr_pull.open('POST', API_HOST + 'pull')
  xhr_pull.send(JSON.stringify(session_data))
}

export function api_request(callback, path, data = {}) {
  console.log("API_REQUEST")
  var payload = JSON.stringify(data)

  var xhr = new XMLHttpRequest()

  xhr.addEventListener('load', () => {
    console.log(xhr.responseText) // FIXME: if there is a token

    var request_token = JSON.parse(xhr.responseText).token;
    var session_data = {token : [ request_token ]};

    api_add_to_pull(callback, request_token, session_data);
  })

  // const cookies = new Cookies();

  // setInterval??? cleanup
  // api_wait = setInterval(api_pull(token, callback), 1000);

  // FIXME: daje maksymlanie 5 sec

  xhr.open('POST', API_HOST + path)
  xhr.send(payload);
}
