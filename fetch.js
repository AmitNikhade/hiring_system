const { Storage } = require('@google-cloud/storage');
const fs = require('fs');

// Replace these values with your own credentials and bucket information
const credentialsPath = 'axonaai-9f40bfe31ab5.json';
const bucketName = 'axona-hs1';
const fileName = 'filtered_dir.txt';

// Initialize the storage client with your credentials
const storage = new Storage({
  keyFilename: credentialsPath,
});

// Get a reference to the bucket
const bucket = storage.bucket(bucketName);

// Get a reference to the file
const file = bucket.file(fileName);

// Read the contents of the file
file.download((err, fileContent) => {
  if (err) {
    console.error('Error downloading file:', err);
    return;
  }

  // Convert the buffer to a string
  const fileContentString = fileContent.toString('utf-8');

  // Print the file content
  console.log('File Content:', fileContentString);
});
