<template>
  <h2>房间ip:192.168.1.13:5173</h2>
  <div class="chat">
    <p style="text-align: center;">广场</p>
    <div class="messages">
      <div v-for="message in messages" :key="message.id" class="message" >
        <strong>{{ message.username }}:</strong> {{ message.message }}<h6 style="font-weight: 30;font-size: 10px;">{{ message.created_at}}</h6>
      </div>
    </div>
    <div class="input-area">
      <p>{{ susername }}</p>
      <!-- <input v-model="newMessage.username" placeholder="Username" /> -->
      <input v-model="newMessage.message" placeholder="Message" />
      <button @click="sendMessage">发送</button>
      <button @click="fetchMessages">手动刷新</button>
    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      sendTimes: [],
      messages: [],
      susername: localStorage.getItem('user'),
      newMessage: {
        username: '',
        message: '',
      }
    };
  },
  created() {
    this.fetchMessages();
    this.startFetchingInterval();
    // this.gapFetch();
  },
  beforeDestroy(){
    this.stopFetchingInterval(); // 组件销毁前清除定时器
  },
  methods: {
    // gapFetch() {
    //   setTimeout(() => {
    //     this.fetchMessages();
    //   }, 3000);
    // },
    async fetchMessages() {
      try {
        const response = await axios.get('/api/get_messages');
        this.messages = response.data;
        // this.sendTimes=response.data('created_at');
        // console.log(response.data('created_at'));
      } catch (error) {
        console.error(error);
      }
    },
    startFetchingInterval() {
      // 设置定时器，每3秒执行一次 fetchMessages 方法
      this.fetchInterval = setInterval(this.fetchMessages, 6000);
    },

    async sendMessage() {
      this.newMessage.username = this.susername;
      // this.newMessage.sendTime=;
      try {
        this.fetchMessages();
        await axios.post('/api/send_message', this.newMessage);
        this.newMessage.message = '';
        this.fetchMessages();
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>

<style scoped>
/* .chat {
  width: 300px;
  margin: 0 auto;
}

.messages {
  border: 1px solid #ccc;
  height: 300px;
  overflow-y: scroll;
  padding: 10px;
}

.message {
  margin-bottom: 10px;
}

.input-area {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

input {
  flex: 1;
  padding: 5px;
}

button {
  padding: 5px 10px;
} */
.chat {
  max-width: 600px;
  /* 设置聊天窗口的最大宽度 */
  margin: 0 auto;
  /* 居中对齐 */
  border: 1px solid #ccc;
  /* 边框 */
  border-radius: 8px;
  /* 圆角 */
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  /* 阴影效果 */
  background-color: #f9f9f9;
  /* 背景颜色 */
  display: flex;
  flex-direction: column;
  /* 垂直排列 */
  height: 80vh;
  /* 设置高度 */
}

.messages {
  flex: 1;
  /* 使消息区域占据剩余空间 */
  padding: 10px;
  /* 内边距 */
  overflow-y: auto;
  /* 允许垂直滚动 */
  border-bottom: 1px solid #ccc;
  /* 底部边框 */
}

.message {
  margin-bottom: 10px;
  /* 消息之间的间距 */
  padding: 8px;
  /* 内边距 */
  border-radius: 5px;
  /* 圆角 */
  background-color: #e1f5fe;
  /* 消息背景颜色 */
}

.input-area {
  display: flex;
  /* 使用 flexbox 布局 */
  padding: 10px;
  /* 内边距 */
  background-color: #fff;
  /* 输入区域背景颜色 */
}

.input-area input {
  flex: 1;
  /* 输入框占据剩余空间 */
  padding: 10px;
  /* 内边距 */
  border: 1px solid #ccc;
  /* 边框 */
  border-radius: 5px;
  /* 圆角 */
  margin-right: 10px;
  /* 右边距 */
}

.input-area button {
  margin: 5px;
  padding: 10px 15px;
  /* 内边距 */
  border: none;
  /* 去掉边框 */
  border-radius: 5px;
  /* 圆角 */
  background-color: #007bff;
  /* 按钮背景颜色 */
  color: white;
  /* 按钮文字颜色 */
  cursor: pointer;
  /* 鼠标悬停时显示手型 */
  transition: background-color 0.3s;
  /* 背景颜色过渡效果 */
}

.input-area button:hover {
  background-color: #0056b3;
  /* 悬停时的背景颜色 */
}
</style>