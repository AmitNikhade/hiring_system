// Replace the URL with the endpoint you want to send the POST request to
const fetch = require('node-fetch');
const apiUrl = 'https://hs9-atjv7x75va-uc.a.run.app/upload';

// Data to be sent in the POST request (replace with your actual data)
const postData = {
    "jtjp":"hnhjm | jmyjm"
};

// Options for the fetch function
const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json', // Set the content type based on your API requirements
    // Add any additional headers if needed
  },
  body: JSON.stringify(postData) // Convert data to JSON string
};
console.log(JSON.stringify( postData ))

// Make the POST request using fetch
fetch(apiUrl, options)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const contentType = response.headers.get('content-type');
    if (contentType && contentType.includes('application/json')) {
      return response.json();
    } else {
      // Handle non-JSON response (e.g., text or HTML)
      return response.text();
    }
  })
  .then(data => {
    console.log('Response data:', data);
  })
  .catch(error => {
    console.error('Error:', error);
  });