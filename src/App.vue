<script>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import AuthForm from './components/AuthForm.vue';
import LoginWindow from './components/LoginWindow.vue';

export default {

  data() {
    return {
      token:null,
      // 这里不需要直接存储 token，但我们可以通过 isAuthenticated 来判断
    };
  },
  computed: {
    isAuthenticated() {
      console.log(localStorage.getItem('token'));
      return !!localStorage.getItem('token');
    }
  },
  methods: {
    login() {
      if (this.isAuthenticated) {
        this.token=localStorage.getItem('token');
        this.$router.push('/home');
      }
    }
  },
  // methods: {
  //   showLogin() {
  //     // 显示登录模态框或重定向到登录页面（这里省略具体实现）
  //   },
  //   logout() {
  //     // 清除 token 并触发事件（这里假设您有一个方法来处理登出逻辑）
  //     localStorage.removeItem('token');
  //     this.$eventBus.$emit('tokenChanged');
  //     // 执行跳转（如果需要立即跳转，可以在这里直接调用 this.$router.push('/home')）
  //     // 但通常，您可能希望在用户成功登出并关闭模态框后再跳转
  //   },
  // checkTokenChange() {
  //   // 这个方法用于监听全局事件总线上的 tokenChanged 事件
  //   this.$eventBus.$on('tokenChanged', () => {
  //     // 检查当前是否已认证，如果是，则跳转到 /home
  //     if (this.isAuthenticated) {
  //       this.$router.push('/home');
  //     }
  //   });
  // },
  // created() {
  //   // 在组件创建时监听 tokenChanged 事件
  //   this.checkTokenChange();
  // },
  beforeDestroy() {
    // 在组件销毁前移除事件监听器，避免内存泄漏
    this.$eventBus.$off('tokenChanged');
  }
};
</script>

<template>
  <!-- <RouterView /> -->
  <RouterView />
  <!-- <AuthForm/> -->

</template>

<style>
/* :root {
    --primary-color: #4460f1;
    --white-color: #ffffff;

    --light-text-color: #9398b3;
    --light-bg-color: #f2f4ff;
    --dark-color: #333333;

    --background-color: #fcfcff;
} */
</style>
