import Vue from 'vue'
import App from './App.vue'
import router from './router'

import MuseUI from 'muse-ui';
import 'muse-ui/dist/muse-ui.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';
import 'material-icons/iconfont/material-icons.css';

window.$ = window.jQuery = require('jquery');

Vue.use(MuseUI);
Vue.config.productionTip = false
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
