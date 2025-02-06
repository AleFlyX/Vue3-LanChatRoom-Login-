<template>
    <div class='body'>
        <div id="page" class="site">
            <div class="container">
                <div class="login">
                    <div class="hero">
                        <h1>你好 世界<br>Hello World</h1>
                        <p>如果你没有账号<br>可以<a href="#">点击这里</a>进行注册.</p>
                    </div>
                    <div class="heroContents">
                        <h1>聊天Room<br>HelloWorld</h1>
                        <p>没有账号懒得注册？<br>可以<a href="/home">点击这里</a>进入游客模式</p>
                    </div>

                    <div class="main">
                        <div class="choice">
                            <div class="toLogin">
                                <RouterLink to="/login">登录</RouterLink>
                                <button @click="switchPage(1)">登录</button>
                            </div>
                            <div class="toRegist">
                                <RouterLink to="/regist">注册</RouterLink>
                                <button @click="switchPage(0)">注册</button>
                            </div>
                        </div>
                        <!-- 登录、注册界面显示部分 -->
                        <!-- <RouterView/> -->
                    </div>
                </div>
            </div>
        </div>
    </div>
    <RouterView/>
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
            message: ''
        };
    },
    methods: {
        switchPage(a){
            if(a==1)
            {
                this.$router.push('/');
            }
            else if(a==0)
            {
                this.$router.push('/regist');
            }
        }
        // async login() {
        //     try {
        //         const response = await axios.post('http://localhost:5000/login', {
        //             username: this.username,
        //             password: this.password
        //         });
        //         this.message = response.data.message;
        //     } catch (error) {
        //         this.message = error.response.data.message;
        //     }
        // }
    },

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

}

a {
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
    background: linear-gradient(to right, var(--primary-color), #c471edbe, #f64f5abd);
    filter: blur(70px);
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

.toLogin button{
    height:100%;
    width: 100%;
    border:rgba(255, 255, 255, 0);
    background-color:rgba(255, 255, 255, 0);
}

.toRegist {
    justify-content: center;
    height: 35px;
    width: 50%;
    display: flex;
}

.toRegist button{
    height:100%;
    width: 100%;
    border:rgba(255, 255, 255, 0);
    background-color:rgba(255, 255, 255, 0);
}

.toLogin button:hover {
    color: #33333350;
    transition: color .3s;
}

.toRegist button:hover {
    color: #33333350;
    transition: color .3s;
}
</style>