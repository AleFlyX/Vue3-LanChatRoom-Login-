import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginWindow from '@/components/LoginWindow.vue'
import regist from '@/components/regist.vue'
import chatRoom from '@/components/chatRoom.vue'
import AuthForm from '@/components/AuthForm.vue'
import backupLogin from '@/components/backupLogin.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'LoginPage',
      component: backupLogin, // 包含登录和注册表单的容器组件
      meta:{title:'Welcome!'},
      children:
        [
          {
            path: '', // 默认子路由
            name: 'LoginDf',
            component: LoginWindow,
          },
          {
            path: 'regist',
            name: 'Regist',
            component: regist,
          },
        ],
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginWindow,
    },
    {
      path: '/home',
      name: 'home',
      component:chatRoom,
      meta:{
        title:'开始聊天吧！',
        requiresAuth:true
      },
      children:[

      ]
    },
  ],
})

// router.beforeEach((to,from,next)=>{
//   //路由保卫
//   if(to.matched.some(r=>r.meta?.requiresAuth)){ //判断每级路由的meta属性是否需要requireAuth函数认证
//     if(!localStorage.getItem('token')){
//       next({name:'loginPage',query:{redirect:to.fullPath}})
//     }
//   }
//   next()
// })

export default router
