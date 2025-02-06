<template>
    <form @submit.prevent="regist">
        <p>
            <input type="username" placeholder="起个名吧(账号)" v-model="username" required>
        </p>
        <p class="password">
            <input type="password" placeholder="编写你的密语吧！" v-model="password" required>
            <i class="ri-eye-off-line"></i>
            <a href="#">记号密码哦~</a>
        </p>
        <p>
            <input type="submit" class="submit" value="注册">
        </p>
    </form>
    <p v-if="message">{{ message }}</p>
</template>

<script>
import axios from 'axios';
import router from '@/router';

export default {
    data() {
        return {
            username: '',
            password: '',
            message: ''
        };
    },
    methods: {
        async regist() {
            try {
                const response = await axios.post('/api/regist', {
                    username: this.username,
                    password: this.password
                });

                this.message = response.data.message + ' 正在跳转...';
                // if (this.message == '用户已存在,请登录') {
                //     this.username = '';
                //     this.password = '';
                // }
                // else {
                    setTimeout(() => {
                        this.$router.push('/');
                    }, 1500);
                    //跳转到登录
                // }



            } catch (error) {
                this.message = error.response.data.message;
            }
        }
    }
};
</script>
