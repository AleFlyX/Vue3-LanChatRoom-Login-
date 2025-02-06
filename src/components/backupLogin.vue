<template>
    <div class='body'>
        <div id="page" class="site">
            <div class="container">
                <div class="login">
                    <div class="hero">
                        <h1>你好 世界<br>Hello World</h1>
                        <p>如果你没有账号<br>可以进行注册.</p>
                    </div>
                    <div class="heroContents">
                        <h1>聊天Room<br>HelloWorld</h1>
                        <div class="a">
                            <p>没有账号懒得注册？<br>
                                <RouterLink to="/home">点击这里</RouterLink>
                                进入游客模式
                            </p>
                        </div>
                    </div>

                    <div class="main">
                        <div class="choice">
                            <div class="toLogin">
                                <RouterLink to="/">登录</RouterLink>
                            </div>
                            <div class="toRegist">
                                <RouterLink to="/regist">注册</RouterLink>
                            </div>
                        </div>
                        <RouterView />
                    </div>
                    <!-- <button @click="testTohome">testGo</button> -->
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import router from '@/router';
import { RouterLink, RouterView, routerViewLocationKey } from 'vue-router';

export default {
    data() {
        return {
            username: '',
            password: '',
            message: '',
            token: null,
        };
    },
    methods: {
        // testTohome(){
        //     router.push('/home')

        // }
        
    //     showLogin() {
    //         // 显示登录模态框或重定向到登录页面（这里省略具体实现）
    //     },
    //     logout() {
    //         // 清除 token 并触发事件（这里假设您有一个方法来处理登出逻辑）
    //         localStorage.removeItem('token');
    //         this.$eventBus.$emit('tokenChanged');
    //         // 执行跳转（如果需要立即跳转，可以在这里直接调用 this.$router.push('/home')）
    //         // 但通常，您可能希望在用户成功登出并关闭模态框后再跳转
    //     },
    //     checkTokenChange() {
    //         // 这个方法用于监听全局事件总线上的 tokenChanged 事件
    //         this.$eventBus.$on('tokenChanged', () => {
    //             // 检查当前是否已认证，如果是，则跳转到 /home
    //             if (this.isAuthenticated) {
    //                 this.$router.push('/home');
    //             }
    //         });
    //     },
    // },
    // computed: {
    //     isAuthenticated() {
    //         console.log(localStorage.getItem('token'));
    //         return !!localStorage.getItem('token');
    //     }
    // },

    // created() {
    //     // 在组件创建时监听 tokenChanged 事件
    //     this.checkTokenChange();
    // },
    // beforeDestroy() {
    //     // 在组件销毁前移除事件监听器，避免内存泄漏
    //     this.$eventBus.$off('tokenChanged');
    // }
    },
    // mounted:{
    //     rmTokem(){
    //         localStorage.clear();
    //     }
     

    // }

};
</script>

<style>
:root {
    --primary-color: #4460f1;
    --white-color: #ffffff;

    --light-text-color: #9398b3;
    --light-bg-color: #f2f4ff;
    --dark-color: #333333;

    --background-color: #fcfcff;
}

* {
    margin: 0;
    padding: 0;
}

*,
::before::after {
    box-sizing: border-box;
}

.body {
    font-family: 'Noto Sans SC', sans-serif;
    font-size: 16px;
    font-weight: 400;
    line-height: 1.8;
    color: var(--dark-color);
    background-color: var(--background-color);
    user-select: none;
    -webkit-user-drag: none;
    /* border: solid; */
}

.a {
    text-decoration: none;
    color: inherit;
    -webkit-tap-highlight-color: transparent;
}

ul {
    list-style: none;
}

h1 {
    font-size: 3em;
    font-weight: 700;
    line-height: normal;
    color: black;
}

.site {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

.container {
    max-width: 1000px;
    width: 100%;
    padding: 0 30px;
    margin: 0 auto;
}

.login {
    display: flex;
    flex-wrap: wrap;
}

.hero {
    flex: 1 0 66.6666%;
    position: fixed;
    display: flex;
    flex-direction: column;
    gap: 50px;
    padding: 70px 0;
    /* background-color: #333333; */
    background: linear-gradient(to right, var(--primary-color), #c471edbe, #f64f5abd);
    filter: blur(70px);
    /* z-index: 1; */
}

.heroContents {
    flex: 1 0 66.6666%;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 50px;
    padding: 70px 0;
    z-index: 1;
}

.heroContents a {
    font-weight: 500;
    color: var(--primary-color);
    transition: color .3s;
}

.heroContents a:hover {
    color: #3333338d;
    font-weight: 1000;
    transition: color .3s;


}

/* .hero::before {
    content: '';
    position: absolute;
    top: 15%;
    left: 0;
    width: 280px;
    height: 100px;
    background: linear-gradient(to right, var(--primary-color), #c471ed, #f64f59);
    z-index: -1;
    filter: blur(70px);
}

.hero a {
    font-weight: 500;
    color: var(--primary-color);
    transition: color .3s;
}

.hero a:hover, */
form .password a:hover {
    color: var(--dark-color);
    text-decoration: underline;
}

.main {
    flex: 1 0 33.3333%;
}

.main form {
    display: flex;
    flex-direction: column;
    gap: 30px;
}

.main form p {
    position: relative;
}

form input {
    font: inherit;
    font-size: 14px;
    width: 100%;
    border: 0;
    outline: 0;
    padding: 0 20px;
    line-height: 60px;
    border-radius: 10px;
    /*修复input 加入padding之后大小变化的问题*/
    box-sizing: border-box;
}

input::placeholder {
    color: var(--dark-color);
    font-family: 'Noto Sans SC', sans-serif;
    font-size: inherit;
}

form input:not(.submit) {
    background-color: var(--light-bg-color);
}

form .password i {
    position: absolute;
    top: calc(60px / 2);
    right: 20px;
    margin-top: -8px;
    line-height: 1;
    color: var(--light-text-color);
    cursor: pointer;
}

form .password a {
    font-size: 13px;
    color: var(--light-text-color);
    float: right;
    margin: 5px 20px 0 0;
}

form input.submit {
    font-weight: 700;
    color: var(--white-color);
    background-color: var(--primary-color);
    box-shadow: var(--primary-color) 0 20px 30px -10px;
    cursor: pointer;
    transition: box-shadow .3s;
}

form input.submit:hover {
    box-shadow: var(--primary-color) 0 10px 30px -10px;
}

.separator {
    position: relative;
    margin: 50px 0 30px;
}

.separator::before {
    content: '';
    position: absolute;
    top: 50%;
    width: 100%;
    height: 1px;
    background-color: var(--light-text-color);
    opacity: .3;
    z-index: 1;
}

.separator p {
    font-size: 14px;
    width: fit-content;
    padding: 0 10px;
    color: var(--light-text-color);
    background-color: var(--background-color);
    margin: 0 auto;
    position: relative;
    z-index: 1;
}

.options ul {
    display: flex;
    justify-content: center;
    gap: 20px;
}

.options ul li a {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 60px;
    height: 60px;
    border-radius: 10px;
    background-color: var(--white-color);
    box-shadow: var(--light-text-color) 0 10px 20px -10px;
    transition: all .3s ease-out;
}

.options ul li a:hover {
    color: var(--white-color);
    box-shadow: none;
}

.choice {
    /* border:solid; */
    display: flex;
}

.toLogin {
    justify-content: center;
    height: 35px;
    width: 50%;
    display: flex;
}

.toRegist {
    justify-content: center;
    height: 35px;
    width: 50%;
    display: flex;
}

.toLogin:hover {
    color: #33333350;
    transition: color .3s;
}

.toRegist:hover {
    color: #33333350;
    transition: color .3s;
}
</style>