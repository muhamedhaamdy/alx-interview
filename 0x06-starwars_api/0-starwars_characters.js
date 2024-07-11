#!/usr/bin/node
const request = require('request');

const id = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (error, res, body) =>{
    if (error) {
        console.error(error);
        return;
    }

    const data = JSON.parse(body);
    const characters = data['characters'];
    for (character_url of characters) {
        request(character_url, (error, res, body) =>{
            if (error) {
                console.error(error);
                return;
            }

            const char_data = JSON.parse(body);
            console.log(char_data['name']);
        });
    }
});

// // function requestPromise(url) {
// //     return new Promise((res, rej) => {
// //         request(url, (error, res, body) => {
// //             if (error) {
// //                 reject(error);
// //             } else {
// //                 resolve(body);
// //             }
// //         });
// //     });
// // }

// // const getCharacterName = async (charUrl) => {
// //     try {
// //         const charactersPromises = charUrl.map(url => requestPromise(url));
// //         const charactersResponse = await Promise.all(charactersPromises);
// //         charactersResponse.forEach(body => {
// //             charData = Json.parse(body)
// //             console.log(charData.name);
// //         })
// //     } catch (error) {
// //         console.error('Error fetching character names:', error);
// //     }
// // };

// // const fetchFilm = async ()=> {
// //     try{
// //         const body = await JSON.parse(requestPromise(url));
// //         const characters = body.characters;
// //         await getCharacterName(characters);
// //     } catch (error) {
// //         console.error('Error fetching film:', error);
// //     }
// // };

// // fetchFilm();

