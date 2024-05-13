# This is vue apollo latest setup guide:

## Setup
### Install @vue/apollo-composable
```
npm install --save @vue/apollo-composable
```


### Connect Apollo Client to Vue

 - Vue 3

```
import { createApp, provide, h } from 'vue'
import { DefaultApolloClient } from '@vue/apollo-composable'

const app = createApp({
  setup () {
    provide(DefaultApolloClient, apolloClient)
  },

  render: () => h(App),
})
```

### Multiple clients - You can also provide multiple Apollo Client instances to be used in your application. In this case, it's recommended to provide a default one:

```
import { provide } from 'vue'
import { ApolloClients } from '@vue/apollo-composable'

const app = new Vue({
  setup () {
    provide(ApolloClients, {
      default: apolloClient,
    })
  },

  render: h => h(App),
})
```

### You can add other client instances alongside it:

```
provide(ApolloClients, {
  default: apolloClient,
  clientA: apolloClientA,
  clientB: apolloClientB,
})
```

### You can then select which one to use in functions we will cover next (such as useQuery, useMutation and useSubscription) with the clientId option.

### Usage outside of setup
 - When using e.g. useQuery outside of vue contexts, the clients cannot be injected using vue's provide/inject mechanism. @vue/apollo-composable can manage their own apollo clients

### Use provideApolloClient for a single default client:

```
import { provideApolloClient } from "@vue/apollo-composable";

const query = provideApolloClient(apolloClient)(() => useQuery(gql`
  query hello {
    hello
  }
`))
const hello = computed(() => query.result.value?.hello ?? '')
```

### Use provideApolloClients for multiple clients:

```
import { provideApolloClients } from "@vue/apollo-composable";

provideApolloClients({
  default: apolloClient,
  clientA: apolloClientA,
  clientB: apolloClientB,
})
```






Integrate apollo with Nuxt.js project following this latest document