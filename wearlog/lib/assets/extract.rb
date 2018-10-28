require 'net/http'
require 'uri'


def extract(img_url)
  uri = URI.parse("https://api.sawdev.info/callback")
  https = Net::HTTP.new(uri.host, uri.port)
  https.use_ssl = true
  img = File.open(img_url, mode = "r+b")

  data = [
    ["imageFile", img]
  ]

  req = Net::HTTP::Post.new(uri.request_uri)
  req.set_form(data, "multipart/form-data")
  res = https.request(req)

  puts res.code
  puts res.body
end

send_notify("sample.jpg")