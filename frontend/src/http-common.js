import axios from 'axios';

export const getAuthURL = action => {
    return `http://0.0.0.0:8000/dj-rest-auth/${action}/`
}

export const instance = axios.create({baseURL: "https://jsonplaceholder.typicode.com/"})

export const setAuthToken = token => {
    if (token) {
        //applying token
        instance.defaults.headers.common['Authorization'] = token;
    } else {
        //deleting the token from header
        delete instance.defaults.headers.common['Authorization'];
    }
}
