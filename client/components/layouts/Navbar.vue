<template>
  <header :class="`w-full ${bgClr} ${txtClr}`">
    <div :class="`container ${cm} ${cp}`">
      <!-- ======= 🌐 STATIC MENU START 🌐 ======= -->
      <div :class="`mobile-navbar w-full flex justify-between items-center ${hp} border-b-primary md:border-0`">
        <div class="menu-wrapper w-1/6 md:w-fit">
          <Icon name="humbleicons:align-text-justify" :color="iconClr" :size="is" @click="toggleMenu" />
        </div>
        <NuxtLink to="/" class="logo-wrapper w-3/6 md:w-fit flex justify-center items-center">
          <img src="/logo.png" alt="webdevlab-logo" class="w-12">
          <span>Web Dev Lab</span>
        </NuxtLink>
        <!-- ======= 🌐 NAV MENU START 🌐 ======= -->
        <div :class="`w-fit hidden md:block`">
          <MainMenuItem :menuList="menuList" />
        </div>
        <!-- ======= 🌐 NAV MENU END 🌐 ======= -->
        <div class="search-mode w-1/6 md:w-fit">
          <Icon name="heroicons-solid:sun" :color="iconClr" :size="is" />
          <Icon name="heroicons-solid:magnifying-glass" :color="iconClr" :size="is" />
        </div>
      </div>
      <!-- ======= 🌐 STATIC MENU END 🌐 ======= -->

      <!-- ======= 🌐 COLLABSABLE MENU START 🌐 ======= -->
      <div
        :class="`collapsable-menu absolute top-0 left-0 w-9/12 md:w-3/6 lg:w-2/6 h-fit md:h-full z-30 ${bgClr} ${txtClr}`"
        v-if="state.menuCollapse">

        <!-- ======= 🌐 TOP BAR START 🌐 ======= -->
        <div :class="`w-full ${hp} border-b-primary flex justify-between items-center ${cmip}`">
          <NuxtLink to="/" class="logo-wrapper flex justify-center items-center">
            <img src="/logo.png" alt="webdevlab-logo" class="w-12">
            <span>Web Dev Lab</span>
          </NuxtLink>
          <div @click="toggleMenu">
            <Icon name="ci:close-md" :color="iconClr" :size="is" />
          </div>
        </div>
        <!-- ======= 🌐 TOP BAR END 🌐 ======= -->

        <!-- ======= 🌐 NAV MENU START 🌐 ======= -->
        <div :class="`w-full md:hidden`">
          <MainMenuItem :menuList="menuList" />
        </div>
        <!-- ======= 🌐 NAV MENU END 🌐 ======= -->

        <!-- ======= 🌐 SOCIAL ICON START 🌐 ======= -->
        <div :class="`w-full ${hp} ${cmip} mt-16`">
          <p :class="`${uph}`">Follow US</p>
          <h4>Social Links</h4>

          <nav class="mt-4">
            <ul class="mt-4 w-full">
              <li v-for="item in socialLinks" :class="`w-full leading-10 bg-gray-700 mb-2 px-2`">
                <NuxtLink :to="item.link" target="_blink" class="w-full flex justify-between items-center">
                  <span>
                    <Icon :name="item.icon" :color="iconClr" :size="is" />
                    <span class="ml-2">{{ item.text }}</span>
                  </span>
                  <span>{{ item.followers }}</span>
                </NuxtLink>
              </li>
            </ul>
          </nav>
        </div>
        <!-- ======= 🌐 SOCIAL ICON END 🌐 ======= -->

        <!-- ======= 🌐 NEWSLETTER START 🌐 ======= -->
        <div :class="`w-full ${hp} ${cmip} mt-16`">
          <div class="p-8 border-primary md:border-0">
            <p :class="`${uph}`">Newsletter</p>
            <h2>Subscribe Now</h2>
            <form>
              <div class="input-group">
                <label for="">Get notified of the best articles, courses, shorts, and more.</label>
                <input type="text" placeholder="Enter Your Email">
              </div>

              <div class="input-group">
                <button type="submit" class="btn btn-primary w-full">Subscribe</button>
              </div>

              <div class="input-group-inline">
                <input type="checkbox" id="agreed">
                <label for="">By checking this box, you confirm that you have read and are agreeing to our terms of use
                  regarding the storage of the data submitted through this form.</label>
              </div>

            </form>
          </div>
        </div>
        <!-- ======= 🌐 NEWSLETTER END 🌐 ======= -->
      </div>
      <!-- ======= 🌐 COLLABSABLE MENU END 🌐 ======= -->
    </div>

    <!-- ======= 🌐 SEARCH COLLAPSE START 🌐 ======= -->
    <!-- <div class="search-collapse absolute w-full top-16 left-0 z-20 bg-gray-800" >
      <div :class="`container ${cm} ${cp}`">
        <br>
        <form @submit.prevent="handleSearch" class="border-primary" >
          <div class="input-group-float flex justify-between items-center">
            <div class="icon-wrapper p-2 bg-gray-700 text-gray-200">
              <Icon name="heroicons-solid:magnifying-glass" :color="iconClr" :size="is" class="outline-none placeholder:text-gray-500 border-b" />
            </div>
            <input type="text" placeholder="Enter Keyword">
            <Icon name="ci:close-md" :color="iconClr" :size="is" class="h-10 outline-none bg-gray-700 text-gray-200 placeholder:text-gray-500"  />
          </div>
        </form>

        <div class="mt-8">
          <p :class="`${uph}`">TOP-picked</p>
          <h3>Top-read Stories</h3>
          
        </div>
      </div>
    </div> -->
    <!-- ======= 🌐 SEARCH COLLAPSE END 🌐 ======= -->


  </header>
</template>

<script lang="ts" setup>
import type { IMenuItem } from '~/types';


const state = reactive({ menuCollapse: false });

const bgClr = "bg-gray-900";
const txtClr = "text-gray-50";
const iconClr = "white";




interface ISocialLink extends IMenuItem {
  icon: string;
  followers: string;
}

const menuList: IMenuItem[] = [
  { id: 1, text: "Home", link: "/" },
  { id: 2, text: "Course", link: "/course" },
  { id: 3, text: "Blog", link: "/blog" },
  { id: 4, text: "Shorts", link: "/shorts" },
  { id: 5, text: "Services", link: "/services" },
  { id: 6, text: "Contact", link: "/contact" },
  { id: 7, text: "About", link: "/about" },
];

const socialLinks: ISocialLink[] = [
  { id: 1, text: "Github", link: "https://github.com/MdSamsuzzohaShayon", icon: "grommet-icons:github", followers: "21" },
  { id: 2, text: "YouTube", link: "https://www.youtube.com/@web-dev-lab", icon: "grommet-icons:youtube", followers: "1.52k" },
  { id: 3, text: "Linkedin", link: "https://bd.linkedin.com/in/md-samsuzzoha?trk=people-guest_people_search-card", icon: "grommet-icons:linkedin", followers: "4.5k" },
  { id: 3, text: "X", link: "https://twitter.com/shayon_md?lang=en", icon: "grommet-icons:twitter", followers: "1.2k" },
];

const toggleMenu = (e: MouseEvent) => {
  e.preventDefault();
  state.menuCollapse = !state.menuCollapse;
}

const handleSearch=(e: Event)=>{

}
</script>
