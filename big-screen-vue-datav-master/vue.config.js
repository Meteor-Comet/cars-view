const path = require('path')
const resolve = dir => {
  return path.join(__dirname, dir)
}
module.exports = {
  devServer: {
  // true 则热更新，false 则手动刷新，默认值为 true
  inline: true,

    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000/',//产生跨域的地址
        changeOrigin: true
      }
    }
},
  publicPath: './',
  transpileDependencies: [],
  chainWebpack: config => {
    config.resolve.alias
      .set('_c', resolve('src/components')) // key,value自行定义，比如.set('@@', resolve('src/components'))
  },
}
