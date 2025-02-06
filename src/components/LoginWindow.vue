<template>
    <form @submit.prevent="login">
        <p>
            <input type="username" placeholder="账号" v-model="username" required>
        </p>
        <p class="password">
            <input type="password" placeholder="密码" v-model="password" required>
            <i class="ri-eye-off-line"></i>
            <a href="#">找回密码</a>
        </p>
        <p>
            <input type="submit" class="submit" value="登录">
        </p>
    </form> 
    <!-- <button @click="testTohome">testGo</button> -->
    <p v-if="message">{{ message }}</p>
</template>
<script>
import axios from 'axios';
import router from '@/router';// 
export default {
    data() {
        return {
            username: '',
            password: '',
            message: ''
        };
    },
    methods: {
        // testTohome(){
        //     router.push('/home')
        // },
        async login() {
            try {
                const response = await axios.post('/api/login', {
                    username: this.username,
                    password: this.password
                });
                this.message = response.data.message;
                localStorage.setItem('token',response.data.token);
                console.log(localStorage.getItem('token'))
                router.push('/home'); 
                localStorage.setItem('user',JSON.stringify(response.data.user));
                console.log(localStorage.getItem('user'))
         
                // this.$router.push('/home')
                //跳转到主页
                // setTimeout(()=>
                // {
                //     this.$router.push('/home');
                // },1500);

            } catch (error) {
                
            }
        }
    }
};
</script>