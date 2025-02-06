import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  server:{
    host:'192.168.1.13',
    port:5173,
    proxy:{
      '/api':{
        target:'http://127.0.0.1:5000',
        //target:'http://192.168.1.240:5000',
        changeOrigin:true,
        // rewrite:(path)=>path //不重写地址，保持原样
      }
    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
