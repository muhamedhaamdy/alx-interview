#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

function requestPromise (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, res, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

async function fetchCharacterName (charUrls) {
  const charactersPromise = charUrls.map(url => requestPromise(url));
  const characterResponee = await Promise.all(charactersPromise);
  characterResponee.forEach(body => {
    const charData = JSON.parse(body);
    console.log(charData.name);
  });
}

async function fetchFilm () {
  const filmData = await requestPromise(url);
  const filmJson = JSON.parse(filmData);
  const characters = filmJson.characters;
  await fetchCharacterName(characters);
}

fetchFilm();
