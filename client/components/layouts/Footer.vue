<template>
  <div class="container">
    <footer class="py-5">
      <div class="row">
        <div class="col-6 col-md-3 mb-3">
          <h5>Main</h5>
          <ul class="nav flex-column">
            <li class="nav-item mb-2" v-for="item in userMenuList" :key="item.id" ><NuxtLink :to="item.link" class="nav-link p-0 text-body-secondary">{{ item.text }}</NuxtLink></li>
          </ul>
        </div>

        <div class="col-6 col-md-3 mb-3">
          <h5>Categories</h5>
          <ul class="nav flex-column">
            <li class="nav-item mb-2" v-for="cat in props.allCategories" :key="cat.id" ><NuxtLink :to="`/category/${cat.id}`" class="nav-link p-0 text-body-secondary">{{cat.name}}</NuxtLink></li>
          </ul>
        </div>

        <div class="col-md-5 offset-md-1 mb-3">
          <form id="subscribe-form" v-on:submit="handleSubscribeNewslatter">
            <h5>Subscribe to our newsletter</h5>
            <p>Monthly digest of what's new and exciting from us.</p>
            <div class="d-flex flex-column flex-sm-row w-100 gap-2">
              <label for="newsletter1" class="visually-hidden">Email address</label>
              <input id="newsletter1" v-model="state.email" type="text" class="form-control"
                placeholder="Email address">
              <button class="btn btn-primary" type="submit">Subscribe</button>
            </div>
          </form>
        </div>
      </div>

      <div class="d-flex flex-column flex-sm-row justify-content-between py-4 my-4 border-top">
        <p>© 2024 WebDevLab. All rights reserved.</p>
        <ul class="list-unstyled d-flex">
          <li class="ms-3"><a class="link-body-emphasis" href="#"><svg class="bi" width="24" height="24">
                <use xlink:href="#twitter"></use>
              </svg></a></li>
          <li class="ms-3"><a class="link-body-emphasis" href="#"><svg class="bi" width="24" height="24">
                <use xlink:href="#instagram"></use>
              </svg></a></li>
          <li class="ms-3"><a class="link-body-emphasis" href="#"><svg class="bi" width="24" height="24">
                <use xlink:href="#facebook"></use>
              </svg></a></li>
        </ul>
      </div>
    </footer>
  </div>
</template>

<script lang="ts" setup>
interface IStateProps {
  email: string | null;
}

const props = defineProps(["allCategories", "userMenuList"]);

const state = reactive<IStateProps>({ email: null });


const handleSubscribeNewslatter = async (e: Event) => {
  e.preventDefault();

  if (state.email) {
    try {
      // Later make it with Django
      /*
      const AZURE_FUNC_API = "https://shayon-flask-demo-app.azurewebsites.net/api/sendemail";
      const response = await $fetch(AZURE_FUNC_API, {
        method: 'POST',
        body: {
          name: "Web Dev Lab - subscriber",
          phone: "01785208590",
          email: state.email,
          subject: "A user subscribed WebDevLab",
          message: "Subscribed newslatter!"
        }
      });
      console.log({ response });
      */

    } catch (error) {
      console.log(error);

    }
  }
}
</script>
