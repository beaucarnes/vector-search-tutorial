# Listings AI vector search demo

This is a small web application to show case [Atlas Vector search](https://www.mongodb.com/products/platform/atlas-vector-search) with GPT-4 filter building out of free text search.

To work with this front end please follow: [Leveraging OpenAI and MongoDB Atlas for Improved Search Functionality](https://www.mongodb.com/developer/products/atlas/atlas-vector-search-openai-filtering/)


## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

Build the relevent API endpoints and point the front end applicaiton to it:

`src/App.vue`:
```
  /*
          TODO: REPLACE WITH YOURS
          <ENDPOINT_APP_SERVICES> is the endpoint of your app services
        */
        const response = await axios.get(
          '<ENDPOINT_APP_SERVICES>',
          { params }
        );
```

### Install


```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```
