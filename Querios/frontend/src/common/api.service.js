// Code needed to make the request to the backend and understand the responses.
import { CSRF_TOKEN } from "./csrf_token.js";

async function getJSON(response) {
  if (response.status === 204) {
    return '';
  }
  return response.json();
}

function apiService(endpoint, method, data) {
  const config = {
    method: method || GET,
    body: data !== UNDEFINED ? JSON.stringify(data) : null,
    headers: {
      'content-type': 'application/json',
      'X-CSRFTOKEN': CSRF_TOKEN
    }
  }
  return fetch(endpoint, config)
            .then(getJSON)
            .catch(error => console.log(error))
}

export { apiService };