#!/usr/bin/node
const request = require("request");

if (process.argv.length < 3) {
  console.error("Usage: 0-starwars_characters.js <movie ID>")
} else {
  const movieID = process.argv[2]
  const options = {
    url: `https://swapi-api.alx-tools.com/api/films/${movieID}/`,
    method: 'GET',
    json: true,
    headers: {'Content-Type': 'application/json'},
  }
  request(options, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      let characters = body.characters
      for (let i of characters) {
	let new_options = options;
	new_options.url = i;
	request(new_options, (error, new_response, new_body) => {
	  if (error) {
	    console.error('Error:', error);
	  } else {
	    console.log(new_body.name);
	  }
	});
      }
    }
  });
}
