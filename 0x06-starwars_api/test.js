#!/usr/bin/node
const request = require('request')

let id = process.argv[2]

let url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (error, response, body) => {
    // Printing the error if occurred
    if (error) console.log(error)

    // Printing status code
    console.log(response);

    console.log('-------------------');
    // Printing body
    console.log(body);
});
