import Vue from 'vue'
import Router from 'vue-router'
import Home from './components/Home.vue'
import Login from '@/components/Login'
import Chat from '@/components/rooms/Chat'
import Room from '@/components/rooms/Room'

Vue.use(Router)

export default new Router({
	mode: 'history',
	routes: [{
			path: '/',
			name: 'room',
			component: Room
		},
		{
			path: '/login/',
			name: 'login',
			component: Login
		},
		{
			path: '/chat/:pk',
			name: 'chat',
			component: Chat
		},
	]
})
