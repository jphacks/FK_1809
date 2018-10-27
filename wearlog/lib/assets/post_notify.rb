require 'net/http'
require 'uri'

File.open("taken.txt", mode = "rt"){|f|
  TOKEN = f.read
}

def send_notify(msg, img_url)
  uri = URI.parse("https://notify-api.line.me/api/notify")
  https = Net::HTTP.new(uri.host, uri.port)
  https.use_ssl = true
  img = File.open(img_url, mode = "r+b")

  data = [
    ["message", msg],
    ["imageFile", img]
  ]

  req = Net::HTTP::Post.new(uri.request_uri)
  req["Authorization"] = "Bearer #{TOKEN}"
  req.set_form(data, "multipart/form-data")
  res = https.request(req)
end

send_notify("hoge", "sample.jpg")