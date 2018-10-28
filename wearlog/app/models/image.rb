class Image < ApplicationRecord
  require 'net/http'
  require 'uri'

  def self.send_notify
    event = Event.find_by(start_date: Date.current)
    return unless event

    token = ""
    File.open("#{Rails.root.to_s}/lib/assets/taken.txt", mode = "rt"){|f|
      token = f.read
    }
    uri = URI.parse("https://notify-api.line.me/api/notify")
    https = Net::HTTP.new(uri.host, uri.port)
    https.use_ssl = true
    event_str = event ? "今日の予定: #{event.title}" : ""
    msg = "今日の天気：#{Weather.today[:weather]}\n#{event_str}\n前回の#{event.title}で着ていた服はこちらです。"
    prev_event = Event.where(title: event.title).order("start_date desc").second
    prev_wear = Image.find_by(wear_date: prev_event.start_date)
    img = File.open("#{Rails.root.to_s}/app/assets/images/wear_images/#{prev_wear.image_path}", mode = "r+b")

    data = [
      ["message", msg],
      ["imageFile", img]
    ]

    req = Net::HTTP::Post.new(uri.request_uri)
    req["Authorization"] = "Bearer #{token}"
    req.set_form(data, "multipart/form-data")
    res = https.request(req)
  end
end
