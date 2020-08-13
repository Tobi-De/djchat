import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Chat from './components/Chat'
import UserAuth from "@/components/UserAuth";

Vue.config.productionTip = false


const router = new VueRouter({
  routes: [
    { path: '/chats', name: 'Chat',component: Chat },
    { path: '/auth', name: 'UserAuth' ,component: UserAuth },
  ]
});

router.beforeEach((to, from, next) => {
  if (sessionStorage.getItem('authToken') !== null || to.path === '/auth') {
    next()
  } else {
    next('/auth')
  }
})

Vue.use(VueRouter)

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
