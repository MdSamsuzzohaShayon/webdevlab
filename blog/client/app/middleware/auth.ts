export default defineNuxtRouteMiddleware((to) => {
    console.log("THis is auth.ts middleware");
    
  /*   // skip middleware on server
  if (import.meta.server) {
    return;
  }
  // skip middleware on client side entirely
  if (import.meta.client) {
    return;
  }
  // or only skip middleware on initial client load
  const nuxtApp = useNuxtApp();
  if (
    import.meta.client &&
    nuxtApp.isHydrating &&
    nuxtApp.payload.serverRendered
  ) {
    return;
  }

  if (to.params.id === "1") {
    return abortNavigation();
  }
  // In a real app you would probably not redirect every route to `/`
  // however it is important to check `to.path` before redirecting or you
  // might get an infinite redirect loop
  if (to.path !== "/") {
    return navigateTo("/");
  }
  */
});
