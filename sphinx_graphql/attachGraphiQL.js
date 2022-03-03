// graphql query fetcher
const graphQLFetcher = function (target, originalHeaders, query, response, variables, endpoint) {
    return function (graphQLParams, options) {
        const headers = options.headers || {};
        const params = {
            method: 'post',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                ...headers
            },
            body: JSON.stringify(graphQLParams),
            credentials: 'omit'
        };
        return fetch(endpoint, params)
            .then(function (resp) {
                return resp.text();
            })
            .then(function (responseBody) {
                try {
                    return JSON.parse(responseBody);
                } catch (error) {
                    return responseBody;
                }
            }).catch(function (error) {
                // Connection failed, remount read-only
                ReactDOM.unmountComponentAtNode(target);
                renderGraphiQL(target, originalHeaders, query, variables, response);
                return originalResponse;
            })
    }
};

// create GraphiQL components and embed into HTML
const attachGraphiQL = function (target, endpoint) {
    const query = target.getElementsByClassName("query")[0].innerHTML.trim();
    const response = target.getElementsByClassName("response")[0].innerHTML.trim();
    const variables = target.getElementsByClassName("variables")[0].innerHTML.trim();
    const headers = target.getElementsByClassName("headers")[0].innerHTML.trim();
    window.sessionStorage.clear();
    renderGraphiQL(target, headers, query, response, variables, endpoint);
}

const renderGraphiQL = function (target, headers, query, response, variables, endpoint) {
    if (endpoint == undefined) {
        target.classList.add("graphiql-ro");
    }
    const graphiQLElement = React.createElement(GraphiQL, {
        fetcher: graphQLFetcher(target, headers, query, response, variables, endpoint),
        schema: (endpoint == undefined) ? null: undefined,
        query: query,
        response: response,
        variables: variables,
        headers: headers,
        storage: window.sessionStorage,
        defaultSecondaryEditorOpen: variables.length > 0,
        readOnly: (endpoint == undefined)
    });
    ReactDOM.render(graphiQLElement, target);
};
