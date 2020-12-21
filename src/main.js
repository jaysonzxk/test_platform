import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import VueAxios from 'vue-axios'

//Vue.config.productionTip = false
axios.defaults.withCredentials = true

Vue.use(VueAxios,axios)
Vue.use(ElementUI)

new Vue({
  render: h => h(App),
}).$mount('#app')