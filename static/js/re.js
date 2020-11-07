function run(flag, model) {
  if (flag==1) {
    stop();
  }else {
    send({"model": model})
  }
}

function x(flag, model) {
  if (flag==1) {
    stop();
  }else {
    send({"model": model})
  }
}

function c(flag, model) {
  if (flag==1) {
    stop();
  }else {
    send({"model": model})
  }
}

function yun(model){
    send({"model": model})
}

function stop() {
  send({"model": "stop"})
}

function send(data) {
  $.ajax({
  url: 'control',
  type: 'post',
  // 设置的是请求参数
  data: data,
  // 用于设置响应体的类型 注意 跟 data 参数没关系！！！
  dataType: 'json',
  success: function (res) {
    // 一旦设置的 dataType 选项，就不再关心 服务端 响应的 Content-Type 了
    // 客户端会主观认为服务端返回的就是 JSON 格式的字符串
    console.log(res)
  }
})
}
